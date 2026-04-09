# Evaluacion — test-OllamaV4

_Iniciada: 2026-04-09 02:15:28_
_Ultima actualizacion: 2026-04-09 02:19:51_

**Estado:** completado
**Archivo de evaluacion:** `tests/evaluacionOllamaTop3.md`
**Preguntas:** 18 | **Conversaciones planificadas:** 3 | **Conversaciones iniciadas:** 3 | **Preguntas procesadas:** 54

**Nota de comparacion con V5:** en este informe se evaluaron las 3 configuraciones de `tests/evaluacionOllamaTop3.md`. Respecto de `V5`, no queda reflejado aqui ningun cambio de `system prompt`; la diferencia explicita en los artefactos de evaluacion es que `V5` agrega una cuarta configuracion: `recursive`, `chunk_size = 300`, `chunk_overlap = 50`, `retrieval_type = similarity_search`, `top_k = 5`, `max_context_chunks = 5`.

**Criterio de puntaje:** 1 punto por respuesta correcta o abstencion correcta en preguntas de borde, 0.5 por respuesta parcial pero util y 0 por respuesta incorrecta, incompleta de forma critica o no sustentada por el contexto.

## Conversacion 1

**Puntaje evaluado: 14 / 18**

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

**Puntaje evaluado: 13.5 / 18**

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

La materia Inteligencia Artificial abarca contenidos como la Introducción a la Inteligencia Artificial (IA), definiciones y objetivos, herramientas y técnicas ofrecidas por el área IA. Además, se desarrollarán temas específicos como la comparativa de métodos entre distintas representaciones, el comportamiento de agentes basados en conocimientos, el diseño de sistemas expertos, la representación de conocimientos mediante reglas y estructura básica, y la integración de la solución difusa final, incluyendo el proceso de defuzzificación y su influencia sobre el funcionamiento del sistema, así como el desarrollo de agentes basados en lógica difusa y redes neuronales artificiales.

**Tokens:** entrada: 924 | salida: 155 | total: 1079

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

**Tokens:** entrada: 889 | salida: 25 | total: 914

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

El plan de estudios de Metodología de la Investigación incluye 12 sesiones distribuidas de la siguiente manera: 

1 y 2: Presentación de la asignatura y teoría conceptual en presencial y virtual respectivamente.
3: Normas APA/escritura académica en línea.
4: Sin clase.
5: Tema o problema en presencial.
6 a 12: Pregunta de investigación, antecedentes, trabajos propios, objetivos específicos, estrategias, reflexiones y decisiones que configuran los procesos de investigación científica, alcances, límites y limitaciones, objetivos, justificación, marco teórico y hipótesis, todas en línea.

Es importante destacar que estos espacios de trabajo se distribuyen a lo largo de un periodo que abarca desde el 12 de marzo hasta el 28 de mayo.

**Tokens:** entrada: 1248 | salida: 193 | total: 1441

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

**Tokens:** entrada: 1345 | salida: 54 | total: 1399

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

La cátedra dispone de dos oportunidades de recuperatorio totales.

**Tokens:** entrada: 1078 | salida: 17 | total: 1095

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

TORA es una herramienta educativa diseñada específicamente para el aprendizaje de la investigación operativa. No tengo información sobre los módulos que incluye según la cátedra, solo menciona que está diseñada para el aprendizaje de la investigación operativa.

**Tokens:** entrada: 1365 | salida: 59 | total: 1424

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

Se recomienda utilizar LINGO (64 bits) para resolver problemas de optimización lineal, ya que está diseñado para modelar y resolver problemas de gran escala.

**Tokens:** entrada: 1001 | salida: 37 | total: 1038

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

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 861 | salida: 14 | total: 875

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

**Puntaje evaluado: 12.5 / 18**

**Parametros modificados respecto a la conversacion anterior:**

| Parametro | Valor |
|---|---|
| top_k | 8 |
| retrieval_type | mmr |
| max_context_chunks | 8 |
| chunk_size | 500 |

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

