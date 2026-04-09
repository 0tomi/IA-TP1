# Evaluacion — test-OllamaV3

_Iniciada: 2026-04-09 01:53:17_
_Ultima actualizacion: 2026-04-09 02:03:39_

**Estado:** completado
**Archivo de evaluacion:** `tests/evaluacionOllama.md`
**Preguntas:** 18 | **Conversaciones planificadas:** 6 | **Conversaciones iniciadas:** 6 | **Preguntas procesadas:** 108

**Criterio de puntaje:** 1 punto por respuesta correcta o abstencion correcta en preguntas de borde, 0.5 por respuesta parcial pero util y 0 por respuesta incorrecta, incompleta de forma critica o no sustentada por el contexto.

## Conversacion 1

**Puntaje evaluado: 10 / 18**

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
| chunk_size | 512 |
| chunk_overlap | 100 |
| embedding_model | BAAI/bge-m3 |
| chunking_technique | recursive |
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
   > Materia: Inteligencia Artificial Sección: Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación

**Respuesta:**

"Los contenidos específicos a desarrollarse en la asignatura se mencionan en la sección 'Descripción' del documento. En ella se indican los temas específicos a desarrollarse en la materia. Sin embargo, no se especifican explícitamente en la pregunta proporcionada, entonces no dispongo de información en mis documentos para enumerarlos."

**Tokens:** entrada: 765 | salida: 76 | total: 841

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
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad II: -Capa física concepto y medios- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad II: -Capa física concepto y medios- Protocolo libre de colisiones, Protocolo de LAN Inalámbricas), Ethernet, concepto sobre el Algoritmo de retroceso exp

**Respuesta:**

La materia en la que se enseña el concepto de Lógica Difusa es la Inteligencia Artificial.

**Tokens:** entrada: 911 | salida: 26 | total: 937

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

En el Contexto, proporcionan el programa de clases de la materia "Metodología de la Investigación", que incluye detalles sobre el día y la modalidad de las clases, el tipo de contenidos a abordar (teóricos y prácticos), y la fecha de cada clase específica. Por lo tanto, según el plan de clases del documento, el plan de estudios de Metodología de la Investigación incluye los siguientes contenidos y fechas, dividido en una primera parte teórica presencial y virtual, y una segunda parte práctica virtual.

Para el contenido teórico, se incluyen fechas de clases tanto presenciales como virtuales:
- 1 12 de marzo Presencial Teórico/práctico Presentación de la asignatura
- 2 19 de marzo Virtual Teoría Conceptos generales para introducción
- 3 26 de marzo Virtual Práctica Normas APA/ escritura académica
- 4 2 de abril (sin clase)
- 5 09 de abril Presencial Teoría Tema/ problema
- 6 16 de abril Virtual Práctica
- 7 23 de abril Virtual Teoría Pregunta de investigación (variables, unidad de análisis, contexto)/ Antecedentes

Y para el contenido práctico, las fechas son:
- 8 30 de abril Presencial (pedir cambio fecha) Práctica
- 9 7 de mayo virtual Teoría Alcances, límites y limitaciones/ Objetivos / Justificación
- 10 14 de mayo Virtual Práctica
- 11 21 de mayo Virtual Teoría Marco Teórico/ hipótesis
- 12 28 de mayo Virtual Teoría

El programa completo de clases de la materia Metodología de la Investigación incluye 12 clases, distribuidas a lo largo de 12 semanas, con una combinación de clases teóricas y prácticas, con un énfasis en que el contenido de la materia va desde una introducción básica a conceptos avanzados de investigación, pasando por la fundamentación epistemológica, los aspectos metodológicos, la estructura de la investigación, los pasos y etapas de la investigación, pasando por la creación de preguntas de investigación, hasta la realización de la práctica de investigación en el ámbito de la investigación cuantitativa y cualitativa.

**Tokens:** entrada: 1089 | salida: 530 | total: 1619

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
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos . Guillerón. 2018 Red Privada Virtual (VPM) sobre Protocolo de Internet versión 6 (IPv6) / Rodrigo Paúl Basso, Maximiliano Sebastián Toso; dir

**Respuesta:**

Para quedar como alumno regular en la materia de Comunicación y Redes, debes cumplir con la condición específica mencionada en el contexto. En concreto, es necesario obtener una calificación promedio de 60 puntos o superior en los 3 parciales. No está descrito, en las condiciones para la condición de Regular, otros requisitos más allá de los parciales.

Para quedar como alumno regular no hay un número fijo de recuperatorios y ni tampoco se menciona el porcentaje de asistencia a la cursada.

**Tokens:** entrada: 1198 | salida: 123 | total: 1321

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

La información proporcionada en el Contexto indica que la cátedra de Investigación Operativa dispone de dos oportunidades de recuperatorio totales. Estas instancias de recuperación pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mismo examen parcial.

**Tokens:** entrada: 919 | salida: 76 | total: 995

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

**Tokens:** entrada: 1206 | salida: 14 | total: 1220

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

No dispongo de información en mis documentos para responder esta consulta. La información proporcionada sobre el equipo docente es diferente para cada materia: Bases de Datos Avanzadas tiene como equipo docente a Sebastián Trossero y Jorge Schmuckler, mientras que Comunicaciones y Redes está compuesto por Luciano M. Caisso e igualmente Jorge Schmuckler.

**Tokens:** entrada: 773 | salida: 83 | total: 856

---

### Pregunta 8

> - ¿Qué otra asignatura, además de la propia materia de Inteligencia Artificial, incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. He
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Unidad 2: Relaciones Humanas en el Contexto Organizacional | Pagina: 2]
   > Materia: Informática y Recursos Humanos Sección: Unidad 2: Relaciones Humanas en el Contexto Organizacional 1. Comunicación interna y cultura organizacional en entornos digitales. 2. Inteligencia emo
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Descripción | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Descripción de los temas específicos a desarrollarse en la asignatura.
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Métodos | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Métodos y mensajes. Representación de Conocimientos mediante reglas. Estructura básica. Representación de reglas mediante objetos.
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Bibliografía Nacional: | Pagina: 2]
   > Materia: Informática y Recursos Humanos Sección: Bibliografía Nacional: Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de

**Respuesta:**

Dispongo de información para responder que, además de la asignatura de Inteligencia Artificial, la asignatura Informática y Recursos Humanos contempla el impacto de la inteligencia artificial en la gestión del talento. Se trata de la unidad 4: El impacto de la inteligencia artificial en la gestión del talento.

**Tokens:** entrada: 770 | salida: 73 | total: 843

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

**Tokens:** entrada: 935 | salida: 14 | total: 949

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

**Tokens:** entrada: 842 | salida: 14 | total: 856

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

Lo siento, pero no dispongo de información en mis documentos para responder esta consulta. El contexto solo proporciona información sobre el programa de Investigación Operativa y no menciona otras materias como Inteligencia Artificial, o la comparativa de requisitos de promoción entre asignaturas diferentes.

**Tokens:** entrada: 958 | salida: 62 | total: 1020

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

Los software recomendados para resolver problemas de optimización lineal son LINDO, LINGO y Storm.

LINDO es un software especializado en la resolución de problemas de programación lineal, entera y no lineal. 

Storm es un software orientado al análisis cuantitativo y gestión de operaciones, que facilita el procesamiento de modelos matemáticos y estadísticos mediante una interfaz basada en menús para la carga de datos.

**Tokens:** entrada: 842 | salida: 103 | total: 945

---

### Pregunta 13

> - ¿Dónde puedo descargar la materia de Cálculo de 1er año?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS 4- BIBLIOGRAFIA Obligatoria Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Ver
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Nacional | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Nacional en https://ediciones.ungs.edu.ar/wp-content/uploads/2018/09/9789876301190-completo.pdf
3. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Nacional | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Nacional : https://youtu.be/9oWM50RDsLQ -> BÚSQUEDA AVANZADA GOOGLE - BÚSQUEDA GOOGLE AVANZADA - 2DA PARTE APRENDER A INVESTIGAR: https://youtu.be/eH
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas s
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Nacional | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Nacional Material audiovisual de la unidad Sobre investigación María Teresa Sirven Clase 1 Maestría Tecnología Educativa https://youtu.be/yBL4Hu9n Fi

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1052 | salida: 14 | total: 1066

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

**Tokens:** entrada: 776 | salida: 14 | total: 790

---

### Pregunta 15

> - ¿Cuál es el costo de la certificación oficial de Cisco que se menciona como opcional en la planificación?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS 4- BIBLIOGRAFIA Obligatoria Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Ver
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Sitios web sobre normativas, tecnologías y soluciones, opcional: | Pagina: 5]
   > Materia: Comunicacion y Redes Sección: Sitios web sobre normativas, tecnologías y soluciones, opcional: IETF -> www.ietf.org IEEE -> www.ieee.org ISO -> www.iso.org CISCO -> www.cisco.com IANA -> www
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Sitios web sobre normativas, tecnologías y soluciones, opcional: | Pagina: 5]
   > Materia: Comunicacion y Redes Sección: Sitios web sobre normativas, tecnologías y soluciones, opcional: LACNIC -> http://lacnic.net/sp/ LAC IPV6 TF -> www.lac.ipv6tf.org 3M -> www.3m.com FURUKAWA ->
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas s
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Sitios web sobre normativas, tecnologías y soluciones, opcional: | Pagina: 5]
   > Materia: Comunicacion y Redes Sección: Sitios web sobre normativas, tecnologías y soluciones, opcional: Lic. Luciano M. CAISSO.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1027 | salida: 14 | total: 1041

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

Lo siento, pero no dispongo de información en mis documentos para responder esta consulta sobre la calificación numérica mínima requerida para aprobar cada trabajo práctico (TP) individual para la condición de Promoción Directa.

**Tokens:** entrada: 1168 | salida: 51 | total: 1219

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

**Tokens:** entrada: 702 | salida: 14 | total: 716

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

**Tokens:** entrada: 890 | salida: 14 | total: 904

---

## Conversacion 2

**Puntaje evaluado: 9 / 18**

**Parametros modificados respecto a la conversacion anterior:**

| Parametro | Valor |
|---|---|
| top_k | 8 |
| retrieval_type | mmr |
| max_context_chunks | 8 |
| refresh | False |

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

No dispongo de información en mis documentos para responder esta consulta.

Si necesitas la información completa, me gustaría ayudarte con el contenido de la materia de Inteligencia Artificial, pero es necesario que me proporciones más datos o secciones del material proporcionado.

**Tokens:** entrada: 982 | salida: 56 | total: 1038

---

### Pregunta 2

> - ¿En qué materia se enseña el concepto de Lógica Difusa?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Capítulo VI | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Capítulo VI Lógica Difusa (Fuzzy). Consideraciones generales, Conjuntos Difusos, definición.
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Procesos | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Procesos basadas en Lógica.
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad II: -Capa física concepto y medios- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad II: -Capa física concepto y medios- Protocolo libre de colisiones, Protocolo de LAN Inalámbricas), Ethernet, concepto sobre el Algoritmo de retroceso exp
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Respecto a las clases: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Respecto a las clases: La cátedra implementará el modelo de aula invertida, en el que los estudiantes adquieren los conocimientos teóricos de mane
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio . FUNDAMENTACIÓN El avance de las tecnologías de la información y la comunicación (TIC) ha tr
6. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos Deep Learning aplicado al aprendizaje automático de ontologías para la representación del conocimiento a partir de texto no estructurado / Enz
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al
8. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Nacional | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Nacional : https://youtu.be/9oWM50RDsLQ -> BÚSQUEDA AVANZADA GOOGLE - BÚSQUEDA GOOGLE AVANZADA - 2DA PARTE APRENDER A INVESTIGAR: https://youtu.be/eH

**Respuesta:**

Según el Contexto, el concepto de Lógica Difusa se enseña en la Materia de Inteligencia Artificial, específicamente en el Capítulo VI, en el que se presentan consideraciones generales, Conjuntos Difusos y la definición de Lógica Difusa.

**Tokens:** entrada: 1511 | salida: 67 | total: 1578

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

No dispongo de información en mis documentos para responder esta consulta. 

El contexto proporcionado incluye un plan de clases, un programa, un cronograma, y materiales y objetivos generales para la materia Metodología de la Investigación, pero no contiene un plan de estudios en el sentido tradicional de planes de estudios que contienen los cursos obligatorios de un programa académico.

**Tokens:** entrada: 1620 | salida: 86 | total: 1706

---

### Pregunta 4

