"""
Script de evaluacion automatizada del RAG.

Uso:
    python evaluacion.py [--retry N] [--file evaluacion.md] [--name NOMBRE]

Lee preguntas y sets de parametros de evaluacion.md, ejecuta conversaciones
contra el RAGService, y genera reportes en tests/test-N.md o tests/NOMBRE.md.
"""
import argparse
import dataclasses
import os
import re
import sys
from datetime import datetime
from pathlib import Path

from carga import es_error_de_cuota_agotada
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
ResultadoPregunta = tuple[str | None, RAGResponse | None]


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


def _reservar_archivo(path: Path) -> bool:
    try:
        fd = os.open(str(path), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        os.close(fd)
        return True
    except FileExistsError:
        return False


def _normalizar_nombre_reporte(name: str) -> str:
    name = name.strip()
    if not name:
        raise ValueError("El nombre del reporte no puede estar vacio.")

    separadores_invalidos = [sep for sep in (os.sep, os.altsep) if sep]
    if any(sep in name for sep in separadores_invalidos):
        raise ValueError("--name debe ser un nombre de archivo, sin directorios.")

    stem = name[:-3] if name.lower().endswith(".md") else name
    stem = stem.strip()
    if stem in {"", ".", ".."}:
        raise ValueError("El nombre del reporte no es valido.")
    return stem


def resolve_test_output(name: str | None) -> tuple[Path, str]:
    """Reserva atomicamente el output del reporte evitando colisiones concurrentes."""
    tests_dir = ROOT / "tests"
    tests_dir.mkdir(exist_ok=True)

    if name is not None:
        base = _normalizar_nombre_reporte(name)
        candidate = tests_dir / f"{base}.md"
        suffix = 2
        while not _reservar_archivo(candidate):
            candidate = tests_dir / f"{base}-{suffix}.md"
            suffix += 1
        return candidate, candidate.stem

    while True:
        numeros = []
        for f in tests_dir.glob("test-*.md"):
            m = re.match(r"test-(\d+)", f.stem)
            if m:
                numeros.append(int(m.group(1)))
        siguiente = max(numeros, default=0) + 1
        candidate = tests_dir / f"test-{siguiente}.md"
        if _reservar_archivo(candidate):
            return candidate, f"Test {siguiente}"


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


def _ruta_relativa_a_root(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def _cantidad_preguntas_procesadas(resultados: list[list[ResultadoPregunta]]) -> int:
    return sum(len(resultados_conv) for resultados_conv in resultados)


def _interrupcion_siguiente_posicion(
    resultados: list[list[ResultadoPregunta]],
    total_conversaciones: int,
    total_preguntas: int,
) -> tuple[int, int] | None:
    if not resultados:
        return (1, 1)

    idx_conv = len(resultados)
    preguntas_procesadas = len(resultados[-1])
    if preguntas_procesadas < total_preguntas:
        return idx_conv, preguntas_procesadas + 1

    if idx_conv < total_conversaciones:
        return idx_conv + 1, 1

    return None


def guardar_snapshot(
    test_path: Path,
    titulo: str,
    fecha_inicio: str,
    eval_path: Path,
    preguntas: list[str],
    resultados: list[list[ResultadoPregunta]],
    configs: list[RAGServiceConfig],
    total_conversaciones: int,
    estado: str,
    interrumpido_en: tuple[int, int] | None = None,
) -> None:
    contenido = generar_markdown(
        titulo=titulo,
        fecha_inicio=fecha_inicio,
        eval_path=eval_path,
        preguntas=preguntas,
        resultados=resultados,
        configs=configs,
        total_conversaciones=total_conversaciones,
        estado=estado,
        interrumpido_en=interrumpido_en,
    )
    tmp_path = test_path.with_name(f"{test_path.name}.tmp")
    tmp_path.write_text(contenido, encoding="utf-8")
    os.replace(tmp_path, test_path)


def generar_markdown(
    titulo: str,
    fecha_inicio: str,
    eval_path: Path,
    preguntas: list[str],
    resultados: list[list[ResultadoPregunta]],
    configs: list[RAGServiceConfig],
    total_conversaciones: int,
    estado: str,
    interrumpido_en: tuple[int, int] | None = None,
) -> str:
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    preguntas_procesadas = _cantidad_preguntas_procesadas(resultados)
    lineas = [
        f"# Evaluacion — {titulo}",
        "",
        f"_Iniciada: {fecha_inicio}_",
        f"_Ultima actualizacion: {ahora}_",
        "",
        f"**Estado:** {estado}",
        f"**Archivo de evaluacion:** `{_ruta_relativa_a_root(eval_path)}`",
        f"**Preguntas:** {len(preguntas)} | **Conversaciones planificadas:** {total_conversaciones} | **Conversaciones iniciadas:** {len(configs)} | **Preguntas procesadas:** {preguntas_procesadas}",
    ]

    if interrumpido_en is not None:
        lineas.append(
            f"**Interrumpida en:** conversacion {interrumpido_en[0]}, antes de la pregunta {interrumpido_en[1]}"
        )

    lineas.append("")

    if not configs:
        lineas.append("_Aun no se inicio ninguna conversacion._")
        lineas.append("")

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

        for idx_preg, (error, respuesta) in enumerate(resultados_conv, start=1):
            pregunta = preguntas[idx_preg - 1]
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

        if len(resultados_conv) < len(preguntas):
            siguiente = len(resultados_conv) + 1
            if estado == "interrumpido" and interrumpido_en == (idx_conv, siguiente):
                lineas.append(
                    f"_Evaluacion interrumpida antes de procesar la pregunta {siguiente}._"
                )
                lineas.append("")
            elif estado == "en progreso" and idx_conv == len(resultados):
                lineas.append(
                    f"_Evaluacion en progreso. La siguiente pregunta a procesar es la {siguiente}._"
                )
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
        "--retry", type=int, default=10,
        help="Reintentos del runner ante excepciones por pregunta (default: 10). "
             "Independiente de max_retries del servicio, que se configura en el archivo de evaluacion."
    )
    parser.add_argument(
        "--file", type=str, default="evaluacion.md",
        help="Archivo de evaluacion (default: evaluacion.md)"
    )
    parser.add_argument(
        "--name", type=str, default=None,
        help="Nombre base del reporte dentro de tests/ (ej: --name corrida-ollama). Si existe, se agrega sufijo automaticamente."
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

    try:
        test_path, report_title = resolve_test_output(args.name)
    except ValueError as e:
        print(f"[evaluacion] Error en --name: {e}")
        sys.exit(1)

    fecha_inicio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[evaluacion] Resultado se guardara en: {test_path}")

    # Acumulacion de parametros entre sets (carry-over)
    defaults = {f.name: f.default for f in dataclasses.fields(RAGServiceConfig)
                if f.default is not dataclasses.MISSING}
    # system_prompt tiene default_factory, lo resolvemos manualmente
    defaults["system_prompt"] = RAGServiceConfig().system_prompt
    # Nota: max_retries del servicio se configura en el archivo de evaluacion.
    # args.retry controla los reintentos del runner (capa externa), son conceptos distintos.

    current_params = dict(defaults)

    todos_resultados: list[list[ResultadoPregunta]] = []
    configs_usadas: list[RAGServiceConfig] = []
    estado = "en progreso"
    interrumpido_en = None

    guardar_snapshot(
        test_path=test_path,
        titulo=report_title,
        fecha_inicio=fecha_inicio,
        eval_path=eval_path,
        preguntas=preguntas,
        resultados=todos_resultados,
        configs=configs_usadas,
        total_conversaciones=len(sets_parametros),
        estado=estado,
    )

    try:
        for idx_conv, set_params in enumerate(sets_parametros, start=1):
            # refresh NO se acumula: default False salvo que este explicitamente en este set
            refresh_explicito = "refresh" in set_params
            current_params.update(set_params)
            if not refresh_explicito:
                current_params["refresh"] = False

            config = construir_config(current_params)
            configs_usadas.append(config)
            resultados_conv: list[ResultadoPregunta] = []
            todos_resultados.append(resultados_conv)

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
                    if es_error_de_cuota_agotada(e):
                        print(
                            f"[evaluacion] Cuota agotada al inicializar conversacion {idx_conv}; "
                            "no se reintenta."
                        )
                        break
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
                resultados_conv.extend([(str(init_error), None)] * len(preguntas))
                guardar_snapshot(
                    test_path=test_path,
                    titulo=report_title,
                    fecha_inicio=fecha_inicio,
                    eval_path=eval_path,
                    preguntas=preguntas,
                    resultados=todos_resultados,
                    configs=configs_usadas,
                    total_conversaciones=len(sets_parametros),
                    estado=estado,
                )
                if es_error_de_cuota_agotada(init_error):
                    estado = "interrumpido"
                    interrumpido_en = _interrupcion_siguiente_posicion(
                        todos_resultados,
                        len(sets_parametros),
                        len(preguntas),
                    )
                    print(
                        "[evaluacion] Cuota agotada detectada. "
                        "Se guarda el parcial y se aborta la evaluacion."
                    )
                    guardar_snapshot(
                        test_path=test_path,
                        titulo=report_title,
                        fecha_inicio=fecha_inicio,
                        eval_path=eval_path,
                        preguntas=preguntas,
                        resultados=todos_resultados,
                        configs=configs_usadas,
                        total_conversaciones=len(sets_parametros),
                        estado=estado,
                        interrumpido_en=interrumpido_en,
                    )
                    sys.exit(2)
                print(f"[evaluacion] Conversacion {idx_conv} finalizada con error de inicializacion.")
                continue

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
                        if es_error_de_cuota_agotada(e):
                            print(
                                f"[evaluacion] Cuota agotada en pregunta {idx_preg}; "
                                "no se reintenta."
                            )
                            break
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

                guardar_snapshot(
                    test_path=test_path,
                    titulo=report_title,
                    fecha_inicio=fecha_inicio,
                    eval_path=eval_path,
                    preguntas=preguntas,
                    resultados=todos_resultados,
                    configs=configs_usadas,
                    total_conversaciones=len(sets_parametros),
                    estado=estado,
                )

                if ultimo_error is not None and es_error_de_cuota_agotada(ultimo_error):
                    estado = "interrumpido"
                    interrumpido_en = _interrupcion_siguiente_posicion(
                        todos_resultados,
                        len(sets_parametros),
                        len(preguntas),
                    )
                    print(
                        "[evaluacion] Cuota agotada detectada. "
                        "Se guarda el parcial y se aborta la evaluacion."
                    )
                    guardar_snapshot(
                        test_path=test_path,
                        titulo=report_title,
                        fecha_inicio=fecha_inicio,
                        eval_path=eval_path,
                        preguntas=preguntas,
                        resultados=todos_resultados,
                        configs=configs_usadas,
                        total_conversaciones=len(sets_parametros),
                        estado=estado,
                        interrumpido_en=interrumpido_en,
                    )
                    sys.exit(2)

            print(f"[evaluacion] Conversacion {idx_conv} finalizada.")

    except KeyboardInterrupt:
        estado = "interrumpido"
        interrumpido_en = _interrupcion_siguiente_posicion(
            todos_resultados,
            len(sets_parametros),
            len(preguntas),
        )
        print("\n[evaluacion] Evaluacion interrumpida por el usuario. Guardando ultimo snapshot...")
        guardar_snapshot(
            test_path=test_path,
            titulo=report_title,
            fecha_inicio=fecha_inicio,
            eval_path=eval_path,
            preguntas=preguntas,
            resultados=todos_resultados,
            configs=configs_usadas,
            total_conversaciones=len(sets_parametros),
            estado=estado,
            interrumpido_en=interrumpido_en,
        )
        print(f"[evaluacion] Reporte parcial guardado en: {test_path}")
        sys.exit(130)

    estado = "completado"
    print(f"\n[evaluacion] Generando reporte final...")
    guardar_snapshot(
        test_path=test_path,
        titulo=report_title,
        fecha_inicio=fecha_inicio,
        eval_path=eval_path,
        preguntas=preguntas,
        resultados=todos_resultados,
        configs=configs_usadas,
        total_conversaciones=len(sets_parametros),
        estado=estado,
    )
    print(f"[evaluacion] Reporte guardado en: {test_path}")


if __name__ == "__main__":
    main()
