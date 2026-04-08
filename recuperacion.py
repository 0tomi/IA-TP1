import argparse
import json
import os
import subprocess
import sys
import tempfile

GREEN = "\033[92m"
RESET = "\033[0m"
_DEBUG_W = 72  # ancho interior del cuadro de debug

import questionary
from questionary import Style

from carga import DATA_DIR
from rag_service import RAGService, RAGServiceConfig, DEFAULT_SYSTEM_PROMPT

# ── Modelos disponibles ────────────────────────────────────────────────────────

GOOGLE_LLM_MODELS = [
    ("Gemini 3.1 Flash Lite Preview  (rápido)", "gemini-3.1-flash-lite-preview"),
    ("Gemini 2.0 Flash",                         "gemini-2.0-flash"),
    ("Gemini 3.0 Flash",                         "gemini-3.0-flash"),
    ("Gemini 2.5 Pro",                           "gemini-2.5-pro"),
]

OLLAMA_LLM_MODELS = [
    ("Llama 3.1                         (Ollama local)", "llama3.1"),
]

EMBEDDING_MODELS = [
    ("Gemini Embedding 001              (Google API)",    "gemini-embedding-001"),
    ("Multilingual E5 Small             (local, rápido)", "intfloat/multilingual-e5-small"),
    ("Paraphrase Multilingual MiniLM    (local)",         "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"),
    ("All MiniLM L6 v2                  (local, inglés)", "sentence-transformers/all-MiniLM-L6-v2"),
    ("BGE M3                            (local, pesado)", "BAAI/bge-m3"),
]

RETRIEVAL_TYPES = [
    ("similarity_search", "similarity_search"),
    ("mmr",               "mmr"),
    ("threshold",         "threshold"),
]

CHUNKING_TECHNIQUES = [
    ("recursive",            "recursive"),
    ("fixed_size_overlap",   "fixed_size_overlap"),
    ("paragraph_custom",     "paragraph_custom"),
]

# ── Estilo ─────────────────────────────────────────────────────────────────────

STYLE = Style([
    ("qmark",       "fg:#00bcd4 bold"),
    ("question",    "bold"),
    ("answer",      "fg:#00e676"),
    ("pointer",     "fg:#00bcd4 bold"),
    ("highlighted", "fg:#00bcd4 bold"),
    ("selected",    "fg:#00e676"),
    ("separator",   "fg:#444444"),
    ("instruction", "fg:#666666 italic"),
    ("text",        ""),
])

# ── Helpers de pregunta ────────────────────────────────────────────────────────

def _mark_default(choices, default_value):
    """Agrega '(default)' en gris al lado de la opción predeterminada."""
    result = []
    for label, value in choices:
        title = f"{label}  (default)" if value == default_value else label
        result.append(questionary.Choice(title=title, value=value))
    return result


def _select(pregunta, choices, default):
    marked = _mark_default(choices, default)
    default_choice = next((c for c in marked if c.value == default), None)
    return questionary.select(
        pregunta,
        choices=marked,
        default=default_choice,
        style=STYLE,
    ).ask()


def _int(pregunta, default):
    def validar(v):
        try:
            int(v)
            return True
        except ValueError:
            return f"Ingresá un entero (ej: {default})"

    raw = questionary.text(
        pregunta,
        default=str(default),
        validate=validar,
        style=STYLE,
    ).ask()
    return int(raw) if raw is not None else None


def _float(pregunta, default):
    def validar(v):
        try:
            float(v)
            return True
        except ValueError:
            return f"Ingresá un número decimal (ej: {default})"

    raw = questionary.text(
        pregunta,
        default=str(default),
        validate=validar,
        style=STYLE,
    ).ask()
    return float(raw) if raw is not None else None


def _confirm(pregunta, default):
    return questionary.confirm(
        pregunta,
        default=default,
        style=STYLE,
    ).ask()


def _build_llm_choices(ollama_habilitado: bool):
    choices = [(label, ("google", value)) for label, value in GOOGLE_LLM_MODELS]
    if ollama_habilitado:
        choices.extend((label, ("ollama", value)) for label, value in OLLAMA_LLM_MODELS)
    return choices

# ── Editor de prompt ───────────────────────────────────────────────────────────

_EDITOR_HEADER = """\
# Editá el prompt del sistema.
# Placeholders obligatorios: {contexto}  y  {pregunta}
# Estas líneas que empiezan con # son comentarios y se descartan al guardar.
# ─────────────────────────────────────────────────────────────────────────────

"""