> - En Comunicaciones y Redes, ¿cómo hago para quedar como alumno regular?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE El alumno accederá a la condición de REGULAR, si cumple con las siguientes con
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos . Guillerón. 2018 Red Privada Virtual (VPM) sobre Protocolo de Internet versión 6 (IPv6) / Rodrigo Paúl Basso, Maximiliano Sebastián Toso; dir
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: SEDE: Oro Verde | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler. AÑO ACADEMICO: 2023 PLAN DE EST
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 8]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Comunicación De rutina y consultas: Lista
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS . As.: Fox Andina, 2013, ISBN: 9789871857784. - USERS. [Disponible en Biblioteca FCyT- Oro Verde] Curso visual y práctico: Adm
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad II: -Capa física concepto y medios- | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: Unidad II: -Capa física concepto y medios- . Protocolo enlace de datos (HDLC -Control de enlace de datos de alto nivel-, Capa de enlace de datos en Internet -Pr

**Respuesta:**

Para quedar como alumno regular en la materia de Comunicaciones y Redes, se establece que el estudiante debe lograr una calificación mínima en ambos parciales.

**Tokens:** entrada: 1616 | salida: 39 | total: 1655

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

**Tokens:** entrada: 1119 | salida: 22 | total: 1141

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

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1604 | salida: 14 | total: 1618

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

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1238 | salida: 14 | total: 1252

---

### Pregunta 8

> - ¿Qué otra asignatura, además de la propia materia de Inteligencia Artificial, incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. He
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Unidad 2: Relaciones Humanas en el Contexto Organizacional | Pagina: 2]
   > Materia: Informática y Recursos Humanos Sección: Unidad 2: Relaciones Humanas en el Contexto Organizacional 1. Comunicación interna y cultura organizacional en entornos digitales. 2. Inteligencia emo
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Descripción | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Descripción de los temas específicos a desarrollarse en la asignatura.
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Bibliografía Nacional: | Pagina: 2]
   > Materia: Informática y Recursos Humanos Sección: Bibliografía Nacional: Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Condiciones | Pagina: 3]
   > Materia: Inteligencia Artificial Sección: Condiciones de inicialización, problema de saturación prematura. Regiones de Decisión. Modo de operación autoasociativo. Capítulo X Generalización en
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Editorial: Pearson Educación (2004 o versiones posteriores) | Pagina: 4]
   > Materia: Inteligencia Artificial Sección: Editorial: Pearson Educación (2004 o versiones posteriores) Título: Aprendizaje automático y aprendizaje profundo con Python, scikit-learn y Tensor Flow-
7. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio . Además, se abordarán aspectos legales fundamentales para comprender el impacto normativo de
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Associative | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Associative Memories).

**Respuesta:**

La respuesta es Informática y Recursos Humanos, ya que su Unidad 2: Relaciones Humanas en el Contexto Organizacional incluye el tema "El impacto de la inteligencia artificial en la gestión del talento".

**Tokens:** entrada: 1060 | salida: 52 | total: 1112

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

Para responder a la pregunta del usuario sobre los requisitos para regularizar en Bases de Datos Avanzadas y en Redes y Comunicaciones, reviso la información proporcionada en el Contexto.

En el documento "BDA Planificación.pdf", en la sección "Régimen | Regularidad:", se establece que "Según norma vigente. Todos los trabajos prácticos aprobados" son los requisitos para regularizar.

Por otro lado, en el documento "Planificación 2025 - Comunicacion y Redes.pdf", en la sección "2- SISTEMA DE EVALUACIÓN | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE", se describe que un alumno con condición de "REGULAR" deberá rendir un examen final de los temas teóricos y prácticos desarrollados en la materia (prueba escrita).

Si bien la información proporcionada sobre los requisitos para regularizar no es idéntica, tanto en Bases de Datos Avanzadas como en Redes y Comunicaciones, la respuesta a la pregunta del usuario sí puede darse en función de la información proporcionada. 

En este caso, se deduce que los requisitos para regularizar en Bases de Datos Avanzadas y en Redes y Comunicaciones tienen diferencias. En Bases de Datos Avanzadas, los requisitos se basan en aprobar todos los trabajos prácticos, mientras que en Redes y Comunicaciones, el alumno con condición de "REGULAR" deberá rendir un examen final. 

Así que la respuesta es que sí, los requisitos para regularizar en Bases de Datos Avanzadas y en Redes y Comunicaciones, son diferentes.

**Tokens:** entrada: 1416 | salida: 377 | total: 1793

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

El porcentaje de asistencia a clases exigido en común por las materias de Investigación Operativa y Metodología de la Investigación es del 80%.

**Tokens:** entrada: 1418 | salida: 36 | total: 1454

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

**Tokens:** entrada: 1210 | salida: 14 | total: 1224

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

Resolvemos esto en dos partes.

Para resolver problemas de optimización lineal, las herramientas recomendadas son LINDO y PHP Simplex, de las cuales LINDO puede resolver problemas de programación lineal, entera y no lineal. Las unidades teóricas relacionadas son Transporte, Redes y Teoría de Juegos de la Sección Simplex.

Sin embargo, en la Sección de Investigación no encontramos información que conecte directamente las herramientas con las unidades teóricas.

**Tokens:** entrada: 1398 | salida: 112 | total: 1510

---

### Pregunta 13

> - ¿Dónde puedo descargar la materia de Cálculo de 1er año?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS 4- BIBLIOGRAFIA Obligatoria Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Ver
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Nacional | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Nacional en https://ediciones.ungs.edu.ar/wp-content/uploads/2018/09/9789876301190-completo.pdf
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas s
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Primer | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Primer Orden.
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Bibliografía Nacional: | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Bibliografía Nacional: Ley de Teletrabajo (Ley 27.555).
6. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio I
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: (Método | Pagina: 1]
   > Materia: Investigación Operativa Sección: (Método recursiva de los cálculos: etapas, estados, decisiones y principio de optimalidad de Bellman.
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad II: -Capa física concepto y medios- | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: Unidad II: -Capa física concepto y medios- . Protocolo enlace de datos (HDLC -Control de enlace de datos de alto nivel-, Capa de enlace de datos en Internet -Pr

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1083 | salida: 14 | total: 1097

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

Lo siento, pero no dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1232 | salida: 19 | total: 1251

---

### Pregunta 15

> - ¿Cuál es el costo de la certificación oficial de Cisco que se menciona como opcional en la planificación?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS 4- BIBLIOGRAFIA Obligatoria Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Ver
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Sitios web sobre normativas, tecnologías y soluciones, opcional: | Pagina: 5]
   > Materia: Comunicacion y Redes Sección: Sitios web sobre normativas, tecnologías y soluciones, opcional: IETF -> www.ietf.org IEEE -> www.ieee.org ISO -> www.iso.org CISCO -> www.cisco.com IANA -> www
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas s
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad II: -Capa física concepto y medios- | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: Unidad II: -Capa física concepto y medios- : -Capa de enlace de dato -sub capa LLC (control de enlace lógico)- Cuestiones en el diseño de la capa de enlace de d
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% Los exámenes se desarrollarán estrictamente en los bloques horarios asignados a la materia. La ausencia no justificada (sin certificado
6. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 9]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Software utilizado PostgreSQL 9.6 o superi
7. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos . 2019 Estrategia para planear una migración de software propietario a software libre para la Facultad de Ciencia y Tecnología (FCyT) Sede Oro
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE El alumno accederá a la condición de REGULAR, si cumple con las siguientes con

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta. La certificación de Cisco mencionada en la planificación es "Guía del primer año" de Cisco Systems, publicada en 2002 por Pearson Educación, pero no se menciona el costo de dicha certificación.

**Tokens:** entrada: 1531 | salida: 62 | total: 1593

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

No dispongo de información en mis documentos para responder esta consulta. La información proporcionada sobre trabajos prácticos no menciona una calificación numérica específica para considerarlos aprobados.

**Tokens:** entrada: 1538 | salida: 42 | total: 1580

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

**Tokens:** entrada: 1220 | salida: 14 | total: 1234

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

**Tokens:** entrada: 1343 | salida: 14 | total: 1357

---

## Conversacion 3

**Puntaje evaluado: 10 / 18**

**Parametros modificados respecto a la conversacion anterior:**

| Parametro | Valor |
|---|---|
| top_k | 5 |
| retrieval_type | similarity_search |
| chunk_size | 300 |
| chunk_overlap | 50 |
| chunking_technique | fixed_size_overlap |
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
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Composición | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Composición amiento del sistema. Proceso de Inferencia. Tratamiento paralelo de las reglas. Determinación del aporte parcial de cada regla.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta. El contenido solicitado corresponde a los temas específicos a desarrollarse en la materia, pero en los fragmentos recuperados solo se mencionan las secciones correspondientes a Introducción a la Inteligencia Artificial (IA), Descripción de los temas específicos a desarrollarse en la asignatura, Métodos comparativas entre las distintas representaciones, Comportamiento de Agentes Basados en Conocimientos, Capítulo IV Diseño de los Sistemas Expertos, Métodos y mensajes, y Composición del aporte del sistema, pero no los contenidos de la materia en sí.

**Tokens:** entrada: 698 | salida: 140 | total: 838

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
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad II: -Capa física concepto y medios- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad II: -Capa física concepto y medios- Protocolo libre de colisiones, Protocolo de LAN Inalámbricas), Ethernet, concepto sobre el Algoritmo de retroceso exp

**Respuesta:**

La materia en la que se enseña el concepto de Lógica Difusa es la Inteligencia Artificial. 

Encontré esta información en la sección "Capítulo VI" de un documento sobre el Programa de Cátedra de IA, donde se menciona que el capítulo es sobre Lógica Difusa.

**Tokens:** entrada: 808 | salida: 73 | total: 881

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
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Sistema de evaluación: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Sistema de evaluación: ablecidas en el cronograma académico. Programa de trabajos prácticos: Tp 1: Escritura académica. Se solicita a los estudi

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 964 | salida: 14 | total: 978

---

### Pregunta 4

> - En Comunicaciones y Redes, ¿cómo hago para quedar como alumno regular?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE Haber realizado y aprobado los dos trabajos práctico impartido por la cátedra.
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE El alumno accederá a la condición de PROMOCIÓN si cumple con las siguientes co
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE s 3 parciales, una calificación promedio superior o igual a los 60 puntos. Ten
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE cada la ausencia. Evaluación Final: El alumno con condición de REGULAR, deber
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE nes parciales como los recuperatorios se realizaran en los horarios asignados

**Respuesta:**

Para quedar como alumno regular en la materia de Comunicación y Redes, debes cumplir con las siguientes condiciones:

1. Obtener en los 3 parciales una calificación promedio superior a una nota determinada.
2. Haber realizado y aprobado los dos trabajos prácticos impartidos por la cátedra.
3. Asistir al 80% de las clases teóricas y prácticas.

No dispongo de información en mis documentos para determinar con certeza la nota determinada para la calificación promedio en los 3 parciales para alcanzar la condición de REGULAR.

**Tokens:** entrada: 1158 | salida: 136 | total: 1294

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
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: PLANIFICACIÓN INVESTIGACIÓN OPERATIVA | Pagina: 1]
   > Materia: Investigación Operativa Sección: PLANIFICACIÓN INVESTIGACIÓN OPERATIVA Unidad I: -Introducción y Modelos Matemáticos- Definición y origen de la Investigación Operativa.
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación tadísticos mediante una interfaz basada en menús para la carga de datos. - TORA: Herramienta educativa diseñada específicamente para

**Respuesta:**

La cátedra de Investigación Operativa dispone de dos oportunidades de recuperatorio totales.

**Tokens:** entrada: 772 | salida: 22 | total: 794

---

### Pregunta 6

> - ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación tadísticos mediante una interfaz basada en menús para la carga de datos. - TORA: Herramienta educativa diseñada específicamente para
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% mientas informáticas utilizadas en la cátedra para la resolución de modelos de optimización y problemas de gestión: - LINDO (Linear, Interactive
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS oria Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] Cisco Systems: Acad
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al

**Respuesta:**

No dispongo de información en mis documentos para responder la parte "qué módulos incluye según la cátedra" de la pregunta. TORA (TORA: Herramienta educativa diseñada específicamente para el aprendizaje de la Investigación Operativa) se utiliza para el aprendizaje de la investigación operativa.

**Tokens:** entrada: 924 | salida: 70 | total: 994

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

La información proporcionada en el Contexto no especifica directamente qué profesor forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes. Sin embargo, podemos encontrar dos fragmentos relevantes de información.

En el Contexto "Comunicacion y Redes.pdf", se menciona que el Equipo Docente de la materia "Comunicaciones y Redes" está compuesto por "Lic. Luciano M. Caisso, Ing. Jorge L. Schmuckler".

Por otro lado, en el Contexto "BDA Planificacion.pdf", se menciona que el Equipo Docente de la materia "Bases de Datos Avanzadas" está compuesto por "Trossero, Sebastián Teoría Trossero.sebastian@uader.edu.ar Schmuckler, Jorge Práctica Schmukler.jorge@uader.edu.ar". 

