from dataclasses import dataclass
import hashlib
import json, os, re, argparse, time
from datetime import datetime
from pathlib import Path
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_classic.embeddings import CacheBackedEmbeddings
from langchain_classic.storage import LocalFileStore
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
REGISTRY_PATH = DATA_DIR / "registry.json"
COLLECTION_NAME = "rag_tp1"
EMBEDDINGS_CACHE_DIR = DATA_DIR / "embeddings_cache"

LOCAL_MODELS = {
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2": {},
    "sentence-transformers/all-MiniLM-L6-v2": {},
    "intfloat/multilingual-e5-small": {},
    "BAAI/bge-m3": {
        "model_kwargs": {"dtype": "float16"},
        "encode_kwargs": {"normalize_embeddings": True},
    },
}

DEFAULT_SECTION_TITLE = "Intro / Sin título"

# Detecta bloques de tabla Markdown (mismo patron que en sanear.py)
_RE_MD_TABLE = re.compile(
    r'(?:^[ \t]*\|[^\n]+\|[ \t]*\n?)+',
    flags=re.MULTILINE,
)


def _split_preserving_tables(text: str) -> list[tuple[str, bool]]:
    """Separa texto en segmentos (contenido, es_tabla). Las tablas deben chunearse atomicamente."""
    segments: list[tuple[str, bool]] = []
    last_end = 0
    for match in _RE_MD_TABLE.finditer(text):
        if match.start() > last_end:
            segments.append((text[last_end:match.start()], False))
        segments.append((match.group(0), True))
        last_end = match.end()
    if last_end < len(text):
        segments.append((text[last_end:], False))
    return segments


TITLE_MAX_LEN = 80
TITLE_MAX_WORDS = 10
TITLE_ALLOWED_CHARS = re.compile(r'^[\w\s\-:,\.()%/]+$')
TITLE_STRUCTURAL_PREFIX = re.compile(
    r'^(?:\d+(?:\.\d+)*(?:[\.)])|[IVXLCM]+[\.)]?|Cap[ií]tulo|Unidad|Tema|M[oó]dulo|Secci[oó]n|Parte|Anexo)\b',
    flags=re.IGNORECASE,
)
TITLE_STOPWORDS = {
    "a", "al", "con", "de", "del", "e", "el", "en", "la", "las",
    "los", "o", "para", "por", "sin", "u", "y",
}
HEADING_CONTINUATION_WORDS = {
    "a", "al", "con", "de", "del", "e", "el", "en", "la", "las",
    "los", "o", "para", "por", "sin", "u", "y",
}
NOISY_SECTION_TITLES = {
    "buenos",
    "cruz",
    "dicho",
    "estas",
    "jimena",
    "santa",
    "tamara",
    "visto",
}


@dataclass
class CargaConfig:
    chunk_size: int = 512
    chunk_overlap: int = 50
    embedding_model: str = "gemini-embedding-001"
    chunking_technique: str = "recursive"  # "recursive" | "fixed_size_overlap" | "paragraph_custom"
    embedding_batch_size: int = 20
    max_retries: int = 3
    retry_wait_seconds: int = 60


def parsear_toon(toon_str: str) -> dict:
    if "\n" not in toon_str:
        raise ValueError("TOON string malformado: no contiene salto de línea.")

    newline_pos = toon_str.index("\n")
    header = toon_str[:newline_pos]
    if not header.startswith("document{"):
        raise ValueError(f"Header TOON inesperado: {header!r}")

    data_line = toon_str[newline_pos + 1:].rstrip("\n")

    if not data_line.startswith('"'):
        raise ValueError(f"Línea de datos TOON malformada: se esperaba '\"', got: {data_line[:30]!r}")

    # Find closing unescaped quote after the opening one
    i = 1  # skip opening quote
    while i < len(data_line):
        if data_line[i] == "\\" and i + 1 < len(data_line):
            i += 2  # skip escaped char
            continue
        if data_line[i] == '"':
            break
        i += 1

    raw_content = data_line[1:i]
    # Unescape: order matters — backslash first
    content = raw_content.replace("\\\\", "\x00BACKSLASH\x00")
    content = content.replace("\\n", "\n")
    content = content.replace("\\f", "\f")
    content = content.replace('\\"', '"')
    content = content.replace("\x00BACKSLASH\x00", "\\")

    rest = data_line[i + 2:]  # skip closing quote and comma
    parts = [p.strip() for p in rest.split(",")]
    source = parts[0]
    sha256 = parts[1]
    pages = int(parts[2])
    chars_original = int(parts[3])
    chars_saneado = int(parts[4].strip())

    return {
        "content": content,
        "source": source,
        "sha256": sha256,
        "pages": pages,
        "chars_original": chars_original,
        "chars_saneado": chars_saneado,
    }