def _abrir_editor(prompt_actual: str) -> str | None:
    editor = os.environ.get("VISUAL") or os.environ.get("EDITOR") or "nano"
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", delete=False, encoding="utf-8"
    ) as f:
        f.write(_EDITOR_HEADER + prompt_actual)
        tmpfile = f.name

    try:
        ret = subprocess.call([editor, tmpfile])
        if ret != 0:
            print(f"\n  [aviso] El editor salió con código {ret}. Se mantiene el prompt original.")
            return prompt_actual

        with open(tmpfile, encoding="utf-8") as f:
            lines = [l for l in f.readlines() if not l.startswith("#")]
        resultado = "".join(lines).strip()

        if not resultado:
            print("\n  [aviso] El prompt quedó vacío. Se mantiene el original.")
            return prompt_actual
        if "{contexto}" not in resultado or "{pregunta}" not in resultado:
            print("\n  [aviso] Faltan {contexto} o {pregunta}. Se mantiene el original.")
            return prompt_actual

        return resultado
    finally:
        os.unlink(tmpfile)


# ── Wizard ─────────────────────────────────────────────────────────────────────

def _cargar_last_config() -> dict:
    path = DATA_DIR / "last_data_process.json"
    if path.exists():
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}


def pedir_configuracion() -> RAGServiceConfig:
    defaults = RAGServiceConfig()
    last = _cargar_last_config()
    if last:
        defaults.embedding_model = last.get("embedding_model", defaults.embedding_model)
        defaults.chunk_size = last.get("chunk_size", defaults.chunk_size)
        defaults.chunk_overlap = last.get("chunk_overlap", defaults.chunk_overlap)
        defaults.chunking_technique = last.get("chunking_technique", defaults.chunking_technique)
        defaults.embedding_batch_size = last.get("embedding_batch_size", defaults.embedding_batch_size)

    print()
    modo = _select(
        "Modo de configuración:",
        [
            ("Default  (usar valores predeterminados)", "default"),
            ("Custom   (modificar parámetros)",         "custom"),
        ],
        default="default",
    )

    if modo is None:
        return None

    if modo == "default":
        print("\n  Configuración por defecto:")
        for k, v in [
            ("top_k", defaults.top_k), ("retrieval_type", defaults.retrieval_type),
            ("threshold", defaults.threshold), ("max_context_chunks", defaults.max_context_chunks),
            ("temperatura", defaults.temperatura), ("llm_provider", defaults.llm_provider),
            ("llm_model", defaults.llm_model),
            ("chunk_size", defaults.chunk_size), ("chunk_overlap", defaults.chunk_overlap),
            ("embedding_model", defaults.embedding_model), ("chunking_technique", defaults.chunking_technique),
            ("embedding_batch_size", defaults.embedding_batch_size), ("max_retries", defaults.max_retries),
            ("retry_wait_seconds", defaults.retry_wait_seconds), ("refresh", defaults.refresh),
            ("debug", defaults.debug),
        ]:
            print(f"    {k:<22}: {v}")
        prompt_preview = defaults.system_prompt.split("\n")[0][:60]
        print(f"    {'system_prompt':<22}: {prompt_preview}…")
        return defaults

    # ── Submenu de grupo ───────────────────────────────────────────────────────
    subgrupo = _select(
        "  ¿Qué querés configurar?",
        [
            ("Retrieval y LLM       (recuperación, modelo, temperatura…)", "llm"),
            ("Chunking y Embedding  (chunks, overlap, modelo de embedding…)", "chunking"),
            ("Todo                  (configuración completa paso a paso)",   "todo"),
        ],
        default="todo",
    )
    if subgrupo is None:
        return None

    configurar_llm      = subgrupo in ("llm", "todo")
    configurar_chunking = subgrupo in ("chunking", "todo")

    # Ollama solo se pregunta si el grupo incluye configuración de LLM
    ollama_habilitado = False
    if configurar_llm:
        ollama_habilitado = _confirm(
            "  ¿Tenés Ollama instalado y querés habilitar Llama 3.1?",
            False,
        )
        if ollama_habilitado is None:
            return None
        if ollama_habilitado:
            defaults.llm_provider = "ollama"
            defaults.llm_model = "llama3.1"

    # ── Definición de pasos ────────────────────────────────────────────────────

    def paso_top_k(kw):
        return _int("  Chunks a recuperar (top_k):", defaults.top_k)

    def paso_retrieval_type(kw):
        return _select("  Tipo de búsqueda (retrieval_type):", RETRIEVAL_TYPES, defaults.retrieval_type)

    def paso_threshold(kw):
        if kw.get("retrieval_type") != "threshold":
            return defaults.threshold  # auto-fill, no preguntar
        return _float("  Similitud mínima (threshold, 0.0–1.0):", defaults.threshold)

    def paso_max_context_chunks(kw):
        return _int("  Chunks máximos al LLM (max_context_chunks):", defaults.max_context_chunks)

    def paso_temperatura(kw):
        return _float("  Temperatura (0.0–2.0):", defaults.temperatura)

    def paso_llm_model(kw):
        default_llm = (defaults.llm_provider, defaults.llm_model)
        selected = _select("  Modelo LLM:", _build_llm_choices(ollama_habilitado), default_llm)
        if selected is None:
            return None
        llm_provider, llm_model = selected
        kw["llm_provider"] = llm_provider
        return llm_model

    def paso_chunk_size(kw):
        return _int("  Tamaño de chunk (chunk_size):", defaults.chunk_size)

    def paso_chunk_overlap(kw):
        return _int("  Overlap entre chunks (chunk_overlap):", defaults.chunk_overlap)

    def paso_embedding_model(kw):
        return _select("  Modelo de embedding:", EMBEDDING_MODELS, defaults.embedding_model)

    def paso_chunking_technique(kw):
        return _select("  Técnica de chunking:", CHUNKING_TECHNIQUES, defaults.chunking_technique)

    def paso_embedding_batch_size(kw):
        return _int("  Batch size de embeddings:", defaults.embedding_batch_size)

    def paso_max_retries(kw):
        return _int("  Reintentos máximos (max_retries):", defaults.max_retries)

    def paso_retry_wait(kw):
        return _int("  Espera entre reintentos en segundos:", defaults.retry_wait_seconds)

    def paso_refresh(kw):
        return _confirm("  ¿Forzar re-procesamiento del corpus? (refresh)", defaults.refresh)

    def paso_debug(kw):
        return _confirm("  ¿Activar modo debug?", defaults.debug)

    def paso_system_prompt(kw):
        editar = _confirm("  ¿Editar el prompt del sistema?", False)
        if editar is None:
            return None
        if not editar:
            return defaults.system_prompt
        return _abrir_editor(defaults.system_prompt)

    PASOS_LLM = [
        ("top_k",              paso_top_k),
        ("retrieval_type",     paso_retrieval_type),
        ("threshold",          paso_threshold),
        ("max_context_chunks", paso_max_context_chunks),
        ("temperatura",        paso_temperatura),
        ("llm_model",          paso_llm_model),
        ("max_retries",        paso_max_retries),
        ("retry_wait_seconds", paso_retry_wait),
        ("debug",              paso_debug),
        ("system_prompt",      paso_system_prompt),
    ]

    PASOS_CHUNKING = [
        ("chunk_size",          paso_chunk_size),
        ("chunk_overlap",       paso_chunk_overlap),
        ("embedding_model",     paso_embedding_model),
        ("chunking_technique",  paso_chunking_technique),
        ("embedding_batch_size",paso_embedding_batch_size),
        ("refresh",             paso_refresh),
    ]

    PASOS_TODO = PASOS_LLM[:6] + PASOS_CHUNKING + PASOS_LLM[6:]

    PASOS = (
        PASOS_TODO     if subgrupo == "todo"     else
        PASOS_LLM      if subgrupo == "llm"      else
        PASOS_CHUNKING
    )

    AUTO_PASOS = {"threshold"}

    # ── Runner del wizard con navegación hacia atrás ───────────────────────────

    # Arrancamos con todos los defaults para que los params no preguntados
    # mantengan su valor aunque el usuario solo configure un subgrupo.
    kwargs = {
        "top_k": defaults.top_k,
        "retrieval_type": defaults.retrieval_type,
        "threshold": defaults.threshold,
        "max_context_chunks": defaults.max_context_chunks,
        "temperatura": defaults.temperatura,
        "llm_provider": defaults.llm_provider,
        "llm_model": defaults.llm_model,
        "chunk_size": defaults.chunk_size,
        "chunk_overlap": defaults.chunk_overlap,
        "embedding_model": defaults.embedding_model,
        "chunking_technique": defaults.chunking_technique,
        "embedding_batch_size": defaults.embedding_batch_size,
        "max_retries": defaults.max_retries,
        "retry_wait_seconds": defaults.retry_wait_seconds,
        "refresh": defaults.refresh,
        "debug": defaults.debug,
        "system_prompt": defaults.system_prompt,
    }

    label = {"llm": "Retrieval y LLM", "chunking": "Chunking y Embedding", "todo": "Todo"}[subgrupo]
    print(f"\n  ── {label}  (Ctrl+C en cualquier pregunta para volver atrás) ──\n")

    cursor = 0
    while cursor < len(PASOS):
        clave, fn = PASOS[cursor]

        is_auto = clave in AUTO_PASOS and kwargs.get("retrieval_type") != "threshold"
        if is_auto:
            kwargs[clave] = fn(kwargs)
            cursor += 1
            continue

        valor = fn(kwargs)

        if valor is None:
            # Ctrl+C: restaurar default del paso actual y retroceder
            kwargs[clave] = getattr(defaults, clave, kwargs.get(clave))
            if clave == "llm_model":
                kwargs["llm_provider"] = defaults.llm_provider
            cursor -= 1
            while cursor > 0 and PASOS[cursor][0] in AUTO_PASOS:
                cursor -= 1
            cursor = max(0, cursor)
            # Restaurar default del paso al que volvemos para que se repregunta limpio
            clave_prev = PASOS[cursor][0]
            kwargs[clave_prev] = getattr(defaults, clave_prev, kwargs.get(clave_prev))
            if clave_prev == "llm_model":
                kwargs["llm_provider"] = defaults.llm_provider
        else:
            kwargs[clave] = valor
            cursor += 1

    return RAGServiceConfig(**kwargs)


