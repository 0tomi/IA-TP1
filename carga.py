from dataclasses import dataclass
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
        "model_kwargs": {"torch_dtype": "float16"},
        "encode_kwargs": {"normalize_embeddings": True},
    },
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


def es_titulo(linea: str) -> bool:
    linea = linea.strip()
    if not linea or len(linea) >= 80:
        return False
    if linea[0].islower():
        return False
    patron = r'^(?:\d+[\.\)]\s*|Cap[ií]tulo\s+|Unidad\s+|Tema\s+)?[A-ZÁÉÍÓÚÑÜ][\w\s\-:,\.]{2,78}$'
    return bool(re.match(patron, linea))


def chunk_recursive(text: str, config: CargaConfig, base_metadata: dict) -> list[Document]:
    # Separamos el texto por secciones (títulos) para evitar rastrear posiciones manualmente
    sections = []
    lines = text.split("\n")
    current_title = "Intro / Sin título"
    current_lines = []

    for line in lines:
        if es_titulo(line):
            if current_lines:
                sections.append((current_title, "\n".join(current_lines)))
            current_title = line.strip()
            current_lines = [line]  # Incluimos el título como parte del contenido para contexto
        else:
            current_lines.append(line)
    
    if current_lines:
        sections.append((current_title, "\n".join(current_lines)))

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.chunk_size,
        chunk_overlap=config.chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""],
    )

    documents = []
    chunk_idx = 0
    for title, content in sections:
        # Realizamos el chunking sobre cada sección de forma aislada y precisa
        raw_chunks = splitter.split_text(content)
        for chunk in raw_chunks:
            documents.append(Document(
                page_content=chunk,
                metadata={**base_metadata, "seccion": title, "chunk_index": chunk_idx},
            ))
            chunk_idx += 1

    return documents


def chunk_fixed_size_overlap(text: str, config: CargaConfig, base_metadata: dict) -> list[Document]:
    splitter = CharacterTextSplitter(
        separator="",
        chunk_size=config.chunk_size,
        chunk_overlap=config.chunk_overlap,
    )
    raw_chunks = splitter.split_text(text)
    return [
        Document(page_content=chunk, metadata={**base_metadata, "seccion": "", "chunk_index": i})
        for i, chunk in enumerate(raw_chunks)
    ]


def chunk_paragraph_custom(text: str, config: CargaConfig, base_metadata: dict) -> list[Document]:
    paragraphs = text.split("\n\n")
    current_section = ""
    documents = []
    chunk_index = 0

    for paragraph in paragraphs:
        paragraph = paragraph.strip()
        if not paragraph:
            continue

        if es_titulo(paragraph):
            current_section = paragraph
            continue

        if len(paragraph) <= config.chunk_size:
            documents.append(Document(
                page_content=paragraph,
                metadata={**base_metadata, "seccion": current_section, "chunk_index": chunk_index},
            ))
            chunk_index += 1
        else:
            # Hard-cut into pieces of chunk_size, no overlap
            for start in range(0, len(paragraph), config.chunk_size):
                piece = paragraph[start:start + config.chunk_size]
                documents.append(Document(
                    page_content=piece,
                    metadata={**base_metadata, "seccion": current_section, "chunk_index": chunk_index},
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

    import hashlib
    prefix = config.embedding_model.encode()
    return CacheBackedEmbeddings.from_bytes_store(
        underlying_embeddings=base,
        document_embedding_cache=LocalFileStore(str(EMBEDDINGS_CACHE_DIR)),
        key_encoder=lambda x: hashlib.sha256(prefix + (x if isinstance(x, bytes) else x.encode())).hexdigest(),
    )


def es_error_de_rate_limit(error: Exception) -> bool:
    error_text = str(error).upper()
    return any(token in error_text for token in ("RESOURCE_EXHAUSTED", "RATE LIMIT", "429", "QUOTA"))


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