def _normalizar_linea(linea: str) -> str:
    return re.sub(r'\s+', ' ', linea.strip())


def _es_titulo_generico(linea: str) -> bool:
    palabras = re.findall(r'[A-Za-zÁÉÍÓÚÑÜáéíóúñü0-9]+', linea)
    if not palabras or len(palabras) > TITLE_MAX_WORDS:
        return False
    if len(palabras) < 2:
        return False

    palabras_contenido = 0
    for palabra in palabras:
        if palabra.lower() in TITLE_STOPWORDS:
            continue
        if palabra.isupper() or palabra[0].isupper():
            palabras_contenido += 1
            continue
        return False

    return palabras_contenido >= 2


def _es_candidato_titulo_contextual(linea: str) -> bool:
    if not linea or len(linea) > TITLE_MAX_LEN:
        return False
    if linea[0].islower() or linea.endswith((".", "!", "?")):
        return False
    if not TITLE_ALLOWED_CHARS.match(linea):
        return False
    if re.search(r'\b(?:https?://|www\.)', linea, flags=re.IGNORECASE):
        return False
    if not re.search(r'[A-Za-zÁÉÍÓÚÑÜáéíóúñü]', linea):
        return False
    if re.fullmatch(r'\d+(?:[.,]\d+)?%?', linea):
        return False
    return len(linea.split()) <= TITLE_MAX_WORDS


def es_titulo(linea: str) -> bool:
    linea = _normalizar_linea(linea)
    if '|' in linea:  # fila de tabla Markdown, nunca es titulo
        return False
    if not _es_candidato_titulo_contextual(linea):
        return False
    if TITLE_STRUCTURAL_PREFIX.match(linea) or linea.isupper():
        return True
    if linea.endswith(":"):
        words = linea.rstrip(":").split()
        return 2 <= len(words) <= TITLE_MAX_WORDS
    return _es_titulo_generico(linea)


def _es_titulo_en_contexto(lines: list[str], index: int) -> bool:
    linea = _normalizar_linea(lines[index])
    if not _es_candidato_titulo_contextual(linea):
        return False

    if es_titulo(linea):
        return True

    prev_line = _normalizar_linea(lines[index - 1]) if index > 0 else ""
    return bool(TITLE_STRUCTURAL_PREFIX.match(prev_line))


def _siguiente_linea_no_vacia(lines: list[str], index: int) -> str:
    for candidate in lines[index + 1:]:
        normalized = _normalizar_linea(candidate)
        if normalized:
            return normalized
    return ""


def _primer_token(texto: str) -> str:
    match = re.match(r'^[^\w]*([A-Za-zÁÉÍÓÚÑÜáéíóúñü]+)', texto)
    return match.group(1).lower() if match else ""


def _debe_degradar_titulo(title: str, next_line: str) -> bool:
    title = _normalizar_linea(title)
    next_line = _normalizar_linea(next_line)

    if not title or title == DEFAULT_SECTION_TITLE:
        return False
    if TITLE_STRUCTURAL_PREFIX.match(title) or "|" in title:
        return False

    words = title.split()
    if len(words) != 1:
        return False

    if words[0].lower() in NOISY_SECTION_TITLES:
        return True

    next_token = _primer_token(next_line)
    if next_token in HEADING_CONTINUATION_WORDS:
        return False

    stripped = next_line.lstrip(" .,:;-)")
    if stripped and stripped[0].islower():
        return True

    return False


