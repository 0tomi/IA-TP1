[Preguntas]

# --- Preguntas trampa (el sistema debe responder que no tiene información) ---

¿Cuál es la nota mínima de aprobación en la materia Inteligencia Artificial?
¿Quién es el profesor titular de Bases de Datos Avanzadas?
¿En qué edificio o aula se dicta Comunicación y Redes?
¿Cuántos estudiantes están inscriptos en Investigación Operativa este año?
¿Qué software de simulación se usa obligatoriamente en el laboratorio de Redes?
¿Cuál fue la última reforma curricular del plan de estudios de Informática y RRHH?

# --- Preguntas comunes (tópico único: Inteligencia Artificial) ---

¿Cuáles son los objetivos generales de la materia Inteligencia Artificial?
¿Qué unidades temáticas componen el programa de Inteligencia Artificial?
¿Qué se entiende por agente inteligente en el marco del programa de IA?
¿Qué métodos o estrategias de búsqueda se estudian en la materia de IA?
¿Qué contenidos de aprendizaje automático o machine learning se incluyen en el programa de IA?
¿Cuáles son los criterios de evaluación o modalidades de trabajo práctico en IA?

# --- Preguntas de integración (múltiples tópicos) ---

¿Qué materias del corpus aplican metodologías de investigación científica como parte de su programa?
¿En qué materias se trabaja con modelos matemáticos o técnicas de optimización?
¿Qué herramientas tecnológicas o lenguajes de programación se mencionan a lo largo de los distintos programas?
¿Cómo se complementan los contenidos de Bases de Datos Avanzadas e Investigación Operativa para el análisis de información?
¿Qué similitudes existen entre los enfoques de evaluación de Inteligencia Artificial y los de Comunicación y Redes?
¿Qué materias abordan explícitamente competencias relacionadas con el trabajo en equipo o habilidades blandas?

[Parametros 1]
llm_provider = ollama
llm_model = llama3.1
embedding_model = BAAI/bge-m3
chunk_size = 1024
chunking_technique = fixed_size_overlap
retrieval_type = similarity_search
top_k = 5
max_context_chunks = 5
refresh = true

[Parametros 2]
retrieval_type = mmr

[Parametros 3]
retrieval_type = threshold
threshold = 0.5
