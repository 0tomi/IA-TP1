"""
saneamiento de corpus pdf para sistema rag.

extrae texto de los pdfs en corpus/, lo limpia
y lo exporta en formato toon para la etapa de chunking.

dependencias: pip install pypdf
"""

import re
import unicodedata
from pathlib import Path
from pypdf import PdfReader

# rutas relativas al script
CORPUS_DIR = Path(__file__).resolve().parent.parent / "corpus"
OUTPUT_DIR = Path(__file__).resolve().parent / "output"


# tablas de reemplazo..
# estos mapeos salen de analizar los pdfs del corpus con un script aparte
# cada entrada resuelve un problema real encontrado en al menos un archivo

# tablas de equivalencias que mete el pdf cuando el font las usa
LIGADURAS = {
    '\uFB01': 'fi', #os {} definen un Diccionario (clave: valor)
    '\uFB02': 'fl',
    '\uFB03': 'ffi',
    '\uFB04': 'ffl',
}

# puntuacion unicode -> ascii equivalente
PUNTUACION = {
    '\u2013': '-',     # en-dash
    '\u2014': '-',     # em-dash
    '\u2018': "'",     # comilla simple izq
    '\u2019': "'",     # comilla simple der
    '\u201C': '"',     # comilla doble izq
    '\u201D': '"',     # comilla doble der
    '\u2026': '...',   # elipsis
    '\u2190': '->',    # flecha izquierda (bda usa esto para horarios)
    '\u2794': '->',    # flecha derecha (metodologia)
}

# bullets decorativos -> guion (para que sea uniforme)
BULLETS = {
    '\u25CF': '-',     # circulo negro
    '\u25CB': '-',     # circulo blanco
    '\u25A0': '-',     # cuadrado negro
    '\u2022': '-',     # bullet clasico
}

#aca aplicamos patrones de busqueda inteligentes
# regex para chars del area privada unicode (wingdings, symbol, etc)
RE_PRIVATE_USE = re.compile(r'[\uF000-\uF8FF]')

""" regex para palabras pegadas por culpa de pypdf
detecta "minusculaMayuscula" y mete un espacio en el medio,
pero solo cuando la parte en mayuscula tiene 3+ letras (para no romper cosas como "iPhone")"""
RE_PALABRAS_PEGADAS = re.compile(r'([a-záéíóúñü])([A-ZÁÉÍÓÚÑÜ][a-záéíóúñü]{2,})')


def extraer_texto(pdf_path):
    """extrae todo el texto de un pdf, pagina por pagina."""
    reader = PdfReader(pdf_path)
    paginas = []
    for page in reader.pages:
        texto = page.extract_text()
        if texto:
            paginas.append(texto)
    return "\n".join(paginas), len(reader.pages)


def sanear(texto):
    """
    pipeline de limpieza.
    el orden importa: primero normalizamos chars, despues estructura.
    """

    # --- fase 1: normalizar caracteres ---

    # componer acentos unicode (ej: a + tilde combinante -> á)
    texto = unicodedata.normalize('NFKC', texto)

    # desarmar ligaduras (ﬁ -> fi, ﬂ -> fl)
    for lig, reemplazo in LIGADURAS.items():
        texto = texto.replace(lig, reemplazo)

    # puntuacion tipografica a ascii
    for char, reemplazo in PUNTUACION.items():
        texto = texto.replace(char, reemplazo)

    # bullets decorativos a guion
    for char, reemplazo in BULLETS.items():
        texto = texto.replace(char, reemplazo)

    # sacar chars privados de fuentes embebidas (quedan como basura invisible)
    texto = RE_PRIVATE_USE.sub('', texto)

    # --- fase 2: reparar estructura rota por la extraccion ---

    # pypdf a veces pega palabras que en el pdf visual estan separadas.
    # ej: "AvanzadasEquipo" -> "Avanzadas Equipo"
    texto = RE_PALABRAS_PEGADAS.sub(r'\1 \2', texto)

    # tambien rompe palabras con saltos de linea espureos
    # ej: "provistas\n \npor\n \nel" -> "provistas por el"
    texto = re.sub(r'(?<=[a-záéíóúñü,;])\n \n(?=[a-záéíóúñüA-ZÁÉÍÓÚÑÜ])', ' ', texto)
    texto = re.sub(r'(?<=[a-záéíóúñü,;])\n(?=[a-záéíóúñü])', ' ', texto)

    # --- fase 3: limpiar espacios y lineas ---

    # colapsar espacios multiples en uno (sin tocar los \n)
    texto = re.sub(r'[^\S\n]+', ' ', texto)

    # espacio antes de punto o coma (artefacto comun)
    # "palabra ." -> "palabra."
    texto = re.sub(r' +([.,;:])', r'\1', texto)

    # colapsar saltos de linea excesivos
    texto = re.sub(r'\n{3,}', '\n\n', texto)

    # numeros de pagina sueltos (lineas que son solo 1-3 digitos)
    texto = re.sub(r'^\s*\d{1,3}\s*$', '', texto, flags=re.MULTILINE)

    # limpiar las lineas vacias que dejaron los pasos anteriores
    texto = re.sub(r'\n{3,}', '\n\n', texto)

    return texto.strip()


