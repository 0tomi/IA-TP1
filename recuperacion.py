import argparse
import sys

import questionary
from questionary import Style

from rag_service import RAGService, RAGServiceConfig

# ── Modelos disponibles ────────────────────────────────────────────────────────

LLM_MODELS = [
    ("Gemini 3.1 Flash Lite Preview  (rápido)", "gemini-3.1-flash-lite-preview"),
    ("Gemini 2.0 Flash",                         "gemini-2.0-flash"),
    ("Gemini 3.0 Flash",                         "gemini-3.0-flash"),
    ("Gemini 2.5 Pro",                           "gemini-2.5-pro"),
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

# ── Wizard ─────────────────────────────────────────────────────────────────────

def pedir_configuracion() -> RAGServiceConfig:
    defaults = RAGServiceConfig()

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
            ("temperatura", defaults.temperatura), ("llm_model", defaults.llm_model),
            ("chunk_size", defaults.chunk_size), ("chunk_overlap", defaults.chunk_overlap),
            ("embedding_model", defaults.embedding_model), ("chunking_technique", defaults.chunking_technique),
            ("embedding_batch_size", defaults.embedding_batch_size), ("max_retries", defaults.max_retries),
            ("retry_wait_seconds", defaults.retry_wait_seconds), ("refresh", defaults.refresh),
            ("debug", defaults.debug),
        ]:
            print(f"    {k:<22}: {v}")
        return RAGServiceConfig()

    # Cada paso es (clave, función que recibe kwargs y retorna valor o None)
    # None = Ctrl+C = el wizard retrocede
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
        return _select("  Modelo LLM:", LLM_MODELS, defaults.llm_model)

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

    PASOS = [
        ("top_k",               paso_top_k),
        ("retrieval_type",      paso_retrieval_type),
        ("threshold",           paso_threshold),
        ("max_context_chunks",  paso_max_context_chunks),
        ("temperatura",         paso_temperatura),
        ("llm_model",           paso_llm_model),
        ("chunk_size",          paso_chunk_size),
        ("chunk_overlap",       paso_chunk_overlap),
        ("embedding_model",     paso_embedding_model),
        ("chunking_technique",  paso_chunking_technique),
        ("embedding_batch_size",paso_embedding_batch_size),
        ("max_retries",         paso_max_retries),
        ("retry_wait_seconds",  paso_retry_wait),
        ("refresh",             paso_refresh),
        ("debug",               paso_debug),
    ]

    # Pasos que se auto-completan sin mostrar prompt (condicionales)
    AUTO_PASOS = {"threshold"}

    kwargs = {}
    cursor = 0

    print("\n  ── Custom config  (Ctrl+C en cualquier pregunta para volver atrás) ──\n")

    while cursor < len(PASOS):
        clave, fn = PASOS[cursor]

        # Si es un paso auto-fill (condicional) que no requiere input, avanzar sin registrar
        is_auto = clave in AUTO_PASOS and kwargs.get("retrieval_type") != "threshold"
        if is_auto:
            kwargs[clave] = fn(kwargs)
            cursor += 1
            continue

        valor = fn(kwargs)

        if valor is None:
            # Ctrl+C: retroceder saltando pasos auto-fill
            kwargs.pop(clave, None)
            cursor -= 1
            while cursor > 0 and PASOS[cursor][0] in AUTO_PASOS:
                kwargs.pop(PASOS[cursor][0], None)
                cursor -= 1
            cursor = max(0, cursor)
            # Limpiar el valor del paso al que volvemos para que se vuelva a preguntar
            kwargs.pop(PASOS[cursor][0], None)
        else:
            kwargs[clave] = valor
            cursor += 1

    return RAGServiceConfig(**kwargs)


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
    service = RAGService(config)

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
                print(f"\n  ┌─ DEBUG: {response.chunks_used} chunks usados de {response.chunks_found} encontrados")
                for detail in response.chunk_details:
                    print(f"  ├─ [{detail['index']}] {detail['source']}")
                    print(f"  │   Sección : {detail['section']}")
                    print(f"  │   Preview : {detail['preview'].strip()[:120]}...")
                print(f"  └{'─' * 50}\n")

            print(f"\n  Agente › {response.answer}\n")

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
