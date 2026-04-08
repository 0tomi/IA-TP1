# IA-TP1: Sistema RAG (LangChain)

Este es un sistema RAG (Retrieval-Augmented Generation) avanzado que responde consultas basadas en un corpus documental consolidado.

## Estructura del Sistema

1. **[Saneamiento](./saneamiento/):** Ingesta de PDFs, limpieza y preparacion de datos.
2. **Carga (Pendiente):** Chunking de archivos .toon e indexacion en base vectorial (ChromaDB).
3. **Recuperacion (Pendiente):** Interfaz de usuario, retrieval semantico y generacion via LLM.

## Instrucciones del Modulo de Saneamiento

Para procesar los PDFs originales y generar los archivos optimizados:

```bash
python saneamiento/sanear.py
```

- Los resultados se guardaran en `./saneamiento/output/`.
- El estado de procesamiento se guardara en `./data/registry.json`.

## Caracteristicas Adicionales

- **Cache Inteligente**: El sistema solo procesa archivos que hayan cambiado de contenido, basandose en SHA256.
- **Portabilidad**: El registro de archivos utiliza rutas relativas y formato POSIX, permitiendo que el proyecto se mueva de entorno sin romper rutas.

## Uso opcional de Ollama con Llama 3.1

El chatbot puede usar Google Gemini o, de manera opcional, un modelo local en Ollama.

- En el wizard de `recuperacion.py` se pregunta si queres habilitar Ollama.
- Si respondes que si, se habilita el modelo local `llama3.1`.
- Si respondes que no, el flujo sigue usando Gemini como hasta ahora.

Para usar Ollama localmente:

```bash
poetry install -E ollama
ollama pull llama3.1
```

Ademas, Ollama debe estar instalado y en ejecucion al momento de iniciar el servicio.

Para mas informacion tecnica detallada, consulte: [GUIA_TECNICA.md](./saneamiento/GUIA_TECNICA.md)
