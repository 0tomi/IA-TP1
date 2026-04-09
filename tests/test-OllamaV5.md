# Evaluacion — test-OllamaV5

_Iniciada: 2026-04-09 02:39:40_
_Ultima actualizacion: 2026-04-09 02:45:45_

**Estado:** completado
**Archivo de evaluacion:** `tests/evaluacionOllamaTop4.md`
**Preguntas:** 18 | **Conversaciones planificadas:** 4 | **Conversaciones iniciadas:** 4 | **Preguntas procesadas:** 72

**Nota de comparacion con V4:** este informe mantiene las mismas primeras 3 configuraciones de `V4` y agrega una cuarta conversacion con `recursive`, `chunk_size = 300`, `chunk_overlap = 50`, `retrieval_type = similarity_search`, `top_k = 5`, `max_context_chunks = 5`. En los artefactos de evaluacion no aparece ningun cambio explicito de `system prompt` entre `V4` y `V5`.

**Criterio de puntaje:** 1 punto por respuesta correcta o abstencion correcta en preguntas de borde, 0.5 por respuesta parcial pero util y 0 por respuesta incorrecta, incompleta de forma critica o no sustentada por el contexto.

## Conversacion 1

**Puntaje evaluado: 11.5 / 18**

**Parametros:**

| Parametro | Valor |
|---|---|
| top_k | 5 |
| retrieval_type | similarity_search |
| threshold | 0.5 |
| max_context_chunks | 5 |
| temperatura | 1.0 |
| debug | False |
| llm_provider | ollama |
| llm_model | llama3.1 |
| chunk_size | 300 |
| chunk_overlap | 30 |
| embedding_model | BAAI/bge-m3 |
| chunking_technique | fixed_size_overlap |
| embedding_batch_size | 20 |
| max_retries | 3 |
| retry_wait_seconds | 60 |
| refresh | True |

### Pregunta 1

> - ¿Cuáles son los contenidos de la materia Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. He
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Descripción | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Descripción de los temas específicos a desarrollarse en la asignatura.
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Métodos | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Métodos comparativas entre las distintas representaciones. Comportamiento de Agentes Basados en Conocimientos. Capítulo IV Diseño de los Sistemas Exper
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Métodos | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Métodos y mensajes. Representación de Conocimientos mediante reglas. Estructura básica. Representación de reglas mediante objetos.
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Integración | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Integración Neuronales Artificiales (RNA). Generalidades, conceptos básicos Reseña Histórica.

**Respuesta:**

La materia de Inteligencia Artificial abarca temas como Agentes Inteligentes, Desarrollo de Representaciones, Métodos comparativos entre representaciones, Comportamiento de Agentes Basados en Conocimientos, Diseño de Sistemas Expertos y su descripción de módulos, Representación de Conocimientos mediante reglas y estructura básica, y Representación de reglas mediante objetos.

**Tokens:** entrada: 839 | salida: 87 | total: 926

---

### Pregunta 2

> - ¿En qué materia se enseña el concepto de Lógica Difusa?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Capítulo VI | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Capítulo VI Lógica Difusa (Fuzzy). Consideraciones generales, Conjuntos Difusos, definición.
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Composición | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Composición MAX-MIN. Capítulo VII Sistemas Difusos. Consideraciones generales. Representación de conocimiento estructurado mediante reglas lingüísticas.
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Integración | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Procesos | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Procesos basadas en Lógica.
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Lógica | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Lógica de

**Respuesta:**

La materia en la que se enseña el concepto de Lógica Difusa es Inteligencia Artificial.

**Tokens:** entrada: 851 | salida: 25 | total: 876

---

### Pregunta 3

> - ¿Cuál es el plan de estudios de Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: JIMENA | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: JIMENA CRUZ; Año de la carrera a la que pertenece la cátedra: 4 Régimen de la materia: Anual Carga horaria semanal: 3 horas Correlativa: Ingeniería
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 1 12 de marzo Presencial Teórico/práctico Presentación de la asignatura | 2 19 de marzo Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 1 12 de marzo Presencial Teórico/práctico Presentación de la asignatura | 2 19 de marzo Virtual Teoría Conceptos generales para introducción 3 26 de
3. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Metodología | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Metodología como el conjunto de estrategias, reflexiones y decisiones que configuran los procesos de investigación científica. Por lo
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 8 30 de abril Presencial (pedir cambio fecha) Práctica | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 8 30 de abril Presencial (pedir cambio fecha) Práctica 9 7 de mayo virtual Teoría Alcances, límites y limitaciones/ Objetivos / Justificación 10 14 d
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Metodología | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Metodología ica desde espacios de reflexión sistemáticos enmarcados en trabajos propios de la disciplina y el campo profesional. Objetivos

**Respuesta:**

El plan de estudios de la materia Metodología de la Investigación incluye varias secciones que se desarrollan a lo largo de unas semanas específicas.

Durante las semanas 1 y 2, se imparten conceptos generales de introducción y se presenta la asignatura, respectivamente.

A partir de la semana 3, el contenido se divide entre teoría y práctica. Las sesiones prácticas se abordan en las semanas 3, 4, 10, 8 y 14, mientras que las sesiones teóricas se desarrollan en las semanas 2, 4, 5, 6, 7, 9, 11 y 12.

En las sesiones prácticas, se profundiza en tópicos como la escritura académica, la pregunta de investigación, el tema o problema y el marco teórico y la hipótesis.

Por otra parte, en las sesiones teóricas se analizan conceptos relacionados con la pregunta de investigación, las variables, la unidad de análisis y el contexto.

Al final del plan de estudios, en la semana 12, se examina el alcance, límites y limitaciones, los objetivos y la justificación de la investigación.

No dispongo de información en mis documentos para responder sobre los objetivos específicos de la materia.

**Tokens:** entrada: 1130 | salida: 291 | total: 1421

---

### Pregunta 4

> - En Comunicaciones y Redes, ¿cómo hago para quedar como alumno regular?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE robado los dos trabajos práctico impartido por la cátedra. 3- Asistir al 80% d
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE El alumno accederá a la condición de PROMOCIÓN si cumple con las siguientes co
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE sistencia a una de estas evaluaciones se tomará como la reprobación de la mism
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE superior o igual a los 60 puntos. Tener aprobado con 60 puntos los tres parcia
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE prácticos desarrollados en la materia (prueba escrita). El alumno LIBRE rendir

**Respuesta:**

Para quedar como alumno regular en la materia de Comunicaciones y Redes, debes cumplir con las siguientes condiciones de cátedra: obtener en los 3 parciales una calificación promedio superior o igual a los 60 puntos y haber realizado y aprobado los dos trabajos prácticos. Además, debes asistir al 80% de las clases teóricas y prácticas.

También menciona el texto que: "El alumno accederá a la condición de REGULAR, si cumple con las siguientes condiciones de cátedra..." sin indicar explícitamente lo que son esas condiciones. Sin embargo, podemos inferir que son las mencionadas anteriormente debido a que posteriormente se detallan las condiciones para PROMOCIÓN y LIBRE.

**Tokens:** entrada: 1305 | salida: 171 | total: 1476

---

### Pregunta 5

> - ¿Qué instancias de recuperación nos provee Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% - ALUMNO LIBRE: Revestirá esta condición todo estudiante que no logre cumplimentar alguno de los requisitos de puntaje, trabajos prácticos o as
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Resolución | Pagina: 1]
   > Materia: Investigación Operativa Sección: Resolución de problemas de diligencia, asignación de recursos y reemplazo de equipos.
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mismo
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación una interfaz basada en menús para la carga de datos. - TORA: Herramienta educativa diseñada específicamente para el aprendizaje de la
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: PLANIFICACIÓN INVESTIGACIÓN OPERATIVA | Pagina: 1]
   > Materia: Investigación Operativa Sección: PLANIFICACIÓN INVESTIGACIÓN OPERATIVA Unidad I: -Introducción y Modelos Matemáticos- Definición y origen de la Investigación Operativa.

**Respuesta:**

La cátedra dispone de dos oportunidades de recuperatorio totales.

**Tokens:** entrada: 923 | salida: 17 | total: 940

---

### Pregunta 6

> - ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación una interfaz basada en menús para la carga de datos. - TORA: Herramienta educativa diseñada específicamente para el aprendizaje de la
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% ustificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen reprobado. Software de Aplicación - Inves
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% ción de modelos de optimización y problemas de gestión: - LINDO (Linear, Interactive, and Discrete Optimizer): Software especializado en la reso

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1020 | salida: 14 | total: 1034

---

### Pregunta 7

> - ¿Qué profesor forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes?

**Chunks de contexto:**

1. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Bases de Datos Avanzadas | Pagina: 2]
   > Materia: Bases de Datos Avanzadas Sección: Bases de Datos Avanzadas Equipo docente Trossero, Sebastián Teoría Trossero.sebastian@uader.edu.ar Schmuckler, Jorge Práctica Schmukler.jorge@uader.edu.ar
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: SEDE: Oro Verde | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler. AÑO ACADEMICO: 2023 PLAN DE EST
3. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Días de clase | Pagina: 3]
   > Materia: Bases de Datos Avanzadas Sección: Días de clase Lunes: 13:30 a 15:30 -> Teoría Viernes: 17:00 a 19:00 -> Práctica NOTA: Los horarios están en proceso de evaluación y pueden sufrir cambios
4. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Bases de Datos Avanzadas | Pagina: 1]
   > Materia: Bases de Datos Avanzadas Sección: Bases de Datos Avanzadas PRESENTACIÓN DE LA MATERIA Facultad de Ciencia Y Tecnología Base de Datos Avanzadas
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio I. FUNDAMENTACIÓN El avance de las tecnologías de la información y la comunicación (TIC) ha t

**Respuesta:**

El profesor que forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes es Jorge L. Schmukler.

**Tokens:** entrada: 998 | salida: 42 | total: 1040

---

### Pregunta 8

> - ¿Qué otra asignatura, además de la propia materia de Inteligencia Artificial, incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. He
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Descripción | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Descripción de los temas específicos a desarrollarse en la asignatura.
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Métodos | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Métodos y mensajes. Representación de Conocimientos mediante reglas. Estructura básica. Representación de reglas mediante objetos.
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Integración | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Integración Neuronales Artificiales (RNA). Generalidades, conceptos básicos Reseña Histórica.
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Métodos | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Métodos comparativas entre las distintas representaciones. Comportamiento de Agentes Basados en Conocimientos. Capítulo IV Diseño de los Sistemas Exper

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 869 | salida: 14 | total: 883

---

### Pregunta 9