Sin embargo, a partir de la información proporcionada, no es posible determinar con certeza qué profesor forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes, ya que solo se menciona al profesor Jorge L. Schmuckler en los dos contextos, pero en diferentes roles y materias. 

No dispongo de información en mis documentos para responder con precisión esta pregunta del usuario.

**Tokens:** entrada: 839 | salida: 300 | total: 1139

---

### Pregunta 8

> - ¿Qué otra asignatura, además de la propia materia de Inteligencia Artificial, incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. He
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Unidad 2: Relaciones Humanas en el Contexto Organizacional | Pagina: 2]
   > Materia: Informática y Recursos Humanos Sección: Unidad 2: Relaciones Humanas en el Contexto Organizacional 1. Comunicación interna y cultura organizacional en entornos digitales. 2. Inteligencia emo
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Descripción | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Descripción de los temas específicos a desarrollarse en la asignatura.
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Métodos | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Métodos y mensajes. Representación de Conocimientos mediante reglas. Estructura básica. Representación de reglas mediante objetos.
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Bibliografía Nacional: | Pagina: 2]
   > Materia: Informática y Recursos Humanos Sección: Bibliografía Nacional: Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de

**Respuesta:**

La materia 'Informática y Recursos Humanos' incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas, específicamente en la unidad 'El impacto de la inteligencia artificial en la gestión del talento'.

**Tokens:** entrada: 770 | salida: 63 | total: 833

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
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE Haber realizado y aprobado los dos trabajos práctico impartido por la cátedra.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 993 | salida: 14 | total: 1007

---

### Pregunta 10

> - ¿Cuál es el porcentaje de asistencia a clases que exigen en común las materias de Investigación Operativa, Comunicaciones y Redes, y Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% de asistencia a las clases teóricas y prácticas.
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% os a la materia. La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen re
3. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Respecto a las clases: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Respecto a las clases: o pueden asistir a todas las clases y, al mismo tiempo, reducir la tasa de abandono. Por ello, los materiales
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% utomáticamente a la nota del examen original. Protocolos de Evaluación: Los resultados se publicarán en un plazo de siete días corridos tras la

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta. El Contexto sólo proporciona información sobre las materias de Investigación Operativa y Metodología de la Investigación.

**Tokens:** entrada: 843 | salida: 39 | total: 882

---

### Pregunta 11

> - Si quiero promocionar todas las materias de 4to año, ¿cuál es la diferencia de promedio exigido entre Investigación Operativa e Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: | Pagina: 1]
   > Materia: Investigación Operativa Sección: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: - ALUMNO PROMOCIONADO: El estudiante logrará la promoción directa si alcanza un prom
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% os a la materia. La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen re
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mismo
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% requisito indispensable la entrega y aprobación de los dos trabajos prácticos obligatorios y el cumplimiento del

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 894 | salida: 14 | total: 908

---

### Pregunta 12

> - ¿Qué herramientas de software se recomiendan en la carrera para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% mientas informáticas utilizadas en la cátedra para la resolución de modelos de optimización y problemas de gestión: - LINDO (Linear, Interactive
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Definición | Pagina: 1]
   > Materia: Investigación Operativa Sección: Definición de variables de decisión, función objetivo y restricciones de sistema y de no negatividad. Unidad II: -Programación Lineal (PL)- Pro
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación resolver problemas de programación lineal
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Método | Pagina: 2]
   > Materia: Investigación Operativa Sección: Método ideal para validaciones rápidas y visualización de regiones factibles. - LINGO (64 bits): Una versión avanzada y más potente del motor LINDO.

**Respuesta:**

Podemos identificar que en la sección de "Investigación" de Investigación Operativa, el software "LINDO" se menciona como herramienta para resolver problemas de optimización lineal, entera y no lineal. Además, en otra sección se refiere a LINGO como una versión avanzada del motor LINDO, que permite modelar y resolver problemas de optimización de gran escala. Por lo tanto, LINDO y LINGO se recomiendan para resolver problemas de optimización lineal.

**Tokens:** entrada: 813 | salida: 115 | total: 928

---

### Pregunta 13

> - ¿Dónde puedo descargar la materia de Cálculo de 1er año?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS oria Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] Cisco Systems: Acad
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Nacional | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Nacional en https://ediciones.ungs.edu.ar/wp-content/uploads/2018/09/9789876301190-completo.pdf Material audiovisual de la unidad Sobre investigació
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas s
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 1- PROGRAMA DE CONTENIDOS | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: 1- PROGRAMA DE CONTENIDOS edes domesticas, topologías. Software de redes, jerarquías de protocolos, aspectos de diseño de las capas, servicios orientados a la c
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Nacional | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Nacional - APRENDER A INVESTIGAR: https://youtu.be/9oWM50RDsLQ -> BÚSQUEDA AVANZADA GOOGLE - BÚSQUEDA GOOGLE AVANZADA - 2DA PARTE APRENDER A INVESTIG

**Respuesta:**

"No dispongo de información en mis documentos para responder esta consulta."

**Tokens:** entrada: 963 | salida: 14 | total: 977

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

**Tokens:** entrada: 776 | salida: 14 | total: 790

---

### Pregunta 15

> - ¿Cuál es el costo de la certificación oficial de Cisco que se menciona como opcional en la planificación?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Sitios web sobre normativas, tecnologías y soluciones, opcional: | Pagina: 5]
   > Materia: Comunicacion y Redes Sección: Sitios web sobre normativas, tecnologías y soluciones, opcional: IETF -> www.ietf.org IEEE -> www.ieee.org ISO -> www.iso.org CISCO -> www.cisco.com IANA -> www
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS oria Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] Cisco Systems: Acad
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Sitios web sobre normativas, tecnologías y soluciones, opcional: | Pagina: 5]
   > Materia: Comunicacion y Redes Sección: Sitios web sobre normativas, tecnologías y soluciones, opcional: 3 NATIONAL FIRE PROTECTION AGENCY (NFPA) -> www.nfpa.org GFI SECURITY AND MESSANGING SOFTWARE -
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas s
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Sitios web sobre normativas, tecnologías y soluciones, opcional: | Pagina: 5]
   > Materia: Comunicacion y Redes Sección: Sitios web sobre normativas, tecnologías y soluciones, opcional: kawa.com.br/internacional.html UNDERWRITERS LABORATORIES (UL) -> www.ul.com PANDUIT -> www.pand

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 995 | salida: 14 | total: 1009

---

### Pregunta 16

> - Para la Promoción Directa, se exige la aprobación de la totalidad de los trabajos prácticos (TP 1 al TP 5). ¿Cuál es la calificación numérica mínima que debe obtenerse en cada TP individual para que se considere aprobado?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos nales y libres: a. Promoción Directa Para acceder a la condición de Promoción Directa, el/la estudiante deberá cumplir con los siguientes requ
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: | Pagina: 1]
   > Materia: Investigación Operativa Sección: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: - ALUMNO PROMOCIONADO: El estudiante logrará la promoción directa si alcanza un prom
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE El alumno accederá a la condición de PROMOCIÓN si cumple con las siguientes co
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: | Pagina: 1]
   > Materia: Investigación Operativa Sección: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: deberá acreditar la aprobación de los dos trabajos prácticos de la cátedra
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos l o superior a 75 (setenta y cinco) puntos. - Entrega de la totalidad de los trabajos prácticos en tiempo y forma. - Pertinencia, coherencia y

**Respuesta:**

Lo siento, pero no dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1025 | salida: 19 | total: 1044

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

Lo siento, pero no dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 692 | salida: 19 | total: 711

---

### Pregunta 18

> - ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% utomáticamente a la nota del examen original. Protocolos de Evaluación: Los resultados se publicarán en un plazo de siete días corridos tras la
3. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 15 18 de junio Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 15 18 de junio Virtual Teoría entro) Teoría Parcial teoría 19 27 de agosto Virtual Tutorías 03 de septiembre Presencial Tutorías Sugerecia entrevist
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 15 18 de junio Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 15 18 de junio Virtual Teoría Marco metodológico II: recolección de datos y análisis de datos RECESO DE INVIERNO/ MESAS DE EXAMENES FINALES 16 06 de
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 15 18 de junio Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 15 18 de junio Virtual Teoría ara 17 de septiembre Teoría Coloquio Avances proyectos a la cátedra- Grupos Jimena 24 de septiembre Virtual Tutorías

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 935 | salida: 14 | total: 949

---

## Conversacion 4

**Puntaje evaluado: 8.5 / 18**

**Parametros modificados respecto a la conversacion anterior:**

| Parametro | Valor |
|---|---|
| top_k | 8 |
| retrieval_type | mmr |
| refresh | False |

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
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Integración | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Integración Capítulo VIII Redes Neuronales Artificiales (RNA). Generalidades, conceptos básicos Reseña Histórica.
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Condiciones | Pagina: 3]
   > Materia: Inteligencia Artificial Sección: Condiciones de inicialización, problema de saturación prematura. Regiones de Decisión. Modo de operación autoasociativo. Capítulo X Generalización en
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Associative | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Associative Memories).
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Adquisición | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Adquisición Estructura de Control: Procedimientos de Inferencia; Interfase con el usuario. Memoria de Trabajo, Módulo generador de explicaciones al usuario.

**Respuesta:**

Los contenidos de la materia Inteligencia Artificial están compuestos por los siguientes temas específicos a desarrollarse: Agentes Inteligentes, Integración de la solución difusa final, Proceso de Defuzzificación, Agentes Basados en Lógica Difusa, Redes Neuronales Artificiales (RNA), Generalización en las RNA, y Sistemas Expertos, entre otros.

**Tokens:** entrada: 978 | salida: 85 | total: 1063

---

### Pregunta 2

> - ¿En qué materia se enseña el concepto de Lógica Difusa?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Capítulo VI | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Capítulo VI Lógica Difusa (Fuzzy). Consideraciones generales, Conjuntos Difusos, definición.
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Procesos | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Procesos basadas en Lógica.
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad II: -Capa física concepto y medios- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad II: -Capa física concepto y medios- Protocolo libre de colisiones, Protocolo de LAN Inalámbricas), Ethernet, concepto sobre el Algoritmo de retroceso exp
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% mientas informáticas utilizadas en la cátedra para la resolución de modelos de optimización y problemas de gestión: - LINDO (Linear, Interactive
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Respecto a las clases: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Respecto a las clases: La cátedra implementará el modelo de aula invertida, en el que los estudiantes adquieren los conocimientos teóricos de mane
6. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio I. FUNDAMENTACIÓN El avance de las tecnologías de la información y la comunicación (TIC) ha t
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Editorial: Pearson Educación (2004 o versiones posteriores) | Pagina: 4]
   > Materia: Inteligencia Artificial Sección: Editorial: Pearson Educación (2004 o versiones posteriores) Título: Aprendizaje automático y aprendizaje profundo con Python, scikit-learn y Tensor Flow-
8. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Nacional | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Nacional - APRENDER A INVESTIGAR: https://youtu.be/9oWM50RDsLQ -> BÚSQUEDA AVANZADA GOOGLE - BÚSQUEDA GOOGLE AVANZADA - 2DA PARTE APRENDER A INVESTIG

**Respuesta:**

La materia en la que se enseña el concepto de Lógica Difusa es "Inteligencia Artificial". Esto se encuentra en el documento "IA - Programa de Cátedra (campus).pdf" en la sección "Capítulo VI" y en la sección "Procesos" bajo la categoría de lógica.

**Tokens:** entrada: 1225 | salida: 76 | total: 1301

---

### Pregunta 3

> - ¿Cuál es el plan de estudios de Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: JIMENA | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: JIMENA CRUZ; Año de la carrera a la que pertenece la cátedra: 4 Régimen de la materia: Anual Carga horaria semanal: 3 horas Correlativa: Ingeniería
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 1 12 de marzo Presencial Teórico/práctico Presentación de la asignatura | 2 19 de marzo Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 1 12 de marzo Presencial Teórico/práctico Presentación de la asignatura | 2 19 de marzo Virtual Teoría Conceptos generales para introducción 3 26 de
3. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Sistema de evaluación: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Sistema de evaluación: ablecidas en el cronograma académico. Programa de trabajos prácticos: Tp 1: Escritura académica. Se solicita a los estudi
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Cronograma de trabajo | METODOLOGÍA DE LA INVESTIGACIÓN- 2026 | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Cronograma de trabajo | METODOLOGÍA DE LA INVESTIGACIÓN- 2026 Clase FECHA Tipo de encuentro Tipo encuentro Tema
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Estructura del aula virtual: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Estructura del aula virtual: Los materiales educativos estarán alojados en el aula virtual "Metodología de la Investigación" dentro de la plataform
6. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Metodología | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Metodología brindar conocimientos y herramientas para indagar la realidad en la búsqueda y desnaturalización de problemas, tanto del
7. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Formulación | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Formulación modos de comunicación de resultados. Tp integrador: Presentación formal escrita y oral de todas las partes realizadas en los trabajos
8. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Unidad 3: La dimensión de la estrategia general de investigación | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Unidad 3: La dimensión de la estrategia general de investigación ¿Cómo se va a estudiar el problema? Tipo de diseños cuantitativos o cualitativos. La