# ── Debug block ────────────────────────────────────────────────────────────────

def _print_debug(response):
    W = _DEBUG_W

    def row(text):
        if len(text) > W - 2:
            text = text[: W - 3] + "…"
        print(f"  ║ {text:<{W - 2}}║")

    header = f" DEBUG · {response.chunks_used} chunks usados de {response.chunks_found} encontrados "
    print(f"\n  ╔{'═' * W}╗")
    print(f"  ║{header:^{W}}║")
    print(f"  ╠{'═' * W}╣")
    for i, detail in enumerate(response.chunk_details):
        row(f"[{detail['index']}] Documento : {detail['source']}")
        row(f"    Materia   : {detail.get('materia', '—')}")
        row(f"    Página    : {detail.get('pagina', '—')}")
        row(f"    Sección   : {detail['section']}")
        preview = detail["preview"].strip().replace("\n", " ")
        row(f"    Preview   : {preview}")
        if i < len(response.chunk_details) - 1:
            print(f"  ╠{'─' * W}╣")
    print(f"  ╚{'═' * W}╝")


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--debug", action="store_true", default=False)
    flags, _ = parser.parse_known_args()

    print("\n╔══════════════════════════════════════╗")
    print("║       Asistente RAG — IA TP1         ║")
    print("╚══════════════════════════════════════╝")

    config = pedir_configuracion()
    if config is None:
        sys.exit(0)
    if flags.debug:
        config.debug = True

    print("\n  Inicializando servicio RAG...")
    service = RAGService.create(config)

    print("\n╔══════════════════════════════════════════════════════╗")
    print("║  Listo. Escribí tu consulta o 'salir' para terminar. ║")
    print("╚══════════════════════════════════════════════════════╝\n")

    while True:
        try:
            user_input = questionary.text("Prompt:", style=STYLE).ask()

            if user_input is None or user_input.lower() in ("salir", "exit", "quit"):
                print("\n  ¡Hasta luego!\n")
                break
            if not user_input.strip():
                continue

            response = service.query(user_input.strip())

            if config.debug:
                _print_debug(response)

            print(f"\n  {GREEN}RAGi ›{RESET} {response.answer}\n")

            if response.prompt_tokens is not None:
                print(
                    f"  [tokens] entrada: {response.prompt_tokens} | "
                    f"salida: {response.completion_tokens} | "
                    f"total: {response.total_tokens}\n"
                )

        except KeyboardInterrupt:
            print("\n\n  ¡Hasta luego!\n")
            break
        except Exception as e:
            print(f"\n  [ERROR] {e}\n")


if __name__ == "__main__":
    main()