def segmentar_pagina_en_secciones(page_text: str, current_title: str) -> tuple[list[tuple[str, str]], str]:
    lines = page_text.split("\n")
    sections: list[tuple[str, str]] = []
    current_lines: list[str] = []
    active_title = _normalizar_linea(current_title) or DEFAULT_SECTION_TITLE
    if not active_title:
        active_title = DEFAULT_SECTION_TITLE

    def flush_section() -> None:
        content = "\n".join(current_lines).strip()
        if content:
            sections.append((active_title, content))

    for index, raw_line in enumerate(lines):
        normalized_line = _normalizar_linea(raw_line)
        if _es_titulo_en_contexto(lines, index):
            next_line = _siguiente_linea_no_vacia(lines, index)
            if not _debe_degradar_titulo(normalized_line, next_line):
                if current_lines:
                    flush_section()
                    current_lines = []
                active_title = normalized_line
                continue

        current_lines.append(raw_line)

    flush_section()
    return sections, active_title


def chunk_recursive(text: str, config: CargaConfig, base_metadata: dict) -> list[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.chunk_size,
        chunk_overlap=config.chunk_overlap,
        # En PDFs extraídos quedan muchos saltos de línea residuales. Conviene
        # priorizar cierres más semánticos antes de cortar por maquetado crudo.
        separators=["\n\n", ". ", "; ", ": ", "\n", " ", ""],
    )

    documents = []
    chunk_idx = 0

    current_title = DEFAULT_SECTION_TITLE  # persiste entre páginas
    for page_num, page_text in enumerate(text.split("\f"), start=1):
        if not page_text.strip():
            continue

        sections, current_title = segmentar_pagina_en_secciones(page_text, current_title)

        for title, content in sections:
            for segment, es_tabla in _split_preserving_tables(content):
                if es_tabla:
                    # Tabla atomica: un chunk completo, sin partir filas
                    bloque = segment.strip()
                    if not bloque:
                        continue
                    documents.append(Document(
                        page_content=bloque,
                        metadata={**base_metadata, "seccion": title, "pagina": page_num, "chunk_index": chunk_idx, "es_tabla": True},
                    ))
                    chunk_idx += 1
                else:
                    for chunk in splitter.split_text(segment):
                        chunk = chunk.strip()
                        if not chunk:
                            continue
                        documents.append(Document(
                            page_content=chunk,
                            metadata={**base_metadata, "seccion": title, "pagina": page_num, "chunk_index": chunk_idx},
                        ))
                        chunk_idx += 1

    return documents


def chunk_fixed_size_overlap(text: str, config: CargaConfig, base_metadata: dict) -> list[Document]:
    splitter = CharacterTextSplitter(
        separator="",
        chunk_size=config.chunk_size,
        chunk_overlap=config.chunk_overlap,
    )
    documents = []
    chunk_idx = 0
    current_title = DEFAULT_SECTION_TITLE

    for page_num, page_text in enumerate(text.split("\f"), start=1):
        if not page_text.strip():
            continue

        sections, current_title = segmentar_pagina_en_secciones(page_text, current_title)

        for title, content in sections:
            for segment, es_tabla in _split_preserving_tables(content):
                if es_tabla:
                    bloque = segment.strip()
                    if not bloque:
                        continue
                    documents.append(Document(
                        page_content=bloque,
                        metadata={**base_metadata, "seccion": title, "pagina": page_num, "chunk_index": chunk_idx, "es_tabla": True},
                    ))
                    chunk_idx += 1
                else:
                    for chunk in splitter.split_text(segment):
                        chunk = chunk.strip()
                        if not chunk:
                            continue
                        documents.append(Document(
                            page_content=chunk,
                            metadata={
                                **base_metadata,
                                "seccion": title,
                                "pagina": page_num,
                                "chunk_index": chunk_idx,
                            },
                        ))
                        chunk_idx += 1
    return documents