**Respuesta:**

"El plan de estudios de Metodología de la Investigación consta de varias unidades y actividades, pero los detalles específicos sobre el plan de estudios no están claramente definidos en el contexto proporcionado. Sin embargo, se menciona que el programa incluye unidades como la introducción, la dimensión de la estrategia general de investigación y la dimensión de las técnicas de obtención y análisis de información empírica. Además, se mencionan actividades prácticas como la escritura académica, la presentación formal escrita y oral y trabajos integradores que involucran la presentación de todos los trabajos realizados y las sugerencias recibidas. Se solicita a los estudiantes seleccionar un artículo de investigación relacionado con su campo profesional. Sin embargo, no se proporciona información sobre la secuencia y duración de estas unidades y actividades o cómo interactúan entre sí."

Nota: Para proporcionar una respuesta más detallada, necesitaríamos más información sobre el plan de estudios, pero en base a lo que tenemos, la respuesta anterior describe los componentes de la materia pero no su secuencia.

**Tokens:** entrada: 1390 | salida: 245 | total: 1635

---

### Pregunta 4

> - En Comunicaciones y Redes, ¿cómo hago para quedar como alumno regular?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE Haber realizado y aprobado los dos trabajos práctico impartido por la cátedra.
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: SEDE: Oro Verde | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler. AÑO ACADEMICO: 2023 PLAN DE EST
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
4. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 8]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Comunicación De rutina y consultas: Lista
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos ed Privada Virtual (VPM) sobre Protocolo de Internet versión 6 (IPv6) / Rodrigo Paúl Basso, Maximiliano Sebastián Toso; director Julio Alberto
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 1- PROGRAMA DE CONTENIDOS | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: 1- PROGRAMA DE CONTENIDOS Unidad I: Introducción -Importancia e Influencia de las Redes en Nuestras Vidas: Comunicación en un mundo centrado en la red, herramie
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad VII: -Capa de Red- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad VII: -Capa de Red- de igual a igual), RIP protocolo de enrutamiento por clase vector de distancia, configuración, VLSM y CIDR; Algoritmos de control de c
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS disponible en Biblioteca FCyT- Oro Verde] Técnico en Redes & Seguridad, Bs. As.: Fox Andina, 2013, ISBN: 9789871857784. - USER

**Respuesta:**

Para quedar como alumno regular en la materia Comunicaciones y Redes, debes cumplir con las condiciones especificadas en el Plan de Estudio 2010, aprobado por la Resolución No 397/10 UADER. Según la información proporcionada, no hay una sección explícita en el Contexto que describa las condiciones para ser alumno regular en Comunicaciones y Redes. Sin embargo, hay varias referencias a condiciones similares en otras materias y documentos, como obtener una calificación mínima en parciales o superar un porcentaje determinado en los exámenes.

Sin embargo, en el documento "BDA Planificación.pdf" se menciona que "ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos parciales." En este punto, es importante destacar que no hay una definición explícita de "puntos" o "calificación mínima" en el Contexto proporcionado. Esto implica que para responder la pregunta del usuario con exactitud, se necesita más información específica acerca de las calificaciones o puntos necesarios para ser alumno regular en la materia Comunicaciones y Redes.

Por lo tanto, la respuesta parcial al usuario sería: "No dispongo de información en mis documentos para determinar los requisitos específicos para ser alumno regular en la materia Comunicaciones y Redes."

**Tokens:** entrada: 1438 | salida: 304 | total: 1742

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
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: (Método | Pagina: 1]
   > Materia: Investigación Operativa Sección: (Método recursiva de los cálculos: etapas, estados, decisiones y principio de optimalidad de Bellman.
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% mientas informáticas utilizadas en la cátedra para la resolución de modelos de optimización y problemas de gestión: - LINDO (Linear, Interactive
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: PL: | Pagina: 1]
   > Materia: Investigación Operativa Sección: PL: región factible, búsqueda de la solución óptima en los vértices, análisis de casos especiales (soluciones múltiples, soluciones no acot
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% de asistencia a las clases teóricas y prácticas.

**Respuesta:**

La cátedra dispone de dos oportunidades de recuperatorio totales.

**Tokens:** entrada: 1062 | salida: 17 | total: 1079

---

### Pregunta 6

> - ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación tadísticos mediante una interfaz basada en menús para la carga de datos. - TORA: Herramienta educativa diseñada específicamente para
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% mientas informáticas utilizadas en la cátedra para la resolución de modelos de optimización y problemas de gestión: - LINDO (Linear, Interactive
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 1- PROGRAMA DE CONTENIDOS | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: 1- PROGRAMA DE CONTENIDOS edes domesticas, topologías. Software de redes, jerarquías de protocolos, aspectos de diseño de las capas, servicios orientados a la c
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 15 18 de junio Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 15 18 de junio Virtual Teoría entro) Teoría Parcial teoría 19 27 de agosto Virtual Tutorías 03 de septiembre Presencial Tutorías Sugerecia entrevist
6. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio ectiva multidisciplinaria, integrando conceptos de informática, gestión organizacional y dere
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS disponible en Biblioteca FCyT- Oro Verde] Técnico en Redes & Seguridad, Bs. As.: Fox Andina, 2013, ISBN: 9789871857784. - USER
8. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Respecto a las clases: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Respecto a las clases: La cátedra implementará el modelo de aula invertida, en el que los estudiantes adquieren los conocimientos teóricos de mane

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1355 | salida: 14 | total: 1369

---

### Pregunta 7

> - ¿Qué profesor forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes?

**Chunks de contexto:**

1. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Bases de Datos Avanzadas | Pagina: 2]
   > Materia: Bases de Datos Avanzadas Sección: Bases de Datos Avanzadas Equipo docente Trossero, Sebastián Teoría Trossero.sebastian@uader.edu.ar Schmuckler, Jorge Práctica Schmukler.jorge@uader.edu.ar
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: SEDE: Oro Verde | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler. AÑO ACADEMICO: 2023 PLAN DE EST
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio I. FUNDAMENTACIÓN El avance de las tecnologías de la información y la comunicación (TIC) ha t
4. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Días de clase | Pagina: 4]
   > Materia: Bases de Datos Avanzadas Sección: Días de clase Cronograma de clases Presenciales/Virtuales A partir de este año la materia será dictada de manera bimodal. El cronograma será definido en su
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS Oro Verde] Huidobro Moya, José Manuel: Redes de datos y convergencia IP / J. M. Huidobro Moya, Ramón Jesús Millán Tejedor. - M
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 1- PROGRAMA DE CONTENIDOS | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: 1- PROGRAMA DE CONTENIDOS spositivos finales. Conceptos usados en Comunicaciones y Redes: Uso de la redes de computadora, aplicaciones de negocios, domésticas,
7. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos Jorge Trossero. 2022 Modelos vectoriales y redes neuronales artificiales, para la aplicación de procesamiento de lenguaje natural en normativa
8. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Programa Sintético | Unidad I: Bases de Datos Activas | Unidad II: Bases de Datos Temporales | Unidad III: Bases de Datos Geográficas | Unidad IV: Bases de Datos Distribuidas | Unidad V: Datawarehouse | Unidad VI: Datamining | Unidad VII: Bases de Datos Orientadas a Objetos | Pagina: 6]
   > Materia: Bases de Datos Avanzadas Sección: Programa Sintético | Unidad I: Bases de Datos Activas | Unidad II: Bases de Datos Temporales | Unidad III: Bases de Datos Geográficas | Unidad IV: Bases de D

**Respuesta:**

Según el Contexto, tanto en el documento "BDA Planificacion.pdf" como en el documento "Planificación 2025 - Comunicacion y Redes.pdf", Schmuckler, Jorge es mencionado como parte del equipo docente tanto para la materia de Bases de Datos Avanzadas como para la materia de Comunicaciones y Redes.

**Tokens:** entrada: 1433 | salida: 77 | total: 1510

---

### Pregunta 8

> - ¿Qué otra asignatura, además de la propia materia de Inteligencia Artificial, incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. He
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Unidad 2: Relaciones Humanas en el Contexto Organizacional | Pagina: 2]
   > Materia: Informática y Recursos Humanos Sección: Unidad 2: Relaciones Humanas en el Contexto Organizacional 1. Comunicación interna y cultura organizacional en entornos digitales. 2. Inteligencia emo
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Descripción | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Descripción de los temas específicos a desarrollarse en la asignatura.
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Bibliografía Complementaria: | Pagina: 3]
   > Materia: Informática y Recursos Humanos Sección: Bibliografía Complementaria: Reglamento de Teletrabajo en Argentina. Legislación sobre delitos informáticos en Argentina. Artículos académicos sobre l
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Condiciones | Pagina: 3]
   > Materia: Inteligencia Artificial Sección: Condiciones de inicialización, problema de saturación prematura. Regiones de Decisión. Modo de operación autoasociativo. Capítulo X Generalización en
6. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio ectiva multidisciplinaria, integrando conceptos de informática, gestión organizacional y dere
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Composición | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Composición MAX-MIN. Capítulo VII Sistemas Difusos. Consideraciones generales. Representación de conocimiento estructurado mediante reglas lingüísticas.
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Editorial: Pearson Educación (2004 o versiones posteriores) | Pagina: 4]
   > Materia: Inteligencia Artificial Sección: Editorial: Pearson Educación (2004 o versiones posteriores) Título: Aprendizaje automático y aprendizaje profundo con Python, scikit-learn y Tensor Flow-

**Respuesta:**

La asignatura que incluye explícitamente el impacto o uso de la 'Inteligencia Artificial' (IA) es "Informática y Recursos Humanos" mencionada en el "PROGRAMA INFORMATICA Y RRHH.pdf" en la sección "Unidad 2: Relaciones Humanas en el Contexto Organizacional" bajo el punto "El impacto de la inteligencia artificial en la gestión del talento".

**Tokens:** entrada: 1167 | salida: 95 | total: 1262

---

### Pregunta 9

> - Los requisitos para regularizar en Bases de Datos Avanzadas y en Redes y Comunicaciones, ¿son iguales? ¿Qué diferencias tienen?

**Chunks de contexto:**

1. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 9]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Software utilizado PostgreSQL 9.6 o superi
2. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Régimen | Regularidad: | Pagina: 7]
   > Materia: Bases de Datos Avanzadas Sección: Régimen | Regularidad: Asistencia: Según norma vigente. Todos los trabajos prácticos aprobados.
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE cada la ausencia. Evaluación Final: El alumno con condición de REGULAR, deber
4. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Días de clase | Pagina: 3]
   > Materia: Bases de Datos Avanzadas Sección: Días de clase Lunes: 13:30 a 15:30 -> Teoría Viernes: 17:00 a 19:00 -> Práctica NOTA: Los horarios están en proceso de evaluación y pueden sufrir cambios
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Programa Sintético | Unidad I: Bases de Datos Activas | Unidad II: Bases de Datos Temporales | Unidad III: Bases de Datos Geográficas | Unidad IV: Bases de Datos Distribuidas | Unidad V: Datawarehouse | Unidad VI: Datamining | Unidad VII: Bases de Datos Orientadas a Objetos | Pagina: 6]
   > Materia: Bases de Datos Avanzadas Sección: Programa Sintético | Unidad I: Bases de Datos Activas | Unidad II: Bases de Datos Temporales | Unidad III: Bases de Datos Geográficas | Unidad IV: Bases de D
6. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Bases de Datos Avanzadas | Pagina: 2]
   > Materia: Bases de Datos Avanzadas Sección: Bases de Datos Avanzadas Equipo docente Trossero, Sebastián Teoría Trossero.sebastian@uader.edu.ar Schmuckler, Jorge Práctica Schmukler.jorge@uader.edu.ar
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad VII: -Capa de Red- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad VII: -Capa de Red- Enrutamiento Estático, Enrutamiento dinámico. Protocolos de enrutamiento. Aspectos de diseño de la capa de red (Conmutación de paquete
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS Oro Verde] Huidobro Moya, José Manuel: Redes de datos y convergencia IP / J. M. Huidobro Moya, Ramón Jesús Millán Tejedor. - M

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1359 | salida: 14 | total: 1373

---

### Pregunta 10

