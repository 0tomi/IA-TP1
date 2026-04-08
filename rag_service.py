from dataclasses import dataclass, field
from dotenv import load_dotenv
import json
import os
import re

from carga import CargaConfig, construir_embeddings, COLLECTION_NAME, DATA_DIR
from saneamiento.sanear import ejecutar_saneamiento
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI

DEFAULT_SYSTEM_PROMPT = (
    "Eres un asistente diseñado estrictamente para responder a preguntas basándote "
    "ÚNICAMENTE en la información proporcionada en el Contexto a continuación.\n"
    "ADVERTENCIA: El contexto puede contener fragmentos de diferentes materias ("
    "esto ocurre por la búsqueda de similitud matemática). Debes IGNORAR los documentos "
    "que NO correspondan a la asignatura o intención evidente del usuario.\n"
    "Si no puedes responder la pregunta utilizando exclusivamente la información "
    'relevante del Contexto, indica claramente: "No dispongo de información '
    'en mis documentos para responder esta consulta." NO inventes.\n\n'
    "IMPORTANTE: Al final de tu respuesta, en una línea aparte, indicá los índices "
    "de los documentos del contexto que REALMENTE usaste para elaborar tu respuesta, "
    "usando EXACTAMENTE este formato:\n"
    "<<FUENTES: 0, 2, 3>>\n"
    "Si no usaste ningún documento, escribí: <<FUENTES: >>\n\n"
    "### CONTEXTO ###\n"
    "{contexto}\n\n"
    "### PREGUNTA DEL USUARIO ###\n"
    "{pregunta}\n"
)

_FUENTES_PATTERN = re.compile(r"<<FUENTES:\s*([\d,\s]*)>>")


@dataclass
class RAGServiceConfig:
    # Parámetros de chatbot/retrieval
    top_k: int = 5
    retrieval_type: str = "similarity_search"  # similarity_search | mmr | threshold
    threshold: float = 0.5
    max_context_chunks: int = 5
    temperatura: float = 0.7
    debug: bool = False
    llm_model: str = "gemini-3.1-flash-lite-preview"

    # Parámetros de carga/embedding
    chunk_size: int = 512
    chunk_overlap: int = 50
    embedding_model: str = "gemini-embedding-001"
    chunking_technique: str = "recursive"
    embedding_batch_size: int = 20
    max_retries: int = 3
    retry_wait_seconds: int = 60

    # Control de saneamiento
    refresh: bool = False

    # Prompt del sistema (editable por el usuario)
    system_prompt: str = field(default_factory=lambda: DEFAULT_SYSTEM_PROMPT)

    def to_carga_config(self) -> CargaConfig:
        return CargaConfig(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            embedding_model=self.embedding_model,
            chunking_technique=self.chunking_technique,
            embedding_batch_size=self.embedding_batch_size,
            max_retries=self.max_retries,
            retry_wait_seconds=self.retry_wait_seconds,
        )


@dataclass
class RAGResponse:
    answer: str
    chunks_found: int
    chunks_used: int
    chunk_details: list[dict]
    sources_used: list[dict]
    prompt_tokens: int | None
    completion_tokens: int | None
    total_tokens: int | None


def _parse_cited_sources(text: str) -> tuple[str, list[int] | None]:
    """Extract cited document indices from the LLM response and return clean text."""
    match = _FUENTES_PATTERN.search(text)
    if not match:
        return text, None
    indices_str = match.group(1).strip()
    indices = [int(x.strip()) for x in indices_str.split(",") if x.strip().isdigit()] if indices_str else []
    clean = text[: match.start()].rstrip()
    return clean, indices