def chunk_paragraph_custom(text: str, config: CargaConfig, base_metadata: dict) -> list[Document]:
    documents = []
    chunk_index = 0
    current_section = DEFAULT_SECTION_TITLE  # persiste entre páginas
    split_parrafos = re.compile(r'\n\s*\n+')

    for page_num, page_text in enumerate(text.split("\f"), start=1):
        if not page_text.strip():
            continue

        sections, current_section = segmentar_pagina_en_secciones(page_text, current_section)

        for title, content in sections:
            for segment, es_tabla in _split_preserving_tables(content):
                if es_tabla:
                    bloque = segment.strip()
                    if not bloque:
                        continue
                    documents.append(Document(
                        page_content=bloque,
                        metadata={**base_metadata, "seccion": title, "pagina": page_num, "chunk_index": chunk_index, "es_tabla": True},
                    ))
                    chunk_index += 1
                    continue

                for paragraph in split_parrafos.split(segment):
                    paragraph = paragraph.strip()
                    if not paragraph:
                        continue

                    if len(paragraph) <= config.chunk_size:
                        documents.append(Document(
                            page_content=paragraph,
                            metadata={**base_metadata, "seccion": title, "pagina": page_num, "chunk_index": chunk_index},
                        ))
                        chunk_index += 1
                    else:
                        step = max(config.chunk_size - config.chunk_overlap, 1)
                        for start in range(0, len(paragraph), step):
                            piece = paragraph[start:start + config.chunk_size]
                            piece = piece.strip()
                            if not piece:
                                continue
                            documents.append(Document(
                                page_content=piece,
                                metadata={**base_metadata, "seccion": title, "pagina": page_num, "chunk_index": chunk_index},
                            ))
                            chunk_index += 1

    return documents


CHUNKERS = {
    "recursive": chunk_recursive,
    "fixed_size_overlap": chunk_fixed_size_overlap,
    "paragraph_custom": chunk_paragraph_custom,
}


def cargar_registro() -> dict:
    if REGISTRY_PATH.exists():
        with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def guardar_registro(registro: dict):
    with open(REGISTRY_PATH, "w", encoding="utf-8") as f:
        json.dump(registro, f, ensure_ascii=False, indent=2)


class _SentenceTransformerEmbeddings:
    """Adapter mínimo para usar sentence-transformers con CacheBackedEmbeddings de LangChain."""

    def __init__(self, model_name: str, model_kwargs: dict | None = None, encode_kwargs: dict | None = None):
        from sentence_transformers import SentenceTransformer
        self.model = SentenceTransformer(model_name, model_kwargs=model_kwargs or {})
        self._encode_kwargs = encode_kwargs or {}

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return self.model.encode(texts, convert_to_numpy=True, **self._encode_kwargs).tolist()

    def embed_query(self, text: str) -> list[float]:
        return self.model.encode(text, convert_to_numpy=True, **self._encode_kwargs).tolist()


def construir_embeddings(config: "CargaConfig") -> CacheBackedEmbeddings:
    if config.embedding_model in LOCAL_MODELS:
        extra = LOCAL_MODELS[config.embedding_model]
        base = _SentenceTransformerEmbeddings(model_name=config.embedding_model, **extra)
    else:
        base = GoogleGenerativeAIEmbeddings(model=f"models/{config.embedding_model}")

    prefix = config.embedding_model.encode()
    return CacheBackedEmbeddings.from_bytes_store(
        underlying_embeddings=base,
        document_embedding_cache=LocalFileStore(str(EMBEDDINGS_CACHE_DIR)),
        query_embedding_cache=True,
        key_encoder=lambda x: hashlib.sha256(prefix + (x if isinstance(x, bytes) else x.encode())).hexdigest(),
    )