> - Los requisitos para regularizar en Bases de Datos Avanzadas y en Redes y Comunicaciones, ¿son iguales? ¿Qué diferencias tienen?

**Chunks de contexto:**

1. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 9]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Software utilizado PostgreSQL 9.6 o superi
2. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 8]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Comunicación De rutina y consultas: Lista
3. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Régimen | Regularidad: | Pagina: 7]
   > Materia: Bases de Datos Avanzadas Sección: Régimen | Regularidad: Asistencia: Según norma vigente. Todos los trabajos prácticos aprobados.
4. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 10]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Bibliografía base Libro: Fundamentos de Si
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Unidad IV: Bases de Datos Distribuidas Parcial | Unidad V: Datawarehouse Parcial | Pagina: 6]
   > Materia: Bases de Datos Avanzadas Sección: Unidad IV: Bases de Datos Distribuidas Parcial | Unidad V: Datawarehouse Parcial Unidad VI: Datamining Parcial + TP Unidad VII: Bases de Datos OO Parcial NO

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1094 | salida: 14 | total: 1108

---

### Pregunta 10

> - ¿Cuál es el porcentaje de asistencia a clases que exigen en común las materias de Investigación Operativa, Comunicaciones y Redes, y Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% de asistencia a las clases teóricas y prácticas.
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
3. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Respecto a las clases: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Respecto a las clases: po, reducir la tasa de abandono. Por ello, los materiales teóricos y las lecturas obligatorias se compartirán
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% a nota del examen original. Protocolos de Evaluación: Los resultados se publicarán en un plazo de siete días corridos tras la evaluación. Los ex
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% requisito indispensable la entrega y aprobación de los dos trabajos prácticos obligatorios y el cumplimiento del

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 934 | salida: 14 | total: 948

---

### Pregunta 11

> - Si quiero promocionar todas las materias de 4to año, ¿cuál es la diferencia de promedio exigido entre Investigación Operativa e Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: | Pagina: 1]
   > Materia: Investigación Operativa Sección: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: - ALUMNO PROMOCIONADO: El estudiante logrará la promoción directa si alcanza un prom
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% a nota del examen original. Protocolos de Evaluación: Los resultados se publicarán en un plazo de siete días corridos tras la evaluación. Los ex
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mismo
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% requisito indispensable la entrega y aprobación de los dos trabajos prácticos obligatorios y el cumplimiento del

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1059 | salida: 14 | total: 1073

---

### Pregunta 12

> - ¿Qué herramientas de software se recomiendan en la carrera para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% ción de modelos de optimización y problemas de gestión: - LINDO (Linear, Interactive, and Discrete Optimizer): Software especializado en la reso
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% ustificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen reprobado. Software de Aplicación - Inves
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Definición | Pagina: 1]
   > Materia: Investigación Operativa Sección: Definición de variables de decisión, función objetivo y restricciones de sistema y de no negatividad. Unidad II: -Programación Lineal (PL)- Pro
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación resolver problemas de programación lineal

**Respuesta:**

LINDO es un software especializado en la resolución de problemas de programación lineal, entera y no lineal. Sin embargo, no se proporciona información específica sobre cómo se relaciona con las unidades teóricas de la carrera.

**Tokens:** entrada: 951 | salida: 54 | total: 1005

---

### Pregunta 13

> - ¿Dónde puedo descargar la materia de Cálculo de 1er año?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Primer | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Primer Orden.
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Clases | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Clases e instancias.
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Entorno | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Entorno de Trabajo.
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Recocido | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Recocido Simulado.
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: (Pruning | Pagina: 3]
   > Materia: Inteligencia Artificial Sección: (Pruning Algorithms).

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 651 | salida: 14 | total: 665

---

### Pregunta 14

> - El profesor Ing. Jorge L. Schmukler da clases en Bases de Datos Avanzadas, en Inteligencia Artificial y en Redes y Comunicaciones.

**Chunks de contexto:**

1. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Bases de Datos Avanzadas | Pagina: 2]
   > Materia: Bases de Datos Avanzadas Sección: Bases de Datos Avanzadas Equipo docente Trossero, Sebastián Teoría Trossero.sebastian@uader.edu.ar Schmuckler, Jorge Práctica Schmukler.jorge@uader.edu.ar
2. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Días de clase | Pagina: 4]
   > Materia: Bases de Datos Avanzadas Sección: Días de clase Cronograma de clases Presenciales/Virtuales A partir de este año la materia será dictada de manera bimodal. El cronograma será definido en su
3. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Unidad IV: Bases de Datos Distribuidas Parcial | Unidad V: Datawarehouse Parcial | Pagina: 6]
   > Materia: Bases de Datos Avanzadas Sección: Unidad IV: Bases de Datos Distribuidas Parcial | Unidad V: Datawarehouse Parcial Unidad VI: Datamining Parcial + TP Unidad VII: Bases de Datos OO Parcial NO
4. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Días de clase | Pagina: 3]
   > Materia: Bases de Datos Avanzadas Sección: Días de clase Lunes: 13:30 a 15:30 -> Teoría Viernes: 17:00 a 19:00 -> Práctica NOTA: Los horarios están en proceso de evaluación y pueden sufrir cambios
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Bases de Datos Avanzadas | Pagina: 1]
   > Materia: Bases de Datos Avanzadas Sección: Bases de Datos Avanzadas PRESENTACIÓN DE LA MATERIA Facultad de Ciencia Y Tecnología Base de Datos Avanzadas

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 935 | salida: 14 | total: 949

---

### Pregunta 15

> - ¿Cuál es el costo de la certificación oficial de Cisco que se menciona como opcional en la planificación?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Estándar | Pagina: 3]
   > Materia: Inteligencia Artificial Sección: Estándar FIPA.
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Recocido | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Recocido Simulado.
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: (Backward | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: (Backward Chaining). Herramientas para el desarrollo de Sistemas Expertos.
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Descripción | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Descripción de los temas específicos a desarrollarse en la asignatura.
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Adquisición | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Adquisición Estructura de Control: Procedimientos de Inferencia; Interfase con el usuario. Memoria de Trabajo, Módulo generador de explicaciones al usuario.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 760 | salida: 14 | total: 774

---

### Pregunta 16

> - Para la Promoción Directa, se exige la aprobación de la totalidad de los trabajos prácticos (TP 1 al TP 5). ¿Cuál es la calificación numérica mínima que debe obtenerse en cada TP individual para que se considere aprobado?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos a la condición de Promoción Directa, el/la estudiante deberá cumplir con los siguientes requisitos: - 80 % de asistencia a la cursada. - Aprob
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: | Pagina: 1]
   > Materia: Investigación Operativa Sección: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: - ALUMNO PROMOCIONADO: El estudiante logrará la promoción directa si alcanza un prom
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE El alumno accederá a la condición de PROMOCIÓN si cumple con las siguientes co
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: | Pagina: 1]
   > Materia: Investigación Operativa Sección: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: deberá acreditar la aprobación de los dos trabajos prácticos de la cátedra
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 8]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Comunicación De rutina y consultas: Lista

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1244 | salida: 14 | total: 1258

---

### Pregunta 17

> - ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible vía URL que
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: PL: | Pagina: 1]
   > Materia: Investigación Operativa Sección: PL: región factible, búsqueda de la solución óptima en los vértices, análisis de casos especiales (soluciones múltiples, soluciones no acot
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación resolver problemas de programación lineal
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% ción de modelos de optimización y problemas de gestión: - LINDO (Linear, Interactive, and Discrete Optimizer): Software especializado en la reso
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex y el

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 861 | salida: 14 | total: 875

---

### Pregunta 18

> - ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% a nota del examen original. Protocolos de Evaluación: Los resultados se publicarán en un plazo de siete días corridos tras la evaluación. Los ex
3. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 15 18 de junio Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 15 18 de junio Virtual Teoría Marco metodológico II: recolección de datos y análisis de datos RECESO DE INVIERNO/ MESAS DE EXAMENES FINALES 16 06 de
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mismo
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 15 18 de junio Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 15 18 de junio Virtual Teoría ances proyectos a la cátedra- Grupos Jimena 24 de septiembre Virtual Tutorías 24 01 de octubre Presencial Tutorías Pre

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1093 | salida: 14 | total: 1107

---

## Conversacion 2

**Puntaje evaluado: 10 / 18**

**Parametros modificados respecto a la conversacion anterior:**

| Parametro | Valor |
|---|---|
| chunk_size | 512 |
| chunk_overlap | 100 |
| chunking_technique | recursive |

### Pregunta 1

> - ¿Cuáles son los contenidos de la materia Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. He
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Descripción | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Descripción de los temas específicos a desarrollarse en la asignatura.
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Métodos | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Métodos comparativas entre las distintas representaciones. Comportamiento de Agentes Basados en Conocimientos. Capítulo IV Diseño de los Sistemas Exper
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Métodos | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Métodos y mensajes. Representación de Conocimientos mediante reglas. Estructura básica. Representación de reglas mediante objetos.
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Integración | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación

**Respuesta:**

La materia Inteligencia Artificial abarca temas como la introducción a la IA, definiciones y objetivos, herramientas y técnicas proporcionadas por el área IA, descripción de los temas específicos a desarrollarse en la asignatura, métodos comparativos entre distintas representaciones, comportamiento de Agentes Basados en Conocimientos, diseño de los Sistemas Expertos, representación de conocimientos mediante reglas, y la integración de la solución difusa final, incluyendo proceso de Defuzzificación y método del centroide.

**Tokens:** entrada: 924 | salida: 117 | total: 1041

---

### Pregunta 2

> - ¿En qué materia se enseña el concepto de Lógica Difusa?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Capítulo VI | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Capítulo VI Lógica Difusa (Fuzzy). Consideraciones generales, Conjuntos Difusos, definición.
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Composición | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Composición MAX-MIN. Capítulo VII Sistemas Difusos. Consideraciones generales. Representación de conocimiento estructurado mediante reglas lingüísticas.
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Integración | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Procesos | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Procesos basadas en Lógica.
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Lógica | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Lógica de

**Respuesta:**

La materia en la que se enseña el concepto de Lógica Difusa es la Inteligencia Artificial.

**Tokens:** entrada: 889 | salida: 26 | total: 915

---

### Pregunta 3

> - ¿Cuál es el plan de estudios de Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: JIMENA | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: JIMENA CRUZ; Año de la carrera a la que pertenece la cátedra: 4 Régimen de la materia: Anual Carga horaria semanal: 3 horas Correlativa: Ingeniería
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 1 12 de marzo Presencial Teórico/práctico Presentación de la asignatura | 2 19 de marzo Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 1 12 de marzo Presencial Teórico/práctico Presentación de la asignatura | 2 19 de marzo Virtual Teoría Conceptos generales para introducción 3 26 de
3. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Metodología | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Metodología en trabajos propios de la disciplina y el campo profesional. Objetivos específicos - Promover el reconocimiento de aspectos meto
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Metodología | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Metodología como el conjunto de estrategias, reflexiones y decisiones que configuran los procesos de investigación científica. Por lo
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 8 30 de abril Presencial (pedir cambio fecha) Práctica | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 8 30 de abril Presencial (pedir cambio fecha) Práctica 9 7 de mayo virtual Teoría Alcances, límites y limitaciones/ Objetivos / Justificación 10 14 d

**Respuesta:**

El plan de estudios de Metodología de la Investigación incluye la presentación de la asignatura, teoría y práctica. Los temas específicos son:

- Se explica que la metodología de la investigación es la ciencia del método.
- Se introduce la epistemología y se sostiene que la metodología de la investigación es una disciplina meta-teórica porque toma como objeto de estudio a la ciencia.
- En el calendario del plan de estudios, se destaca que la asignatura tiene sesiones presenciales y virtuales teóricas y prácticas.
- En las sesiones presenciales, se desarrollan temas como la introducción a la asignatura, el tema/problema, y se pide a los estudiantes que escriban según las normas APA.
- En las sesiones virtuales, se trabajan teoría y práctica sobre preguntas de investigación, antecedentes, alcances, límites y limitaciones, objetivos, justificación, marco teórico e hipótesis.

No tengo información sobre qué otras materias se relacionan con la materia Metodología de la Investigación.

**Tokens:** entrada: 1248 | salida: 246 | total: 1494

---

### Pregunta 4

> - En Comunicaciones y Redes, ¿cómo hago para quedar como alumno regular?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE El alumno accederá a la condición de REGULAR, si cumple con las siguientes con
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE El alumno accederá a la condición de PROMOCIÓN si cumple con las siguientes co
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE . Tener aprobado con 60 puntos los tres parciales. 2- Haber realizado y aproba
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE Evaluación Final: El alumno con condición de REGULAR, deberá rendir un examen
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: SEDE: Oro Verde | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler. AÑO ACADEMICO: 2023 PLAN DE EST

**Respuesta:**

Para quedar como alumno regular en Comunicaciones y Redes, debes cumplir con las siguientes condiciones de cátedra:

1 - Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos.

No dispongo de información en mis documentos para saber si también debes cumplir con alguna otra condición adicional, como la realización de trabajos prácticos o la asistencia a cierta cantidad de clases.

**Tokens:** entrada: 1345 | salida: 99 | total: 1444

---

### Pregunta 5

> - ¿Qué instancias de recuperación nos provee Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% - ALUMNO LIBRE: Revestirá esta condición todo estudiante que no logre cumplimentar alguno de los requisitos de puntaje, trabajos prácticos o as
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mismo
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Resolución | Pagina: 1]
   > Materia: Investigación Operativa Sección: Resolución de problemas de diligencia, asignación de recursos y reemplazo de equipos.
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: PLANIFICACIÓN INVESTIGACIÓN OPERATIVA | Pagina: 1]
   > Materia: Investigación Operativa Sección: PLANIFICACIÓN INVESTIGACIÓN OPERATIVA Unidad I: -Introducción y Modelos Matemáticos- Definición y origen de la Investigación Operativa.
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al