La materia Inteligencia Artificial abarca varios temas específicos que se desarrollan en la asignatura. Entre ellos se encuentran la Introducción a la IA, definiciones y objetivos, herramientas y técnicas proporcionadas por el área de IA. Además, se estudian los temas como la Representación de Conocimientos mediante reglas y estructura básica, la Representación de reglas mediante objetos, la Integración de la solución difusa final, el Proceso de Defuzzificación, el Método del centroide, el Método de máxima, la Influencia de la aplicación de los distintos métodos sobre el funcionamiento del sistema, Agentes Basados en Lógica Difusa, Redes Neuronales Artificiales (RNA), Generalidades, conceptos básicos y Reseña Histórica.

**Tokens:** entrada: 1141 | salida: 176 | total: 1317

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

La Lógica Difusa se enseña en la materia de Inteligencia Artificial.

**Tokens:** entrada: 1180 | salida: 20 | total: 1200

---

### Pregunta 3

> - ¿Cuál es el plan de estudios de Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: JIMENA | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: JIMENA CRUZ; Año de la carrera a la que pertenece la cátedra: 4 Régimen de la materia: Anual Carga horaria semanal: 3 horas Correlativa: Ingeniería
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 1 12 de marzo Presencial Teórico/práctico Presentación de la asignatura | 2 19 de marzo Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 1 12 de marzo Presencial Teórico/práctico Presentación de la asignatura | 2 19 de marzo Virtual Teoría Conceptos generales para introducción 3 26 de
3. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Estructura del aula virtual: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Estructura del aula virtual: Los materiales educativos estarán alojados en el aula virtual "Metodología de la Investigación" dentro de la plataform
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Sistema de evaluación: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Sistema de evaluación: examen contará con una (1) instancia de recuperación, conforme al cronograma establecido por la cátedra. - Entre
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Unidad 3: La dimensión de la estrategia general de investigación | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Unidad 3: La dimensión de la estrategia general de investigación ¿Cómo se va a estudiar el problema? Tipo de diseños cuantitativos o cualitativos. La
6. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Cronograma de trabajo | METODOLOGÍA DE LA INVESTIGACIÓN- 2026 | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Cronograma de trabajo | METODOLOGÍA DE LA INVESTIGACIÓN- 2026 Clase FECHA Tipo de encuentro Tipo encuentro Tema
7. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Metodología | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Metodología brindar conocimientos y herramientas para indagar la realidad en la búsqueda y desnaturalización de problemas, tanto del
8. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Nacional | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Nacional en https://ediciones.ungs.edu.ar/wp-content/uploads/2018/09/9789876301190-completo.pdf

**Respuesta:**

El plan de estudios de Metodología de la Investigación incluye 12 clases distribuidas en 6 unidades, abarcando temas como la presentación de la asignatura, teoría y práctica, escritura académica, tema y problema, pregunta de investigación, antecedentes, estrategia general de investigación, técnicas de obtención y análisis de información, comunicación de resultados, análisis de datos y más.