> - ¿Cuál es el porcentaje de asistencia a clases que exigen en común las materias de Investigación Operativa, Comunicaciones y Redes, y Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% de asistencia a las clases teóricas y prácticas.
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% os a la materia. La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen re
3. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Respecto a las clases: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Respecto a las clases: o pueden asistir a todas las clases y, al mismo tiempo, reducir la tasa de abandono. Por ello, los materiales
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: JIMENA | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: JIMENA CRUZ; Año de la carrera a la que pertenece la cátedra: 4 Régimen de la materia: Anual Carga horaria semanal: 3 horas Correlativa: Ingeniería
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% mientas informáticas utilizadas en la cátedra para la resolución de modelos de optimización y problemas de gestión: - LINDO (Linear, Interactive
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% reconocido por su sintaxis sencilla para ingresar ecuaciones y restricciones de manera directa. - WinQSB 2.0: Una suite clásica (dividida en
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad VII: -Capa de Red- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad VII: -Capa de Red- de igual a igual), RIP protocolo de enrutamiento por clase vector de distancia, configuración, VLSM y CIDR; Algoritmos de control de c
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE Haber realizado y aprobado los dos trabajos práctico impartido por la cátedra.

**Respuesta:**

La materia de Investigación Operativa establece que la asistencia no justificada se considerará como examen reprobado (no se proporciona la condición específica de porcentaje de asistencia).

La materia de Comunicación y Redes especifica que el alumno debe asistir al 80% de las clases teóricas y prácticas para alcanzar la condición de REGULAR.

La materia de Metodología de la Investigación no proporciona información sobre el porcentaje de asistencia solicitado (lo que sugiere que puede no ser un requisito de asistencia concreto).

**Tokens:** entrada: 1303 | salida: 129 | total: 1432

---

### Pregunta 11

> - Si quiero promocionar todas las materias de 4to año, ¿cuál es la diferencia de promedio exigido entre Investigación Operativa e Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: | Pagina: 1]
   > Materia: Investigación Operativa Sección: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: - ALUMNO PROMOCIONADO: El estudiante logrará la promoción directa si alcanza un prom
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación tadísticos mediante una interfaz basada en menús para la carga de datos. - TORA: Herramienta educativa diseñada específicamente para
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% mientas informáticas utilizadas en la cátedra para la resolución de modelos de optimización y problemas de gestión: - LINDO (Linear, Interactive
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% de asistencia a las clases teóricas y prácticas.
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% reconocido por su sintaxis sencilla para ingresar ecuaciones y restricciones de manera directa. - WinQSB 2.0: Una suite clásica (dividida en
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Composición | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Composición MAX-MIN. Capítulo VII Sistemas Difusos. Consideraciones generales. Representación de conocimiento estructurado mediante reglas lingüísticas.
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Agentes | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Agentes que aprenden. Capítulo II Procesos de Búsqueda. Representación en un espacio de estados. Búsqueda Ciega, definición; búsqueda primero en amplitud,
8. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas s

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1153 | salida: 14 | total: 1167

---

### Pregunta 12

> - ¿Qué herramientas de software se recomiendan en la carrera para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% mientas informáticas utilizadas en la cátedra para la resolución de modelos de optimización y problemas de gestión: - LINDO (Linear, Interactive
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible vía URL que
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% reconocido por su sintaxis sencilla para ingresar ecuaciones y restricciones de manera directa. - WinQSB 2.0: Una suite clásica (dividida en
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Problema | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Problema de separación lineal. Aplicaciones.
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio ectiva multidisciplinaria, integrando conceptos de informática, gestión organizacional y dere
6. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos én Orlando Almada; director Alejandro Javier Hadad. 2018 Herramientas ágiles utilizadas en el desarrollo de software aplicando modelos de cali
7. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Sistema de evaluación: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Sistema de evaluación: ablecidas en el cronograma académico. Programa de trabajos prácticos: Tp 1: Escritura académica. Se solicita a los estudi
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad II: -Capa física concepto y medios- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad II: -Capa física concepto y medios- colisiones). Switches (ancho de banda dedicado a cada puerto, entorno libre de colisiones, operación full-duplex, tab

**Respuesta:**

La respuesta está dada en el Documento "PROGRAMA - Investigación Operativa.pdf" y es el siguiente:

- LINDO (Linear, Interactive, and Discrete Optimizer): Software especializado en la resolución de problemas de programación lineal, entera y no lineal.

PHP Simplex: Herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el algoritmo de Simplex.

WinQSB 2.0: Una suite clásica que abarca múltiples módulos de resolución de problemas de optimización lineal.

Las herramientas de software se relacionan con las unidades teóricas de Investigación Operativa, específicamente con el tema de optimización lineal y problemas de gestión.

**Tokens:** entrada: 1203 | salida: 164 | total: 1367

---

### Pregunta 13

> - ¿Dónde puedo descargar la materia de Cálculo de 1er año?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS oria Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] Cisco Systems: Acad
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Nacional | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Nacional - APRENDER A INVESTIGAR: https://youtu.be/9oWM50RDsLQ -> BÚSQUEDA AVANZADA GOOGLE - BÚSQUEDA GOOGLE AVANZADA - 2DA PARTE APRENDER A INVESTIG
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad II: -Capa física concepto y medios- | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: Unidad II: -Capa física concepto y medios- munal, Internet a través de cable, asignación de espectro, modem de cable, ADSL en comparación con el cable). Unidad
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: UNIVERSIDAD AUTÓNOMA DE ENTRE RÍOS | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: UNIVERSIDAD AUTÓNOMA DE ENTRE RÍOS FACULTAD DE CIENCIA Y TECNOLOGÍA PROGRAMA DE CÁTEDRA: INFORMÁTICA Y RELACIONES HUMANAS
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: JIMENA | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: JIMENA CRUZ; Año de la carrera a la que pertenece la cátedra: 4 Régimen de la materia: Anual Carga horaria semanal: 3 horas Correlativa: Ingeniería
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Primer | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Primer Orden.
7. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Bibliografía Nacional: | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Bibliografía Nacional: Ley de Teletrabajo (Ley 27.555).
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: (Método | Pagina: 1]
   > Materia: Investigación Operativa Sección: (Método recursiva de los cálculos: etapas, estados, decisiones y principio de optimalidad de Bellman.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1157 | salida: 14 | total: 1171

---

### Pregunta 14

> - El profesor Ing. Jorge L. Schmukler da clases en Bases de Datos Avanzadas, en Inteligencia Artificial y en Redes y Comunicaciones.

**Chunks de contexto:**

1. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Bases de Datos Avanzadas | Pagina: 2]
   > Materia: Bases de Datos Avanzadas Sección: Bases de Datos Avanzadas Equipo docente Trossero, Sebastián Teoría Trossero.sebastian@uader.edu.ar Schmuckler, Jorge Práctica Schmukler.jorge@uader.edu.ar
2. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Unidad IV: Bases de Datos Distribuidas Parcial | Unidad V: Datawarehouse Parcial | Pagina: 6]
   > Materia: Bases de Datos Avanzadas Sección: Unidad IV: Bases de Datos Distribuidas Parcial | Unidad V: Datawarehouse Parcial Unidad VI: Datamining Parcial + TP Unidad VII: Bases de Datos OO Parcial NO
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: SEDE: Oro Verde | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler. AÑO ACADEMICO: 2023 PLAN DE EST
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Principal (Disponibles en biblioteca) | Pagina: 4]
   > Materia: Inteligencia Artificial Sección: Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig.
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Clases | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Clases e instancias.
6. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Respecto a las clases: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Respecto a las clases: La cátedra implementará el modelo de aula invertida, en el que los estudiantes adquieren los conocimientos teóricos de mane
7. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio I. FUNDAMENTACIÓN El avance de las tecnologías de la información y la comunicación (TIC) ha t
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad VII: -Capa de Red- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad VII: -Capa de Red- ciones. División de subredes (por clase y vlsm (mascara de subred de longitud variable)), icmpv4 (Internet Control Message Protocol -

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1220 | salida: 14 | total: 1234

---

### Pregunta 15

> - ¿Cuál es el costo de la certificación oficial de Cisco que se menciona como opcional en la planificación?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Sitios web sobre normativas, tecnologías y soluciones, opcional: | Pagina: 5]
   > Materia: Comunicacion y Redes Sección: Sitios web sobre normativas, tecnologías y soluciones, opcional: IETF -> www.ietf.org IEEE -> www.ieee.org ISO -> www.iso.org CISCO -> www.cisco.com IANA -> www
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS oria Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] Cisco Systems: Acad
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas s
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% os a la materia. La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen re
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Bibliografía Nacional: | Pagina: 2]
   > Materia: Informática y Recursos Humanos Sección: Bibliografía Nacional: Ley Nacional de Protección de Datos Personales (Ley 25.326). Código Civil y Comercial de la Nación (aspectos relacionados con c
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE El alumno accederá a la condición de PROMOCIÓN si cumple con las siguientes co
7. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 9]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Software utilizado PostgreSQL 9.6 o superi
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad II: -Capa física concepto y medios- | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: Unidad II: -Capa física concepto y medios- espera, Protocolo símplex para un canal con ruido, Protocolo de ventana corrediza). Protocolo enlace de datos (HDLC -

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1397 | salida: 14 | total: 1411

---

### Pregunta 16

> - Para la Promoción Directa, se exige la aprobación de la totalidad de los trabajos prácticos (TP 1 al TP 5). ¿Cuál es la calificación numérica mínima que debe obtenerse en cada TP individual para que se considere aprobado?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos nales y libres: a. Promoción Directa Para acceder a la condición de Promoción Directa, el/la estudiante deberá cumplir con los siguientes requ
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos l o superior a 75 (setenta y cinco) puntos. - Entrega de la totalidad de los trabajos prácticos en tiempo y forma. - Pertinencia, coherencia y
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% requisito indispensable la entrega y aprobación de los dos trabajos prácticos obligatorios y el cumplimiento del
4. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 9]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Software utilizado PostgreSQL 9.6 o superi
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos ir una instancia de evaluación teórica oral y realizar la defensa oral del trabajo práctico integrador. La calificación del traba
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos
7. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Régimen | Regularidad: | Pagina: 7]
   > Materia: Bases de Datos Avanzadas Sección: Régimen | Regularidad: Asistencia: Según norma vigente. Todos los trabajos prácticos aprobados.
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE cada la ausencia. Evaluación Final: El alumno con condición de REGULAR, deber

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1312 | salida: 14 | total: 1326

---

### Pregunta 17

> - ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible vía URL que
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% mientas informáticas utilizadas en la cátedra para la resolución de modelos de optimización y problemas de gestión: - LINDO (Linear, Interactive
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Problema | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Problema de separación lineal. Aplicaciones.
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Metodología | Pagina: 1]
   > Materia: Investigación Operativa Sección: Metodología de la construcción de modelos: definición del problema, construcción del modelo matemático, obtención de una solución y validaci
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Reactivo | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Reactivo Simple.
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad X -Dirección IPv6- | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: Unidad X -Dirección IPv6- io para compartir archivos, snmp, netbios, ipp -internet printing protocol-, lpd -line printer daemon protocol-). Resolución básica de
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE cha del examen en forma escrita de los conceptos teóricos, una prueba teórica
8. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos én Orlando Almada; director Alejandro Javier Hadad. 2018 Herramientas ágiles utilizadas en el desarrollo de software aplicando modelos de cali

**Respuesta:**

Lo siento, pero no dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1019 | salida: 19 | total: 1038

---

### Pregunta 18

> - ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% utomáticamente a la nota del examen original. Protocolos de Evaluación: Los resultados se publicarán en un plazo de siete días corridos tras la
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mismo
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% de asistencia a las clases teóricas y prácticas.
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 15 18 de junio Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 15 18 de junio Virtual Teoría r posibilidad 26 15 de octubre Virtual Tutorías 27 22 de octubre Virtual Tutorías
6. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos ación y defensa oral del trabajo práctico integrador en la mesa de examen final, previa instancia de revisión y devolución con el equip
7. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Días de clase | Pagina: 3]
   > Materia: Bases de Datos Avanzadas Sección: Días de clase Lunes: 13:30 a 15:30 -> Teoría Viernes: 17:00 a 19:00 -> Práctica NOTA: Los horarios están en proceso de evaluación y pueden sufrir cambios
8. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Días de clase | Pagina: 4]
   > Materia: Bases de Datos Avanzadas Sección: Días de clase Cronograma de clases Presenciales/Virtuales A partir de este año la materia será dictada de manera bimodal. El cronograma será definido en su

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1146 | salida: 14 | total: 1160

---

## Conversacion 5

**Puntaje evaluado: 9.5 / 18**

**Parametros modificados respecto a la conversacion anterior:**

| Parametro | Valor |
|---|---|
| chunk_size | 500 |
| chunk_overlap | 100 |
| chunking_technique | recursive |
| refresh | True |

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

La información proporcionada en el Contexto no describe de manera explícita los contenidos de la materia Inteligencia Artificial. Sin embargo, hay referencias a varias secciones relacionadas con la materia en varios documentos.