**Respuesta:**

La cátedra dispone de dos oportunidades de recuperatorio totales, lo que significa que se ofrecen dos instancias de recuperación para que los estudiantes puedan mejorar sus calificaciones. Estas instancias pueden utilizarse para cualquiera de los dos parciales, siempre y cuando no se apliquen ambos recuperatorios al mismo examen parcial.

**Tokens:** entrada: 1078 | salida: 78 | total: 1156

---

### Pregunta 6

> - ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% Los exámenes se desarrollarán estrictamente en los bloques horarios asignados a la materia. La ausencia no justificada (sin certificado
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 15 18 de junio Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 15 18 de junio Virtual Teoría Marco metodológico II: recolección de datos y análisis de datos RECESO DE INVIERNO/ MESAS DE EXAMENES FINALES 16 06 de
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS 4- BIBLIOGRAFIA Obligatoria Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Ver

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1365 | salida: 14 | total: 1379

---

### Pregunta 7

> - ¿Qué profesor forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes?

**Chunks de contexto:**

1. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Bases de Datos Avanzadas | Pagina: 2]
   > Materia: Bases de Datos Avanzadas Sección: Bases de Datos Avanzadas Equipo docente Trossero, Sebastián Teoría Trossero.sebastian@uader.edu.ar Schmuckler, Jorge Práctica Schmukler.jorge@uader.edu.ar
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: SEDE: Oro Verde | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler. AÑO ACADEMICO: 2023 PLAN DE EST
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Sitios web sobre normativas, tecnologías y soluciones, opcional: | Pagina: 5]
   > Materia: Comunicacion y Redes Sección: Sitios web sobre normativas, tecnologías y soluciones, opcional: Lic. Luciano M. CAISSO.
4. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Días de clase | Pagina: 3]
   > Materia: Bases de Datos Avanzadas Sección: Días de clase Lunes: 13:30 a 15:30 -> Teoría Viernes: 17:00 a 19:00 -> Práctica NOTA: Los horarios están en proceso de evaluación y pueden sufrir cambios
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Bases de Datos Avanzadas | Pagina: 1]
   > Materia: Bases de Datos Avanzadas Sección: Bases de Datos Avanzadas PRESENTACIÓN DE LA MATERIA Facultad de Ciencia Y Tecnología Base de Datos Avanzadas

**Respuesta:**

El profesor Jorge L. Schmukler forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes.

**Tokens:** entrada: 932 | salida: 40 | total: 972

---

### Pregunta 8

> - ¿Qué otra asignatura, además de la propia materia de Inteligencia Artificial, incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. He
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Descripción | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Descripción de los temas específicos a desarrollarse en la asignatura.
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Métodos | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Métodos y mensajes. Representación de Conocimientos mediante reglas. Estructura básica. Representación de reglas mediante objetos.
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Integración | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Métodos | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Métodos comparativas entre las distintas representaciones. Comportamiento de Agentes Basados en Conocimientos. Capítulo IV Diseño de los Sistemas Exper

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 954 | salida: 14 | total: 968

---

### Pregunta 9

> - Los requisitos para regularizar en Bases de Datos Avanzadas y en Redes y Comunicaciones, ¿son iguales? ¿Qué diferencias tienen?

**Chunks de contexto:**

1. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 9]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Software utilizado PostgreSQL 9.6 o superi
2. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 8]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Comunicación De rutina y consultas: Lista
3. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Régimen | Regularidad: | Pagina: 7]
   > Materia: Bases de Datos Avanzadas Sección: Régimen | Regularidad: Asistencia: Según norma vigente. Todos los trabajos prácticos aprobados.
4. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 10]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Bibliografía base Libro: Fundamentos de Si
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Unidad IV: Bases de Datos Distribuidas Parcial | Unidad V: Datawarehouse Parcial | Pagina: 6]
   > Materia: Bases de Datos Avanzadas Sección: Unidad IV: Bases de Datos Distribuidas Parcial | Unidad V: Datawarehouse Parcial Unidad VI: Datamining Parcial + TP Unidad VII: Bases de Datos OO Parcial NO

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1094 | salida: 14 | total: 1108

---

### Pregunta 10

> - ¿Cuál es el porcentaje de asistencia a clases que exigen en común las materias de Investigación Operativa, Comunicaciones y Redes, y Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% de asistencia a las clases teóricas y prácticas.
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Respecto a las clases: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Respecto a las clases: a todas las clases y, al mismo tiempo, reducir la tasa de abandono. Por ello, los materiales teóricos y las
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% Los exámenes se desarrollarán estrictamente en los bloques horarios asignados a la materia. La ausencia no justificada (sin certificado
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% requisito indispensable la entrega y aprobación de los dos trabajos prácticos obligatorios y el cumplimiento del

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1001 | salida: 14 | total: 1015

---

### Pregunta 11

> - Si quiero promocionar todas las materias de 4to año, ¿cuál es la diferencia de promedio exigido entre Investigación Operativa e Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: | Pagina: 1]
   > Materia: Investigación Operativa Sección: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: - ALUMNO PROMOCIONADO: El estudiante logrará la promoción directa si alcanza un prom
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% requisito indispensable la entrega y aprobación de los dos trabajos prácticos obligatorios y el cumplimiento del
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: | Pagina: 1]
   > Materia: Investigación Operativa Sección: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: deberá acreditar la aprobación de los dos trabajos prácticos de la cátedra
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mismo

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1117 | salida: 14 | total: 1131

---

### Pregunta 12

> - ¿Qué herramientas de software se recomiendan en la carrera para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% de modelos de optimización y problemas de gestión: - LINDO (Linear, Interactive, and Discrete Optimizer): Software especializado en la resolución
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Definición | Pagina: 1]
   > Materia: Investigación Operativa Sección: Definición de variables de decisión, función objetivo y restricciones de sistema y de no negatividad. Unidad II: -Programación Lineal (PL)- Pro
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación resolver problemas de programación lineal
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Método | Pagina: 2]
   > Materia: Investigación Operativa Sección: Método ideal para validaciones rápidas y visualización de regiones factibles. - LINGO (64 bits): Una versión avanzada y más potente del motor LINDO.

**Respuesta:**

El software LINDO se menciona como especializado en la resolución de problemas de programación lineal, entera y no lineal, lo que sugiere que sería útil para resolver problemas de optimización lineal. Por otro lado, la herramienta LINGO es una versión avanzada del motor LINDO y se describe como ideal para modelar y resolver problemas de optimización de gran escala, que incluiría la optimización lineal. La herramienta Storm facilita el procesamiento de modelos matemáticos y estadísticos mediante una interfaz basada en menús para la carga de datos, lo que podría usarse para el análisis de datos y optimización. La herramienta TORA se menciona como diseñada específicamente para el aprendizaje de la optimización.

**Tokens:** entrada: 1001 | salida: 170 | total: 1171

---

### Pregunta 13

> - ¿Dónde puedo descargar la materia de Cálculo de 1er año?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Primer | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Primer Orden.
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Clases | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Clases e instancias.
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Entorno | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Entorno de Trabajo.
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Recocido | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Recocido Simulado.
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: (Pruning | Pagina: 3]
   > Materia: Inteligencia Artificial Sección: (Pruning Algorithms).

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 651 | salida: 14 | total: 665

---

### Pregunta 14

> - El profesor Ing. Jorge L. Schmukler da clases en Bases de Datos Avanzadas, en Inteligencia Artificial y en Redes y Comunicaciones.

