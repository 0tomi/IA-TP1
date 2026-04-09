"""
Script de saneamiento de PDFs para el pipeline del RAG.

Extrae texto, limpia ruido tipografico y estructura rota por la extraccion,
y exporta en formato .toon. Tiene cache por sha256 para no reprocesar archivos repetidos.
"""

import argparse
import hashlib
import json
import re
import shutil
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from carga import CargaConfig, procesar_lote_documentos

ROOT        = Path(__file__).resolve().parent.parent
CORPUS_DIR  = ROOT / "corpus"
OUTPUT_DIR  = Path(__file__).resolve().parent / "output"
REGISTRY    = ROOT / "data" / "registry.json"

# Tablas de limpieza hardcodeadas que salieron de revisar a mano que rompe pypdf
# o que caracteres raros meten las fuentes (ligaduras, webdings, etc)

LIGADURAS_TIPOGRAFICAS = {
    '\uFB01': 'fi',
    '\uFB02': 'fl',
    '\uFB03': 'ffi',
    '\uFB04': 'ffl',
}

PUNTUACION = {
    '\u2013': '-',     # en-dash
    '\u2014': '-',     # em-dash
    '\u2018': "'",     # comilla simple izq
    '\u2019': "'",     # comilla simple der
    '\u201C': '"',     # comilla doble izq
    '\u201D': '"',     # comilla doble der
    '\u2026': '...',   # ellipsis
    '\u2190': '->',    # flecha izq (usada en horarios en tp1)
    '\u2794': '->',    # flecha der
}

BULLETS = {
    '\u25CF': '-',
    '\u25CB': '-',
    '\u25A0': '-',
    '\u2022': '-',
}

# Regex para borrar caracteres de areas privadas de fuentes
RE_PRIVATE_USE = re.compile(r'[\uF000-\uF8FF]')

# Párrafos vacíos que quedaron con espacios en el medio, ej. "\n \n"
RE_LINEAS_EN_BLANCO = re.compile(r'\n[^\S\n\f]*\n+')

# Casos de extracción donde una URL queda pegada a la palabra anterior.
RE_URL_PEGADA = re.compile(r'(?<=[0-9A-Za-zÁÉÍÓÚÑÜáéíóúñü])(?=(?:https?://|www\.))')

# Pypdf a veces se come el espacio entre mayuscula y minuscula.
# E.g. "HolaMundo" -> "Hola Mundo".
# El {2,} es para no romper siglas tipo "iPhone" o "macOS".
RE_PALABRAS_PEGADAS = re.compile(r'([a-záéíóúñü])([A-ZÁÉÍÓÚÑÜ][a-záéíóúñü]{2,})')
RE_FINAL_PUNTUACION_FUERTE = re.compile(r'[\.!\?:…»"\'\)\]]$')
RE_INICIO_ESTRUCTURAL = re.compile(
    r'^(?:[-*]|\d+(?:\.\d+)*[\.)]?|[IVXLCM]+[\.)]?|Cap[ií]tulo\b|Unidad\b|Tema\b|M[oó]dulo\b|Secci[oó]n\b)',
    flags=re.IGNORECASE,
)


def _es_linea_estructural(linea: str) -> bool:
    if not linea:
        return False
    if RE_INICIO_ESTRUCTURAL.match(linea):
        return True

    palabras = linea.split()
    if linea.isupper() and len(palabras) <= 6:
        return True
    if linea.endswith(':') and len(palabras) <= 10:
        return True
    return False


def _debe_unir_lineas(linea_anterior: str, linea_actual: str) -> bool:
    if not linea_anterior or not linea_actual:
        return False
    if RE_FINAL_PUNTUACION_FUERTE.search(linea_anterior):
        return False
    if _es_linea_estructural(linea_actual):
        return False
    return True


