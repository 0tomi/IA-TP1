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

# C) Preguntas de Límite

- ¿Dónde puedo descargar la materia de Cálculo de 1er año?
- El profesor Ing. Jorge L. Schmukler da clases en Bases de Datos Avanzadas, en Inteligencia Artificial y en Redes y Comunicaciones.
- ¿Cuál es el costo de la certificación oficial de Cisco que se menciona como opcional en la planificación?
- Para la Promoción Directa, se exige la aprobación de la totalidad de los trabajos prácticos (TP 1 al TP 5). ¿Cuál es la calificación numérica mínima que debe obtenerse en cada TP individual para que se considere aprobado?
- ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?
- ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

[Parametros 1]
llm_provider = google
llm_model = gemini-3.1-flash-lite-preview
embedding_model = gemini-embedding-001
chunk_size = 800
chunk_overlap = 200
chunking_technique = fixed_size_overlap
retrieval_type = similarity_search
top_k = 5
max_context_chunks = 5
refresh = true

[Parametros 2]
retrieval_type = mmr

[Parametros 3]
retrieval_type = threshold
threshold = 0.7

[Parametros 4]
retrieval_type = threshold
threshold = 0.5

[Parametros 5]
chunk_size = 1024
chunking_technique = recursive
retrieval_type = similarity_search
top_k = 7
max_context_chunks = 5
refresh = true

[Parametros 6]
retrieval_type = mmr

[Parametros 7]
retrieval_type = threshold
threshold = 0.5