**Chunks de contexto:**

1. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Bases de Datos Avanzadas | Pagina: 2]
   > Materia: Bases de Datos Avanzadas Sección: Bases de Datos Avanzadas Equipo docente Trossero, Sebastián Teoría Trossero.sebastian@uader.edu.ar Schmuckler, Jorge Práctica Schmukler.jorge@uader.edu.ar
2. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Días de clase | Pagina: 4]
   > Materia: Bases de Datos Avanzadas Sección: Días de clase Cronograma de clases Presenciales/Virtuales A partir de este año la materia será dictada de manera bimodal. El cronograma será definido en su
3. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Unidad IV: Bases de Datos Distribuidas Parcial | Unidad V: Datawarehouse Parcial | Pagina: 6]
   > Materia: Bases de Datos Avanzadas Sección: Unidad IV: Bases de Datos Distribuidas Parcial | Unidad V: Datawarehouse Parcial Unidad VI: Datamining Parcial + TP Unidad VII: Bases de Datos OO Parcial NO
4. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Días de clase | Pagina: 3]
   > Materia: Bases de Datos Avanzadas Sección: Días de clase Lunes: 13:30 a 15:30 -> Teoría Viernes: 17:00 a 19:00 -> Práctica NOTA: Los horarios están en proceso de evaluación y pueden sufrir cambios
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Bases de Datos Avanzadas | Pagina: 1]
   > Materia: Bases de Datos Avanzadas Sección: Bases de Datos Avanzadas PRESENTACIÓN DE LA MATERIA Facultad de Ciencia Y Tecnología Base de Datos Avanzadas

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 935 | salida: 14 | total: 949

---

### Pregunta 15

> - ¿Cuál es el costo de la certificación oficial de Cisco que se menciona como opcional en la planificación?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Estándar | Pagina: 3]
   > Materia: Inteligencia Artificial Sección: Estándar FIPA.
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Recocido | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Recocido Simulado.
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: (Backward | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: (Backward Chaining). Herramientas para el desarrollo de Sistemas Expertos.
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Descripción | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Descripción de los temas específicos a desarrollarse en la asignatura.
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Adquisición | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Adquisición Estructura de Control: Procedimientos de Inferencia; Interfase con el usuario. Memoria de Trabajo, Módulo generador de explicaciones al usuario.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 760 | salida: 14 | total: 774

---

### Pregunta 16

> - Para la Promoción Directa, se exige la aprobación de la totalidad de los trabajos prácticos (TP 1 al TP 5). ¿Cuál es la calificación numérica mínima que debe obtenerse en cada TP individual para que se considere aprobado?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: | Pagina: 1]
   > Materia: Investigación Operativa Sección: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: - ALUMNO PROMOCIONADO: El estudiante logrará la promoción directa si alcanza un prom
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos . Guillerón. 2018 Red Privada Virtual (VPM) sobre Protocolo de Internet versión 6 (IPv6) / Rodrigo Paúl Basso, Maximiliano Sebastián Toso; dir
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE El alumno accederá a la condición de PROMOCIÓN si cumple con las siguientes co
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos . - Aprobación del examen parcial teórico con una calificación igual o superior a 75 (setenta y cinco) puntos. - Entrega de la totalidad de lo
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Sistema de evaluación: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Sistema de evaluación: examen contará con una (1) instancia de recuperación, conforme al cronograma establecido por la cátedra. - Entre

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1327 | salida: 14 | total: 1341

---

### Pregunta 17

> - ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible vía URL que
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: PL: | Pagina: 1]
   > Materia: Investigación Operativa Sección: PL: región factible, búsqueda de la solución óptima en los vértices, análisis de casos especiales (soluciones múltiples, soluciones no acot
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación resolver problemas de programación lineal
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% de modelos de optimización y problemas de gestión: - LINDO (Linear, Interactive, and Discrete Optimizer): Software especializado en la resolución
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex y el

**Respuesta:**

Lo siento, pero no dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 861 | salida: 19 | total: 880

---

### Pregunta 18

> - ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mismo
3. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 15 18 de junio Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 15 18 de junio Virtual Teoría 10 de septiembre Virtual Tutorías Avances proyectos a la cátedra- Grupos Tamara 17 de septiembre Teoría Coloquio Avanc
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% requisito indispensable la entrega y aprobación de los dos trabajos prácticos obligatorios y el cumplimiento del
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% de asistencia a las clases teóricas y prácticas.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1049 | salida: 14 | total: 1063

---

## Conversacion 3

**Puntaje evaluado: 11 / 18**

**Parametros modificados respecto a la conversacion anterior:**

| Parametro | Valor |
|---|---|
| top_k | 8 |
| retrieval_type | mmr |
| max_context_chunks | 8 |

### Pregunta 1

> - ¿Cuáles son los contenidos de la materia Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. He
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Descripción | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Descripción de los temas específicos a desarrollarse en la asignatura.
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Métodos | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Métodos y mensajes. Representación de Conocimientos mediante reglas. Estructura básica. Representación de reglas mediante objetos.
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Integración | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Adquisición | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Adquisición de Conocimiento. Base de Conocimientos, características generales.
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Condiciones | Pagina: 3]
   > Materia: Inteligencia Artificial Sección: Condiciones de inicialización, problema de saturación prematura. Regiones de Decisión. Modo de operación autoasociativo. Capítulo X Generalización en
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Associative | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Associative Memories).
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Adquisición | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Adquisición Estructura de Control: Procedimientos de Inferencia; Interfase con el usuario. Memoria de Trabajo, Módulo generador de explicaciones al usuario.

**Respuesta:**

La materia de Inteligencia Artificial (IA) comprende varios capítulos y contenidos específicos. Entre estos se incluyen la Introducción a la IA, con definiciones y objetivos, así como herramientas y técnicas proporcionadas por el área de IA.

También se destacan los Agentes Inteligentes, con sus características y aplicaciones.

En el apartado de Descripción, se presentan los temas específicos a desarrollarse en la asignatura, destacando la importancia de la representación de conocimientos mediante reglas y la estructura básica de la representación de reglas mediante objetos.

La Integración de la solución difusa final, incluye el proceso de Defuzzificación, y se analizan los métodos del centroide y la máxima.

Además, se cubren temas como la Adquisición de Conocimiento, la Base de Conocimientos y sus características generales, así como la Estructura de Control y los Procedimientos de Inferencia.

También se incluyen temas sobre la Generalización en las Redes Neuronales Artificiales (RNA) y la Funcionalidad de los Sistemas Expertos, como procesos de inferencia y la generación de explicaciones al usuario.

En cuanto a la Memoria, se abordan los conceptos de Memoria de Trabajo y la Interfase con el usuario.

Finalmente, se mencionan Redes Neuronales Artificiales (RNA) y los procesos de inferencia en los Sistemas Expertos.

En resumen, la materia de Inteligencia Artificial abarca un rango amplio de temas, desde la introducción y definiciones hasta la representación de conocimientos, la adquisición de conocimiento y la integración de soluciones difusas, pasando por la generalización en RNA y la funcionalidad de sistemas expertos.

**Tokens:** entrada: 1141 | salida: 399 | total: 1540

---

### Pregunta 2

> - ¿En qué materia se enseña el concepto de Lógica Difusa?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Capítulo VI | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Capítulo VI Lógica Difusa (Fuzzy). Consideraciones generales, Conjuntos Difusos, definición.
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Composición | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Composición MAX-MIN. Capítulo VII Sistemas Difusos. Consideraciones generales. Representación de conocimiento estructurado mediante reglas lingüísticas.
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Integración | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Procesos | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Procesos basadas en Lógica.
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Agentes | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Agentes que aprenden. Capítulo II Procesos de Búsqueda. Representación en un espacio de estados. Búsqueda Ciega, definición; búsqueda primero en amplitud,
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Editorial: Pearson Educación (2004 o versiones posteriores) | Pagina: 4]
   > Materia: Inteligencia Artificial Sección: Editorial: Pearson Educación (2004 o versiones posteriores) Título: Aprendizaje automático y aprendizaje profundo con Python, scikit-learn y Tensor Flow-
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Problema | Pagina: 3]
   > Materia: Inteligencia Artificial Sección: Problema Capítulo IX Redes Perceptron Multicapa, estructura básica. Proceso de Entrenamiento Backpropagation (BP).
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Generativos | Pagina: 3]
   > Materia: Inteligencia Artificial Sección: Generativos Capítulo XI Redes Autoorganizadas. Características generales. Red SOM (Kohonen). Proceso de aprendizaje competitivo. Realimentación lateral.

**Respuesta:**

La materia donde se enseña el concepto de Lógica Difusa es la Inteligencia Artificial.

**Tokens:** entrada: 1180 | salida: 24 | total: 1204

---

### Pregunta 3

> - ¿Cuál es el plan de estudios de Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: JIMENA | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: JIMENA CRUZ; Año de la carrera a la que pertenece la cátedra: 4 Régimen de la materia: Anual Carga horaria semanal: 3 horas Correlativa: Ingeniería
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 1 12 de marzo Presencial Teórico/práctico Presentación de la asignatura | 2 19 de marzo Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 1 12 de marzo Presencial Teórico/práctico Presentación de la asignatura | 2 19 de marzo Virtual Teoría Conceptos generales para introducción 3 26 de
3. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Unidad 3: La dimensión de la estrategia general de investigación | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Unidad 3: La dimensión de la estrategia general de investigación ¿Cómo se va a estudiar el problema? Tipo de diseños cuantitativos o cualitativos. La
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Estructura del aula virtual: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Estructura del aula virtual: Los materiales educativos estarán alojados en el aula virtual "Metodología de la Investigación" dentro de la plataform
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Sistema de evaluación: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Sistema de evaluación: examen contará con una (1) instancia de recuperación, conforme al cronograma establecido por la cátedra. - Entre
6. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Cronograma de trabajo | METODOLOGÍA DE LA INVESTIGACIÓN- 2026 | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Cronograma de trabajo | METODOLOGÍA DE LA INVESTIGACIÓN- 2026 Clase FECHA Tipo de encuentro Tipo encuentro Tema
7. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Metodología | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Metodología brindar conocimientos y herramientas para indagar la realidad en la búsqueda y desnaturalización de problemas, tanto del
8. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Nacional | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Nacional en https://ediciones.ungs.edu.ar/wp-content/uploads/2018/09/9789876301190-completo.pdf

**Respuesta:**

El plan de estudios de Metodología de la Investigación comprende varias unidades y temáticas que se desarrollan a lo largo del curso. Las unidades mencionadas en el plan incluyen:

