from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, field_validator
from contextlib import asynccontextmanager
import logging
import threading

from rag_service import RAGService, RAGServiceConfig

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MAX_MESSAGE_LENGTH = 500  # caracteres máximos por consulta


# ── Modelos de request / response ────────────────────────────────────────────

class ChatRequest(BaseModel):
    message: str

    @field_validator("message")
    @classmethod
    def message_no_vacio_y_longitud(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("El mensaje no puede estar vacío.")
        if len(v) > MAX_MESSAGE_LENGTH:
            raise ValueError(f"El mensaje no puede superar los {MAX_MESSAGE_LENGTH} caracteres.")
        return v

class ChatResponse(BaseModel):
    response: str
    sources: list[str]

class StatusResponse(BaseModel):
    status: str
    phase: str = ""
    current_file: str = ""
    files_processed: int = 0
    total_files: int = 0
    message: str = ""


# ── Estado de inicialización ──────────────────────────────────────────────────

_rag: RAGService | None = None
_init_lock = threading.Lock()
_init_status: dict = {
    "status": "loading",
    "phase": "starting",
    "current_file": "",
    "files_processed": 0,
    "total_files": 0,
    "message": "Iniciando servicio...",
}


def _progress_callback(event: dict):
    global _init_status
    with _init_lock:
        _init_status.update(event)


def _init_worker():
    global _rag, _init_status
    try:
        logger.info("Inicializando RAGService en background...")
        config = RAGServiceConfig()
        _rag = RAGService(config, progress_callback=_progress_callback)
        with _init_lock:
            _init_status = {"status": "ready", "phase": "ready", "message": "Servicio listo."}
        logger.info("RAGService listo.")
    except Exception as e:
        logger.error("Error inicializando RAGService: %s", e, exc_info=True)
        with _init_lock:
            _init_status = {"status": "error", "phase": "error", "message": str(e)}


@asynccontextmanager
async def lifespan(app: FastAPI):
    thread = threading.Thread(target=_init_worker, daemon=True)
    thread.start()
    yield


# ── App ───────────────────────────────────────────────────────────────────────

app = FastAPI(
    title="Ragy — Asistente UADER FCyT",
    description="API RAG para alumnos de 4° año de Licenciatura en Sistemas de Información",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",   # Vite dev
        "http://localhost:4173",   # Vite preview
        "http://localhost:3000",
    ],
    allow_methods=["POST", "GET"],
    allow_headers=["Content-Type"],
)


# ── Endpoints ─────────────────────────────────────────────────────────────────

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/status", response_model=StatusResponse)
def status():
    with _init_lock:
        return StatusResponse(**{
            "status": _init_status.get("status", "loading"),
            "phase": _init_status.get("phase", ""),
            "current_file": _init_status.get("current_file", ""),
            "files_processed": _init_status.get("files_processed", 0),
            "total_files": _init_status.get("total_files", 0),
            "message": _init_status.get("message", ""),
        })


@app.post("/api/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    if _rag is None:
        raise HTTPException(status_code=503, detail="El servicio aún se está inicializando. Esperá unos segundos.")

    try:
        result = _rag.query(req.message)
    except Exception as e:
        logger.error("Error en RAGService.query: %s", e, exc_info=True)
        raise HTTPException(status_code=503, detail="El servicio de IA no está disponible en este momento.")

    # Deduplicar fuentes realmente usadas por el LLM
    seen: set[str] = set()
    sources: list[str] = []
    for chunk in result.sources_used:
        src = chunk.get("source", "")
        pag = chunk.get("pagina")
        if src and src != "Oculto":
            pag_str = str(pag) if pag is not None and str(pag) != "—" else ""
            src_str = f"{src} (Pág. {pag_str})" if pag_str else src
            if src_str not in seen:
                seen.add(src_str)
                sources.append(src_str)

    return ChatResponse(response=result.answer, sources=sources)