**Tokens:** entrada: 1775 | salida: 94 | total: 1869

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
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad II: -Capa física concepto y medios- | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: Unidad II: -Capa física concepto y medios- . Protocolo enlace de datos (HDLC -Control de enlace de datos de alto nivel-, Capa de enlace de datos en Internet -Pr
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad VII: -Capa de Red- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad VII: -Capa de Red- . Proveedores de servicio de internet (ISP), descripción Ipv6. Unidad IX -VLans- Definiciones de Vlan, Beneficios de una Vlan, Rangos
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS . Reid, Jim Lorenz, Cheryl Schmidt. - Madrid: Pearson Educación, 2009. ISBN 9788483224694 [Disponible en Biblioteca FCyT- Oro

**Respuesta:**

Para quedar como alumno regular en la materia de Comunicaciones y Redes, debes cumplir con las condiciones establecidas en el sistema de evaluación. En específico, debes obtener una calificación promedio superior o igual a los 60 puntos en los tres parciales.

**Tokens:** entrada: 1701 | salida: 62 | total: 1763

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

La cátedra dispone de dos oportunidades de recuperatorio totales.

**Tokens:** entrada: 1278 | salida: 17 | total: 1295

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

TORA es una herramienta educativa diseñada específicamente para el aprendizaje de la Investigación Operativa.

**Tokens:** entrada: 1763 | salida: 25 | total: 1788

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

Jorge L. Schmukler.

**Tokens:** entrada: 1397 | salida: 10 | total: 1407

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

En Bases de Datos Avanzadas, para regularizar, el alumno debe rendir un examen de los temas teóricos y prácticos desarrollados en la materia (prueba escrita) y tener aprobados 6 de los 7 parciales con más del 50%. Esto se desprende de la información proporcionada en el documento "BDA Planificación.pdf".

En Redes y Comunicaciones, para regularizar, el alumno debe rendir un examen final sobre el programa vigente a la fecha del examen en forma escrita de los conceptos teóricos, y una prueba teórica y la práctica será realizada en la pc haciendo uso del simulador. El alumno también debe tener aprobados todos los trabajos prácticos.

Las diferencias principales entre los requisitos de regularización en ambas materias son:

* En Bases de Datos Avanzadas, se requiere rendir un examen de temas teóricos y prácticos, mientras que en Redes y Comunicaciones solo se requiere rendir un examen final sobre el programa vigente y realizar una prueba teórica y práctica.
* En Bases de Datos Avanzadas, se requiere aprobar 6 de los 7 parciales con más del 50%, mientras que en Redes y Comunicaciones no se especifica ningún requisito de aprobación de parciales.

**Tokens:** entrada: 1575 | salida: 303 | total: 1878

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
   > Materia: Investigación Operativa Sección: 80% la evaluación. Los exámenes se desarrollarán estrictamente en los bloques horarios asignados a la materia. La ausencia no justificada
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: JIMENA | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: JIMENA CRUZ; Año de la carrera a la que pertenece la cátedra: 4 Régimen de la materia: Anual Carga horaria semanal: 3 horas Correlativa: Ingeniería
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% reconocido por su sintaxis sencilla para ingresar ecuaciones y restricciones de manera directa. - WinQSB 2.0: Una suite clásica (dividida en
7. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos . Guillerón. 2018 Red Privada Virtual (VPM) sobre Protocolo de Internet versión 6 (IPv6) / Rodrigo Paúl Basso, Maximiliano Sebastián Toso; dir
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad VII: -Capa de Red- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad VII: -Capa de Red- ; Algoritmos de enrutamiento (Principio de optimización, Enrutamiento por la ruta más corta, Inundación, Enrutamiento por vector de di

**Respuesta:**

El porcentaje de asistencia a clases que exigen comúnmente las materias de Investigación Operativa y Metodología de la Investigación es del 80%.

**Tokens:** entrada: 1583 | salida: 36 | total: 1619

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
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible vía URL que
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Problema | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Problema de separación lineal. Aplicaciones.
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad VII: -Capa de Red- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad VII: -Capa de Red- ; Algoritmos de enrutamiento (Principio de optimización, Enrutamiento por la ruta más corta, Inundación, Enrutamiento por vector de di
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio integrando conceptos de informática, gestión organizacional y derecho informático. Los estudi
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Sitios web sobre normativas, tecnologías y soluciones, opcional: | Pagina: 5]
   > Materia: Comunicacion y Redes Sección: Sitios web sobre normativas, tecnologías y soluciones, opcional: LACNIC -> http://lacnic.net/sp/ LAC IPV6 TF -> www.lac.ipv6tf.org 3M -> www.3m.com FURUKAWA ->
7. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos . 2019 Estrategia para planear una migración de software propietario a software libre para la Facultad de Ciencia y Tecnología (FCyT) Sede Oro
8. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Sistemas | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Sistemas que el/la estudiante cuente con herramientas conceptuales y prácticas para encarar los desafíos que suponen el ejercicio de

**Respuesta:**

LINDO (Linear, Interactive, and Discrete Optimizer) es un software especializado en la resolución de problemas de programación lineal, entera y no lineal.

PHP Simplex es una herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el método Simplex.

No dispongo de información en mis documentos para describir la relación entre estas herramientas y las unidades teóricas mencionadas en la carrera.

**Tokens:** entrada: 1519 | salida: 98 | total: 1617

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
   > Materia: Comunicacion y Redes Sección: Unidad VII: -Capa de Red- . Direcciones (especiales, públicas y privadas). Direccionamiento estático y dinámico. Planificación del direccionamiento (segmentació
7. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos . 2022 Modelos vectoriales y redes neuronales artificiales, para la aplicación de procesamiento de lenguaje natural en normativas jurídicas /
8. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio integrando conceptos de informática, gestión organizacional y derecho informático. Los estudi

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1404 | salida: 14 | total: 1418

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
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 9]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Software utilizado PostgreSQL 9.6 o superi
6. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Régimen | Regularidad: | Pagina: 7]
   > Materia: Bases de Datos Avanzadas Sección: Régimen | Regularidad: Asistencia: Según norma vigente. Todos los trabajos prácticos aprobados.
7. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Formulación | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Formulación modos de comunicación de resultados. Tp integrador: Presentación formal escrita y oral de todas las partes realizadas en los trabajos
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE . La nota obtenida en este reemplaza a la obtenida en el parcial que se recupe

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1660 | salida: 14 | total: 1674

---

### Pregunta 17

> - ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible vía URL que
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% de modelos de optimización y problemas de gestión: - LINDO (Linear, Interactive, and Discrete Optimizer): Software especializado en la resolución
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex y el
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Problema | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Problema de separación lineal. Aplicaciones.
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Reactivo | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Reactivo Simple.
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE Evaluación Final: El alumno con condición de REGULAR, deberá rendir un examen
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: (Método | Pagina: 1]
   > Materia: Investigación Operativa Sección: (Método recursiva de los cálculos: etapas, estados, decisiones y principio de optimalidad de Bellman.
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Composición | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Composición MAX-MIN. Capítulo VII Sistemas Difusos. Consideraciones generales. Representación de conocimiento estructurado mediante reglas lingüísticas.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1188 | salida: 14 | total: 1202

---

### Pregunta 18

> - ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mismo
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
3. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 15 18 de junio Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 15 18 de junio Virtual Teoría 10 de septiembre Virtual Tutorías Avances proyectos a la cátedra- Grupos Tamara 17 de septiembre Teoría Coloquio Avanc
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% de asistencia a las clases teóricas y prácticas.
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos de revisión y devolución con el equipo docente. El trabajo deberá entregarse con una antelación mínima de diez (10) días h
6. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Días de clase | Pagina: 3]
   > Materia: Bases de Datos Avanzadas Sección: Días de clase Lunes: 13:30 a 15:30 -> Teoría Viernes: 17:00 a 19:00 -> Práctica NOTA: Los horarios están en proceso de evaluación y pueden sufrir cambios
7. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Días de clase | Pagina: 4]
   > Materia: Bases de Datos Avanzadas Sección: Días de clase Cronograma de clases Presenciales/Virtuales A partir de este año la materia será dictada de manera bimodal. El cronograma será definido en su
8. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 8]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Comunicación De rutina y consultas: Lista

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1571 | salida: 14 | total: 1585

---

## Resumen de tokens

| Conversacion | Entrada | Salida | Total |
|---|---|---|---|
| 1 | 17517 | 1055 | 18572 |
| 2 | 18531 | 720 | 19251 |
| 3 | 25060 | 953 | 26013 |
| **Total** | **61108** | **2728** | **63836** |
