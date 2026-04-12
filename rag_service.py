from dataclasses import dataclass, field, replace
from dotenv import load_dotenv
import json
import os
import re
import time
import unicodedata
from urllib.error import URLError
from urllib.request import urlopen

from carga import (
    CargaConfig,
    construir_embeddings,
    COLLECTION_NAME,
    DATA_DIR,
    es_error_de_cuota_agotada,
    es_error_de_rate_limit,
)
from saneamiento.sanear import ejecutar_saneamiento
from langchain_classic.chains.combine_documents.stuff import create_stuff_documents_chain
from langchain_chroma import Chroma
from langchain_core.output_parsers.base import BaseOutputParser
from langchain_core.outputs import Generation
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

OLLAMA_BASE_URL = "http://127.0.0.1:11434"

DEFAULT_SYSTEM_PROMPT = (
    "Eres un asistente diseñado estrictamente para responder a preguntas basándote "
    "ÚNICAMENTE en la información proporcionada en el Contexto a continuación.\n"
    "Sintetiza la información de TODOS los fragmentos proporcionados proactivamente. "
    "Si te piden comparar o buscar puntos en común, cruza los datos de los distintos "
    "fragmentos obligatoriamente para formar una sola respuesta consolidada y completa.\n"
    "Responde con voz directa y segura, como si dominaras el tema, pero sin salirte "
    "jamás de la información disponible.\n"
    "NO menciones el Contexto, los fragmentos recuperados, los documentos, ni expliques "
    "tu proceso de búsqueda o validación, salvo que el usuario te lo pida explícitamente.\n"
    "Si la evidencia alcanza para responder el núcleo de la pregunta, respóndelo sin "
    "dudar ni pedir más información.\n"
    "Si el Contexto permite responder solo una parte de la pregunta, responde esa parte "
    "con claridad y aclara brevemente qué dato puntual falta o qué parte no está respaldada.\n"
    "Si no puedes responder la pregunta del usuario utilizando exclusivamente la "
    'información del Contexto, debes indicar claramente "No dispongo de información '
    'en mis documentos para responder esta consulta."\n'
    "Reserva esa frase solo para los casos en los que ni siquiera el núcleo de la "
    "respuesta esté respaldado.\n"
    "NO inventes respuestas, NO completes huecos con conocimiento externo y NO afirmes "
    "que un dato existe si en el Contexto aparece incompleto, truncado o ambiguo.\n"
    "Cuando respondas, prioriza ser preciso, citar condiciones o diferencias relevantes y "
    "mantenerte dentro de lo que efectivamente dicen los fragmentos recuperados.\n"
    "Evita muletillas como 'según el contexto', 'el documento dice', 'la información proporcionada' "
    "o equivalentes.\n\n"
    "### CONTEXTO ###\n"
    "{contexto}\n\n"
    "### PREGUNTA DEL USUARIO ###\n"
    "{pregunta}\n"
)


@dataclass
class RAGServiceConfig:
    # Parámetros de chatbot/retrieval
    top_k: int = 5
    retrieval_type: str = "similarity_search"  # similarity_search | mmr | threshold
    threshold: float = 0.5
    max_context_chunks: int = 5
    temperatura: float = 1.0
    debug: bool = False
    llm_provider: str = "google"
    llm_model: str = "gemini-3.1-flash-lite-preview"

    # Parámetros de carga/embedding
    chunk_size: int = 300
    chunk_overlap: int = 30
    embedding_model: str = "gemini-embedding-001"
    chunking_technique: str = "fixed_size_overlap"
    embedding_batch_size: int = 20
    max_retries: int = 3
    retry_wait_seconds: int = 60
    include_metadata_in_embedding: bool = True

    # Control de preparacion de datos
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
            include_metadata_in_embedding=self.include_metadata_in_embedding,
        )


@dataclass
class RAGResponse:
    answer: str
    chunks_found: int
    chunks_used: int
    chunk_details: list[dict]
    prompt_tokens: int | None
    completion_tokens: int | None
    total_tokens: int | None


class _RawLLMMessageOutputParser(BaseOutputParser):
    """
    Parser "passthrough" para chains de documentos.

    Contexto importante:
    - Nosotros NO necesitamos convertir la respuesta del LLM a `str`.
    - Pero `create_stuff_documents_chain(...)`, por default, usa un parser de texto
      (`StrOutputParser`) y termina devolviendo solo string.
    - Si dejamos ese default, perdemos el `AIMessage` crudo y su `usage_metadata`
      (tokens de entrada/salida/total).

    ¿Qué hace este parser?
    - Mantiene la salida "cruda" cuando está disponible (`Generation.message`).
    - Si el wrapper no entrega mensaje, cae a `Generation.text`.

    Así, en `_ejecutar_query` podemos seguir leyendo:
    - `response.content`
    - `response.usage_metadata` (cuando el backend lo provee)
    """

    @property
    def _type(self) -> str:
        return "raw_llm_message_output_parser"

    def parse(self, text: str):
        return text

    def parse_result(self, result: list[Generation], *, partial: bool = False):
        # `result` viene del chain: tomamos solo la primera generación.
        # Priorizamos devolver el mensaje crudo para no perder metadata de uso.
        if not result:
            return ""
        first = result[0]
        if hasattr(first, "message"):
            return first.message
        return first.text


