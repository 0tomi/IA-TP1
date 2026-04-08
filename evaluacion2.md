[Preguntas]
# A) Preguntas de Recuperación Directa

- ¿Cuáles son los requisitos previos para promocionar Inteligencia Artificial?
- ¿En qué materia se enseña el concepto RAGs?
- ¿Cuál es el plan de estudios de Metodología de la Investigación?
- En Comunicaciones y Redes, ¿cómo hago para quedar como alumno regular?
- ¿Qué temas entran en el parcial de Investigación Operativa del 15 de junio?
- ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

# B) Preguntas de Integración

- ¿Qué vinculaciones temáticas existen entre Bases de Datos Avanzadas y Comunicación y Redes que resulten pertinentes para el perfil de un arquitecto de sistemas?
- ¿En qué asignaturas de 4to año se analiza el impacto de la Inteligencia Artificial en las personas o las organizaciones, y desde qué enfoque lo aborda cada una?
- Los requisitos para regularizar en Bases de Datos Avanzadas y en Redes y Comunicaciones, ¿son iguales? ¿Qué diferencias tienen?
- ¿De qué manera el algoritmo de la ruta más corta de Redes de la unidad 7 se relaciona con los modelos de transporte y transbordo de Investigación Operativa en la Unidad 5?
- Si quiero promocionar todas las materias de 4to año, ¿cuál es la diferencia de promedio exigido entre Investigación Operativa e Inteligencia Artificial?
- ¿Qué herramientas de software se recomiendan en la carrera para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas?

# C) Preguntas de Borde

- ¿Dónde puedo descargar la materia de Cálculo de 1er año?
- El profesor Ing. Jorge L. Schmukler da clases en Bases de Datos Avanzadas, en Inteligencia Artificial y en Redes y Comunicaciones.
- ¿Cuál es el costo de la certificación oficial de Cisco que se menciona como opcional en la planificación?
- Para la Promoción Directa, se exige la aprobación de la totalidad de los trabajos prácticos (TP 1 al TP 5). ¿Cuál es la calificación numérica mínima que debe obtenerse en cada TP individual para que se considere aprobado?
- ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?
- ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

[Parametros 1]
# Baseline: Temp 0.5, Prompt default, Chunks 512
llm_provider = ollama
llm_model = llama3.1
embedding_model = BAAI/bge-m3
temperatura = 0.5
chunk_size = 512
chunk_overlap = 50
chunking_technique = recursive
retrieval_type = similarity_search
top_k = 5
max_context_chunks = 5
refresh = true

[Parametros 2]
# Subimos temperatura a 1.0 (Sin tocar nada más)
temperatura = 1.0

[Parametros 3]
# Temperatura 1.5 y Chunks grandes (1000/200) para contexto más amplio
temperatura = 1.5
chunk_size = 1000
chunk_overlap = 200
refresh = true

[Parametros 4]
# Temperatura 2.0 (Caos controlado con prompt restrictivo por defecto)
temperatura = 2.0

[Parametros 5]
# TEST: System Prompt ABIERTO + Temperatura 1.0 + Chunks fragmentados (300/30)
# Queremos ver si el modelo "rellena" los huecos del chunking malo con su conocimiento
temperatura = 1.0
system_prompt = Sos un asistente académico experto. Usá el contexto proporcionado: {contexto}. Si la información es escasa, completá con tu conocimiento general de ingeniería pero aclaralo. Pregunta: {pregunta}
chunk_size = 300
chunk_overlap = 30
chunking_technique = fixed_size_overlap
refresh = true

[Parametros 6]
# Mismo prompt abierto pero con MMR para ver si la diversidad de fuentes ayuda
retrieval_type = mmr
top_k = 8

[Parametros 7]
# Subimos a 1.5 con el prompt abierto
temperatura = 1.5

[Parametros 8]
# TEST: System Prompt EXTREMADAMENTE CERRADO + Temperatura 2.0
# Buscamos ver si un prompt muy rígido puede contener el delirio de una temperatura tan alta
temperatura = 2.0
system_prompt = SOS UN ROBOT DE EXTRACCIÓN. PROHIBIDO AGREGAR COMENTARIOS. Si la respuesta no está LITERAL en el contexto, respondé: 'DATO NO ENCONTRADO'. No uses tu conocimiento previo. Contexto: {contexto}. Pregunta: {pregunta}
chunk_size = 600
chunk_overlap = 100
chunking_technique = recursive
refresh = true
