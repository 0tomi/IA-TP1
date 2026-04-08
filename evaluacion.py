"""
Script de evaluacion automatizada del RAG.

Uso:
    python evaluacion.py [--retry N] [--file evaluacion.md]

Lee preguntas y sets de parametros de evaluacion.md, ejecuta conversaciones
contra el RAGService, y genera reportes en tests/test-N.md.
"""
import argparse
import dataclasses
import os
import re
import sys
from datetime import datetime
from pathlib import Path

from rag_service import RAGService, RAGServiceConfig, RAGResponse

# Tipos de cada campo de RAGServiceConfig para parseo automatico
_FIELD_TYPES: dict[str, type] = {
    "top_k": int,
    "retrieval_type": str,
    "threshold": float,
    "max_context_chunks": int,
    "temperatura": float,
    "debug": bool,
    "llm_provider": str,
    "llm_model": str,
    "chunk_size": int,
    "chunk_overlap": int,
    "embedding_model": str,
    "chunking_technique": str,
    "embedding_batch_size": int,
    "max_retries": int,
    "retry_wait_seconds": int,
    "refresh": bool,
    "system_prompt": str,
}

ROOT = Path(__file__).resolve().parent


def _castear_valor(clave: str, valor_str: str) -> object:
    tipo = _FIELD_TYPES.get(clave)
    if tipo is bool:
        val = valor_str.strip().lower()
        if val not in ("true", "false"):
            raise ValueError(
                f"Valor invalido para '{clave}': '{valor_str.strip()}'. "
                "Se esperaba 'true' o 'false'."
            )
        return val == "true"
    if tipo is int:
        return int(valor_str.strip())
    if tipo is float:
        return float(valor_str.strip())
    return valor_str.strip()


def parsear_evaluacion(path: Path) -> tuple[list[str], list[dict]]:
    """Parsea evaluacion.md y retorna (preguntas, lista_de_parametros)."""
    texto = path.read_text(encoding="utf-8")
    lineas = texto.splitlines()

    seccion_actual = None
    in_params_section = False
    preguntas: list[str] = []
    sets_parametros: list[dict] = []
    params_actuales: dict = {}

    for linea in lineas:
        encabezado = re.match(r"^\[(.+)\]\s*$", linea)
        if encabezado:
            # Cerrar seccion de parametros anterior (incluso si estaba vacia)
            if in_params_section:
                sets_parametros.append(params_actuales)
                params_actuales = {}
                in_params_section = False
            seccion_actual = encabezado.group(1).strip()
            if seccion_actual.lower().startswith("par"):
                in_params_section = True
            continue

        if seccion_actual is None:
            continue

        if seccion_actual.lower() == "preguntas":
            stripped = linea.strip()
            # Ignorar lineas vacias y comentarios
            if stripped and not stripped.startswith("#"):
                preguntas.append(stripped)
        elif in_params_section:
            if "=" in linea:
                clave, _, valor = linea.partition("=")
                clave = clave.strip().replace("-", "_")
                if clave in _FIELD_TYPES:
                    params_actuales[clave] = _castear_valor(clave, valor)
                else:
                    print(f"[evaluacion] Advertencia: parametro desconocido '{clave}', se ignora.")

    # Cerrar ultimo bloque de parametros
    if in_params_section:
        sets_parametros.append(params_actuales)

    if not preguntas:
        raise ValueError("No se encontraron preguntas en el archivo de evaluacion.")
    if not sets_parametros:
        raise ValueError("No se encontraron sets de parametros en el archivo de evaluacion.")

    return preguntas, sets_parametros


def construir_config(params: dict) -> RAGServiceConfig:
    return RAGServiceConfig(**params)