def _guardar_last_data_process(config: RAGServiceConfig) -> None:
    last_process_path = DATA_DIR / "last_data_process.json"
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(last_process_path, "w", encoding="utf-8") as f:
        json.dump({
            "embedding_model": config.embedding_model,
            "chunk_size": config.chunk_size,
            "chunk_overlap": config.chunk_overlap,
            "chunking_technique": config.chunking_technique,
            "embedding_batch_size": config.embedding_batch_size,
            "include_metadata_in_embedding": config.include_metadata_in_embedding,
        }, f, ensure_ascii=False, indent=2)


def preparar_datos_rag(config: RAGServiceConfig) -> None:
    # El saneamiento puede borrar /data, asi que soltamos cualquier cliente
    # de Chroma abierto en este proceso antes de tocar el storage.
    RAGService.reset()
    ejecutar_saneamiento(config.to_carga_config(), refresh=config.refresh)
    _guardar_last_data_process(config)


class RAGService:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def create(cls, config: RAGServiceConfig) -> "RAGService":
        preparar_datos_rag(config)
        return cls(config)

    def __init__(self, config: RAGServiceConfig):
        runtime_config = self._runtime_config(config)
        if self._initialized:
            if self.config != runtime_config:
                raise RuntimeError(
                    "RAGService ya está inicializado con una configuración distinta. "
                    "Llamá RAGService.reset() antes de crear una nueva instancia."
                )
            return

        self.config = runtime_config

        load_dotenv()
        self._validar_llm_config()

        # El modelo ya fue descargado durante el saneamiento. Suprimimos las
        # progress bars de huggingface_hub para que la segunda carga (desde
        # cache local) no interfiera con el input de questionary en la consola.
        try:
            from huggingface_hub.utils import disable_progress_bars, enable_progress_bars
            disable_progress_bars()
            embeddings = construir_embeddings(self.config.to_carga_config())
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

        self._search_type = search_type
        self._search_kwargs = search_kwargs

        self._retriever = self._vectorstore.as_retriever(
            search_type=search_type,
            search_kwargs=search_kwargs,
        )

        self._llm = self._crear_llm()
        self._document_prompt = PromptTemplate.from_template(
            "Documento: {documento}\n"
            "Materia: {materia}\n"
            "Sección: {seccion}\n"
            "Página: {pagina}\n"
            "Contenido:\n{page_content}"
        )
        self._qa_prompt = PromptTemplate.from_template(self.config.system_prompt)
        self._document_chain = create_stuff_documents_chain(
            self._llm,
            self._qa_prompt,
            document_prompt=self._document_prompt,
            output_parser=_RawLLMMessageOutputParser(),
            document_variable_name="contexto",
        )
        RAGService._initialized = True

    @staticmethod
    def _runtime_config(config: RAGServiceConfig) -> RAGServiceConfig:
        return replace(config, refresh=False)

    def _validar_llm_config(self):
        if self.config.llm_provider == "google":
            if not os.environ.get("GOOGLE_API_KEY"):
                raise EnvironmentError(
                    "GOOGLE_API_KEY no se encontró en el entorno. Por favor verifica tu .env"
                )
            return

        if self.config.llm_provider == "ollama":
            try:
                from langchain_ollama import ChatOllama  # noqa: F401
            except ImportError as exc:
                raise ImportError(
                    "Falta la dependencia opcional 'langchain-ollama'. "
                    "Instalala antes de usar Ollama."
                ) from exc

            self._validar_ollama_local(self.config.llm_model)
            return

        raise ValueError(
            f"Proveedor LLM inválido: '{self.config.llm_provider}'. "
            "Usá 'google' o 'ollama'."
        )

    def _validar_ollama_local(self, model_name: str):
        try:
            with urlopen(f"{OLLAMA_BASE_URL}/api/tags", timeout=2) as response:
                payload = json.load(response)
        except URLError as exc:
            raise EnvironmentError(
                "No pude conectarme a Ollama en local. Verificá que esté instalado y en ejecución. "
                "Si usás la app de Ollama, abrila; si usás CLI, corré 'ollama serve'."
            ) from exc

        model_names = {
            model.get("name", "")
            for model in payload.get("models", [])
            if isinstance(model, dict)
        }
        if model_name not in model_names and f"{model_name}:latest" not in model_names:
            raise EnvironmentError(
                f"Ollama está disponible, pero no encontré el modelo '{model_name}'. "
                f"Descargalo con 'ollama pull {model_name}'."
            )

    def _crear_llm(self):
        if self.config.llm_provider == "google":
            return ChatGoogleGenerativeAI(
                model=self.config.llm_model,
                temperature=self.config.temperatura,
                max_retries=2,
            )

        if self.config.llm_provider == "ollama":
            from langchain_ollama import ChatOllama

            return ChatOllama(
                model=self.config.llm_model,
                temperature=self.config.temperatura,
            )

        raise ValueError(
            f"Proveedor LLM inválido: '{self.config.llm_provider}'. "
            "Usá 'google' o 'ollama'."
        )

    def query(self, user_query: str) -> RAGResponse:
        max_attempts = self.config.max_retries + 1
        for attempt in range(1, max_attempts + 1):
            try:
                return self._ejecutar_query(user_query)
            except Exception as e:
                if es_error_de_cuota_agotada(e):
                    print("[rag] Cuota agotada detectada; no se reintenta la query.")
                    raise
                if not es_error_de_rate_limit(e) or attempt >= max_attempts:
                    raise
                print(
                    f"[rag] Rate limit en query (intento {attempt}/{max_attempts}), "
                    f"esperando {self.config.retry_wait_seconds}s..."
                )
                time.sleep(self.config.retry_wait_seconds)

    def _ejecutar_query(self, user_query: str) -> RAGResponse:
        docs = self._recuperar_documentos(user_query)

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
                prompt_tokens=None,
                completion_tokens=None,
                total_tokens=None,
            )

        response = self._document_chain.invoke(
            {
                "contexto": docs_contexto,
                "pregunta": user_query,
            }
        )

        # Extraer texto — content puede ser str o lista de bloques según el wrapper.
        if isinstance(response, str):
            content = response
        else:
            content = response.content
            if isinstance(content, list):
                content = next(
                    (b["text"] for b in content if isinstance(b, dict) and b.get("type") == "text"),
                    "",
                )

        # Extraer tokens — usage_metadata puede ser dict o objeto con atributos
        prompt_tokens = None
        completion_tokens = None
        total_tokens = None

        if hasattr(response, "usage_metadata") and response.usage_metadata is not None:
            usage = response.usage_metadata
            if isinstance(usage, dict):
                # Los wrappers modernos suelen usar input_tokens/output_tokens/total_tokens.
                # Algunos wrappers viejos usan prompt_token_count/candidates_token_count.
                prompt_tokens = usage.get("input_tokens") or usage.get("prompt_token_count")
                completion_tokens = usage.get("output_tokens") or usage.get("candidates_token_count")
                total_tokens = usage.get("total_tokens") or usage.get("total_token_count")
            else:
                prompt_tokens = getattr(usage, "input_tokens", None)
                completion_tokens = getattr(usage, "output_tokens", None)
                total_tokens = getattr(usage, "total_tokens", None)

        return RAGResponse(
            answer=content,
            chunks_found=chunks_found,
            chunks_used=chunks_used,
            chunk_details=chunk_details,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            total_tokens=total_tokens,
        )

    @staticmethod
    def _normalizar_texto(texto: str) -> str:
        texto = unicodedata.normalize("NFKD", texto)
        texto = "".join(char for char in texto if not unicodedata.combining(char))
        return texto.lower()

    def _recuperar_documentos(self, user_query: str):
        return self._retriever.invoke(user_query)

    @classmethod
    def reset(cls):
        if cls._instance is not None:
            instance = cls._instance
            # Cerrar explicitamente el cliente de ChromaDB para liberar el lock
            # SQLite ANTES de borrar referencias. Sin esto, un refresh=True en la
            # siguiente conversacion hace shutil.rmtree con el archivo todavia
            # abierto, causando SQLITE_READONLY_DBMOVED (code 1032).
            if hasattr(instance, "_vectorstore"):
                try:
                    client = instance._vectorstore._client
                    if hasattr(client, "_system"):
                        client._system.stop()
                    # Limpiar el SharedSystemClient interno de ChromaDB. Sin esto,
                    # la proxima llamada a Chroma(persist_directory=...) intenta
                    # reusar el sistema parado y falla con "Could not connect to
                    # tenant default_tenant" al hacer refresh consecutivos.
                    import chromadb.api.client as _chroma_client
                    if hasattr(_chroma_client, "SharedSystemClient"):
                        id_map = getattr(_chroma_client.SharedSystemClient, "_identifier_to_system", None)
                        if id_map is not None:
                            id_map.clear()
                except Exception:
                    pass
            for attr in ("_vectorstore", "_retriever", "_llm", "_document_chain", "_document_prompt", "_qa_prompt"):
                if hasattr(instance, attr):
                    delattr(instance, attr)
        cls._instance = None
        cls._initialized = False
        # gc.collect() siempre, no solo cuando torch esta disponible
        import gc
        gc.collect()
        # Liberar VRAM cacheada por PyTorch
        try:
            import torch
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
        except ImportError:
            pass
