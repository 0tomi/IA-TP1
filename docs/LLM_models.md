## Modelos Google

Estos modelos aparecen siempre en el wizard y usan `ChatGoogleGenerativeAI`.

- `gemini-3.1-flash-lite-preview`
- `gemini-2.0-flash`
- `gemini-3.0-flash`
- `gemini-2.5-pro`

Requisitos:

- Tener `GOOGLE_API_KEY` configurada en el entorno o en `.env`.
- No requieren Ollama.

## Modelo local con Ollama

Modelo soportado actualmente:

- `llama3.1`

Este modelo usa `ChatOllama` mediante `langchain-ollama`.

Requisitos:

1. Instalar las dependencias opcionales del proyecto para Ollama:

```bash
poetry install -E ollama
```

2. Tener Ollama instalado en la PC.

3. Descargar el modelo localmente:

```bash
ollama pull llama3.1
```

4. Tener Ollama en ejecución al momento de correr el asistente.

## Uso en `evaluacion.md`

Para correr una evaluación automática con Ollama, agregá estas dos entradas en el set de parámetros:

llm_provider=ollama
llm_model=llama3.1

Si no incluís esas dos claves, `evaluacion.py` sigue usando el default del proyecto:

llm_provider=google
llm_model=gemini-3.1-flash-lite-preview
