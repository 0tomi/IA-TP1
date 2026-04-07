# Saneamiento de Corpus - Pipeline RAG

Este modulo se encarga de transformar los documentos PDF originales en archivos de texto estructurado (.toon) optimizados para su ingesta en un LLM.

## Caracteristicas Principales

- **Busqueda Recursiva**: Escanea automaticamente todas las subcarpetas del directorio `corpus/`.
- **Deduplicacion por Hash**: Utiliza el algoritmo SHA256 para verificar si un archivo ya fue procesado. Si el contenido no cambio, el script lo saltea automaticamente.
- **Limpieza Adaptativa**: Corrije artefactos comunes de la extraccion de PDFs (ligaduras tipograficas, espacios perdidos entre palabras y saltos de linea huerfanos).
- **Formato TOON**: Genera archivos individuales con una cabecera de metadatos y el contenido escapado en una sola linea, maximizando la eficiencia de tokens.

## Flujo de Trabajo

1. **Calculo de Identidad**: Se genera un hash unico para cada PDF encontrado.
2. **Consulta al Registro**: Se verifica en `data/registry.json` si el hash ya existe.
3. **Procesamiento (si es necesario)**:
    - Extraccion de texto via `pypdf`.
    - Normalizacion de caracteres (NFKC).
    - Eliminacion de ruido (headers, footers basicos, numeracion de paginas).
    - Exportacion a `saneamiento/output/[nombre].toon`.
4. **Actualizacion de Estado**: Se registra el nuevo SHA y la ruta del TOON en el archivo central de datos.

## Estructura del Proyecto Relacionada

- `/corpus/`: Fuentes PDF (admite carpetas anidadas).
- `/saneamiento/sanear.py`: Logica principal del modulo.
- `/saneamiento/output/*.toon`: Resultados listos para el RAG.
- `/data/registry.json`: Fuente de verdad sobre el estado del sistema.

## Integracion con el Modulo de Carga

El script marca cada nuevo documento con el flag `"cargado_en_chroma": false`. El siguiente modulo del pipeline debe:
1. Leer el `registry.json`.
2. Procesar solo los archivos con estado `false`.
3. Actualizar el estado a `true` tras una carga exitosa en la base vectorial.

## Requisitos
- `pypdf`: Para la extraccion base.
- `pathlib`: Para manejo de rutas cross-platform.