def es_error_de_rate_limit(error: Exception) -> bool:
    error_text = str(error).upper()
    return any(token in error_text for token in ("RESOURCE_EXHAUSTED", "RATE LIMIT", "429", "QUOTA"))


def es_error_de_cuota_agotada(error: Exception) -> bool:
    error_text = str(error).upper()
    patrones = (
        "GENERATEREQUESTSPERDAYPERPROJECTPERMODEL-FREETIER",
        "PERDAYPERPROJECTPERMODEL",
        "GENERATE_CONTENT_FREE_TIER_REQUESTS",
        "CHECK YOUR PLAN AND BILLING DETAILS",
        "CURRENT QUOTA",
    )
    return "RESOURCE_EXHAUSTED" in error_text and any(patron in error_text for patron in patrones)


def construir_chunk_ids(filename: str, sha256: str, chunks: list[Document]) -> list[str]:
    version = sha256 or "sin-sha"
    return [f"{filename}:{version}:{chunk.metadata['chunk_index']}" for chunk in chunks]


def agregar_documentos_en_lotes(
    vectorstore: Chroma,
    chunks: list[Document],
    chunk_ids: list[str],
    config: CargaConfig,
):
    total_batches = (len(chunks) + config.embedding_batch_size - 1) // config.embedding_batch_size

    for batch_index, start in enumerate(range(0, len(chunks), config.embedding_batch_size), start=1):
        batch_chunks = chunks[start:start + config.embedding_batch_size]
        batch_ids = chunk_ids[start:start + config.embedding_batch_size]

        for attempt in range(1, config.max_retries + 2):
            try:
                print(
                    f"[carga]   -> Batch {batch_index}/{total_batches}: {len(batch_chunks)} chunks "
                    f"(intento {attempt}/{config.max_retries + 1})"
                )
                vectorstore.add_documents(batch_chunks, ids=batch_ids)
                break
            except Exception as error:
                if not es_error_de_rate_limit(error) or attempt > config.max_retries:
                    raise

                print(
                    f"[carga]   -> Rate limit detectado en batch {batch_index}/{total_batches}: {error}. "
                    f"Esperando {config.retry_wait_seconds}s antes de reintentar..."
                )
                time.sleep(config.retry_wait_seconds)