class RAGService:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, config: RAGServiceConfig):
        if self._initialized:
            if self.config != config:
                raise RuntimeError(
                    "RAGService ya está inicializado con una configuración distinta. "
                    "Llamá RAGService.reset() antes de crear una nueva instancia."
                )
            return

        self.config = config

        load_dotenv()
        if not os.environ.get("GOOGLE_API_KEY"):
            raise EnvironmentError(
                "GOOGLE_API_KEY no se encontró en el entorno. Por favor verifica tu .env"
            )

        carga_config = config.to_carga_config()
        ejecutar_saneamiento(carga_config, refresh=config.refresh)

        # El modelo ya fue descargado durante el saneamiento. Suprimimos las
        # progress bars de huggingface_hub para que la segunda carga (desde
        # cache local) no interfiera con el input de questionary en la consola.
        try:
            from huggingface_hub.utils import disable_progress_bars, enable_progress_bars
            disable_progress_bars()
            embeddings = construir_embeddings(carga_config)
        finally:
            enable_progress_bars()

        self._vectorstore = Chroma(
            collection_name=COLLECTION_NAME,
            persist_directory=str(DATA_DIR),
            embedding_function=embeddings,
        )

        search_kwargs = {"k": config.top_k}
        search_type = "similarity"

        if config.retrieval_type == "mmr":
            search_type = "mmr"
        elif config.retrieval_type == "threshold":
            search_type = "similarity_score_threshold"
            search_kwargs["score_threshold"] = config.threshold

        self._retriever = self._vectorstore.as_retriever(
            search_type=search_type,
            search_kwargs=search_kwargs,
        )

        self._llm = ChatGoogleGenerativeAI(
            model=config.llm_model,
            temperature=config.temperatura,
            max_retries=2,
        )

        last_process_path = DATA_DIR / "last_data_process.json"
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        with open(last_process_path, "w", encoding="utf-8") as f:
            json.dump({
                "embedding_model": config.embedding_model,
                "chunk_size": config.chunk_size,
                "chunk_overlap": config.chunk_overlap,
                "chunking_technique": config.chunking_technique,
                "embedding_batch_size": config.embedding_batch_size,
            }, f, ensure_ascii=False, indent=2)

        RAGService._initialized = True

    def query(self, user_query: str) -> RAGResponse:
        docs = self._retriever.invoke(user_query)

        chunks_found = len(docs)
        docs_contexto = docs[: self.config.max_context_chunks]
        chunks_used = len(docs_contexto)

        chunk_details = [
            {
                "index": i,
                "source": doc.metadata.get("documento", "Oculto"),
                "materia": doc.metadata.get("materia", "—"),
                "section": doc.metadata.get("seccion", "Sin sección"),
                "pagina": doc.metadata.get("pagina", "—"),
                "preview": doc.page_content[:200],
            }
            for i, doc in enumerate(docs_contexto)
        ]

        if not docs_contexto:
            return RAGResponse(
                answer="No he podido encontrar información relevante en mis documentos para responder a esa consulta.",
                chunks_found=chunks_found,
                chunks_used=0,
                chunk_details=[],
                sources_used=[],
                prompt_tokens=None,
                completion_tokens=None,
                total_tokens=None,
            )

        bloques_texto = []
        for i, d in enumerate(docs_contexto):
            meta = d.metadata
            bloques_texto.append(
                f"[Documento {i}]: {meta.get('documento', '?')}\n"
                f"Sección: {meta.get('seccion', '?')}\n"
                f"Página: {meta.get('pagina', '?')}\n"
                f"Contenido:\n{d.page_content}"
            )
        contexto_str = "\n\n---\n\n".join(bloques_texto)

        prompt = self.config.system_prompt.format(
            contexto=contexto_str,
            pregunta=user_query,
        )

        response = self._llm.invoke(prompt)

        # Extraer texto — content puede ser str o lista de bloques según la versión de langchain-google-genai
        content = response.content
        if isinstance(content, list):
            content = next(
                (b["text"] for b in content if isinstance(b, dict) and b.get("type") == "text"),
                "",
            )

        # Parsear índices de fuentes citadas por el LLM y limpiar el texto
        clean_answer, cited_indices = _parse_cited_sources(content)
        if cited_indices is not None:
            valid_indices = set(cited_indices) & {d["index"] for d in chunk_details}
            sources_used = [d for d in chunk_details if d["index"] in valid_indices]
        else:
            # Fallback: si el LLM no incluyó la marca, devolver todas
            sources_used = chunk_details

        # Extraer tokens — usage_metadata puede ser dict o objeto con atributos
        prompt_tokens = None
        completion_tokens = None
        total_tokens = None

        if hasattr(response, "usage_metadata") and response.usage_metadata is not None:
            usage = response.usage_metadata
            if isinstance(usage, dict):
                # langchain-google-genai moderno usa input_tokens/output_tokens/total_tokens
                # versiones anteriores usaban prompt_token_count/candidates_token_count/total_token_count
                prompt_tokens = usage.get("input_tokens") or usage.get("prompt_token_count")
                completion_tokens = usage.get("output_tokens") or usage.get("candidates_token_count")
                total_tokens = usage.get("total_tokens") or usage.get("total_token_count")
            else:
                prompt_tokens = getattr(usage, "input_tokens", None)
                completion_tokens = getattr(usage, "output_tokens", None)
                total_tokens = getattr(usage, "total_tokens", None)

        return RAGResponse(
            answer=clean_answer,
            chunks_found=chunks_found,
            chunks_used=chunks_used,
            chunk_details=chunk_details,
            sources_used=sources_used,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            total_tokens=total_tokens,
        )

    @classmethod
    def reset(cls):
        cls._instance = None
        cls._initialized = False