def next_test_path() -> Path:
    """Reserva atomicamente el proximo test-N.md para evitar colisiones concurrentes."""
    tests_dir = ROOT / "tests"
    tests_dir.mkdir(exist_ok=True)

    while True:
        numeros = []
        for f in tests_dir.glob("test-*.md"):
            m = re.match(r"test-(\d+)", f.stem)
            if m:
                numeros.append(int(m.group(1)))
        siguiente = max(numeros, default=0) + 1
        candidate = tests_dir / f"test-{siguiente}.md"
        try:
            fd = os.open(str(candidate), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.close(fd)
            return candidate
        except FileExistsError:
            continue


def formatear_chunks(chunk_details: list[dict]) -> str:
    if not chunk_details:
        return "_Sin chunks recuperados._\n"
    lineas = []
    for i, c in enumerate(chunk_details, start=1):
        lineas.append(
            f"{i}. [Documento: {c['source']} | Materia: {c['materia']} "
            f"| Seccion: {c['section']} | Pagina: {c['pagina']}]"
        )
        preview = c["preview"].replace("\n", " ").strip()
        lineas.append(f"   > {preview}")
    return "\n".join(lineas) + "\n"


def formatear_tokens(r: RAGResponse) -> str:
    entrada = r.prompt_tokens if r.prompt_tokens is not None else "—"
    salida = r.completion_tokens if r.completion_tokens is not None else "—"
    total = r.total_tokens if r.total_tokens is not None else "—"
    return f"**Tokens:** entrada: {entrada} | salida: {salida} | total: {total}"


def _mostrar_token_count(valor: int) -> int | str:
    return valor


def generar_markdown(
    test_n: int,
    preguntas: list[str],
    resultados: list[list[tuple[str | None, RAGResponse | None]]],
    configs: list[RAGServiceConfig],
) -> str:
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lineas = [f"# Evaluacion — Test {test_n}", f"", f"_Generado: {ahora}_", ""]

    total_entrada = 0
    total_salida = 0
    total_total = 0
    resumen_filas: list[tuple[int, int | str, int | str, int | str]] = []

    prev_config = None
    for idx_conv, (config, resultados_conv) in enumerate(zip(configs, resultados), start=1):
        lineas.append(f"## Conversacion {idx_conv}")
        lineas.append("")

        campos = [f for f in dataclasses.fields(config) if f.name != "system_prompt"]
        if prev_config is None:
            filas_params = [(f.name, getattr(config, f.name)) for f in campos]
            lineas.append("**Parametros:**")
        else:
            filas_params = [
                (f.name, getattr(config, f.name))
                for f in campos
                if getattr(config, f.name) != getattr(prev_config, f.name)
            ]
            lineas.append("**Parametros modificados respecto a la conversacion anterior:**")

        lineas.append("")
        if filas_params:
            lineas.append("| Parametro | Valor |")
            lineas.append("|---|---|")
            for nombre, valor in filas_params:
                lineas.append(f"| {nombre} | {valor} |")
        else:
            lineas.append("_Sin cambios respecto a la conversacion anterior._")
        lineas.append("")
        prev_config = config

        conv_entrada = 0
        conv_salida = 0
        conv_total = 0

        for idx_preg, (pregunta, (error, respuesta)) in enumerate(
            zip(preguntas, resultados_conv), start=1
        ):
            if error:
                lineas.append(f"### Pregunta {idx_preg} [ERROR]")
                lineas.append("")
                lineas.append(f"> {pregunta}")
                lineas.append("")
                lineas.append(f"**Error:** {error}")
            else:
                lineas.append(f"### Pregunta {idx_preg}")
                lineas.append("")
                lineas.append(f"> {pregunta}")
                lineas.append("")
                lineas.append("**Chunks de contexto:**")
                lineas.append("")
                lineas.append(formatear_chunks(respuesta.chunk_details))
                lineas.append("**Respuesta:**")
                lineas.append("")
                lineas.append(respuesta.answer)
                lineas.append("")
                lineas.append(formatear_tokens(respuesta))

                if respuesta.prompt_tokens is not None:
                    conv_entrada += respuesta.prompt_tokens
                if respuesta.completion_tokens is not None:
                    conv_salida += respuesta.completion_tokens
                if respuesta.total_tokens is not None:
                    conv_total += respuesta.total_tokens

            lineas.append("")
            lineas.append("---")
            lineas.append("")

        total_entrada += conv_entrada
        total_salida += conv_salida
        total_total += conv_total
        resumen_filas.append((
            idx_conv,
            _mostrar_token_count(conv_entrada),
            _mostrar_token_count(conv_salida),
            _mostrar_token_count(conv_total),
        ))

    lineas.append("## Resumen de tokens")
    lineas.append("")
    lineas.append("| Conversacion | Entrada | Salida | Total |")
    lineas.append("|---|---|---|---|")
    for fila in resumen_filas:
        lineas.append(f"| {fila[0]} | {fila[1]} | {fila[2]} | {fila[3]} |")
    lineas.append(
        f"| **Total** | **{_mostrar_token_count(total_entrada)}** | **{_mostrar_token_count(total_salida)}** | **{_mostrar_token_count(total_total)}** |"
    )
    lineas.append("")

    return "\n".join(lineas)


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluacion automatizada del RAG")
    parser.add_argument(
        "--retry", type=int, default=3,
        help="Reintentos del runner ante excepciones por pregunta (default: 3). "
             "Independiente de max_retries del servicio, que se configura en el archivo de evaluacion."
    )
    parser.add_argument(
        "--file", type=str, default="evaluacion.md",
        help="Archivo de evaluacion (default: evaluacion.md)"
    )
    args = parser.parse_args()

    eval_path = ROOT / args.file
    if not eval_path.exists():
        print(f"[evaluacion] Error: no se encontro el archivo '{eval_path}'.")
        sys.exit(1)

    print(f"[evaluacion] Leyendo '{eval_path}'...")
    try:
        preguntas, sets_parametros = parsear_evaluacion(eval_path)
    except ValueError as e:
        print(f"[evaluacion] Error al parsear el archivo: {e}")
        sys.exit(1)

    print(f"[evaluacion] {len(preguntas)} pregunta(s), {len(sets_parametros)} set(s) de parametros.")

    test_path = next_test_path()
    test_n = int(re.search(r"\d+", test_path.stem).group())
    print(f"[evaluacion] Resultado se guardara en: {test_path}")

    # Acumulacion de parametros entre sets (carry-over)
    defaults = {f.name: f.default for f in dataclasses.fields(RAGServiceConfig)
                if f.default is not dataclasses.MISSING}
    # system_prompt tiene default_factory, lo resolvemos manualmente
    defaults["system_prompt"] = RAGServiceConfig().system_prompt
    # Nota: max_retries del servicio se configura en el archivo de evaluacion.
    # args.retry controla los reintentos del runner (capa externa), son conceptos distintos.

    current_params = dict(defaults)

    todos_resultados: list[list[tuple[str | None, RAGResponse | None]]] = []
    configs_usadas: list[RAGServiceConfig] = []

    for idx_conv, set_params in enumerate(sets_parametros, start=1):
        # refresh NO se acumula: default False salvo que este explicitamente en este set
        refresh_explícito = "refresh" in set_params
        current_params.update(set_params)
        if not refresh_explícito:
            current_params["refresh"] = False

        config = construir_config(current_params)
        configs_usadas.append(config)

        print(f"\n[evaluacion] Conversacion {idx_conv} iniciada")

        service = None
        init_error = None
        for intento in range(1, args.retry + 1):
            try:
                service = RAGService.create(config)
                init_error = None
                break
            except Exception as e:
                init_error = e
                if intento < args.retry:
                    print(
                        f"[evaluacion] Error al inicializar conversacion {idx_conv} "
                        f"(intento {intento}/{args.retry}): {e}"
                    )
                else:
                    print(
                        f"[evaluacion] Error al inicializar conversacion {idx_conv} "
                        f"tras {args.retry} intento(s): {e}"
                    )

        if init_error is not None:
            todos_resultados.append([(str(init_error), None)] * len(preguntas))
            print(f"[evaluacion] Conversacion {idx_conv} finalizada con error de inicializacion.")
            continue

        resultados_conv: list[tuple[str | None, RAGResponse | None]] = []

        for idx_preg, pregunta in enumerate(preguntas, start=1):
            print(f"[evaluacion] Pregunta {idx_preg}/{len(preguntas)}...")
            exito = False
            ultimo_error = None

            for intento in range(1, args.retry + 1):
                try:
                    respuesta = service.query(pregunta)
                    resultados_conv.append((None, respuesta))
                    exito = True
                    break
                except Exception as e:
                    ultimo_error = e
                    if intento < args.retry:
                        print(
                            f"[evaluacion] Error en pregunta {idx_preg} "
                            f"(intento {intento}/{args.retry}): {e}"
                        )
                    else:
                        print(
                            f"[evaluacion] Error en pregunta {idx_preg} "
                            f"tras {args.retry} intento(s): {e}"
                        )

            if not exito:
                resultados_conv.append((str(ultimo_error), None))

        todos_resultados.append(resultados_conv)
        print(f"[evaluacion] Conversacion {idx_conv} finalizada.")

    print(f"\n[evaluacion] Generando reporte...")
    contenido = generar_markdown(test_n, preguntas, todos_resultados, configs_usadas)
    test_path.write_text(contenido, encoding="utf-8")
    print(f"[evaluacion] Reporte guardado en: {test_path}")


if __name__ == "__main__":
    main()
