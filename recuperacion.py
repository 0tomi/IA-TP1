import argparse

from rag_service import RAGService, RAGServiceConfig


def pedir_configuracion() -> RAGServiceConfig:
    defaults = RAGServiceConfig()

    print("\n=== Configuracion del Asistente RAG ===\n")
    print("Modo de configuracion:")
    print("  [1] Default (usar valores predeterminados)")
    print("  [2] Custom (modificar parametros)")

    while True:
        opcion = input("\nSeleccione (1/2): ").strip()
        if opcion in ("1", "2"):
            break
        print("Opcion invalida. Ingrese 1 o 2.")

    if opcion == "1":
        print("\nUsando configuracion por defecto:")
        print(f"  top_k                : {defaults.top_k}")
        print(f"  retrieval_type       : {defaults.retrieval_type}")
        print(f"  threshold            : {defaults.threshold}")
        print(f"  max_context_chunks   : {defaults.max_context_chunks}")
        print(f"  temperatura          : {defaults.temperatura}")
        print(f"  llm_model            : {defaults.llm_model}")
        print(f"  chunk_size           : {defaults.chunk_size}")
        print(f"  chunk_overlap        : {defaults.chunk_overlap}")
        print(f"  embedding_model      : {defaults.embedding_model}")
        print(f"  chunking_technique   : {defaults.chunking_technique}")
        print(f"  embedding_batch_size : {defaults.embedding_batch_size}")
        print(f"  max_retries          : {defaults.max_retries}")
        print(f"  retry_wait_seconds   : {defaults.retry_wait_seconds}")
        print(f"  refresh              : {defaults.refresh}")
        print(f"  debug                : {defaults.debug}")
        return RAGServiceConfig()

    # --- Modo Custom ---
    kwargs = {}

    def pedir_int(nombre, default):
        while True:
            raw = input(f"  {nombre} [{default}]: ").strip()
            if raw == "":
                return default
            try:
                return int(raw)
            except ValueError:
                print(f"    Error: '{raw}' no es un entero valido.")

    def pedir_float(nombre, default):
        while True:
            raw = input(f"  {nombre} [{default}]: ").strip()
            if raw == "":
                return default
            try:
                return float(raw)
            except ValueError:
                print(f"    Error: '{raw}' no es un numero valido.")

    def pedir_str(nombre, default, choices=None):
        while True:
            hint = "/".join(choices) if choices else default
            raw = input(f"  {nombre} [{hint}]: ").strip()
            if raw == "":
                return default
            if choices and raw not in choices:
                print(f"    Error: opciones validas son {choices}.")
            else:
                return raw

    def pedir_bool(nombre, default):
        default_hint = "s" if default else "n"
        while True:
            raw = input(f"  {nombre} [s/n, default={default_hint}]: ").strip().lower()
            if raw == "":
                return default
            if raw in ("s", "si", "y", "yes", "true"):
                return True
            if raw in ("n", "no", "false"):
                return False
            print("    Error: ingrese s o n.")

    # Grupo 1: Retrieval
    print("\n-- Retrieval --")
    kwargs["top_k"] = pedir_int("top_k", defaults.top_k)
    kwargs["retrieval_type"] = pedir_str(
        "retrieval_type",
        defaults.retrieval_type,
        choices=["similarity_search", "mmr", "threshold"],
    )
    if kwargs["retrieval_type"] == "threshold":
        kwargs["threshold"] = pedir_float("threshold", defaults.threshold)
    else:
        kwargs["threshold"] = defaults.threshold
    kwargs["max_context_chunks"] = pedir_int("max_context_chunks", defaults.max_context_chunks)

    # Grupo 2: LLM
    print("\n-- LLM --")
    kwargs["temperatura"] = pedir_float("temperatura", defaults.temperatura)
    kwargs["llm_model"] = pedir_str("llm_model", defaults.llm_model)

    # Grupo 3: Embedding/Chunking
    print("\n-- Embedding/Chunking --")
    kwargs["chunk_size"] = pedir_int("chunk_size", defaults.chunk_size)
    kwargs["chunk_overlap"] = pedir_int("chunk_overlap", defaults.chunk_overlap)
    kwargs["embedding_model"] = pedir_str("embedding_model", defaults.embedding_model)
    kwargs["chunking_technique"] = pedir_str(
        "chunking_technique",
        defaults.chunking_technique,
        choices=["recursive", "fixed_size_overlap", "paragraph_custom"],
    )
    kwargs["embedding_batch_size"] = pedir_int("embedding_batch_size", defaults.embedding_batch_size)

    # Grupo 4: Retry
    print("\n-- Retry --")
    kwargs["max_retries"] = pedir_int("max_retries", defaults.max_retries)
    kwargs["retry_wait_seconds"] = pedir_int("retry_wait_seconds", defaults.retry_wait_seconds)

    # Grupo 5: Pipeline
    print("\n-- Pipeline --")
    kwargs["refresh"] = pedir_bool("refresh", defaults.refresh)
    kwargs["debug"] = pedir_bool("debug", defaults.debug)

    return RAGServiceConfig(**kwargs)


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--debug", action="store_true", default=False)
    flags, _ = parser.parse_known_args()

    config = pedir_configuracion()
    if flags.debug:
        config.debug = True

    print("\n[RAG] Inicializando servicio...")
    service = RAGService(config)

    print("\n=== Asistente RAG Listo (escribe 'salir', 'exit' o 'quit' para terminar) ===")

    while True:
        try:
            user_input = input("\nUsuario> ").strip()
            if not user_input:
                continue
            if user_input.lower() in ("salir", "exit", "quit"):
                print("\nAgente> ¡Hasta luego!")
                break

            response = service.query(user_input)

            if config.debug:
                print(f"\n[DEBUG] --- Chunks ({response.chunks_used} usados de {response.chunks_found} encontrados) ---")
                for detail in response.chunk_details:
                    print(f"  [{detail['index']}] {detail['source']} | Seccion: {detail['section']}")
                    print(f"      Texto: {detail['preview']}...\n")
                print("[DEBUG] -------------------------------------")

            print(f"\nAgente> {response.answer}")

            if response.prompt_tokens is not None:
                print(
                    f"\n[Metadatos de Consumo] Tokens de entrada: {response.prompt_tokens} | "
                    f"Tokens de salida: {response.completion_tokens} | "
                    f"Total usados: {response.total_tokens}"
                )
            else:
                print("\nNo se detectaron estadísticas de consumo (tokens).")

        except KeyboardInterrupt:
            print("\nAgente> ¡Hasta luego!")
            break
        except Exception as e:
            print(f"\n[ERROR EN CADENA] -> {e}")


if __name__ == "__main__":
    main()