# --- formato toon ---

def escapar_toon(text):
    """escapa comillas y saltos de linea para que el valor sea valido en toon."""
    return text.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')


def guardar_toon(documentos, output_path):
    """
    guarda en toon (token-oriented object notation).
    es como un json pero columnar: declara los campos una vez
    y despues cada linea es un registro. ahorra ~40% de tokens.
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"documents[{len(documentos)}]{{content,source,pages,chars_original,chars_saneado}}:\n")
        for doc in documentos:
            content = escapar_toon(doc['content'])
            f.write(f'"{content}",{doc["source"]},{doc["pages"]},{doc["chars_original"]},{doc["chars_saneado"]}\n')


# --- reporte ---

def imprimir_reporte(documentos):
    """muestra un antes/despues por archivo y el total."""
    total_antes = sum(d['chars_original'] for d in documentos)
    total_despues = sum(d['chars_saneado'] for d in documentos)
    reduccion = (1 - total_despues / total_antes) * 100 if total_antes else 0

    print("\n" + "=" * 55)
    print("  reporte de saneamiento")
    print("=" * 55)

    for doc in documentos:
        red = (1 - doc['chars_saneado'] / doc['chars_original']) * 100 if doc['chars_original'] else 0
        print(f"\n  {doc['source']}")
        print(f"    {doc['chars_original']:>6,} -> {doc['chars_saneado']:>6,} chars  (-{red:.1f}%)")

    print(f"\n  {'─'*45}")
    print(f"  total antes:        {total_antes:,} chars")
    print(f"  total despues:      {total_despues:,} chars")
    print(f"  reduccion de ruido: {reduccion:.1f}%")
    print(f"  documentos:         {len(documentos)}")
    print("=" * 55)


# --- main ---

def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    documentos = []

    print(f"corpus: {CORPUS_DIR}")
    print(f"output: {OUTPUT_DIR}\n")

    pdfs = sorted(CORPUS_DIR.glob("*.pdf"))
    if not pdfs:
        print("no se encontraron pdfs en el corpus.")
        return

    for pdf_path in pdfs:
        nombre = pdf_path.name
        print(f"  procesando: {nombre}")

        texto_crudo, num_paginas = extraer_texto(str(pdf_path))
        texto_limpio = sanear(texto_crudo)

        documentos.append({
            'content': texto_limpio,
            'source': nombre,
            'pages': num_paginas,
            'chars_original': len(texto_crudo),
            'chars_saneado': len(texto_limpio),
        })

        print(f"    {len(texto_crudo):,} -> {len(texto_limpio):,} chars")

    # guardar
    toon_path = OUTPUT_DIR / "corpus_saneado.toon"
    guardar_toon(documentos, str(toon_path))
    print(f"\n  guardado: {toon_path}")

    imprimir_reporte(documentos)


if __name__ == "__main__":
    main()