- La dimensión de la estrategia general de investigación: Aquí se estudia cómo se va a investigar el problema, los tipos de diseños (cuantitativos o cualitativos) y las estrategias de indagación según la perspectiva metodológica seleccionada.
- La dimensión de las técnicas de obtención y análisis de información empírica: En esta unidad, se analiza la comunicación de los resultados, así como las opciones para el análisis de los datos, incluyendo teorias y procedimientos.
- La estructura del aula virtual: En este sección se describe la plataforma Moodle y la organización del aula virtual, incluyendo la disponibilidad de materiales, la información general de la cátedra, el programa, el equipo docente, el cronograma, los objetivos, los materiales utilizados, el enlace de videoconferencia, la descripción de la metodología de trabajo y evaluación, la bibliografía y un foro de discusión.

El sistema de evaluación incluye un examen con una instancia de recuperación y la entrega obligatoria de las actividades prácticas, así como la aprobación del trabajo práctico integrador final.

El plan de estudios tiene como objetivo brindar conocimientos y herramientas para indagar la realidad y buscar problemas en diversos ámbitos, y se centra en acercar al campo de la investigación científica de manera sistemática.

En cuanto a los objetivos generales del curso, se mencionan: 

- Acercar al campo de la investigación científica desde espacios de reflexión sistemáticos enmarcados en trabajos propios de la disciplina y el campo.

El cronograma de trabajo y los temas específicos se desarrollan a lo largo del curso.

Para obtener más detalles, es preciso acceder al enlace en https://ediciones.ungs.edu.ar/wp-content/uploads/2018/09/9789876301190-completo.pdf

**Tokens:** entrada: 1779 | salida: 474 | total: 2253

---

### Pregunta 4

> - En Comunicaciones y Redes, ¿cómo hago para quedar como alumno regular?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE El alumno accederá a la condición de REGULAR, si cumple con las siguientes con
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: SEDE: Oro Verde | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler. AÑO ACADEMICO: 2023 PLAN DE EST
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 1- PROGRAMA DE CONTENIDOS | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: 1- PROGRAMA DE CONTENIDOS Unidad I: Introducción -Importancia e Influencia de las Redes en Nuestras Vidas: Comunicación en un mundo centrado en la red, herramie
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Sitios web sobre normativas, tecnologías y soluciones, opcional: | Pagina: 5]
   > Materia: Comunicacion y Redes Sección: Sitios web sobre normativas, tecnologías y soluciones, opcional: Lic. Luciano M. CAISSO.
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad II: -Capa física concepto y medios- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad II: -Capa física concepto y medios- . ARP (protocolo de resolución de direcciones). Mantenimiento de la tabla ARP. ARP proxy. Cableado Estructurado: Sele
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad VII: -Capa de Red- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad VII: -Capa de Red- . Proveedores de servicio de internet (ISP), descripción Ipv6. Unidad IX -VLans- Definiciones de Vlan, Beneficios de una Vlan, Rangos
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS . Reid, Jim Lorenz, Cheryl Schmidt. - Madrid: Pearson Educación, 2009. ISBN 9788483224694 [Disponible en Biblioteca FCyT- Oro

**Respuesta:**

Para quedar como alumno regular en Comunicaciones y Redes, debes cumplir con las siguientes condiciones de cátedra:

1 - Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos

Es importante tener en cuenta que, además de cumplir con estas condiciones, también debes aprobar los dos trabajos prácticos que se realizan en el horario de clase, para obtener la regularidad.

**Tokens:** entrada: 1698 | salida: 98 | total: 1796

---

### Pregunta 5

> - ¿Qué instancias de recuperación nos provee Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% - ALUMNO LIBRE: Revestirá esta condición todo estudiante que no logre cumplimentar alguno de los requisitos de puntaje, trabajos prácticos o as
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Resolución | Pagina: 1]
   > Materia: Investigación Operativa Sección: Resolución de problemas de diligencia, asignación de recursos y reemplazo de equipos.
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: PLANIFICACIÓN INVESTIGACIÓN OPERATIVA | Pagina: 1]
   > Materia: Investigación Operativa Sección: PLANIFICACIÓN INVESTIGACIÓN OPERATIVA Unidad I: -Introducción y Modelos Matemáticos- Definición y origen de la Investigación Operativa.
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: (Método | Pagina: 1]
   > Materia: Investigación Operativa Sección: (Método recursiva de los cálculos: etapas, estados, decisiones y principio de optimalidad de Bellman.
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: PL: | Pagina: 1]
   > Materia: Investigación Operativa Sección: PL: región factible, búsqueda de la solución óptima en los vértices, análisis de casos especiales (soluciones múltiples, soluciones no acot
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Método | Pagina: 2]
   > Materia: Investigación Operativa Sección: Método ideal para validaciones rápidas y visualización de regiones factibles. - LINGO (64 bits): Una versión avanzada y más potente del motor LINDO.
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% de asistencia a las clases teóricas y prácticas.

**Respuesta:**

La cátedra de Investigación Operativa dispone de dos oportunidades de recuperatorio totales.

**Tokens:** entrada: 1278 | salida: 22 | total: 1300

---

### Pregunta 6

> - ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS 4- BIBLIOGRAFIA Obligatoria Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Ver
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Método | Pagina: 2]
   > Materia: Investigación Operativa Sección: Método ideal para validaciones rápidas y visualización de regiones factibles. - LINGO (64 bits): Una versión avanzada y más potente del motor LINDO.
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 15 18 de junio Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 15 18 de junio Virtual Teoría 10 de septiembre Virtual Tutorías Avances proyectos a la cátedra- Grupos Tamara 17 de septiembre Teoría Coloquio Avanc
6. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio . Además, se abordarán aspectos legales fundamentales para comprender el impacto normativo de
7. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Respecto a las clases: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Respecto a las clases: La cátedra implementará el modelo de aula invertida, en el que los estudiantes adquieren los conocimientos teóricos de mane
8. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos Deep Learning aplicado al aprendizaje automático de ontologías para la representación del conocimiento a partir de texto no estructurado / Enz

**Respuesta:**

El software TORA es una herramienta educativa diseñada específicamente para el aprendizaje de la investigación operativa. No se especifica su función en el contexto de los módulos de la cátedra, por lo que no puedo proporcionar una respuesta completa.

**Tokens:** entrada: 1763 | salida: 57 | total: 1820

---

### Pregunta 7

> - ¿Qué profesor forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes?

**Chunks de contexto:**

1. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Bases de Datos Avanzadas | Pagina: 2]
   > Materia: Bases de Datos Avanzadas Sección: Bases de Datos Avanzadas Equipo docente Trossero, Sebastián Teoría Trossero.sebastian@uader.edu.ar Schmuckler, Jorge Práctica Schmukler.jorge@uader.edu.ar
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: SEDE: Oro Verde | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler. AÑO ACADEMICO: 2023 PLAN DE EST
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Sitios web sobre normativas, tecnologías y soluciones, opcional: | Pagina: 5]
   > Materia: Comunicacion y Redes Sección: Sitios web sobre normativas, tecnologías y soluciones, opcional: Lic. Luciano M. CAISSO.
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos . 2022 Modelos vectoriales y redes neuronales artificiales, para la aplicación de procesamiento de lenguaje natural en normativas jurídicas /
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Días de clase | Pagina: 4]
   > Materia: Bases de Datos Avanzadas Sección: Días de clase Cronograma de clases Presenciales/Virtuales A partir de este año la materia será dictada de manera bimodal. El cronograma será definido en su
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 1- PROGRAMA DE CONTENIDOS | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: 1- PROGRAMA DE CONTENIDOS . Conceptos usados en Comunicaciones y Redes: Uso de la redes de computadora, aplicaciones de negocios, domésticas, distintos usuarios
7. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Investigación | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Investigación Carrera: Licenciatura en Sistemas de Información Cátedra: Metodología de la Investigación Año Académico: 2026 Equipo docente: PROFESORA
8. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio I

**Respuesta:**

En la información proporcionada se menciona que el equipo docente de la materia de Comunicaciones y Redes está integrado por el Lic. Luciano M. Caisso e Ing. Jorge L. Schmukler. De manera similar, se menciona que el equipo docente de la materia de Bases de Datos Avanzadas está integrado por el Sr. Sebastián Teoría y Jorge Schmukler.

**Tokens:** entrada: 1397 | salida: 92 | total: 1489

---

### Pregunta 8

> - ¿Qué otra asignatura, además de la propia materia de Inteligencia Artificial, incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. He
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Descripción | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Descripción de los temas específicos a desarrollarse en la asignatura.
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Adquisición | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Adquisición Estructura de Control: Procedimientos de Inferencia; Interfase con el usuario. Memoria de Trabajo, Módulo generador de explicaciones al usuario.
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Condiciones | Pagina: 3]
   > Materia: Inteligencia Artificial Sección: Condiciones de inicialización, problema de saturación prematura. Regiones de Decisión. Modo de operación autoasociativo. Capítulo X Generalización en
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Editorial: Pearson Educación (2004 o versiones posteriores) | Pagina: 4]
   > Materia: Inteligencia Artificial Sección: Editorial: Pearson Educación (2004 o versiones posteriores) Título: Aprendizaje automático y aprendizaje profundo con Python, scikit-learn y Tensor Flow-
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Associative | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Associative Memories).
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Composición | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Composición MAX-MIN. Capítulo VII Sistemas Difusos. Consideraciones generales. Representación de conocimiento estructurado mediante reglas lingüísticas.
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Problema | Pagina: 3]
   > Materia: Inteligencia Artificial Sección: Problema heurística y matemática del procedimiento BP.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1186 | salida: 14 | total: 1200

---

### Pregunta 9

> - Los requisitos para regularizar en Bases de Datos Avanzadas y en Redes y Comunicaciones, ¿son iguales? ¿Qué diferencias tienen?

**Chunks de contexto:**

1. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 9]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Software utilizado PostgreSQL 9.6 o superi
2. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Régimen | Regularidad: | Pagina: 7]
   > Materia: Bases de Datos Avanzadas Sección: Régimen | Regularidad: Asistencia: Según norma vigente. Todos los trabajos prácticos aprobados.
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE Evaluación Final: El alumno con condición de REGULAR, deberá rendir un examen
4. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Días de clase | Pagina: 3]
   > Materia: Bases de Datos Avanzadas Sección: Días de clase Lunes: 13:30 a 15:30 -> Teoría Viernes: 17:00 a 19:00 -> Práctica NOTA: Los horarios están en proceso de evaluación y pueden sufrir cambios
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Programa Sintético | Unidad I: Bases de Datos Activas | Unidad II: Bases de Datos Temporales | Unidad III: Bases de Datos Geográficas | Unidad IV: Bases de Datos Distribuidas | Unidad V: Datawarehouse | Unidad VI: Datamining | Unidad VII: Bases de Datos Orientadas a Objetos | Pagina: 6]
   > Materia: Bases de Datos Avanzadas Sección: Programa Sintético | Unidad I: Bases de Datos Activas | Unidad II: Bases de Datos Temporales | Unidad III: Bases de Datos Geográficas | Unidad IV: Bases de D
6. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Bases de Datos Avanzadas | Pagina: 2]
   > Materia: Bases de Datos Avanzadas Sección: Bases de Datos Avanzadas Equipo docente Trossero, Sebastián Teoría Trossero.sebastian@uader.edu.ar Schmuckler, Jorge Práctica Schmukler.jorge@uader.edu.ar
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad II: -Capa física concepto y medios- | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: Unidad II: -Capa física concepto y medios- . Protocolo enlace de datos (HDLC -Control de enlace de datos de alto nivel-, Capa de enlace de datos en Internet -Pr
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Sitios web sobre normativas, tecnologías y soluciones, opcional: | Pagina: 5]
   > Materia: Comunicacion y Redes Sección: Sitios web sobre normativas, tecnologías y soluciones, opcional: IETF -> www.ietf.org IEEE -> www.ieee.org ISO -> www.iso.org CISCO -> www.cisco.com IANA -> www

**Respuesta:**

Los requisitos para regularizar en Bases de Datos Avanzadas y en Redes y Comunicaciones no son iguales. En Bases de Datos Avanzadas, se precisa obtener más del 70% en todos los parciales, mientras que en Redes y Comunicaciones, un estudiante con condición de REGULAR deberá rendir un examen de los temas teóricos y prácticos desarrollados en la materia (prueba escrita), y un estudiante LIBRE rendirá un examen final sobre el programa vigente a la fecha del examen en forma escrita de los conceptos teóricos.

**Tokens:** entrada: 1575 | salida: 136 | total: 1711

---

### Pregunta 10

> - ¿Cuál es el porcentaje de asistencia a clases que exigen en común las materias de Investigación Operativa, Comunicaciones y Redes, y Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% de asistencia a las clases teóricas y prácticas.
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Respecto a las clases: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Respecto a las clases: a todas las clases y, al mismo tiempo, reducir la tasa de abandono. Por ello, los materiales teóricos y las
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% Los exámenes se desarrollarán estrictamente en los bloques horarios asignados a la materia. La ausencia no justificada (sin certificado
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: JIMENA | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: JIMENA CRUZ; Año de la carrera a la que pertenece la cátedra: 4 Régimen de la materia: Anual Carga horaria semanal: 3 horas Correlativa: Ingeniería
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% reconocido por su sintaxis sencilla para ingresar ecuaciones y restricciones de manera directa. - WinQSB 2.0: Una suite clásica (dividida en
7. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos . Guillerón. 2018 Red Privada Virtual (VPM) sobre Protocolo de Internet versión 6 (IPv6) / Rodrigo Paúl Basso, Maximiliano Sebastián Toso; dir
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad VII: -Capa de Red- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad VII: -Capa de Red- ; Algoritmos de enrutamiento (Principio de optimización, Enrutamiento por la ruta más corta, Inundación, Enrutamiento por vector de di

**Respuesta:**

El porcentaje de asistencia común exigido por las materias de Investigación Operativa, Metodología de la Investigación y no por Comunicaciones y Redes (que no está relacionada en el contexto con el 80% de asistencia) es del 80%.

**Tokens:** entrada: 1577 | salida: 60 | total: 1637

---

### Pregunta 11

> - Si quiero promocionar todas las materias de 4to año, ¿cuál es la diferencia de promedio exigido entre Investigación Operativa e Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: | Pagina: 1]
   > Materia: Investigación Operativa Sección: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: - ALUMNO PROMOCIONADO: El estudiante logrará la promoción directa si alcanza un prom
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% de asistencia a las clases teóricas y prácticas.
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% reconocido por su sintaxis sencilla para ingresar ecuaciones y restricciones de manera directa. - WinQSB 2.0: Una suite clásica (dividida en
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Agentes | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Agentes que aprenden. Capítulo II Procesos de Búsqueda. Representación en un espacio de estados. Búsqueda Ciega, definición; búsqueda primero en amplitud,
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas s
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: PL: | Pagina: 1]
   > Materia: Investigación Operativa Sección: PL: región factible, búsqueda de la solución óptima en los vértices, análisis de casos especiales (soluciones múltiples, soluciones no acot
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% de modelos de optimización y problemas de gestión: - LINDO (Linear, Interactive, and Discrete Optimizer): Software especializado en la resolución
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Integración | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1369 | salida: 14 | total: 1383

---

### Pregunta 12

> - ¿Qué herramientas de software se recomiendan en la carrera para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% de modelos de optimización y problemas de gestión: - LINDO (Linear, Interactive, and Discrete Optimizer): Software especializado en la resolución
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible vía URL que
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Problema | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Problema de separación lineal. Aplicaciones.
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio integrando conceptos de informática, gestión organizacional y derecho informático. Los estudi
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Sitios web sobre normativas, tecnologías y soluciones, opcional: | Pagina: 5]
   > Materia: Comunicacion y Redes Sección: Sitios web sobre normativas, tecnologías y soluciones, opcional: LACNIC -> http://lacnic.net/sp/ LAC IPV6 TF -> www.lac.ipv6tf.org 3M -> www.3m.com FURUKAWA ->
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad II: -Capa física concepto y medios- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad II: -Capa física concepto y medios- . ARP (protocolo de resolución de direcciones). Mantenimiento de la tabla ARP. ARP proxy. Cableado Estructurado: Sele
8. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos . 2019 Estrategia para planear una migración de software propietario a software libre para la Facultad de Ciencia y Tecnología (FCyT) Sede Oro

**Respuesta:**

Disponemos de varias herramientas de software específicas para resolver problemas de optimización lineal.

Para resolver problemas de optimización lineal, se pueden utilizar herramientas como LINDO, que es un software especializado en la resolución de problemas de programación lineal, entera y no lineal. 

Sin embargo, la respuesta a si se relacionan con las unidades teóricas no está respaldada.

**Tokens:** entrada: 1557 | salida: 89 | total: 1646

---

### Pregunta 13

> - ¿Dónde puedo descargar la materia de Cálculo de 1er año?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Primer | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Primer Orden.
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Entorno | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Entorno de Trabajo.
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Recocido | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Recocido Simulado.
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Lenguaje | Pagina: 3]
   > Materia: Inteligencia Artificial Sección: Lenguaje ACL.
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Adquisición | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Adquisición de Conocimiento. Base de Conocimientos, características generales.
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Búsqueda | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Búsqueda A*,
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Problema | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Problema XOR.
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Problema | Pagina: 3]
   > Materia: Inteligencia Artificial Sección: Problema heurística y matemática del procedimiento BP.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 810 | salida: 14 | total: 824

---

### Pregunta 14

> - El profesor Ing. Jorge L. Schmukler da clases en Bases de Datos Avanzadas, en Inteligencia Artificial y en Redes y Comunicaciones.

**Chunks de contexto:**

1. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Bases de Datos Avanzadas | Pagina: 2]
   > Materia: Bases de Datos Avanzadas Sección: Bases de Datos Avanzadas Equipo docente Trossero, Sebastián Teoría Trossero.sebastian@uader.edu.ar Schmuckler, Jorge Práctica Schmukler.jorge@uader.edu.ar
2. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Días de clase | Pagina: 4]
   > Materia: Bases de Datos Avanzadas Sección: Días de clase Cronograma de clases Presenciales/Virtuales A partir de este año la materia será dictada de manera bimodal. El cronograma será definido en su
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: SEDE: Oro Verde | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler. AÑO ACADEMICO: 2023 PLAN DE EST
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Principal (Disponibles en biblioteca) | Pagina: 4]
   > Materia: Inteligencia Artificial Sección: Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig.
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Clases | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Clases e instancias.
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad VII: -Capa de Red- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad VII: -Capa de Red- . Direccionamiento estático y dinámico. Planificación del direccionamiento (segmentación de red). Clase de direccionamiento (clase a,
7. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos . 2022 Modelos vectoriales y redes neuronales artificiales, para la aplicación de procesamiento de lenguaje natural en normativas jurídicas /
8. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio integrando conceptos de informática, gestión organizacional y derecho informático. Los estudi

**Respuesta:**

El profesor Ing. Jorge L. Schmukler da clases en Bases de Datos Avanzadas y en Comunicación y Redes.

**Tokens:** entrada: 1391 | salida: 32 | total: 1423

---

### Pregunta 15

> - ¿Cuál es el costo de la certificación oficial de Cisco que se menciona como opcional en la planificación?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Estándar | Pagina: 3]
   > Materia: Inteligencia Artificial Sección: Estándar FIPA.
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Recocido | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Recocido Simulado.
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: (Backward | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: (Backward Chaining). Herramientas para el desarrollo de Sistemas Expertos.
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Agentes | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Agentes que aprenden. Capítulo II Procesos de Búsqueda. Representación en un espacio de estados. Búsqueda Ciega, definición; búsqueda primero en amplitud,
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Editorial: Pearson Educación (2004 o versiones posteriores) | Pagina: 4]
   > Materia: Inteligencia Artificial Sección: Editorial: Pearson Educación (2004 o versiones posteriores) Título: Aprendizaje automático y aprendizaje profundo con Python, scikit-learn y Tensor Flow-
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Problema | Pagina: 3]
   > Materia: Inteligencia Artificial Sección: Problema Capítulo IX Redes Perceptron Multicapa, estructura básica. Proceso de Entrenamiento Backpropagation (BP).
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Adquisición | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Adquisición de Conocimiento. Base de Conocimientos, características generales.
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Tamaño | Pagina: 3]
   > Materia: Inteligencia Artificial Sección: Tamaño del conjunto de patrones para el entrenamiento.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 960 | salida: 14 | total: 974

---

### Pregunta 16

