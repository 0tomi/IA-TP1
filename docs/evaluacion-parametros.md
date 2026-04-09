# Parámetros configurables de `evaluacion.md`

Referencia completa de todos los parámetros que pueden aparecer en las secciones
`[Parametros N]` del archivo de evaluación.

---

## Formato del archivo

```
[Preguntas]
Pregunta 1
Pregunta 2
...

[Parametros 1]
clave = valor
...

[Parametros 2]
clave = valor   ← solo los que cambian respecto al set anterior
...
```

**Carry-over:** los parámetros se acumulan entre sets. Si `chunk_size` no aparece
en `[Parametros 2]`, conserva el valor del set anterior.  
**Excepción:** `refresh` nunca se acumula — siempre es `false` salvo que esté
explícitamente en el set actual.

---

## Parámetros de Retrieval

| Parámetro | Tipo | Default | Descripción |
|---|---|---|---|
| `top_k` | int | `5` | Cantidad de chunks recuperados del vectorstore antes de filtrar |
| `retrieval_type` | str | `similarity_search` | Estrategia de recuperación (ver opciones abajo) |
| `threshold` | float | `0.5` | Similitud mínima para incluir un chunk (solo aplica con `retrieval_type = threshold`) |
| `max_context_chunks` | int | `5` | Máximo de chunks que se envían al LLM como contexto (trunca el resultado de `top_k`) |

### Opciones de `retrieval_type`

| Valor | Descripción |
|---|---|
| `similarity_search` | Cosine similarity clásica. Retorna los `top_k` más similares sin importar redundancia |
| `mmr` | Maximal Marginal Relevance. Balancea similitud y diversidad — evita chunks repetitivos |
| `threshold` | Solo retorna chunks cuya similitud supere el valor de `threshold` |

---

## Parámetros del LLM

| Parámetro | Tipo | Default | Descripción |
|---|---|---|---|
| `llm_provider` | str | `google` | Proveedor del modelo de lenguaje (ver opciones abajo) |
| `llm_model` | str | `gemini-3.1-flash-lite-preview` | Nombre del modelo a usar (debe corresponder al proveedor) |
| `temperatura` | float | `0.7` | Creatividad de las respuestas. `0.0` = determinístico, `2.0` = muy aleatorio |
| `system_prompt` | str | _(prompt interno)_ | Prompt del sistema. Debe contener los placeholders `{contexto}` y `{pregunta}` |

### Opciones de `llm_provider`

| Valor | Requisito |
|---|---|
| `google` | Variable de entorno `GOOGLE_API_KEY` en `.env` |
| `ollama` | Ollama corriendo en local (`ollama serve`) con el modelo descargado |

### Opciones de `llm_model` según proveedor

**Google (`llm_provider = google`):**

| Valor | Descripción |
|---|---|
| `gemini-3.1-flash-lite-preview` | Rápido, liviano. **Default** |
| `gemini-2.0-flash` | Más capaz que lite |
| `gemini-3.0-flash` | Generación más reciente de flash |
| `gemini-2.5-pro` | Máxima capacidad, mayor costo de tokens |

**Ollama (`llm_provider = ollama`):**

| Valor | Descripción |
|---|---|
| `llama3.1` | Llama 3.1 corriendo localmente |

---

## Parámetros de Chunking

| Parámetro | Tipo | Default | Descripción |
|---|---|---|---|
| `chunk_size` | int | `512` | Tamaño máximo de cada chunk en caracteres |
| `chunk_overlap` | int | `50` | Superposición en caracteres entre chunks consecutivos |
| `chunking_technique` | str | `recursive` | Estrategia de división del texto (ver opciones abajo) |
| `refresh` | bool | `false` | Si `true`, borra y re-procesa todo el corpus desde cero. **No se acumula entre sets** |

### Opciones de `chunking_technique`

| Valor | Descripción |
|---|---|
| `recursive` | Divide recursivamente por `\n\n`, `\n`, `. `, etc. Detecta secciones por título. **Recomendado** |
| `fixed_size_overlap` | Corte fijo por caracteres con overlap configurable. Más simple y predecible |
| `paragraph_custom` | Divide por párrafos (`\n\n`). Párrafos cortos = un chunk; largos = corte fijo |

---

## Parámetros de Embedding

| Parámetro | Tipo | Default | Descripción |
|---|---|---|---|
| `embedding_model` | str | `gemini-embedding-001` | Modelo usado para vectorizar chunks y queries |
| `embedding_batch_size` | int | `20` | Chunks procesados por lote al cargar al vectorstore |

### Opciones de `embedding_model`

| Valor | Tipo | Notas |
|---|---|---|
| `gemini-embedding-001` | API Google | Requiere `GOOGLE_API_KEY`. **Default** |
| `intfloat/multilingual-e5-small` | Local | Rápido, multilingüe, liviano |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | Local | Multilingüe, equilibrado |
| `sentence-transformers/all-MiniLM-L6-v2` | Local | Solo inglés, muy rápido |
| `BAAI/bge-m3` | Local | Alta calidad, requiere más RAM y tiempo de carga |

> **Importante:** cambiar `embedding_model` o `chunk_size` invalida los documentos
> ya indexados. Usá `refresh = true` en el set que introduzca ese cambio.

---

## Parámetros de Retry

| Parámetro | Tipo | Default | Descripción |
|---|---|---|---|
| `max_retries` | int | `3` | Reintentos ante errores de rate limit (RESOURCE_EXHAUSTED) tanto en embedding como en query |
| `retry_wait_seconds` | int | `60` | Segundos de espera entre reintentos |

---

## Parámetros de diagnóstico

| Parámetro | Tipo | Default | Descripción |
|---|---|---|---|
| `debug` | bool | `false` | Si `true`, imprime por consola los chunks recuperados y metadata de cada query |

---

## Ejemplo completo

```
[Preguntas]
¿Cuáles son los objetivos de la materia IA?
¿Qué técnicas de búsqueda se estudian en IA?

[Parametros 1]
retrieval_type = similarity_search
top_k = 5
chunk_size = 512
chunk_overlap = 50
chunking_technique = recursive
embedding_model = gemini-embedding-001
llm_provider = google
llm_model = gemini-3.1-flash-lite-preview
temperatura = 0.3
max_retries = 3
retry_wait_seconds = 60
refresh = true

[Parametros 2]
retrieval_type = mmr
top_k = 8

[Parametros 3]
chunk_size = 256
chunk_overlap = 30
refresh = true
```

En este ejemplo:
- **Set 1**: configuración completa de referencia, reconstruye el índice (`refresh = true`)
- **Set 2**: cambia solo la estrategia de retrieval a MMR con más chunks. Hereda todo lo demás del set 1. `refresh` vuelve a `false` automáticamente
- **Set 3**: achica los chunks a 256 caracteres y fuerza re-indexado porque cambió `chunk_size`
