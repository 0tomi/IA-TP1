from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, field_validator
from contextlib import asynccontextmanager
import logging

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


# ── Inicialización del RAGService al arrancar ─────────────────────────────────

_rag: RAGService | None = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global _rag
    logger.info("Inicializando RAGService...")
    config = RAGServiceConfig()
    _rag = RAGService(config)
    logger.info("RAGService listo.")
    yield


# ── App ───────────────────────────────────────────────────────────────────────

app = FastAPI(
    title="Ragy — Asistente UADER FCyT",
    description="API RAG para alumnos de 4° año de Ingeniería en Sistemas",
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


@app.post("/api/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
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