def _reconstruir_lineas_quebradas(texto: str) -> str:
    paginas_reconstruidas = []

    for pagina in texto.split("\f"):
        lineas_reconstruidas: list[str] = []

        for raw_line in pagina.split("\n"):
            linea = raw_line.strip()

            if not linea:
                lineas_reconstruidas.append("")
                continue

            if not lineas_reconstruidas or not lineas_reconstruidas[-1]:
                lineas_reconstruidas.append(linea)
                continue

            if _debe_unir_lineas(lineas_reconstruidas[-1], linea):
                lineas_reconstruidas[-1] = f"{lineas_reconstruidas[-1]} {linea}"
            else:
                lineas_reconstruidas.append(linea)

        paginas_reconstruidas.append("\n".join(lineas_reconstruidas))

    return "\f".join(paginas_reconstruidas)

def calcular_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        # Leemos en chunks por si meten un pdf muy pesado
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()

def cargar_registro() -> dict:
    if REGISTRY.exists() and REGISTRY.stat().st_size > 2:
        with open(REGISTRY, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def guardar_registro(registro: dict):
    with open(REGISTRY, 'w', encoding='utf-8') as f:
        json.dump(registro, f, ensure_ascii=False, indent=2)

def extraer_texto(pdf_path: Path) -> tuple[str, int]:
    from pypdf import PdfReader
    reader = PdfReader(pdf_path)
    paginas = []
    for page in reader.pages:
        texto = page.extract_text()
        # Incluimos siempre — aunque sea vacía — para que el índice \f
        # coincida exactamente con el número de página física del PDF.
        paginas.append(texto or "")
    # \f (form feed) como separador de páginas — se preserva hasta los chunkers
    # para que puedan anotar el número de página en cada chunk.
    return "\f".join(paginas), len(reader.pages)

def sanear(texto: str) -> str:
    # 1. Limpieza de caracteres raros
    texto = unicodedata.normalize('NFKC', texto)

    for lig, rmpl in LIGADURAS_TIPOGRAFICAS.items():
        texto = texto.replace(lig, rmpl)
    for char, rmpl in PUNTUACION.items():
        texto = texto.replace(char, rmpl)
    for char, rmpl in BULLETS.items():
        texto = texto.replace(char, rmpl)

    texto = RE_PRIVATE_USE.sub('', texto)
    texto = RE_URL_PEGADA.sub(' ', texto)

    # 2. Arreglo de estructura y saltos de linea random de pypdf
    texto = RE_PALABRAS_PEGADAS.sub(r'\1 \2', texto)

    # A veces quedan saltos de linea cortando oraciones a la mitad. Si la linea
    # anterior no cierra una idea fuerte, la rearmamos incluso si la siguiente
    # arranca con mayuscula.
    texto = _reconstruir_lineas_quebradas(texto)

    # 3. Trim general y colapso de whitespaces
    texto = re.sub(r'[^\S\n\f]+', ' ', texto)           # espacios multiples a uno solo (preserva \f)
    texto = re.sub(r' +([.,;:])', r'\1', texto)        # arregla el espacio feo antes de comas/puntos
    texto = RE_LINEAS_EN_BLANCO.sub('\n\n', texto)    # normaliza párrafos tipo "\n \n"
    texto = re.sub(r'\n{3,}', '\n\n', texto)

    # Vuela numeros sueltos asumiendo que son nros de pagina
    texto = re.sub(r'^\s*\d{1,3}\s*$', '', texto, flags=re.MULTILINE)
    texto = RE_LINEAS_EN_BLANCO.sub('\n\n', texto)
    texto = re.sub(r'\n{3,}', '\n\n', texto)

    # Recortamos por página para no perder separadores \f en bordes del documento.
    paginas = [pagina.strip() for pagina in texto.split("\f")]
    return "\f".join(paginas)

def escapar_toon(text: str) -> str:
    # Helper para que no rompa el formato toon
    return text.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n').replace('\f', '\\f')

def guardar_toon(doc: dict, output_path: Path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("document{content,source,sha256,pages,chars_original,chars_saneado}:\n")
        content = escapar_toon(doc['content'])
        f.write(
            f'"{content}",'
            f'{doc["source"]},'
            f'{doc["sha256"]},'
            f'{doc["pages"]},'
            f'{doc["chars_original"]},'
            f'{doc["chars_saneado"]}\n'
        )

def imprimir_reporte(procesados: list, salteados: list, cargados: list, carga_errores: list):
    print("\n" + "=" * 55)
    print("  Reporte RAG - Sanitize")
    print("=" * 55)

    if procesados:
        print("\n  [+] Procesados (nuevos/cambios):")
        for doc in procesados:
            red = (1 - doc['chars_saneado'] / doc['chars_original']) * 100 if doc['chars_original'] else 0
            print(f"      {doc['source']}")
            print(f"      {doc['chars_original']:>6,} -> {doc['chars_saneado']:>6,} chars  (-{red:.1f}%)")

    if salteados:
        print("\n  [-] Salteados (en cache):")
        for nombre in salteados:
            print(f"      {nombre}")

    if cargados:
        print("\n  [chroma] Cargados en ChromaDB:")
        for nombre in cargados:
            print(f"      {nombre}")

    if carga_errores:
        print("\n  [chroma-error] Errores en carga:")
        for nombre in carga_errores:
            print(f"      {nombre}")

    print(f"\n  {'─'*45}")
    print(f"  Totales : {len(procesados)} proc. | {len(salteados)} cache. | {len(cargados)} chroma OK | {len(carga_errores)} chroma err.")
    print("=" * 55)

def parsear_args() -> CargaConfig:
    parser = argparse.ArgumentParser(
        description="Saneamiento de PDFs y carga en ChromaDB para el pipeline RAG."
    )
    parser.add_argument("--chunk-size", type=int, default=512,
                        help="Tamaño de cada chunk en caracteres (default: 512)")
    parser.add_argument("--chunk-overlap", type=int, default=50,
                        help="Solapamiento entre chunks en caracteres (default: 50)")
    parser.add_argument("--embedding-model", type=str, default="gemini-embedding-001",
                        help="Modelo de embeddings a usar (default: gemini-embedding-001)")
    parser.add_argument(
        "--chunking-technique",
        type=str,
        choices=["recursive", "fixed_size_overlap", "paragraph_custom"],
        default="recursive",
        help="Técnica de chunking a usar (default: recursive)",
    )
    parser.add_argument("--embedding-batch-size", type=int, default=20,
                        help="Cantidad de chunks por batch al embedear (default: 20)")
    parser.add_argument("--max-retries", type=int, default=3,
                        help="Reintentos ante rate limit (default: 3)")
    parser.add_argument("--retry-wait-seconds", type=int, default=60,
                        help="Segundos de espera entre reintentos (default: 60)")

    parser.add_argument(
        "--refresh",
        action="store_true",
        help="Borra /data/ y /output/ completamente antes de procesar.",
    )

    args = parser.parse_args()
    config = CargaConfig(
        chunk_size=args.chunk_size,
        chunk_overlap=args.chunk_overlap,
        embedding_model=args.embedding_model,
        chunking_technique=args.chunking_technique,
        embedding_batch_size=args.embedding_batch_size,
        max_retries=args.max_retries,
        retry_wait_seconds=args.retry_wait_seconds,
    )
    return config, args.refresh


def ejecutar_saneamiento(config: CargaConfig, refresh: bool = False, progress_callback=None) -> None:
    def _report(**kwargs):
        if progress_callback:
            progress_callback(kwargs)

    if refresh:
        data_dir = ROOT / "data"
        if data_dir.exists():
            shutil.rmtree(data_dir)
            print("[sanear] /data/ eliminado.")
        if OUTPUT_DIR.exists():
            shutil.rmtree(OUTPUT_DIR)
            print("[sanear] /output/ eliminado.")

    REGISTRY.parent.mkdir(parents=True, exist_ok=True)
    if not REGISTRY.exists():
        guardar_registro({})

    OUTPUT_DIR.mkdir(exist_ok=True)

    registro = cargar_registro()
    procesados = []
    salteados = []
    cargados = []
    carga_errores = []

    # rglob = escanea las subcarpetas
    pdfs = sorted(CORPUS_DIR.rglob("*.pdf"))
    if not pdfs:
        print("Aviso: No hay pdfs en el corpus para procesar.")
        _report(phase="ready", message="No hay documentos para procesar.")
        return

    total = len(pdfs)
    _report(phase="saneamiento", total_files=total, files_processed=0, current_file="", message="Escaneando corpus...")

    for idx, pdf_path in enumerate(pdfs):
        nombre = pdf_path.name
        sha256 = calcular_sha256(pdf_path)

        # Chequeamos el cache del registro a ver si podemos skipear la extraccion
        if nombre in registro and registro[nombre].get("sha256") == sha256:
            print(f"  [cache] {nombre}")
            salteados.append(nombre)
            _report(phase="saneamiento", total_files=total, files_processed=idx + 1, current_file=nombre, message=f"En caché: {nombre}")
            continue

        print(f"  [proc]  {nombre}")
        _report(phase="saneamiento", total_files=total, files_processed=idx, current_file=nombre, message=f"Procesando: {nombre}")

        texto_crudo, num_paginas = extraer_texto(pdf_path)
        texto_limpio = sanear(texto_crudo)

        doc = {
            'content':        texto_limpio,
            'source':         nombre,
            'sha256':         sha256,
            'pages':          num_paginas,
            'chars_original': len(texto_crudo),
            'chars_saneado':  len(texto_limpio),
        }

        toon_path = OUTPUT_DIR / f"{pdf_path.stem}.toon"
        guardar_toon(doc, toon_path)

        # Derivamos la materia del subdirectorio en corpus/
        relative = pdf_path.relative_to(CORPUS_DIR)
        materia = relative.parts[0] if len(relative.parts) > 1 else "General"

        # Actualizamos el estado para la etapa de embeddings (carga.py)
        registro[nombre] = {
            "sha256":         sha256,
            "toon":           toon_path.relative_to(ROOT).as_posix(),
            "pages":          num_paginas,
            "chars_original": len(texto_crudo),
            "chars_saneado":  len(texto_limpio),
            "cargado_en_chroma": False,
            "materia":        materia,
        }

        procesados.append(doc)
        _report(phase="saneamiento", total_files=total, files_processed=idx + 1, current_file=nombre, message=f"Saneado: {nombre}")

        # Guardamos el registro por si el script falla al parsear el siguiente
        guardar_registro(registro)

    # === FASE 2: CARGA EN LOTE A CHROMA ===
    nuevos_archivos = [doc['source'] for doc in procesados]

    if nuevos_archivos:
        print(f"\n[sanear] Iniciando carga en lote a ChromaDB para {len(nuevos_archivos)} archivos nuevos...")
        _report(phase="embeddings", total_files=len(nuevos_archivos), files_processed=0, current_file="", message=f"Generando embeddings para {len(nuevos_archivos)} archivos...")
        try:
            resultados = procesar_lote_documentos(nuevos_archivos, config=config, progress_callback=progress_callback)
            for nombre, ok in resultados:
                if ok:
                    cargados.append(nombre)
                else:
                    carga_errores.append(nombre)
        except Exception as e:
            print(f"[sanear] FATAL ERROR en carga por lote: {e}")

    # Recargamos el registro final por si carga.py lo actualizó internamente
    registro = cargar_registro()
    imprimir_reporte(procesados, salteados, cargados, carga_errores)


def main():
    config, refresh = parsear_args()
    ejecutar_saneamiento(config, refresh)

if __name__ == "__main__":
    main()