def procesar_lote_documentos(
    archivos: list[str],
    config: CargaConfig | None = None,
) -> list[tuple[str, bool]]:
    config = config or CargaConfig()
    if config.embedding_model not in LOCAL_MODELS and not os.environ.get("GOOGLE_API_KEY"):
        raise EnvironmentError("GOOGLE_API_KEY no encontrada en el entorno. Configurá el .env.")

    if config.chunking_technique not in CHUNKERS:
        raise ValueError(f"chunking_technique inválido: '{config.chunking_technique}'. Opciones: {list(CHUNKERS.keys())}")

    if config.chunk_overlap >= config.chunk_size:
        raise ValueError(f"chunk_overlap ({config.chunk_overlap}) debe ser menor que chunk_size ({config.chunk_size})")

    if config.embedding_batch_size <= 0:
        raise ValueError(f"embedding_batch_size ({config.embedding_batch_size}) debe ser mayor a 0")

    if config.max_retries < 0:
        raise ValueError(f"max_retries ({config.max_retries}) no puede ser negativo")

    if config.retry_wait_seconds <= 0:
        raise ValueError(f"retry_wait_seconds ({config.retry_wait_seconds}) debe ser mayor a 0")

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    EMBEDDINGS_CACHE_DIR.mkdir(parents=True, exist_ok=True)

    print(f"[carga] Inicializando modelos y ChromaDB para {len(archivos)} archivo(s)...")
    embeddings = construir_embeddings(config)
    vectorstore = Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=str(DATA_DIR),
        embedding_function=embeddings,
    )

    registro = cargar_registro()
    chunker = CHUNKERS[config.chunking_technique]
    resultados = []

    for filename in archivos:
        if filename not in registro:
            print(f"[carga] ERROR: {filename} no está en el registro.")
            resultados.append((filename, False))
            continue
            
        entry = registro[filename]
        toon_path = ROOT / entry.get("toon", "")
        if not toon_path.exists():
            print(f"[carga] ERROR: El archivo {toon_path} no existe.")
            resultados.append((filename, False))
            continue

        materia = entry.get("materia", "General")
        sha256 = entry.get("sha256", "")
        
        try:
            with open(toon_path, "r", encoding="utf-8") as f:
                toon_content = f.read()

            parsed = parsear_toon(toon_content)
            content = parsed["content"]

            print(f"[carga] Procesando {filename}  (Sección: {materia})...")

            base_metadata = {"materia": materia, "documento": filename, "sha256": sha256}
            chunks = chunker(content, config, base_metadata)
            chunk_ids = construir_chunk_ids(filename, sha256, chunks)

            existing = vectorstore.get(where={"documento": filename})
            if existing and existing["ids"]:
                vectorstore.delete(ids=existing["ids"])

            agregar_documentos_en_lotes(vectorstore, chunks, chunk_ids, config)

            carga_info = {
                "fecha_procesamiento": datetime.now().isoformat(),
                "cantidad_chunks": len(chunks),
                "params": {
                    "chunk_size": config.chunk_size,
                    "chunk_overlap": config.chunk_overlap,
                    "embedding_model": config.embedding_model,
                    "chunking_technique": config.chunking_technique,
                    "embedding_batch_size": config.embedding_batch_size,
                    "max_retries": config.max_retries,
                    "retry_wait_seconds": config.retry_wait_seconds,
                },
                "state": "incorporado",
                "error_message": None,
            }
            
            registro[filename]["cargado_en_chroma"] = True
            registro[filename]["carga"] = carga_info
            
            print(f"[carga]   -> OK: {len(chunks)} chunks ingresados a ChromaDB")
            resultados.append((filename, True))

        except Exception as e:
            print(f"[carga] ERROR procesando {filename}: {e}")
            registro[filename]["cargado_en_chroma"] = False
            registro[filename]["carga"] = {
                "fecha_procesamiento": datetime.now().isoformat(),
                "cantidad_chunks": 0,
                "params": {
                    "chunk_size": config.chunk_size,
                    "chunk_overlap": config.chunk_overlap,
                    "embedding_model": config.embedding_model,
                    "chunking_technique": config.chunking_technique,
                    "embedding_batch_size": config.embedding_batch_size,
                    "max_retries": config.max_retries,
                    "retry_wait_seconds": config.retry_wait_seconds,
                },
                "state": "error",
                "error_message": str(e),
            }
            resultados.append((filename, False))

    guardar_registro(registro)
    return resultados


def main():
    parser = argparse.ArgumentParser(description="Carga un lote de documentos en ChromaDB para RAG")
    parser.add_argument("--archivos", nargs="+", required=True, help="Lista de nombre de archivos (ej. tp1.pdf) registrados")
    parser.add_argument("--chunk-size", type=int, default=512)
    parser.add_argument("--chunk-overlap", type=int, default=50)
    parser.add_argument("--embedding-model", type=str, default="gemini-embedding-001")
    parser.add_argument("--embedding-batch-size", type=int, default=20)
    parser.add_argument("--max-retries", type=int, default=3)
    parser.add_argument("--retry-wait-seconds", type=int, default=60)
    parser.add_argument(
        "--chunking-technique",
        type=str,
        choices=["recursive", "fixed_size_overlap", "paragraph_custom"],
        default="recursive",
    )

    args = parser.parse_args()

    config = CargaConfig(
        chunk_size=args.chunk_size,
        chunk_overlap=args.chunk_overlap,
        embedding_model=args.embedding_model,
        chunking_technique=args.chunking_technique,
        embedding_batch_size=args.embedding_batch_size,
        max_retries=args.max_retries,
        retry_wait_seconds=args.retry_wait_seconds,
    )

    procesar_lote_documentos(
        archivos=args.archivos,
        config=config,
    )


if __name__ == "__main__":
    main()