Por ejemplo, se menciona la sección "Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes", lo que podría sugerir que se trata de contenidos relacionados con la introducción a la inteligencia artificial, definiciones y objetivos, herramientas y técnicas, agentes inteligentes, etc.

Asimismo, la sección "Descripción de los temas específicos a desarrollarse en la asignatura" podría ofrecer una visión general de los contenidos que se cubrirán en la materia.

Sin embargo, para dar una respuesta más precisa a la pregunta, sería necesario consultar la sección "Descripción de los temas específicos a desarrollarse en la asignatura" en el documento correspondiente.

**Tokens:** entrada: 982 | salida: 203 | total: 1185

---

### Pregunta 2

> - ¿En qué materia se enseña el concepto de Lógica Difusa?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Capítulo VI | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Capítulo VI Lógica Difusa (Fuzzy). Consideraciones generales, Conjuntos Difusos, definición.
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Procesos | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Procesos basadas en Lógica.
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad II: -Capa física concepto y medios- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad II: -Capa física concepto y medios- Protocolo libre de colisiones, Protocolo de LAN Inalámbricas), Ethernet, concepto sobre el Algoritmo de retroceso exp
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Respecto a las clases: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Respecto a las clases: La cátedra implementará el modelo de aula invertida, en el que los estudiantes adquieren los conocimientos teóricos de mane
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio . FUNDAMENTACIÓN El avance de las tecnologías de la información y la comunicación (TIC) ha tr
6. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos Deep Learning aplicado al aprendizaje automático de ontologías para la representación del conocimiento a partir de texto no estructurado / Enz
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al
8. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Nacional | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Nacional : https://youtu.be/9oWM50RDsLQ -> BÚSQUEDA AVANZADA GOOGLE - BÚSQUEDA GOOGLE AVANZADA - 2DA PARTE APRENDER A INVESTIGAR: https://youtu.be/eH

**Respuesta:**

La materia en la que se enseña el concepto de Lógica Difusa es la "Inteligencia Artificial".

**Tokens:** entrada: 1511 | salida: 27 | total: 1538

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

El plan de estudios de Metodología de la Investigación incluye los siguientes temas y actividades:

- Presentación de la asignatura
- Introducción a los conceptos generales de la metodología de la investigación
- Normas APA/escritura académica
- Tema/problema
- Pregunta de investigación (variables, unidad de análisis, contexto)/ Antecedentes
- Seleccionar un artículo de investigación sobre un tema de interés específico relacionado con el campo profesional
- Tipos de diseños cuantitativos o cualitativos
- Estrategias de indagación según la perspectiva metodológica seleccionada
- Universo de análisis y población
- Análisis de los datos en la investigación: teorías y métodos
- Presentación de un trabajo práctico integrador final, que incluye la entrega de las actividades prácticas y la aprobación del trabajo final.

Los objetivos generales de la asignatura son brindar conocimientos y herramientas para indagar la realidad en la búsqueda y desnaturalización de problemas.

**Tokens:** entrada: 1616 | salida: 236 | total: 1852

---

### Pregunta 4

> - En Comunicaciones y Redes, ¿cómo hago para quedar como alumno regular?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE El alumno accederá a la condición de REGULAR, si cumple con las siguientes con
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos . Guillerón. 2018 Red Privada Virtual (VPM) sobre Protocolo de Internet versión 6 (IPv6) / Rodrigo Paúl Basso, Maximiliano Sebastián Toso; dir
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: SEDE: Oro Verde | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler. AÑO ACADEMICO: 2023 PLAN DE EST
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 8]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Comunicación De rutina y consultas: Lista
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad VII: -Capa de Red- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad VII: -Capa de Red- ; Algoritmos de enrutamiento (Principio de optimización, Enrutamiento por la ruta más corta, Inundación, Enrutamiento por vector de di
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS . As.: Fox Andina, 2013, ISBN: 9789871857784. - USERS. [Disponible en Biblioteca FCyT- Oro Verde] Curso visual y práctico: Adm

**Respuesta:**

Para quedar como alumno regular en Comunicaciones y Redes, debes cumplir con las siguientes condiciones: 

1. En los 3 parciales, obtener una calificación promedio superior o igual a los 60 puntos, según se indica en el Documento "Planificación 2025 - Comunicacion y Redes.pdf".

Además, se menciona en el Documento "Planificación 2025 - Comunicacion y Redes.pdf" que, para obtener la regularidad, también deben ser aprobados 2 trabajos Prácticos desarrollados en el horario de clase, pero este detalle no se explicita en ningún otro documento de los consultados, por lo que no puedo confirmar la importancia de cumplir con estos dos trabajos para quedar como alumno regular.

**Tokens:** entrada: 1607 | salida: 168 | total: 1775

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

La información proporcionada en el Contexto menciona que la cátedra de Investigación Operativa dispone de dos oportunidades de recuperatorio totales.

**Tokens:** entrada: 1119 | salida: 33 | total: 1152

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

No dispongo de información en mis documentos sobre el software TORA.

**Tokens:** entrada: 1604 | salida: 15 | total: 1619

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

El profesor que forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes es Jorge L. Schmukler.

**Tokens:** entrada: 1238 | salida: 42 | total: 1280

---

### Pregunta 8

> - ¿Qué otra asignatura, además de la propia materia de Inteligencia Artificial, incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. He
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Unidad 2: Relaciones Humanas en el Contexto Organizacional | Pagina: 2]
   > Materia: Informática y Recursos Humanos Sección: Unidad 2: Relaciones Humanas en el Contexto Organizacional 1. Comunicación interna y cultura organizacional en entornos digitales. 2. Inteligencia emo
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Descripción | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Descripción de los temas específicos a desarrollarse en la asignatura.
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Bibliografía Nacional: | Pagina: 2]
   > Materia: Informática y Recursos Humanos Sección: Bibliografía Nacional: Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Condiciones | Pagina: 3]
   > Materia: Inteligencia Artificial Sección: Condiciones de inicialización, problema de saturación prematura. Regiones de Decisión. Modo de operación autoasociativo. Capítulo X Generalización en
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Editorial: Pearson Educación (2004 o versiones posteriores) | Pagina: 4]
   > Materia: Inteligencia Artificial Sección: Editorial: Pearson Educación (2004 o versiones posteriores) Título: Aprendizaje automático y aprendizaje profundo con Python, scikit-learn y Tensor Flow-
7. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio . Además, se abordarán aspectos legales fundamentales para comprender el impacto normativo de
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Associative | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Associative Memories).

**Respuesta:**

La otra asignatura que incluye explícitamente el impacto o uso de la "Inteligencia artificial" (IA) dentro de sus unidades temáticas es Informática y Recursos Humanos, como se desprende de la siguiente información.

En el DOCUMENTO: PROGRAMA INFORMATICA Y RRHH.pdf, sección Unidad 2: Relaciones Humanas en el Contexto Organizacional, se puede leer: "4. El impacto de la inteligencia artificial en la gestión del talento."

Además, en el mismo DOCUMENTO: PROGRAMA INFORMATICA Y RRHH.pdf, sección Bibliografía Nacional: se menciona la siguiente obra: "Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales" de Gonzalo Ana Dobratinich, "Derecho y nuevas tecnologías".

**Tokens:** entrada: 1060 | salida: 186 | total: 1246

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

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1416 | salida: 14 | total: 1430

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

La información proporcionada en el Contexto indica que las materias de Investigación Operativa y Metodología de la Investigación exigen el 80% de asistencia a clases para ser considerados estudiantes regulares, como se menciona en los documentos "PROGRAMA - Investigación Operativa.pdf" y "PROGRAMA- Metodología de la Investigación.docx.pdf".

No se proporciona información específica en el Contexto sobre las materias de Comunicaciones y Redes y su requisito de asistencia.

**Tokens:** entrada: 1424 | salida: 109 | total: 1533

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

**Tokens:** entrada: 1210 | salida: 14 | total: 1224

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

En la materia de Investigación Operativa, se recomienda utilizar LINDO (Linear, Interactive, and Discrete Optimizer) para resolver problemas de programación lineal, entera y no lineal.

Asimismo, se puede mencionar que PHP Simplex es una herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el método del Simplex.

En la carrera, se incorpora el uso de herramientas de software para enfrentar los desafíos que conlleva la práctica profesional y la investigación científica.

La relación con las unidades teóricas, en particular con la Unidad VII sobre la Capa de Red, es que enrutamiento de redes puede implicar el uso de técnicas de optimización, como por ejemplo el algoritmo de enrutamiento más corto.

**Tokens:** entrada: 1360 | salida: 179 | total: 1539

---

### Pregunta 13

> - ¿Dónde puedo descargar la materia de Cálculo de 1er año?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS 4- BIBLIOGRAFIA Obligatoria Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Ver
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Nacional | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Nacional en https://ediciones.ungs.edu.ar/wp-content/uploads/2018/09/9789876301190-completo.pdf
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas s
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Primer | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Primer Orden.
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Bibliografía Nacional: | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Bibliografía Nacional: Ley de Teletrabajo (Ley 27.555).
6. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio I
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: (Método | Pagina: 1]
   > Materia: Investigación Operativa Sección: (Método recursiva de los cálculos: etapas, estados, decisiones y principio de optimalidad de Bellman.
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad II: -Capa física concepto y medios- | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: Unidad II: -Capa física concepto y medios- . Protocolo enlace de datos (HDLC -Control de enlace de datos de alto nivel-, Capa de enlace de datos en Internet -Pr

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1083 | salida: 14 | total: 1097

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

Lo siento, pero no dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1245 | salida: 19 | total: 1264

---

### Pregunta 15

> - ¿Cuál es el costo de la certificación oficial de Cisco que se menciona como opcional en la planificación?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS 4- BIBLIOGRAFIA Obligatoria Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Ver
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Sitios web sobre normativas, tecnologías y soluciones, opcional: | Pagina: 5]
   > Materia: Comunicacion y Redes Sección: Sitios web sobre normativas, tecnologías y soluciones, opcional: IETF -> www.ietf.org IEEE -> www.ieee.org ISO -> www.iso.org CISCO -> www.cisco.com IANA -> www
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas s
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad II: -Capa física concepto y medios- | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: Unidad II: -Capa física concepto y medios- : -Capa de enlace de dato -sub capa LLC (control de enlace lógico)- Cuestiones en el diseño de la capa de enlace de d
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% la evaluación. Los exámenes se desarrollarán estrictamente en los bloques horarios asignados a la materia. La ausencia no justificada
6. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 9]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Software utilizado PostgreSQL 9.6 o superi
7. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos . 2019 Estrategia para planear una migración de software propietario a software libre para la Facultad de Ciencia y Tecnología (FCyT) Sede Oro
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE El alumno accederá a la condición de REGULAR, si cumple con las siguientes con

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta. La información proporcionada solo menciona la existencia de una "Guía del primer año" de Cisco Systems, pero no se menciona el costo de ninguna certificación oficial.

**Tokens:** entrada: 1537 | salida: 50 | total: 1587

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

**Tokens:** entrada: 1501 | salida: 14 | total: 1515

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

Lo siento, pero no dispongo de información en mis documentos para responder esta consulta sobre cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel. La información proporcionada se refiere a herramientas y métodos para la resolución de problemas de programación lineal, como PHP Simplex y LINDO, pero no incluye instrucciones específicas sobre cómo usar estos métodos dentro de Excel.

**Tokens:** entrada: 1029 | salida: 92 | total: 1121

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

**Tokens:** entrada: 1412 | salida: 14 | total: 1426

---

## Conversacion 6

**Puntaje evaluado: 10 / 18**

**Parametros modificados respecto a la conversacion anterior:**

| Parametro | Valor |
|---|---|
| chunk_size | 600 |

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

Según el Contexto, los contenidos de la materia Inteligencia Artificial están descritos en los siguientes apartados:

1.  Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes: Introducción a la IA. Definiciones y objetivos. Herramientas y técnicas provistas por el área IA.
2.  Descripción: temas específicos a desarrollarse en la asignatura.
3.  Métodos y mensajes: Representación de Conocimientos mediante reglas. Estructura básica. Representación de reglas mediante objetos.
4.  Integración: solución difusa final. Proceso de Defuzzificación. Agentes Basados en Lógica Difusa.
5.  Adquisición de Conocimiento: Base de Conocimientos, características generales.
6.  Condiciones de inicialización, problema de saturación prematura. Regiones de Decisión. Modo de operación autoasociativo.
7.  Associative Memories).
8.  Adquisición: Estructura de Control. Procedimientos de Inferencia. Interfase con el usuario. Memoria de Trabajo. Módulo generador de explicaciones al usuario.
9.  Capítulo V Funcionalidad de los Sistemas Expertos: Procesos de inferencia: Encadenamiento hacia adelante.

**Tokens:** entrada: 982 | salida: 292 | total: 1274

