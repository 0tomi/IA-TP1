from dataclasses import dataclass
import json, os, re, argparse
from datetime import datetime
from pathlib import Path
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
REGISTRY_PATH = DATA_DIR / "registry.json"
COLLECTION_NAME = "rag_tp1"


@dataclass
class CargaConfig:
    chunk_size: int = 512
    chunk_overlap: int = 50
    embedding_model: str = "gemini-embedding-001"
    chunking_technique: str = "recursive"  # "recursive" | "fixed_size_overlap" | "paragraph_custom"


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
    # Build a map from char position to section by scanning full text
    section_at_pos = {}
    current_section = ""
    pos = 0
    for line in text.split("\n"):
        if es_titulo(line):
            current_section = line.strip()
        section_at_pos[pos] = current_section
        pos += len(line) + 1  # +1 for the \n

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.chunk_size,
        chunk_overlap=config.chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    raw_chunks = splitter.split_text(text)

    # For each chunk, find its start position in the original text
    documents = []
    search_start = 0
    for i, chunk in enumerate(raw_chunks):
        chunk_pos = text.find(chunk[:80], search_start)
        if chunk_pos == -1:
            chunk_pos = text.find(chunk[:40], search_start)
        if chunk_pos == -1:
            print(f"[carga] WARN: no se encontró posición exacta del chunk {i}, usando aproximación")
            chunk_pos = search_start

        # Find closest section at or before chunk_pos
        seccion = ""
        for p in sorted(section_at_pos.keys()):
            if p <= chunk_pos:
                seccion = section_at_pos[p]
            else:
                break

        documents.append(Document(
            page_content=chunk,
            metadata={**base_metadata, "seccion": seccion, "chunk_index": i},
        ))
        search_start = max(0, chunk_pos + len(chunk) - config.chunk_overlap)

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


def procesar_documento(
    toon_content: str,
    filename: str,
    sha256: str,
    materia: str,
    config: CargaConfig | None = None,
) -> dict:
    if not os.environ.get("GOOGLE_API_KEY"):
        raise EnvironmentError("GOOGLE_API_KEY no encontrada en el entorno. Configurá el .env.")

    config = config or CargaConfig()

    if config.chunking_technique not in CHUNKERS:
        raise ValueError(
            f"chunking_technique inválido: '{config.chunking_technique}'. "
            f"Opciones: {list(CHUNKERS.keys())}"
        )

    if config.chunk_overlap >= config.chunk_size:
        raise ValueError(
            f"chunk_overlap ({config.chunk_overlap}) debe ser menor que chunk_size ({config.chunk_size})"
        )

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    try:
        parsed = parsear_toon(toon_content)
        content = parsed["content"]

        print(f"[carga] Procesando {filename}...")

        chunker = CHUNKERS[config.chunking_technique]
        base_metadata = {"materia": materia, "documento": filename, "sha256": sha256}
        chunks = chunker(content, config, base_metadata)

        embeddings = GoogleGenerativeAIEmbeddings(model=f"models/{config.embedding_model}")
        vectorstore = Chroma(
            collection_name=COLLECTION_NAME,
            persist_directory=str(DATA_DIR),
            embedding_function=embeddings,
        )
        existing = vectorstore.get(where={"documento": filename})
        if existing and existing["ids"]:
            vectorstore.delete(ids=existing["ids"])

        vectorstore.add_documents(chunks)

    except Exception as e:
        print(f"[carga] ERROR procesando {filename}: {e}")

        registro = cargar_registro()
        if filename not in registro:
            registro[filename] = {"sha256": sha256}

        registro[filename]["cargado_en_chroma"] = False
        registro[filename]["carga"] = {
            "fecha_procesamiento": datetime.now().isoformat(),
            "cantidad_chunks": 0,
            "params": {
                "chunk_size": config.chunk_size,
                "chunk_overlap": config.chunk_overlap,
                "embedding_model": config.embedding_model,
                "chunking_technique": config.chunking_technique,
            },
            "state": "error",
            "error_message": str(e),
        }
        guardar_registro(registro)
        raise

    carga_info = {
        "fecha_procesamiento": datetime.now().isoformat(),
        "cantidad_chunks": len(chunks),
        "params": {
            "chunk_size": config.chunk_size,
            "chunk_overlap": config.chunk_overlap,
            "embedding_model": config.embedding_model,
            "chunking_technique": config.chunking_technique,
        },
        "state": "incorporado",
        "error_message": None,
    }

    registro = cargar_registro()
    if filename not in registro:
        registro[filename] = {"sha256": sha256}

    registro[filename]["cargado_en_chroma"] = True
    registro[filename]["carga"] = carga_info
    guardar_registro(registro)

    print(f"[carga] {filename} OK — {len(chunks)} chunks generados")
    return carga_info


def main():
    parser = argparse.ArgumentParser(description="Carga documentos .toon en ChromaDB para RAG")
    parser.add_argument("--toon-content", required=True, help="Contenido TOON del documento")
    parser.add_argument("--filename", required=True, help="Nombre original del archivo")
    parser.add_argument("--sha256", required=True, help="Hash SHA256 del documento")
    parser.add_argument("--materia", required=True, help="Nombre de la materia")
    parser.add_argument("--chunk-size", type=int, default=512)
    parser.add_argument("--chunk-overlap", type=int, default=50)
    parser.add_argument("--embedding-model", type=str, default="gemini-embedding-001")
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
    )

    procesar_documento(
        toon_content=args.toon_content,
        filename=args.filename,
        sha256=args.sha256,
        materia=args.materia,
        config=config,
    )


if __name__ == "__main__":
    main()
