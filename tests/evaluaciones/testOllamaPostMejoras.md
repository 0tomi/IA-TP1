[Preguntas]
# A) Preguntas de Recuperación Directa

- ¿Cuáles son los contenidos de la materia Inteligencia Artificial?
- ¿En qué materia se enseña el concepto de Lógica Difusa?
- ¿Cuál es el plan de estudios de Metodología de la Investigación?
- ¿Qué herramientas de software se recomiendan en la carrera para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas?
- ¿Qué instancias de recuperación nos provee Investigación Operativa?
- ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

# B) Preguntas de Integración

- ¿Qué profesor forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes?
- ¿Qué otra asignatura, además de la propia materia de Inteligencia Artificial, incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas?
- Los requisitos para regularizar en Bases de Datos Avanzadas y en Redes y Comunicaciones, ¿son iguales? ¿Qué diferencias tienen?
- ¿Cuál es el porcentaje de asistencia a clases que exigen en común las materias de Investigación Operativa, Comunicaciones y Redes, y Metodología de la Investigación?
- Un proyecto integrador requiere utilizar un software para resolver problemas de optimización a gran escala que pueda conectarse de forma fluida con bases de datos espaciales.
  Según las herramientas enseñadas en las materias, ¿qué combinación de software visto en Bases de Datos Avanzadas e Investigación Operativa sería la más adecuada para este objetivo?
- Si un estudiante desea investigar sobre el impacto de los "Agentes que aprenden" y las "Redes Neuronales" en la selección de personal y el teletrabajo en Argentina, ¿qué
  normativas legales y temas específicos de los programas de Inteligencia Artificial y RRHH debería cruzar en su marco teórico?

# C) Preguntas de Borde

- ¿Dónde puedo descargar la materia de Cálculo de 1er año?
- El profesor Ing. Jorge L. Schmukler da clases en Bases de Datos Avanzadas, en Inteligencia Artificial y en Redes y Comunicaciones.
- ¿Cuál es el costo de la certificación oficial de Cisco que se menciona como opcional en la planificación?
- Para la Promoción Directa, se exige la aprobación de la totalidad de los trabajos prácticos (TP 1 al TP 5). ¿Cuál es la calificación numérica mínima que debe obtenerse en cada TP individual para que se considere aprobado?
- ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?
- ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

[Parametros 1]
# Mejor score observado: fixed chunks chicos + similarity
llm_provider = ollama
llm_model = llama3.1
embedding_model = BAAI/bge-m3
temperatura = 1.0
chunk_size = 300
chunk_overlap = 30
chunking_technique = fixed_size_overlap
retrieval_type = similarity_search
top_k = 6
max_context_chunks = 6
refresh = true

[Parametros 1.2]
# Chunk mas grande
chunk_size = 500
chunk_overlap = 100
refresh = true

[Parametros 2]
# Segundo mejor score: recursive 512/100 + similarity
chunking_technique = recursive
chunk_size = 512
chunk_overlap = 100
retrieval_type = similarity_search
top_k = 5
max_context_chunks = 5
refresh = true

[Parametros 3]
# Tercer mejor grupo: recursive 500/100 + MMR
retrieval_type = mmr
top_k = 8
max_context_chunks = 8
refresh = true

[Parametros 4]
# Ultima variante a contrastar: recursive 300/50 + similarity
chunking_technique = recursive
chunk_size = 300
chunk_overlap = 50
retrieval_type = similarity_search
top_k = 5
max_context_chunks = 5
refresh = true
