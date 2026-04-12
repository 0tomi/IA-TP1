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

DEFAULT_SECTION_TITLE = "General"

# Detecta bloques de tabla Markdown (sincronizado con sanear.py)
_RE_MD_TABLE = re.compile(r'(?:^[ \t]*\|[^\n]+\|[ \t]*\n?)+', flags=re.MULTILINE)


def _split_preserving_tables(text: str) -> list[tuple[str, bool]]:
    """Separa texto en segmentos (contenido, es_tabla). Tablas = chunk atomico."""
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


@dataclass
class CargaConfig:
    chunk_size: int = 512
    chunk_overlap: int = 50
    embedding_model: str = "gemini-embedding-001"
    chunking_technique: str = "recursive"  # "recursive" | "fixed_size_overlap" | "paragraph_custom"
    embedding_batch_size: int = 20
    max_retries: int = 3
    retry_wait_seconds: int = 60


def chunk_recursive(paginas: list[dict], config: CargaConfig, base_metadata: dict) -> list[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.chunk_size,
        chunk_overlap=config.chunk_overlap,
        separators=["\n\n", ". ", "; ", ": ", "\n", " ", ""],
    )

    documents = []
    chunk_idx = 0

    for pagina in paginas:
        page_num = pagina["numero"]
        page_text = pagina["contenido"].strip()
        if not page_text:
            continue

        for segment, es_tabla in _split_preserving_tables(page_text):
            if es_tabla:
                bloque = segment.strip()
                if bloque:
                    documents.append(Document(
                        page_content=bloque,
                        metadata={**base_metadata, "seccion": DEFAULT_SECTION_TITLE, "pagina": page_num, "chunk_index": chunk_idx, "es_tabla": True},
                    ))
                    chunk_idx += 1
            else:
                for chunk in splitter.split_text(segment):
                    chunk = chunk.strip()
                    if not chunk:
                        continue
                    documents.append(Document(
                        page_content=chunk,
                        metadata={**base_metadata, "seccion": DEFAULT_SECTION_TITLE, "pagina": page_num, "chunk_index": chunk_idx},
                    ))
                    chunk_idx += 1

    return documents


def chunk_fixed_size_overlap(paginas: list[dict], config: CargaConfig, base_metadata: dict) -> list[Document]:
    splitter = CharacterTextSplitter(
        separator="",
        chunk_size=config.chunk_size,
        chunk_overlap=config.chunk_overlap,
    )
    documents = []
    chunk_idx = 0

    for pagina in paginas:
        page_num = pagina["numero"]
        page_text = pagina["contenido"].strip()
        if not page_text:
            continue

        for segment, es_tabla in _split_preserving_tables(page_text):
            if es_tabla:
                bloque = segment.strip()
                if bloque:
                    documents.append(Document(
                        page_content=bloque,
                        metadata={**base_metadata, "seccion": DEFAULT_SECTION_TITLE, "pagina": page_num, "chunk_index": chunk_idx, "es_tabla": True},
                    ))
                    chunk_idx += 1
            else:
                for chunk in splitter.split_text(segment):
                    chunk = chunk.strip()
                    if not chunk:
                        continue
                    documents.append(Document(
                        page_content=chunk,
                        metadata={**base_metadata, "seccion": DEFAULT_SECTION_TITLE, "pagina": page_num, "chunk_index": chunk_idx},
                    ))
                    chunk_idx += 1
    return documents


def chunk_paragraph_custom(paginas: list[dict], config: CargaConfig, base_metadata: dict) -> list[Document]:
    documents = []
    chunk_index = 0
    split_parrafos = re.compile(r'\n\s*\n+')

    for pagina in paginas:
        page_num = pagina["numero"]
        page_text = pagina["contenido"].strip()
        if not page_text:
            continue

        for segment, es_tabla in _split_preserving_tables(page_text):
            if es_tabla:
                bloque = segment.strip()
                if bloque:
                    documents.append(Document(
                        page_content=bloque,
                        metadata={**base_metadata, "seccion": DEFAULT_SECTION_TITLE, "pagina": page_num, "chunk_index": chunk_index, "es_tabla": True},
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
                        metadata={**base_metadata, "seccion": DEFAULT_SECTION_TITLE, "pagina": page_num, "chunk_index": chunk_index},
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
                            metadata={**base_metadata, "seccion": DEFAULT_SECTION_TITLE, "pagina": page_num, "chunk_index": chunk_index},
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
        json_rel = entry.get("json_path", "")
        json_file = ROOT / json_rel
        if not json_file.exists():
            print(f"[carga] ERROR: El archivo {json_file} no existe.")
            resultados.append((filename, False))
            continue

        materia = entry.get("materia", "General")
        sha256 = entry.get("sha256", "")
        
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                parsed = json.load(f)

            paginas = parsed["paginas"]

            print(f"[carga] Procesando {filename}  (Sección: {materia})...")

            base_metadata = {"materia": materia, "documento": filename, "sha256": sha256}
            chunks = chunker(paginas, config, base_metadata)
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