> - Para la Promoción Directa, se exige la aprobación de la totalidad de los trabajos prácticos (TP 1 al TP 5). ¿Cuál es la calificación numérica mínima que debe obtenerse en cada TP individual para que se considere aprobado?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: | Pagina: 1]
   > Materia: Investigación Operativa Sección: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: - ALUMNO PROMOCIONADO: El estudiante logrará la promoción directa si alcanza un prom
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos . Guillerón. 2018 Red Privada Virtual (VPM) sobre Protocolo de Internet versión 6 (IPv6) / Rodrigo Paúl Basso, Maximiliano Sebastián Toso; dir
3. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos . - Aprobación del examen parcial teórico con una calificación igual o superior a 75 (setenta y cinco) puntos. - Entrega de la totalidad de lo
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos aprobación o no aprobación, se establecerán exclusivamente en la mesa de examen final. c. Alumno Libre El/la estudiante que no se
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE . Tener aprobado con 60 puntos los tres parciales. 2- Haber realizado y aproba
6. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 9]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Software utilizado PostgreSQL 9.6 o superi
7. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Régimen | Regularidad: | Pagina: 7]
   > Materia: Bases de Datos Avanzadas Sección: Régimen | Regularidad: Asistencia: Según norma vigente. Todos los trabajos prácticos aprobados.
8. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Formulación | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Formulación modos de comunicación de resultados. Tp integrador: Presentación formal escrita y oral de todas las partes realizadas en los trabajos

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1697 | salida: 14 | total: 1711

---

### Pregunta 17

> - ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible vía URL que
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% de modelos de optimización y problemas de gestión: - LINDO (Linear, Interactive, and Discrete Optimizer): Software especializado en la resolución
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Problema | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Problema de separación lineal. Aplicaciones.
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Reactivo | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Reactivo Simple.
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE Evaluación Final: El alumno con condición de REGULAR, deberá rendir un examen
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: (Método | Pagina: 1]
   > Materia: Investigación Operativa Sección: (Método recursiva de los cálculos: etapas, estados, decisiones y principio de optimalidad de Bellman.
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Composición | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Composición MAX-MIN. Capítulo VII Sistemas Difusos. Consideraciones generales. Representación de conocimiento estructurado mediante reglas lingüísticas.
8. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Unidad 3: La dimensión de la estrategia general de investigación | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Unidad 3: La dimensión de la estrategia general de investigación ¿Cómo se va a estudiar el problema? Tipo de diseños cuantitativos o cualitativos. La

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1379 | salida: 14 | total: 1393

---

### Pregunta 18

> - ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mismo
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% de asistencia a las clases teóricas y prácticas.
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 13 04 de junio Presencial Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 13 04 de junio Presencial Teoría Marco metodológico I: enfoque y tipo de investigación / muestra 14 11 de junio Virtual Práctica
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Días de clase | Pagina: 3]
   > Materia: Bases de Datos Avanzadas Sección: Días de clase Lunes: 13:30 a 15:30 -> Teoría Viernes: 17:00 a 19:00 -> Práctica NOTA: Los horarios están en proceso de evaluación y pueden sufrir cambios
6. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos de revisión y devolución con el equipo docente. El trabajo deberá entregarse con una antelación mínima de diez (10) días h
7. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Días de clase | Pagina: 4]
   > Materia: Bases de Datos Avanzadas Sección: Días de clase Cronograma de clases Presenciales/Virtuales A partir de este año la materia será dictada de manera bimodal. El cronograma será definido en su
8. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 8]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Comunicación De rutina y consultas: Lista

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1502 | salida: 14 | total: 1516

---

## Conversacion 4

**Puntaje evaluado: 11 / 18**

**Parametros modificados respecto a la conversacion anterior:**

| Parametro | Valor |
|---|---|
| top_k | 5 |
| retrieval_type | similarity_search |
| max_context_chunks | 5 |
| chunk_size | 300 |
| chunk_overlap | 50 |

### Pregunta 1

> - ¿Cuáles son los contenidos de la materia Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. He
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Integración | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Integración del sistema. Agentes Basados en Lógica Difusa. Capítulo VIII Redes Neuronales Artificiales (RNA). Generalidades, conceptos básicos Reseña Hist
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Descripción | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Descripción de los temas específicos a desarrollarse en la asignatura.
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Métodos | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Métodos comparativas entre las distintas representaciones. Comportamiento de Agentes Basados en Conocimientos. Capítulo IV Diseño de los Sistemas Exper
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Métodos | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Métodos y mensajes. Representación de Conocimientos mediante reglas. Estructura básica. Representación de reglas mediante objetos.

**Respuesta:**

Los contenidos de la materia Inteligencia Artificial incluyen las siguientes secciones: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes, Integración del sistema, que abarca Agentes Basados en Lógica Difusa, Capítulo VIII Redes Neuronales Artificiales (RNA) con generalidades y conceptos básicos, Reseña Histórica; Descripción de los temas específicos a desarrollarse, que no se detalla; y Métodos comparativos entre las distintas representaciones, que incluye Comportamiento de Agentes Basados en Conocimientos, Capítulo IV Diseño de los Sistemas Expertos, y Métodos y mensajes, que abarca la Representación de Conocimientos mediante reglas y su estructura básica.

**Tokens:** entrada: 861 | salida: 174 | total: 1035

---

### Pregunta 2

> - ¿En qué materia se enseña el concepto de Lógica Difusa?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Capítulo VI | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Capítulo VI Lógica Difusa (Fuzzy). Consideraciones generales, Conjuntos Difusos, definición.
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Composición | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Composición MAX-MIN. Capítulo VII Sistemas Difusos. Consideraciones generales. Representación de conocimiento estructurado mediante reglas lingüísticas.
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Integración | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Integración del sistema. Agentes Basados en Lógica Difusa. Capítulo VIII Redes Neuronales Artificiales (RNA). Generalidades, conceptos básicos Reseña Hist
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Integración | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Procesos | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Procesos basadas en Lógica.

**Respuesta:**

La materia en la que se enseña el concepto de Lógica Difusa es la Inteligencia Artificial.

**Tokens:** entrada: 870 | salida: 26 | total: 896

---

### Pregunta 3

> - ¿Cuál es el plan de estudios de Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: JIMENA | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: JIMENA Año de la carrera a la que pertenece la cátedra: 4 Régimen de la materia: Anual Carga horaria semanal: 3 horas Correlativa: Ingeniería del Sof
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 1 12 de marzo Presencial Teórico/práctico Presentación de la asignatura | 2 19 de marzo Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 1 12 de marzo Presencial Teórico/práctico Presentación de la asignatura | 2 19 de marzo Virtual Teoría Conceptos generales para introducción 3 26 de
3. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Metodología | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Metodología como el conjunto de estrategias, reflexiones y decisiones que configuran los procesos de investigación científica. Por lo
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 8 30 de abril Presencial (pedir cambio fecha) Práctica | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 8 30 de abril Presencial (pedir cambio fecha) Práctica 9 7 de mayo virtual Teoría Alcances, límites y limitaciones/ Objetivos / Justificación 10 14 d
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Metodología | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Metodología cotidiano, productivo y organizacional. Objetivos generales: - Acercar al campo de la investigación científica desde espacios de refl

**Respuesta:**

El plan de estudios de Metodología de la Investigación incluye varias secciones y contenidos organizados en fechas específicas. La materia tiene una carga horaria semanal de 3 horas y es correlativa con otras asignaturas como Ingeniería del Software I (208) y Probabilidad y Estadística (317).

Las secciones se presentan en dos fechas diferentes: el 12 de marzo presencial teórico/práctico para la presentación de la asignatura y el 19 de marzo virtual para la teoría de los conceptos generales para la introducción.

El contenido de la materia se divide en varios temas:

- Presentación de la asignatura
- Conceptos generales para la introducción (teoría)
- Normas APA/escritura académica (práctica)
- Tema/ problema (teoría)
- Alcances, límites y limitaciones/Objetivos/Justificación (teoría)
- Marco Teórico/Hipótesis (teoría)

Además, se menciona que el conjunto de estrategias, reflexiones y decisiones que configuran los procesos de investigación científica es parte de la metodología.

**Tokens:** entrada: 1074 | salida: 259 | total: 1333

---

### Pregunta 4

> - En Comunicaciones y Redes, ¿cómo hago para quedar como alumno regular?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE El alumno accederá a la condición de REGULAR, si cumple con las siguientes con
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE . Tener aprobado con 60 puntos los tres parciales. 2- Haber realizado y aproba
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE . Con ninguna nota inferior a 60 puntos en cada parcial. 2- Haber realizado y
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE El alumno accederá a la condición de PROMOCIÓN si cumple con las siguientes co
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE Evaluación Final: El alumno con condición de REGULAR, deberá rendir un examen

**Respuesta:**

Para quedar como alumno regular en Comunicaciones y Redes, debes cumplir con las siguientes condiciones de cátedra: 

1 - Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos

También debes tener aprobado con 60 puntos los tres parciales. Además, debes haber realizado y aprobado los dos trabajos Práctico impartido por la cátedra, y asistir al 80% de las clases teóricas y prácticas.

La nota mínima en los parciales es de 60 puntos, no de 60 puntos en cada uno de ellos.

**Tokens:** entrada: 1190 | salida: 145 | total: 1335

---

### Pregunta 5

> - ¿Qué instancias de recuperación nos provee Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% - ALUMNO LIBRE: Revestirá esta condición todo estudiante que no logre cumplimentar alguno de los requisitos de puntaje, trabajos prácticos o as
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mismo
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Resolución | Pagina: 1]
   > Materia: Investigación Operativa Sección: Resolución de problemas de diligencia, asignación de recursos y reemplazo de equipos.
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación mediante una interfaz basada en menús para la carga de datos. - TORA: Herramienta educativa diseñada específicamente para el aprendiz
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: PLANIFICACIÓN INVESTIGACIÓN OPERATIVA | Pagina: 1]
   > Materia: Investigación Operativa Sección: PLANIFICACIÓN INVESTIGACIÓN OPERATIVA Unidad I: -Introducción y Modelos Matemáticos- Definición y origen de la Investigación Operativa.

**Respuesta:**

La cátedra dispone de dos oportunidades de recuperatorio totales, que pueden utilizarse para cualquiera de los dos parciales, siempre y cuando no se apliquen ambos recuperatorios al mismo examen parcial.

**Tokens:** entrada: 924 | salida: 51 | total: 975

---

### Pregunta 6

> - ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación mediante una interfaz basada en menús para la carga de datos. - TORA: Herramienta educativa diseñada específicamente para el aprendiz
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% se considerará como examen reprobado. Software de Aplicación - Investigación Operativa A continuación, se describen las herramientas informáticas ut
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio integrando conceptos de informática, gestión organizacional y derecho informático. Los estudi

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 985 | salida: 14 | total: 999

---

### Pregunta 7

> - ¿Qué profesor forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes?

**Chunks de contexto:**

1. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Bases de Datos Avanzadas | Pagina: 2]
   > Materia: Bases de Datos Avanzadas Sección: Bases de Datos Avanzadas Equipo docente Trossero, Sebastián Teoría Trossero.sebastian@uader.edu.ar Schmuckler, Jorge Práctica Schmukler.jorge@uader.edu.ar
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: SEDE: Oro Verde | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler. AÑO ACADEMICO: 2023 PLAN DE EST
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Sitios web sobre normativas, tecnologías y soluciones, opcional: | Pagina: 5]
   > Materia: Comunicacion y Redes Sección: Sitios web sobre normativas, tecnologías y soluciones, opcional: Lic. Luciano M. CAISSO.
4. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Días de clase | Pagina: 3]
   > Materia: Bases de Datos Avanzadas Sección: Días de clase Lunes: 13:30 a 15:30 -> Teoría Viernes: 17:00 a 19:00 -> Práctica NOTA: Los horarios están en proceso de evaluación y pueden sufrir cambios
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Bases de Datos Avanzadas | Pagina: 1]
   > Materia: Bases de Datos Avanzadas Sección: Bases de Datos Avanzadas PRESENTACIÓN DE LA MATERIA Facultad de Ciencia Y Tecnología Base de Datos Avanzadas

**Respuesta:**

El profesor Schmuckler, Jorge, forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes.

**Tokens:** entrada: 932 | salida: 40 | total: 972

---

### Pregunta 8

> - ¿Qué otra asignatura, además de la propia materia de Inteligencia Artificial, incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. He
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Descripción | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Descripción de los temas específicos a desarrollarse en la asignatura.
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Integración | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Integración del sistema. Agentes Basados en Lógica Difusa. Capítulo VIII Redes Neuronales Artificiales (RNA). Generalidades, conceptos básicos Reseña Hist
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Métodos | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Métodos y mensajes. Representación de Conocimientos mediante reglas. Estructura básica. Representación de reglas mediante objetos.
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Métodos | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Métodos comparativas entre las distintas representaciones. Comportamiento de Agentes Basados en Conocimientos. Capítulo IV Diseño de los Sistemas Exper

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 891 | salida: 14 | total: 905

---

### Pregunta 9

> - Los requisitos para regularizar en Bases de Datos Avanzadas y en Redes y Comunicaciones, ¿son iguales? ¿Qué diferencias tienen?

**Chunks de contexto:**

1. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 9]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Software utilizado PostgreSQL 9.6 o superi
2. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 8]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Comunicación De rutina y consultas: Lista
3. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Régimen | Regularidad: | Pagina: 7]
   > Materia: Bases de Datos Avanzadas Sección: Régimen | Regularidad: Asistencia: Según norma vigente. Todos los trabajos prácticos aprobados.
4. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 10]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Bibliografía base Libro: Fundamentos de Si
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Unidad IV: Bases de Datos Distribuidas Parcial | Unidad V: Datawarehouse Parcial | Pagina: 6]
   > Materia: Bases de Datos Avanzadas Sección: Unidad IV: Bases de Datos Distribuidas Parcial | Unidad V: Datawarehouse Parcial Unidad VI: Datamining Parcial + TP Unidad VII: Bases de Datos OO Parcial NO

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1094 | salida: 14 | total: 1108

---

### Pregunta 10

> - ¿Cuál es el porcentaje de asistencia a clases que exigen en común las materias de Investigación Operativa, Comunicaciones y Redes, y Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% de asistencia a las clases teóricas y prácticas.
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Respecto a las clases: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Respecto a las clases: y, al mismo tiempo, reducir la tasa de abandono. Por ello, los materiales teóricos y las lecturas obligatoria
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% requisito indispensable la entrega y aprobación de los dos trabajos prácticos obligatorios y el cumplimiento del
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% asignados a la materia. La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como exa

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 907 | salida: 14 | total: 921

---

### Pregunta 11

> - Si quiero promocionar todas las materias de 4to año, ¿cuál es la diferencia de promedio exigido entre Investigación Operativa e Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: | Pagina: 1]
   > Materia: Investigación Operativa Sección: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: - ALUMNO PROMOCIONADO: El estudiante logrará la promoción directa si alcanza un prom
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mismo
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% requisito indispensable la entrega y aprobación de los dos trabajos prácticos obligatorios y el cumplimiento del
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación mediante una interfaz basada en menús para la carga de datos. - TORA: Herramienta educativa diseñada específicamente para el aprendiz

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1009 | salida: 14 | total: 1023

---

### Pregunta 12

> - ¿Qué herramientas de software se recomiendan en la carrera para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% de optimización y problemas de gestión: - LINDO (Linear, Interactive, and Discrete Optimizer): Software especializado en la resolución de problem
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% se considerará como examen reprobado. Software de Aplicación - Investigación Operativa A continuación, se describen las herramientas informáticas ut
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Definición | Pagina: 1]
   > Materia: Investigación Operativa Sección: Definición de variables de decisión, función objetivo y restricciones de sistema y de no negatividad. Unidad II: -Programación Lineal (PL)- Pro
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación resolver problemas de programación lineal

**Respuesta:**

Se recomienda utilizar LINDO (Linear, Interactive, and Discrete Optimizer) para la resolución de problemas de programación lineal. No dispongo de información en mis documentos para describir la relación con las unidades teóricas de la materia Investigación Operativa.

**Tokens:** entrada: 923 | salida: 59 | total: 982

---

### Pregunta 13

> - ¿Dónde puedo descargar la materia de Cálculo de 1er año?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Primer | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Primer Orden.
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Clases | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Clases e instancias.
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Entorno | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Entorno de Trabajo.
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Recocido | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Recocido Simulado.
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: (Pruning | Pagina: 3]
   > Materia: Inteligencia Artificial Sección: (Pruning Algorithms).

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 651 | salida: 14 | total: 665

---

### Pregunta 14

> - El profesor Ing. Jorge L. Schmukler da clases en Bases de Datos Avanzadas, en Inteligencia Artificial y en Redes y Comunicaciones.

**Chunks de contexto:**

1. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Bases de Datos Avanzadas | Pagina: 2]
   > Materia: Bases de Datos Avanzadas Sección: Bases de Datos Avanzadas Equipo docente Trossero, Sebastián Teoría Trossero.sebastian@uader.edu.ar Schmuckler, Jorge Práctica Schmukler.jorge@uader.edu.ar
2. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Días de clase | Pagina: 4]
   > Materia: Bases de Datos Avanzadas Sección: Días de clase Cronograma de clases Presenciales/Virtuales A partir de este año la materia será dictada de manera bimodal. El cronograma será definido en su
3. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Unidad IV: Bases de Datos Distribuidas Parcial | Unidad V: Datawarehouse Parcial | Pagina: 6]
   > Materia: Bases de Datos Avanzadas Sección: Unidad IV: Bases de Datos Distribuidas Parcial | Unidad V: Datawarehouse Parcial Unidad VI: Datamining Parcial + TP Unidad VII: Bases de Datos OO Parcial NO
4. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Días de clase | Pagina: 3]
   > Materia: Bases de Datos Avanzadas Sección: Días de clase Lunes: 13:30 a 15:30 -> Teoría Viernes: 17:00 a 19:00 -> Práctica NOTA: Los horarios están en proceso de evaluación y pueden sufrir cambios
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Bases de Datos Avanzadas | Pagina: 1]
   > Materia: Bases de Datos Avanzadas Sección: Bases de Datos Avanzadas PRESENTACIÓN DE LA MATERIA Facultad de Ciencia Y Tecnología Base de Datos Avanzadas

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 935 | salida: 14 | total: 949

---

### Pregunta 15

> - ¿Cuál es el costo de la certificación oficial de Cisco que se menciona como opcional en la planificación?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Estándar | Pagina: 3]
   > Materia: Inteligencia Artificial Sección: Estándar FIPA.
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Recocido | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Recocido Simulado.
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: (Backward | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: (Backward Chaining). Herramientas para el desarrollo de Sistemas Expertos.
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Descripción | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Descripción de los temas específicos a desarrollarse en la asignatura.
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Adquisición | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Adquisición Estructura de Control: Procedimientos de Inferencia; Interfase con el usuario. Memoria de Trabajo, Módulo generador de explicaciones al usuario.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 760 | salida: 14 | total: 774

---

### Pregunta 16

> - Para la Promoción Directa, se exige la aprobación de la totalidad de los trabajos prácticos (TP 1 al TP 5). ¿Cuál es la calificación numérica mínima que debe obtenerse en cada TP individual para que se considere aprobado?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos . Promoción Directa Para acceder a la condición de Promoción Directa, el/la estudiante deberá cumplir con los siguientes requisitos: - 80 % de
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: | Pagina: 1]
   > Materia: Investigación Operativa Sección: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: - ALUMNO PROMOCIONADO: El estudiante logrará la promoción directa si alcanza un prom
3. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos . - Aprobación del examen parcial teórico con una calificación igual o superior a 75 (setenta y cinco) puntos. - Entrega de la totalidad de lo
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE . Con ninguna nota inferior a 60 puntos en cada parcial. 2- Haber realizado y
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE El alumno accederá a la condición de PROMOCIÓN si cumple con las siguientes co

**Respuesta:**

Lo siento, pero no dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1137 | salida: 19 | total: 1156

---

### Pregunta 17

> - ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible vía URL que
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: PL: | Pagina: 1]
   > Materia: Investigación Operativa Sección: PL: región factible, búsqueda de la solución óptima en los vértices, análisis de casos especiales (soluciones múltiples, soluciones no acot
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación resolver problemas de programación lineal
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex y el
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Definición | Pagina: 1]
   > Materia: Investigación Operativa Sección: Definición de variables de decisión, función objetivo y restricciones de sistema y de no negatividad. Unidad II: -Programación Lineal (PL)- Pro

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 849 | salida: 14 | total: 863

---

### Pregunta 18

> - ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 15 18 de junio Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 15 18 de junio Virtual Teoría investigación 17 13 de agosto Virtual Tutorías 18 20 de agosto Presencial (cambio encuentro) Teoría Parcial teoría 19 2
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% automáticamente a la nota del examen original. Protocolos de Evaluación: Los resultados se publicarán en un plazo de siete días corridos tras la
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 15 18 de junio Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 15 18 de junio Virtual Teoría 24 de septiembre Virtual Tutorías 24 01 de octubre Presencial Tutorías Presentación tesina- ver posibilidad 25 08 de oc
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mismo

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1054 | salida: 14 | total: 1068

---

## Resumen de tokens

| Conversacion | Entrada | Salida | Total |
|---|---|---|---|
| 1 | 17517 | 841 | 18358 |
| 2 | 18531 | 935 | 19466 |
| 3 | 25239 | 1581 | 26820 |
| 4 | 17046 | 913 | 17959 |
| **Total** | **78333** | **4270** | **82603** |
