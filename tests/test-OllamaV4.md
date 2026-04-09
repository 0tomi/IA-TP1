# Evaluacion — test-OllamaV4

_Iniciada: 2026-04-09 02:15:28_
_Ultima actualizacion: 2026-04-09 02:17:06_

**Estado:** en progreso
**Archivo de evaluacion:** `tests/evaluacionOllamaTop3.md`
**Preguntas:** 18 | **Conversaciones planificadas:** 3 | **Conversaciones iniciadas:** 1 | **Preguntas procesadas:** 14

## Conversacion 1

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

La materia de Inteligencia Artificial se desarrolla en varios capítulos y secciones. En la sección de "Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes" se cubren temas relacionados con la introducción a la Inteligencia Artificial, definiciones y objetivos, así como las herramientas y técnicas proporcionadas por el área.

En la sección "Descripción", se presentan los temas específicos a desarrollarse en la asignatura, aunque la información proporcionada es muy general y no se mencionan detalles concretos.

En la sección "Métodos comparativas entre las distintas representaciones", se abordan los comportamientos de Agentes Basados en Conocimientos y se describe la estructura básica de la representación de conocimientos mediante reglas, incluyendo la representación mediante objetos.

Finalmente, en la sección "Integración", se introduce el tema de Neuronales Artificiales (RNA), con una breve reseña histórica de los conceptos básicos.

Además de estos temas, hay varias otras secciones mencionadas pero sin contenido. No dispongo de información en mis documentos para proporcionar un inventario completo de los contenidos de la materia.

**Tokens:** entrada: 839 | salida: 267 | total: 1106

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

El plan de estudios de la materia Metodología de la Investigación tiene 12 sesiones. Comienza el 12 de marzo con una presentación presencial y se reparten entre teoría y práctica. Algunas sesiones están programadas para presencial y otras para virtual.

- Semana 1: 12 de marzo, presencial, teórico/práctico, presentación de la asignatura.
- Semana 2: 19 de marzo, virtual, teoría. Conceptos generales para introducción.
- Semana 3: 26 de marzo, virtual, práctica. Normas APA/escritura académica.
- Semana 4: 2 de abril, sin clase.
- Semana 5: 9 de abril, presencial, teoría. Tema/ problema.
- Semana 6: 16 de abril, virtual, práctica. 
- Semana 7: 23 de abril, virtual, teoría. Pregunta de investigación (variables, unidad de análisis, contexto).
- Semana 8: 30 de abril, presencial (se sugiere cambio de fecha), práctica.
- Semana 9: 7 de mayo, virtual, teoría. Alcances, límites y limitaciones/ Objetivos / Justificación.
- Semana 10: 14 de mayo, virtual, práctica.
- Semana 11: 21 de mayo, virtual, teoría. Marco Teórico/ hipótesis.
- Semana 12: 28 de mayo, virtual, teoría.

No dispongo de información en mis documentos para saber si esto es todo el plan de estudios, ya que no hay un contenido más allá de esta información.

**Tokens:** entrada: 1130 | salida: 372 | total: 1502

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

Para quedar como alumno regular en Comunicaciones y Redes, debes cumplir con las siguientes condiciones: obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos. Tener aprobado con 60 puntos los tres parciales. Asistir al 80% de las clases teóricas y prácticas.

**Tokens:** entrada: 1305 | salida: 81 | total: 1386

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

La cátedra de Investigación Operativa dispone de dos oportunidades de recuperatorio totales.

**Tokens:** entrada: 923 | salida: 22 | total: 945

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

TORA es una herramienta educativa diseñada específicamente para el aprendizaje de la Investigación Operativa.

**Tokens:** entrada: 1020 | salida: 25 | total: 1045

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

Schmuckler, Jorge forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes.

**Tokens:** entrada: 998 | salida: 36 | total: 1034

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

LINDO (Linear, Interactive, and Discrete Optimizer) es un software especializado en la resolución de problemas de programación lineal, entera y no lineal. Storm es otra herramienta utilizada para el análisis cuantitativo y gestión de operaciones, lo que facilita el procesamiento de modelos matemáticos y estadísticos mediante una interfaz basada en macros.

**Tokens:** entrada: 951 | salida: 87 | total: 1038

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

_Evaluacion en progreso. La siguiente pregunta a procesar es la 15._

## Resumen de tokens

| Conversacion | Entrada | Salida | Total |
|---|---|---|---|
| 1 | 13559 | 999 | 14558 |
| **Total** | **13559** | **999** | **14558** |