---

### Pregunta 2

> - ¿En qué materia se enseña el concepto de Lógica Difusa?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Capítulo VI | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Capítulo VI Lógica Difusa (Fuzzy). Consideraciones generales, Conjuntos Difusos, definición.
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Integración | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Procesos | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Procesos basadas en Lógica.
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad VII: -Capa de Red- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad VII: -Capa de Red- . Clase de direccionamiento (clase a, b, c, d y e). Prefijo y Mascara de red. Lógica de and. Calculo de direcciones. División de subre
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Respecto a las clases: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Respecto a las clases: La cátedra implementará el modelo de aula invertida, en el que los estudiantes adquieren los conocimientos teóricos de mane
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% a la materia. La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen reprob
7. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio I. FUNDAMENTACIÓN El avance de las tecnologías de la información y la comunicación (TIC) ha t
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Editorial: Pearson Educación (2004 o versiones posteriores) | Pagina: 4]
   > Materia: Inteligencia Artificial Sección: Editorial: Pearson Educación (2004 o versiones posteriores) Título: Aprendizaje automático y aprendizaje profundo con Python, scikit-learn y Tensor Flow-

**Respuesta:**

La materia en la que se enseña el concepto de Lógica Difusa es la Inteligencia Artificial.

**Tokens:** entrada: 1406 | salida: 26 | total: 1432

---

### Pregunta 3

> - ¿Cuál es el plan de estudios de Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: JIMENA | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: JIMENA CRUZ; Año de la carrera a la que pertenece la cátedra: 4 Régimen de la materia: Anual Carga horaria semanal: 3 horas Correlativa: Ingeniería
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 1 12 de marzo Presencial Teórico/práctico Presentación de la asignatura | 2 19 de marzo Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 1 12 de marzo Presencial Teórico/práctico Presentación de la asignatura | 2 19 de marzo Virtual Teoría Conceptos generales para introducción 3 26 de
3. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Metodología | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Metodología brindar conocimientos y herramientas para indagar la realidad en la búsqueda y desnaturalización de problemas, tanto del
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Estructura del aula virtual: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Estructura del aula virtual: Los materiales educativos estarán alojados en el aula virtual "Metodología de la Investigación" dentro de la plataform
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Sistema de evaluación: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Sistema de evaluación: examen contará con una (1) instancia de recuperación, conforme al cronograma establecido por la cátedra. - Entre
6. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Unidad 3: La dimensión de la estrategia general de investigación | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Unidad 3: La dimensión de la estrategia general de investigación ¿Cómo se va a estudiar el problema? Tipo de diseños cuantitativos o cualitativos. La
7. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Cronograma de trabajo | METODOLOGÍA DE LA INVESTIGACIÓN- 2026 | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Cronograma de trabajo | METODOLOGÍA DE LA INVESTIGACIÓN- 2026 Clase FECHA Tipo de encuentro Tipo encuentro Tema
8. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Nacional | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Nacional en https://ediciones.ungs.edu.ar/wp-content/uploads/2018/09/9789876301190-completo.pdf

**Respuesta:**

El plan de estudios de Metodología de la Investigación incluye los siguientes temas y actividades, según el programa proporcionado:

*   Sección: 1 y 2
    Temas:
        *   Presentación de la asignatura (12 de marzo presencial teórico/práctico)
        *   Conceptos generales para introducción (19 de marzo virtual)
        *   Normas APA/ escritura académica (3 de abril virtual)
        *   Tema/problema (9 de abril presencial teórico)
        *   Pregunta de investigación (variables, unidad de análisis, contexto)/ Antecedentes (16 de abril virtual)
        *   Pregunta de investigación (variables, unidad de análisis, contexto)/ Antecedentes (23 de abril virtual)
*   Sección: Metodología
    Temas:
        *   Brindar conocimientos y herramientas para indagar la realidad en la búsqueda y desnaturalización de problemas, tanto del entorno académico, cotidiano, productivo y organizacional.
    Objetivos generales:
        *   Acercar al campo de la investigación científica desde espacios de reflexión sistemáticos enmarcados en trabajos propios de la disciplina y el campo profesional.
    Objetivos específicos:
        *   Promover el reconocimiento de aspectos metodológicos de la investigación caracterizando las instancias y fases del proceso de investigación cualitativa y cuantitativa.
*   Sección: Estructura del aula virtual:
    Los materiales educativos estarán alojados en el aula virtual "Metodología de la Investigación" dentro de la plataforma Moodle.
    La organización será la siguiente:
        *   Inicio del curso: contendrá información general de la cátedra, incluyendo el programa, el equipo docente, el cronograma, los objetivos, los materiales utilizados, el enlace de videoconferencia, la descripción de la metodología de trabajo y evaluación, la bibliografía y un foro de discusión.
*   Sección: Sistema de evaluación:
    El examen contará con una (1) instancia de recuperación, conforme al cronograma establecido por la cátedra.
    La entrega obligatoria de las actividades prácticas y la aprobación del trabajo práctico integrador final, respetando las fechas establecidas en el cronograma académico.

No dispongo de información en mis documentos para responder esta consulta: El resto de actividades del plan de estudios no se especifican en los fragmentos recuperados.

**Tokens:** entrada: 1735 | salida: 565 | total: 2300

---

### Pregunta 4

> - En Comunicaciones y Redes, ¿cómo hago para quedar como alumno regular?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE El alumno accederá a la condición de REGULAR, si cumple con las siguientes con
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos . 2018 Requisitos para rendir como estudiantes regulares, promocionales y libres: a. Promoción Directa Para acceder a la condición de Promoció
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: SEDE: Oro Verde | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler. AÑO ACADEMICO: 2023 PLAN DE EST
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 8]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Comunicación De rutina y consultas: Lista
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 1- PROGRAMA DE CONTENIDOS | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: 1- PROGRAMA DE CONTENIDOS . Explicar el propósito de IOS como Sistema Operativo de red, Explicar cómo acceder al IOS y cómo explorarlo para configurar los dispo
8. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos . 2018 Implementación de Bases de Datos NOSQL / Rubén Orlando Almada; director Alejandro Javier Hadad. 2018 Herramientas ágiles utilizadas en

**Respuesta:**

Según el Documento "Planificación 2025 - Comunicacion y Redes.pdf" (Sección: 2- SISTEMA DE EVALUACIÓN), para quedar como alumno regular en Comunicaciones y Redes, debes cumplir con las siguientes condiciones de cátedra:

1. Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos.

Además, según el Documento "Planificación 2025 - Comunicacion y Redes.pdf" (Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS), también es necesario aprobar los dos trabajos prácticos que se realizan en el horario de clase.

**Tokens:** entrada: 1612 | salida: 153 | total: 1765

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
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% a la materia. La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen reprob
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: PL: | Pagina: 1]
   > Materia: Investigación Operativa Sección: PL: región factible, búsqueda de la solución óptima en los vértices, análisis de casos especiales (soluciones múltiples, soluciones no acot
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% de asistencia a las clases teóricas y prácticas.
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% reconocido por su sintaxis sencilla para ingresar ecuaciones y restricciones de manera directa. - WinQSB 2.0: Una suite clásica (dividida en

**Respuesta:**

La cátedra de Investigación Operativa dispone de dos oportunidades de recuperatorio totales.

**Tokens:** entrada: 1205 | salida: 22 | total: 1227

---

### Pregunta 6

> - ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% a la materia. La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen reprob
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Alejandra, | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Alejandra, los contenidos teóricos previstos en el programa, a fin de que el segundo cuatrimestre esté destinado de manera priorita
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio . Además, se abordarán aspectos legales fundamentales para comprender el impacto normativo de
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 1- PROGRAMA DE CONTENIDOS | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: 1- PROGRAMA DE CONTENIDOS . Hardware de redes, Sistema Cliente/Servidor, tipos de redes LAN, MAN, WAN, redes inalámbricas, redes domesticas, topologías. Softwar
7. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 15 18 de junio Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 15 18 de junio Virtual Teoría 17 de septiembre Teoría Coloquio Avances proyectos a la cátedra- Grupos Jimena 24 de septiembre Virtual Tutorías 24 01
8. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos Deep Learning aplicado al aprendizaje automático de ontologías para la representación del conocimiento a partir de texto no estructurado / Enz

**Respuesta:**

Según el Contexto, el software TORA es una herramienta educativa diseñada específicamente para el aprendizaje de la Investigación Operativa. Sin embargo, en el documento "PROGRAMA - Investigación Operativa.pdf" no se proporcionan detalles específicos sobre los módulos que incluye el software TORA.

**Tokens:** entrada: 1626 | salida: 69 | total: 1695

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
6. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio I. FUNDAMENTACIÓN El avance de las tecnologías de la información y la comunicación (TIC) ha t
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 1- PROGRAMA DE CONTENIDOS | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: 1- PROGRAMA DE CONTENIDOS . Hardware de redes, Sistema Cliente/Servidor, tipos de redes LAN, MAN, WAN, redes inalámbricas, redes domesticas, topologías. Softwar
8. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos . 2020 Domótica aplicada en ambientes educativos / Francisco Gastón Gregorutti, Dante Emanuel Tortul Cuatrín; director José Luis Mengarelli. 2

**Respuesta:**

El profesor que forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes es Jorge L. Schmukler.

**Tokens:** entrada: 1452 | salida: 42 | total: 1494

---

### Pregunta 8

> - ¿Qué otra asignatura, además de la propia materia de Inteligencia Artificial, incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. He
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Unidad 2: Relaciones Humanas en el Contexto Organizacional | Pagina: 2]
   > Materia: Informática y Recursos Humanos Sección: Unidad 2: Relaciones Humanas en el Contexto Organizacional 1. Comunicación interna y cultura organizacional en entornos digitales. 2. Inteligencia emo
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Descripción | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Descripción de los temas específicos a desarrollarse en la asignatura.
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Bibliografía Nacional: | Pagina: 2]
   > Materia: Informática y Recursos Humanos Sección: Bibliografía Nacional: Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Condiciones | Pagina: 3]
   > Materia: Inteligencia Artificial Sección: Condiciones de inicialización, problema de saturación prematura. Regiones de Decisión. Modo de operación autoasociativo. Capítulo X Generalización en
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Editorial: Pearson Educación (2004 o versiones posteriores) | Pagina: 4]
   > Materia: Inteligencia Artificial Sección: Editorial: Pearson Educación (2004 o versiones posteriores) Título: Aprendizaje automático y aprendizaje profundo con Python, scikit-learn y Tensor Flow-
7. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio . Además, se abordarán aspectos legales fundamentales para comprender el impacto normativo de
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Associative | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Associative Memories).

**Respuesta:**

La materia "Informática y Recursos Humanos" en el documento "PROGRAMA INFORMATICA Y RRHH.pdf" incluye explícitamente el impacto o uso de la Inteligencia Artificial (IA) dentro de sus unidades temáticas, específicamente en la Unidad 2: Relaciones Humanas en el Contexto Organizacional, en el punto 4: "El impacto de la inteligencia artificial en la gestión del talento".

**Tokens:** entrada: 1060 | salida: 97 | total: 1157

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
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos . 2018 Implementación de Bases de Datos NOSQL / Rubén Orlando Almada; director Alejandro Javier Hadad. 2018 Herramientas ágiles utilizadas en
6. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Programa Sintético | Unidad I: Bases de Datos Activas | Unidad II: Bases de Datos Temporales | Unidad III: Bases de Datos Geográficas | Unidad IV: Bases de Datos Distribuidas | Unidad V: Datawarehouse | Unidad VI: Datamining | Unidad VII: Bases de Datos Orientadas a Objetos | Pagina: 6]
   > Materia: Bases de Datos Avanzadas Sección: Programa Sintético | Unidad I: Bases de Datos Activas | Unidad II: Bases de Datos Temporales | Unidad III: Bases de Datos Geográficas | Unidad IV: Bases de D
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad II: -Capa física concepto y medios- | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: Unidad II: -Capa física concepto y medios- . Protocolo enlace de datos (HDLC -Control de enlace de datos de alto nivel-, Capa de enlace de datos en Internet -Pr
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS . F. Arena. - Buenos Aires: Gradi, 2010. ISBN 9789872601386 [Disponible en Biblioteca FCyT- Oro Verde] Graziani, Rick: Concept

**Respuesta:**

No dispongo de información en mis documentos para comparar los requisitos de regularización en ambas materias.

**Tokens:** entrada: 1640 | salida: 24 | total: 1664

---

### Pregunta 10

> - ¿Cuál es el porcentaje de asistencia a clases que exigen en común las materias de Investigación Operativa, Comunicaciones y Redes, y Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% de asistencia a las clases teóricas y prácticas.
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% a la materia. La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen reprob
3. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Respecto a las clases: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Respecto a las clases: y desarrollo de ejercicios vinculados con la construcción progresiva del anteproyecto de investigación. Esta meto
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: JIMENA | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: JIMENA CRUZ; Año de la carrera a la que pertenece la cátedra: 4 Régimen de la materia: Anual Carga horaria semanal: 3 horas Correlativa: Ingeniería
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% reconocido por su sintaxis sencilla para ingresar ecuaciones y restricciones de manera directa. - WinQSB 2.0: Una suite clásica (dividida en
6. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos . 2018 Requisitos para rendir como estudiantes regulares, promocionales y libres: a. Promoción Directa Para acceder a la condición de Promoció
7. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos . 2018 Implementación de Bases de Datos NOSQL / Rubén Orlando Almada; director Alejandro Javier Hadad. 2018 Herramientas ágiles utilizadas en
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 1- PROGRAMA DE CONTENIDOS | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: 1- PROGRAMA DE CONTENIDOS . Hardware de redes, Sistema Cliente/Servidor, tipos de redes LAN, MAN, WAN, redes inalámbricas, redes domesticas, topologías. Softwar

**Respuesta:**

La información proporcionada sobre las materias de Investigación Operativa, Metodología de la Investigación y Comunicaciones y Redes muestra que el porcentaje de asistencia a clases requerido es de 80% en ambas materias que tenemos documentadas: Investigación Operativa y Metodología de la Investigación.

Sin embargo, la información sobre la materia de Comunicaciones y Redes es incompleta en lo que respecta a los requisitos de asistencia a clases.

**Tokens:** entrada: 1664 | salida: 103 | total: 1767

---

### Pregunta 11

> - Si quiero promocionar todas las materias de 4to año, ¿cuál es la diferencia de promedio exigido entre Investigación Operativa e Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: | Pagina: 1]
   > Materia: Investigación Operativa Sección: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: - ALUMNO PROMOCIONADO: El estudiante logrará la promoción directa si alcanza un prom
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% a la materia. La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen reprob
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mismo
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% de asistencia a las clases teóricas y prácticas.
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% reconocido por su sintaxis sencilla para ingresar ecuaciones y restricciones de manera directa. - WinQSB 2.0: Una suite clásica (dividida en
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Agentes | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Agentes que aprenden. Capítulo II Procesos de Búsqueda. Representación en un espacio de estados. Búsqueda Ciega, definición; búsqueda primero en amplitud,
7. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas s
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Integración | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1413 | salida: 14 | total: 1427

---

### Pregunta 12

> - ¿Qué herramientas de software se recomiendan en la carrera para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% a la materia. La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen reprob
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Investigación | Pagina: 2]
   > Materia: Investigación Operativa Sección: Investigación modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible vía URL que
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Problema | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Problema de separación lineal. Aplicaciones.
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad VII: -Capa de Red- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad VII: -Capa de Red- ; Algoritmos de enrutamiento (Principio de optimización, Enrutamiento por la ruta más corta, Inundación, Enrutamiento por vector de di
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Sitios web sobre normativas, tecnologías y soluciones, opcional: | Pagina: 5]
   > Materia: Comunicacion y Redes Sección: Sitios web sobre normativas, tecnologías y soluciones, opcional: LACNIC -> http://lacnic.net/sp/ LAC IPV6 TF -> www.lac.ipv6tf.org 3M -> www.3m.com FURUKAWA ->
7. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Sistemas | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Sistemas que el/la estudiante cuente con herramientas conceptuales y prácticas para encarar los desafíos que suponen el ejercicio de
8. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Unidad 3: Gestión del Talento en la Era Digital | Pagina: 2]
   > Materia: Informática y Recursos Humanos Sección: Unidad 3: Gestión del Talento en la Era Digital 1. Procesos de selección y reclutamiento digital. 2. Evaluación del desempeño con herramientas tecnoló

**Respuesta:**

Según el documento "PROGRAMA - Investigación Operativa.pdf" sección "Software de Aplicación", se recomiendan las siguientes herramientas de software para resolver problemas de optimización lineal:

1. LINDO (Linear, Interactive, and Discrete Optimizer): Es un software especializado en la resolución de problemas de programación lineal, entera y no lineal.
2. PHP Simplex: Es una herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el método Simplex.

Estas herramientas se relacionan con las unidades teóricas de la materia Investigación Operativa, específicamente con las secciones "80%" y "Simplex", que cubren temas como la programación lineal, el transporte, las redes y la teoría de juegos.

Además, en la sección "Investigación" de "PROGRAMA - Investigación Operativa.pdf" se mencionan otros modelos y teorías que se relacionan con la resolución de problemas de optimización, como la programación dinámica y la teoría de colas. Sin embargo, estas secciones no mencionan específicamente herramientas de software para resolver problemas de optimización lineal.

**Tokens:** entrada: 1471 | salida: 260 | total: 1731

---

### Pregunta 13

> - ¿Dónde puedo descargar la materia de Cálculo de 1er año?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Nacional | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Nacional en https://ediciones.ungs.edu.ar/wp-content/uploads/2018/09/9789876301190-completo.pdf
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas s
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 1- PROGRAMA DE CONTENIDOS | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: 1- PROGRAMA DE CONTENIDOS Unidad I: Introducción -Importancia e Influencia de las Redes en Nuestras Vidas: Comunicación en un mundo centrado en la red, herramie
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Primer | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Primer Orden.
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS . Stallings. - 7a. - Madrid: Pearson Educación, 2004. ISBN 9788420541105 [Disponible en Biblioteca FCyT- Oro Verde] Tanenbaum,
6. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Bibliografía Nacional: | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Bibliografía Nacional: Ley de Teletrabajo (Ley 27.555).
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Sitios web sobre normativas, tecnologías y soluciones, opcional: | Pagina: 5]
   > Materia: Comunicacion y Redes Sección: Sitios web sobre normativas, tecnologías y soluciones, opcional: IETF -> www.ietf.org IEEE -> www.ieee.org ISO -> www.iso.org CISCO -> www.cisco.com IANA -> www
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: (Método | Pagina: 1]
   > Materia: Investigación Operativa Sección: (Método recursiva de los cálculos: etapas, estados, decisiones y principio de optimalidad de Bellman.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1223 | salida: 14 | total: 1237

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
   > Materia: Comunicacion y Redes Sección: Unidad VII: -Capa de Red- . Clase de direccionamiento (clase a, b, c, d y e). Prefijo y Mascara de red. Lógica de and. Calculo de direcciones. División de subre
7. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos . 2022 Modelos vectoriales y redes neuronales artificiales, para la aplicación de procesamiento de lenguaje natural en normativas jurídicas /
8. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio I. FUNDAMENTACIÓN El avance de las tecnologías de la información y la comunicación (TIC) ha t

**Respuesta:**

Lo siento, pero no puedo encontrar esa información en los fragmentos de contexto proporcionados.

**Tokens:** entrada: 1277 | salida: 20 | total: 1297

---

### Pregunta 15

> - ¿Cuál es el costo de la certificación oficial de Cisco que se menciona como opcional en la planificación?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS 4- BIBLIOGRAFIA Obligatoria Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Ver
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Sitios web sobre normativas, tecnologías y soluciones, opcional: | Pagina: 5]
   > Materia: Comunicacion y Redes Sección: Sitios web sobre normativas, tecnologías y soluciones, opcional: IETF -> www.ietf.org IEEE -> www.ieee.org ISO -> www.iso.org CISCO -> www.cisco.com IANA -> www
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas s
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% a la materia. La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen reprob
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad II: -Capa física concepto y medios- | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: Unidad II: -Capa física concepto y medios- : -Capa de enlace de dato -sub capa LLC (control de enlace lógico)- Cuestiones en el diseño de la capa de enlace de d
6. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio . Además, se abordarán aspectos legales fundamentales para comprender el impacto normativo de
7. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 9]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Software utilizado PostgreSQL 9.6 o superi
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE El alumno accederá a la condición de REGULAR, si cumple con las siguientes con

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1566 | salida: 14 | total: 1580

---

### Pregunta 16

> - Para la Promoción Directa, se exige la aprobación de la totalidad de los trabajos prácticos (TP 1 al TP 5). ¿Cuál es la calificación numérica mínima que debe obtenerse en cada TP individual para que se considere aprobado?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos . 2018 Requisitos para rendir como estudiantes regulares, promocionales y libres: a. Promoción Directa Para acceder a la condición de Promoció
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos en condición libre. Deberá presentar el trabajo práctico integrador con una antelación mínima de veinte (20) días hábiles respecto de la
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% requisito indispensable la entrega y aprobación de los dos trabajos prácticos obligatorios y el cumplimiento del
4. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 9]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Software utilizado PostgreSQL 9.6 o superi
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Régimen | Regularidad: | Pagina: 7]
   > Materia: Bases de Datos Avanzadas Sección: Régimen | Regularidad: Asistencia: Según norma vigente. Todos los trabajos prácticos aprobados.
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE Evaluación Final: El alumno con condición de REGULAR, deberá rendir un examen
7. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Sistema de evaluación: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Sistema de evaluación: se les pide redactar un resumen conciso de la lectura realizada, abarcando entre y palabras. Tp 2: Elaboración d
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos

**Respuesta:**

Lo siento, pero no tengo suficiente información en el Contexto proporcionado para responder a esta pregunta. El Contexto menciona que los TP 1 y 2 están definidos en el documento "PROGRAMA- Metodología de la Investigación.docx.pdf", pero no menciona la calificación mínima requerida para cada TP individual. Sin embargo, el documento "PROGRAMA - Investigación Operativa.pdf" menciona "los dos trabajos prácticos obligatorios" y el documento "BDA Planificacion.pdf" menciona que "todos los trabajos prácticos aprobados" son un requisito, pero no se proporciona información detallada sobre las calificaciones mínimas.

Por lo tanto, no dispongo de información en mis documentos para determinar la calificación numérica mínima que debe obtenerse en cada TP individual para considerarlo aprobado.

**Tokens:** entrada: 1479 | salida: 185 | total: 1664

---

### Pregunta 17

> - ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible vía URL que
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Problema | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Problema de separación lineal. Aplicaciones.
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% a la materia. La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen reprob
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE Evaluación Final: El alumno con condición de REGULAR, deberá rendir un examen
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: (Método | Pagina: 1]
   > Materia: Investigación Operativa Sección: (Método recursiva de los cálculos: etapas, estados, decisiones y principio de optimalidad de Bellman.
6. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos . 2018 Implementación de Bases de Datos NOSQL / Rubén Orlando Almada; director Alejandro Javier Hadad. 2018 Herramientas ágiles utilizadas en
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Composición | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Composición MAX-MIN. Capítulo VII Sistemas Difusos. Consideraciones generales. Representación de conocimiento estructurado mediante reglas lingüísticas.
8. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Unidad 3: La dimensión de la estrategia general de investigación | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Unidad 3: La dimensión de la estrategia general de investigación ¿Cómo se va a estudiar el problema? Tipo de diseños cuantitativos o cualitativos. La

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta. La información proporcionada en el contexto se centra en la investigación operativa, inteligencia artificial, métodos y herramientas para la resolución de problemas de optimización, pero no se menciona específicamente cómo implementar el método de Simplex en Excel.

**Tokens:** entrada: 1489 | salida: 67 | total: 1556

---

### Pregunta 18

> - ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mismo
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
3. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 15 18 de junio Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 15 18 de junio Virtual Teoría 17 de septiembre Teoría Coloquio Avances proyectos a la cátedra- Grupos Jimena 24 de septiembre Virtual Tutorías 24 01
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% de asistencia a las clases teóricas y prácticas.
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Buenos | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Buenos en condición libre. Deberá presentar el trabajo práctico integrador con una antelación mínima de veinte (20) días hábiles respecto de la
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% a la materia. La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen reprob
7. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Días de clase | Pagina: 3]
   > Materia: Bases de Datos Avanzadas Sección: Días de clase Lunes: 13:30 a 15:30 -> Teoría Viernes: 17:00 a 19:00 -> Práctica NOTA: Los horarios están en proceso de evaluación y pueden sufrir cambios
8. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Días de clase | Pagina: 4]
   > Materia: Bases de Datos Avanzadas Sección: Días de clase Cronograma de clases Presenciales/Virtuales A partir de este año la materia será dictada de manera bimodal. El cronograma será definido en su

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1428 | salida: 14 | total: 1442

---

## Resumen de tokens

| Conversacion | Entrada | Salida | Total |
|---|---|---|---|
| 1 | 16823 | 1315 | 18138 |
| 2 | 24139 | 1054 | 25193 |
| 3 | 15862 | 1094 | 16956 |
| 4 | 22317 | 1323 | 23640 |
| 5 | 23954 | 1429 | 25383 |
| 6 | 25728 | 1981 | 27709 |
| **Total** | **128823** | **8196** | **137019** |
