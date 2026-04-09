# Evaluacion — test-OllamaV2

_Iniciada: 2026-04-09 01:18:26_
_Ultima actualizacion: 2026-04-09 01:26:54_

**Estado:** completado
**Archivo de evaluacion:** `tests/evaluacionOllama.md`
**Preguntas:** 18 | **Conversaciones planificadas:** 6 | **Conversaciones iniciadas:** 6 | **Preguntas procesadas:** 108

**Criterio de puntaje:** 1 punto por respuesta correcta o abstencion correcta en preguntas de borde, 0.5 por respuesta parcial pero util y 0 por respuesta incorrecta, incompleta de forma critica o no sustentada por el contexto.

## Conversacion 1

**Puntaje evaluado: 11 / 18**

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
   > Materia: Inteligencia Artificial Sección: Métodos y mensajes. Representación de Conocimientos mediante reglas. Estructura básica. Representación de reglas mediante objetos.
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Tópicos | Pagina: 3]
   > Materia: Inteligencia Artificial Sección: Tópicos avanzados en tecnología de
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Integración | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación

**Respuesta:**

Dispongo de información en mis documentos para responder esta consulta.

El contenido de la materia Inteligencia Artificial está distribuido en las siguientes secciones:

1. **Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes**: donde se encuentra la definición e introducción a la IA, así como las herramientas y técnicas proveidas por el área de IA.
2. **Descripción de los temas específicos a desarrollarse en la asignatura**: donde se menciona que se desarrollarán temas específicos relacionados con la materia, aunque no se proporcionan detalles.
3. **Métodos y mensajes. Representación de Conocimientos mediante reglas**: donde se describe la representación de conocimientos mediante reglas, incluyendo la estructura básica y la representación de reglas mediante objetos.
4. **Tópicos avanzados en tecnología de**: donde se menciona la existencia de tópicos avanzados en tecnología, pero no se proporcionan detalles.
5. **Integración de la solución difusa final**: donde se describe el proceso de Defuzzificación, incluyendo el Método del centroide y el Método de máxima, así como la influencia de la aplicación de estos métodos sobre el funcionamiento del sistema.
6. **Agentes Basados en Lógica Difusa**: donde se describe el funcionamiento de agentes basados en lógica difusa.
7. **Capítulo VIII Redes Neuronales Artificiales (RNA). Generalidades, conceptos básicos Reseña Histórica.**: donde se proporciona información general sobre Redes Neuronales Artificiales.

**Tokens:** entrada: 595 | salida: 355 | total: 950

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
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Estructuras | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Estructuras basadas en Lógica.
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad II: -Capa física concepto y medios- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad II: -Capa física concepto y medios- Protocolo libre de colisiones, Protocolo de LAN Inalámbricas), Ethernet, concepto sobre el Algoritmo de retroceso exp

**Respuesta:**

La respuesta es "Inteligencia Artificial".

**Tokens:** entrada: 779 | salida: 10 | total: 789

---

### Pregunta 3

> - ¿Cuál es el plan de estudios de Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: SANTA | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: SANTA CRUZ; Año de la carrera a la que pertenece la cátedra: 4 Régimen de la materia: Anual Carga horaria semanal: 3 horas Correlativa: Ingeniería d
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 1 12 de marzo Presencial Teórico/práctico Presentación de la asignatura | 2 19 de marzo Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 1 12 de marzo Presencial Teórico/práctico Presentación de la asignatura | 2 19 de marzo Virtual Teoría Conceptos generales para introducción 3 26 de
3. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 8 30 de abril Presencial (pedir cambio fecha) Práctica | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 8 30 de abril Presencial (pedir cambio fecha) Práctica 9 7 de mayo virtual Teoría Alcances, límites y limitaciones/ Objetivos / Justificación 10 14 d
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Dicho | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Dicho examen contará con una (1) instancia de recuperación, conforme al cronograma establecido por la cátedra. - Entrega obligatoria de
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Unidad 3: La dimensión de la estrategia general de investigación | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Unidad 3: La dimensión de la estrategia general de investigación ¿Cómo se va a estudiar el problema? Tipo de diseños cuantitativos o cualitativos. La

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1085 | salida: 14 | total: 1099

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
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Visto | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Visto . Guillerón. 2018 Red Privada Virtual (VPM) sobre Protocolo de Internet versión 6 (IPv6) / Rodrigo Paúl Basso, Maximiliano Sebastián Toso; dire

**Respuesta:**

De acuerdo con la información del documento "Planificación 2025 - Comunicacion y Redes.pdf", para quedar como alumno regular en la materia de Comunicación y Redes, debes cumplir con la condición de regular, que se menciona en la sección del sistema de evaluación. Esto implica que debes obtener en los 3 parciales una calificación promedio superior o igual a los 60 puntos.

**Tokens:** entrada: 1068 | salida: 93 | total: 1161

---

### Pregunta 5

> - ¿Qué instancias de recuperación nos provee Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% - ALUMNO LIBRE: Revestirá esta condición todo estudiante que no logre cumplimentar alguno de los requisitos de puntaje, trabajos prácticos o as
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mism
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Resolución | Pagina: 1]
   > Materia: Investigación Operativa Sección: Resolución de problemas de diligencia, asignación de recursos y reemplazo de equipos.
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Permite | Pagina: 2]
   > Materia: Investigación Operativa Sección: Permite resolver problemas de programación lineal
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: PLANIFICACIÓN INVESTIGACIÓN OPERATIVA | Pagina: 1]
   > Materia: Investigación Operativa Sección: PLANIFICACIÓN INVESTIGACIÓN OPERATIVA Unidad I: -Introducción y Modelos Matemáticos- Definición y origen de la Investigación Operativa.

**Respuesta:**

La Investigación Operativa nos ofrece dos oportunidades de recuperatorio totales.

**Tokens:** entrada: 667 | salida: 17 | total: 684

---

### Pregunta 6

> - ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: (LP), | Pagina: 2]
   > Materia: Investigación Operativa Sección: (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al análisis
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Tamara | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Tamara de las clases presenciales y remotas. Asimismo, se establece que durante el primer cuatrimestre se abordará y desarrollará la mayor part
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Incluye | Pagina: 2]
   > Materia: Investigación Operativa Sección: Incluye módulos para el
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Tamara | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Tamara y otro destinado a los grupos a cargo de la profesora Jimena. Las clases teóricas se dictarán de manera conjunta para la
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 941 | salida: 14 | total: 955

---

### Pregunta 7

> - ¿Qué vinculaciones temáticas existen entre Bases de Datos Avanzadas y Comunicación y Redes que resulten pertinentes para el perfil de un arquitecto de sistemas?

**Chunks de contexto:**

1. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Bases de Datos Avanzadas | Pagina: 2]
   > Materia: Bases de Datos Avanzadas Sección: Bases de Datos Avanzadas Equipo docente Trossero, Sebastián Teoría Trossero.sebastian@uader.edu.ar Schmuckler, Jorge Práctica Schmukler.jorge@uader.edu.ar
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 1- PROGRAMA DE CONTENIDOS | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: 1- PROGRAMA DE CONTENIDOS . La red como plataforma comunicación a través de redes (elementos que intervienen una red, redes convergentes, arquitectura de Intern
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 1- PROGRAMA DE CONTENIDOS | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: 1- PROGRAMA DE CONTENIDOS . Conceptos usados en Comunicaciones y Redes: Uso de la redes de computadora, aplicaciones de negocios, domésticas, distintos usuarios
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio . FUNDAMENTACIÓN El avance de las tecnologías de la información y la comunicación (TIC) ha tr
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Unidad IV: Bases de Datos Distribuidas Parcial | Unidad V: Datawarehouse Parcial | Pagina: 6]
   > Materia: Bases de Datos Avanzadas Sección: Unidad IV: Bases de Datos Distribuidas Parcial | Unidad V: Datawarehouse Parcial Unidad VI: Datamining Parcial + TP Unidad VII: Bases de Datos OO Parcial NO

**Respuesta:**

Dispongo de información en mis documentos para responder esta consulta.

Bases de Datos Avanzadas y Comunicación y Redes comparten conceptos y tecnologías relevantes para el perfil de un arquitecto de sistemas. En Comunicación y Redes, se estudia la arquitectura de Internet, redes convergentes, arquitectura de red tolerante a fallas y escalable, y calidad de servicio. Estos conceptos son esenciales para el diseño y la implementación de redes de computadoras, incluidas las redes que sostienen las bases de datos distribuidas.

Además, la materia de Bases de Datos Avanzadas aborda técnicas para optimizar el acceso y la recuperación de información en bases de datos distribuidas y en entornos con múltiples usuarios, lo cual está directamente relacionado con la calidad de servicio y la tolerancia a fallas de las redes, ya que estos aspectos permiten a las bases de datos funcionar de manera eficiente en entornos compartidos y a gran escala.

En la relación entre estas dos materias, se puede encontrar también la importancia de la comunicación efectiva entre sistemas y bases de datos para que puedan compartir y intercambiar información de manera eficiente y segura. El arquitecto de sistemas necesita comprender cómo las bases de datos interactúan con las redes de computadoras y cómo estas últimas garantizan la conectividad y la calidad de servicio para el funcionamiento óptimo de las aplicaciones que utilizan las bases de datos.

Por lo tanto, existen varias vinculaciones temáticas entre Bases de Datos Avanzadas y Comunicación y Redes que son pertinentes para el perfil de un arquitecto de sistemas.

**Tokens:** entrada: 830 | salida: 379 | total: 1209

---

### Pregunta 8

> - ¿En qué asignaturas de 4to año se analiza el impacto de la Inteligencia Artificial en las personas o las organizaciones, y desde qué enfoque lo aborda cada una?

**Chunks de contexto:**

1. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Unidad 2: Relaciones Humanas en el Contexto Organizacional | Pagina: 2]
   > Materia: Informática y Recursos Humanos Sección: Unidad 2: Relaciones Humanas en el Contexto Organizacional 1. Comunicación interna y cultura organizacional en entornos digitales. 2. Inteligencia emo
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Ventajas | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Ventajas comparativas entre las distintas representaciones. Comportamiento de Agentes Basados en Conocimientos. Capítulo IV Diseño de los Sistemas Expe
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio integrando conceptos de informática, gestión organizacional y derecho informático. Los estudi
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Integración | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. He

**Respuesta:**

Dispongo de información en mis documentos para responder esta consulta.

La pregunta relaciona el tema de Inteligencia Artificial (IA), que se analiza en dos documentos: IA - Programa de Cátedra (campus).pdf y PROGRAMA INFORMATICA Y RRHH.pdf.

El impacto de la inteligencia artificial en la gestión del talento se analiza en la asignatura Informática y Recursos Humanos, específicamente en la unidad 2: Relaciones Humanas en el Contexto Organizacional, y en la sección del programa de contenidos de la asignatura de Inteligencia Artificial. 

Por lo tanto, tanto la asignatura de Informática y Recursos Humanos como la asignatura de Inteligencia Artificial, analizan el impacto de la Inteligencia Artificial en las personas o las organizaciones desde distintos enfoques.

En el caso de la asignatura de Informática y Recursos Humanos, se considera el impacto de la IA en la gestión del talento y en las relaciones humanas en el contexto organizacional.

Por otro lado, la asignatura de Inteligencia Artificial, aborda el tema desde su definición y descripción de sus módulos componentes y la importancia de la IA para las organizaciones.

**Tokens:** entrada: 777 | salida: 271 | total: 1048

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

No dispongo de información en mis documentos para responder esta consulta. La información proporcionada solo se refiere a la materia Bases de Datos Avanzadas y sus requisitos, pero no hay información sobre la materia Redes y Comunicaciones.

**Tokens:** entrada: 803 | salida: 51 | total: 854

---

### Pregunta 10

> - ¿De qué manera el algoritmo de la ruta más corta de Redes de la unidad 7 se relaciona con los modelos de transporte y transbordo de Investigación Operativa en la Unidad 5?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad VII: -Capa de Red- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad VII: -Capa de Red- ; Algoritmos de enrutamiento (Principio de optimización, Enrutamiento por la ruta más corta, Inundación, Enrutamiento por vector de di
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Análisis | Pagina: 1]
   > Materia: Investigación Operativa Sección: Análisis de dualidad y sensibilidad básica en modelos lineales. Unidad IV: -Modelos de Transporte y Transbordo- El problema del transporte: estructur
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Problemas | Pagina: 1]
   > Materia: Investigación Operativa Sección: Problemas de transbordo y el problema de la asignación
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad VII: -Capa de Red- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad VII: -Capa de Red- ; Algoritmos de control de congestión (Principios generales del control de congestión, Políticas de prevención de congestión, Control
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad VII: -Capa de Red- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad VII: -Capa de Red- . Aspectos de diseño de la capa de red (Conmutación de paquetes de almacenamiento y reenvío, Servicios proporcionados a la capa de tra

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 759 | salida: 14 | total: 773

---

### Pregunta 11

> - Si quiero promocionar todas las materias de 4to año, ¿cuál es la diferencia de promedio exigido entre Investigación Operativa e Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: | Pagina: 1]
   > Materia: Investigación Operativa Sección: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: - ALUMNO PROMOCIONADO: El estudiante logrará la promoción directa si alcanza un prom
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Ventajas | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Ventajas comparativas entre las distintas representaciones. Comportamiento de Agentes Basados en Conocimientos. Capítulo IV Diseño de los Sistemas Expe
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% de asistencia a las clases teóricas y prácticas.
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: (LP), | Pagina: 2]
   > Materia: Investigación Operativa Sección: (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al análisis

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 726 | salida: 14 | total: 740

---

### Pregunta 12

> - ¿Qué herramientas de software se recomiendan en la carrera para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas de modelos de optimización y problemas de gestión: - LINDO (Linear, Interactive, and Discrete Optimizer): Software especializado en la resoluci
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: (LP), | Pagina: 2]
   > Materia: Investigación Operativa Sección: (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al análisis
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Definición | Pagina: 1]
   > Materia: Investigación Operativa Sección: Definición de variables de decisión, función objetivo y restricciones de sistema y de no negatividad. Unidad II: -Programación Lineal (PL)- Pro
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Es | Pagina: 2]
   > Materia: Investigación Operativa Sección: Es ideal para validaciones rápidas y visualización de regiones factibles. - LINGO (64 bits): Una versión avanzada y más potente del motor LINDO. Está
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas Los exámenes se desarrollarán estrictamente en los bloques horarios asignados a la materia. La ausencia no justificada (sin certifica

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 842 | salida: 14 | total: 856

---

### Pregunta 13

> - ¿Dónde puedo descargar la materia de Cálculo de 1er año?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS 4- BIBLIOGRAFIA Obligatoria Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Ver
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Visto | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Visto en https://ediciones.ungs.edu.ar/wp-content/uploads/2018/09/9789876301190-completo.pdf
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas s
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Visto | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Visto : https://youtu.be/9oWM50RDsLQ -> BÚSQUEDA AVANZADA GOOGLE - BÚSQUEDA GOOGLE AVANZADA - 2DA PARTE APRENDER A INVESTIGAR: https://youtu.be/eHjUq
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Visto | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Visto Material audiovisual de la unidad Sobre investigación María Teresa Sirven Clase 1 Maestría Tecnología Educativa https://youtu.be/yBL4Hu9n Fic M

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 926 | salida: 14 | total: 940

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

**Tokens:** entrada: 644 | salida: 14 | total: 658

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

**Tokens:** entrada: 895 | salida: 14 | total: 909

---

### Pregunta 16

> - Para la Promoción Directa, se exige la aprobación de la totalidad de los trabajos prácticos (TP 1 al TP 5). ¿Cuál es la calificación numérica mínima que debe obtenerse en cada TP individual para que se considere aprobado?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: | Pagina: 1]
   > Materia: Investigación Operativa Sección: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: - ALUMNO PROMOCIONADO: El estudiante logrará la promoción directa si alcanza un prom
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Visto | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Visto . Guillerón. 2018 Red Privada Virtual (VPM) sobre Protocolo de Internet versión 6 (IPv6) / Rodrigo Paúl Basso, Maximiliano Sebastián Toso; dire
3. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Visto | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Visto . - Aprobación del examen parcial teórico con una calificación igual o superior a 75 (setenta y cinco) puntos. - Entrega de la totalidad de los
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE El alumno accederá a la condición de PROMOCIÓN si cumple con las siguientes co
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Dicho | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Dicho examen contará con una (1) instancia de recuperación, conforme al cronograma establecido por la cátedra. - Entrega obligatoria de

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1036 | salida: 14 | total: 1050

---

### Pregunta 17

> - ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible vía URL que
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: PL: | Pagina: 1]
   > Materia: Investigación Operativa Sección: PL: región factible, búsqueda de la solución óptima en los vértices, análisis de casos especiales (soluciones múltiples, soluciones no acot
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Permite | Pagina: 2]
   > Materia: Investigación Operativa Sección: Permite resolver problemas de programación lineal
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas de modelos de optimización y problemas de gestión: - LINDO (Linear, Interactive, and Discrete Optimizer): Software especializado en la resoluci
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex y el

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 570 | salida: 14 | total: 584

---

### Pregunta 18

> - ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mism
3. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 15 18 de junio Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 15 18 de junio Virtual Teoría 10 de septiembre Virtual Tutorías Avances proyectos a la cátedra- Grupos Tamara 17 de septiembre Teoría Coloquio Avanc
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% de asistencia a las clases teóricas y prácticas.
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 8 30 de abril Presencial (pedir cambio fecha) Práctica | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 8 30 de abril Presencial (pedir cambio fecha) Práctica 9 7 de mayo virtual Teoría Alcances, límites y limitaciones/ Objetivos / Justificación 10 14 d

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 813 | salida: 14 | total: 827

---

## Conversacion 2

**Puntaje evaluado: 10.5 / 18**

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
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Ventajas | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Ventajas comparativas entre las distintas representaciones. Comportamiento de Agentes Basados en Conocimientos. Capítulo IV Diseño de los Sistemas Expe

**Respuesta:**

Según el contexto proporcionado, los contenidos de la materia "Inteligencia Artificial" están descritos en cuatro documentos PDF: "IA - Programa de Cátedra (campus).pdf" (documento general), "IA - Programa de Cátedra (campus).pdf" (Sección: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes), "IA - Programa de Cátedra (campus).pdf" (Sección: Descripción), "IA - Programa de Cátedra (campus).pdf" (Sección: Métodos), "IA - Programa de Cátedra (campus).pdf" (Sección: Integración), "IA - Programa de Cátedra (campus).pdf" (Sección: Ventajas), y otros capítulos (no mencionados).

Entre los contenidos se mencionan:

- Capítulo I Agentes Inteligentes: Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas por el área de IA.

- Sección Descripción: Descripción de los temas específicos a desarrollarse en la asignatura. No hay información específica al respecto.

- Sección Métodos: Representación de Conocimientos mediante reglas. Estructura básica. Representación de reglas mediante objetos.

- Sección Integración: Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación de los distintos métodos sobre el funcionamiento del sistema. Agentes Basados en Lógica Difusa.

- Capítulo VIII Redes Neuronales Artificiales (RNA): Generalidades, conceptos básicos Reseña Histórica.

- Sección Ventajas: Comparativas entre las distintas representaciones. Comportamiento de Agentes Basados en Conocimientos.

- Capítulo IV Diseño de los Sistemas Expertos: Definición y descripción de sus módulos componentes.

En resumen, los contenidos de la materia "Inteligencia Artificial" incluyen conceptos relacionados con la IA, los agentes inteligentes, los métodos de representación de conocimientos, la integración de la solución difusa, las redes neuronales artificiales y el diseño de los sistemas expertos.

**Tokens:** entrada: 633 | salida: 513 | total: 1146

---

### Pregunta 2

> - ¿En qué materia se enseña el concepto de Lógica Difusa?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Capítulo VI | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Capítulo VI Lógica Difusa (Fuzzy). Consideraciones generales, Conjuntos Difusos, definición.
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Integración | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad II: -Capa física concepto y medios- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad II: -Capa física concepto y medios- . Control de enlace lógico, Control de acceso al medio. Implementación de ethernet. Dominios de colisiones - La antig
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Visto | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Visto Deep Learning aplicado al aprendizaje automático de ontologías para la representación del conocimiento a partir de texto no estructurado / Enzo
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Respecto a las clases: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Respecto a las clases: La cátedra implementará el modelo de aula invertida, en el que los estudiantes adquieren los conocimientos teóricos de mane

**Respuesta:**

La respuesta se encuentra en el contexto proporcionado en el Documento: IA - Programa de Cátedra (campus).pdf, Sección: Capítulo VI.

La Lógica Difusa (Fuzzy) se encuentra explicada en el Capítulo VI de la materia Inteligencia Artificial.

**Tokens:** entrada: 886 | salida: 65 | total: 951

---

### Pregunta 3

> - ¿Cuál es el plan de estudios de Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: SANTA | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: SANTA CRUZ; Año de la carrera a la que pertenece la cátedra: 4 Régimen de la materia: Anual Carga horaria semanal: 3 horas Correlativa: Ingeniería d
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 1 12 de marzo Presencial Teórico/práctico Presentación de la asignatura | 2 19 de marzo Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 1 12 de marzo Presencial Teórico/práctico Presentación de la asignatura | 2 19 de marzo Virtual Teoría Conceptos generales para introducción 3 26 de
3. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Dicho | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Dicho examen contará con una (1) instancia de recuperación, conforme al cronograma establecido por la cátedra. - Entrega obligatoria de
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Unidad 3: La dimensión de la estrategia general de investigación | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Unidad 3: La dimensión de la estrategia general de investigación ¿Cómo se va a estudiar el problema? Tipo de diseños cuantitativos o cualitativos. La
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Estructura del aula virtual: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Estructura del aula virtual: Los materiales educativos estarán alojados en el aula virtual "Metodología de la Investigación" dentro de la plataform

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1150 | salida: 14 | total: 1164

---

### Pregunta 4

> - En Comunicaciones y Redes, ¿cómo hago para quedar como alumno regular?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE El alumno accederá a la condición de REGULAR, si cumple con las siguientes con
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Visto | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Visto . Guillerón. 2018 Red Privada Virtual (VPM) sobre Protocolo de Internet versión 6 (IPv6) / Rodrigo Paúl Basso, Maximiliano Sebastián Toso; dire
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: SEDE: Oro Verde | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler. AÑO ACADEMICO: 2023 PLAN DE EST
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 8]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Comunicación De rutina y consultas: Lista

**Respuesta:**

Para quedar como alumno regular en la materia de Comunicaciones y Redes, es necesario cumplir con las siguientes condiciones de cátedra, de acuerdo con la información proporcionada en el documento "Planificación 2025 - Comunicacion y Redes.pdf":

1. Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos.

**Tokens:** entrada: 889 | salida: 82 | total: 971

---

### Pregunta 5

> - ¿Qué instancias de recuperación nos provee Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% - ALUMNO LIBRE: Revestirá esta condición todo estudiante que no logre cumplimentar alguno de los requisitos de puntaje, trabajos prácticos o as
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mism
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Permite | Pagina: 2]
   > Materia: Investigación Operativa Sección: Permite resolver problemas de programación lineal
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: PLANIFICACIÓN INVESTIGACIÓN OPERATIVA | Pagina: 1]
   > Materia: Investigación Operativa Sección: PLANIFICACIÓN INVESTIGACIÓN OPERATIVA Unidad I: -Introducción y Modelos Matemáticos- Definición y origen de la Investigación Operativa.
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: (LP), | Pagina: 2]
   > Materia: Investigación Operativa Sección: (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al análisis

**Respuesta:**

La Investigación Operativa provee de 2 instancias de recuperatorio totales. Estas instancias de recuperación se pueden utilizar para cualquiera de los dos parciales con la restricción de que no se pueden aplicar ambos recuperatorios al mismo examen parcial. La calificación obtenida en la instancia de recuperación sustituirá automáticamente a la nota del examen original.

**Tokens:** entrada: 769 | salida: 86 | total: 855

---

### Pregunta 6

> - ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: (LP), | Pagina: 2]
   > Materia: Investigación Operativa Sección: (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al análisis
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Incluye | Pagina: 2]
   > Materia: Investigación Operativa Sección: Incluye módulos para el
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS 4- BIBLIOGRAFIA Obligatoria Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Ver
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 15 18 de junio Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 15 18 de junio Virtual Teoría 10 de septiembre Virtual Tutorías Avances proyectos a la cátedra- Grupos Tamara 17 de septiembre Teoría Coloquio Avanc

**Respuesta:**

Dispongo de información para responder esta pregunta. 
TORA es una herramienta educativa diseñada específicamente para el aprendizaje de la Investigación Operativa.

**Tokens:** entrada: 908 | salida: 36 | total: 944

---

### Pregunta 7

> - ¿Qué vinculaciones temáticas existen entre Bases de Datos Avanzadas y Comunicación y Redes que resulten pertinentes para el perfil de un arquitecto de sistemas?

**Chunks de contexto:**

1. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Bases de Datos Avanzadas | Pagina: 2]
   > Materia: Bases de Datos Avanzadas Sección: Bases de Datos Avanzadas Equipo docente Trossero, Sebastián Teoría Trossero.sebastian@uader.edu.ar Schmuckler, Jorge Práctica Schmukler.jorge@uader.edu.ar
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 1- PROGRAMA DE CONTENIDOS | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: 1- PROGRAMA DE CONTENIDOS . Conceptos usados en Comunicaciones y Redes: Uso de la redes de computadora, aplicaciones de negocios, domésticas, distintos usuarios
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio . FUNDAMENTACIÓN El avance de las tecnologías de la información y la comunicación (TIC) ha tr
4. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Unidad IV: Bases de Datos Distribuidas Parcial | Unidad V: Datawarehouse Parcial | Pagina: 6]
   > Materia: Bases de Datos Avanzadas Sección: Unidad IV: Bases de Datos Distribuidas Parcial | Unidad V: Datawarehouse Parcial Unidad VI: Datamining Parcial + TP Unidad VII: Bases de Datos OO Parcial NO
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Bases de Datos Avanzadas | Pagina: 1]
   > Materia: Bases de Datos Avanzadas Sección: Bases de Datos Avanzadas PRESENTACIÓN DE LA MATERIA Facultad de Ciencia Y Tecnología Base de Datos Avanzadas

**Respuesta:**

Dispongo de información para responder esta consulta y la respuesta es:

La vinculación temática entre Bases de Datos Avanzadas y Comunicación y Redes es relevante para el perfil de un arquitecto de sistemas, ya que ambos temas están relacionados con la infraestructura y el diseño de sistemas de información.

Las bases de datos avanzadas se ocupan del diseño y la implementación de bases de datos que puedan manejar grandes cantidades de datos y proporcionar información precisa y eficiente a los usuarios.

Por otro lado, la comunicación y redes se refiere a la infraestructura y los protocolos utilizados para transmitir datos entre dispositivos y sistemas. Los arquitectos de sistemas deben considerar cómo las redes y los protocolos de comunicación pueden impactar en el diseño y la implementación de bases de datos y sistemas de información en general.

En particular, la asignatura de Bases de Datos Avanzadas tiene una unidad (Unidad IV) dedicada a las Bases de Datos Distribuidas, que se ocupa del diseño y la implementación de bases de datos que se distribuyen entre diferentes ubicaciones y se acceden a través de una red.

Por lo tanto, es probable que los arquitectos de sistemas necesiten considerar la conectividad y la comunicación entre diferentes componentes de un sistema de información que involucre bases de datos distribuidas, y así deberían conocer los temas relacionados con la Comunicación y Redes.

**Tokens:** entrada: 771 | salida: 315 | total: 1086

---

### Pregunta 8

> - ¿En qué asignaturas de 4to año se analiza el impacto de la Inteligencia Artificial en las personas o las organizaciones, y desde qué enfoque lo aborda cada una?

**Chunks de contexto:**

1. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Unidad 2: Relaciones Humanas en el Contexto Organizacional | Pagina: 2]
   > Materia: Informática y Recursos Humanos Sección: Unidad 2: Relaciones Humanas en el Contexto Organizacional 1. Comunicación interna y cultura organizacional en entornos digitales. 2. Inteligencia emo
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Ventajas | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Ventajas comparativas entre las distintas representaciones. Comportamiento de Agentes Basados en Conocimientos. Capítulo IV Diseño de los Sistemas Expe
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Editorial: Pearson Educación (2004 o versiones posteriores) | Pagina: 4]
   > Materia: Inteligencia Artificial Sección: Editorial: Pearson Educación (2004 o versiones posteriores) Título: Aprendizaje automático y aprendizaje profundo con Python, scikit-learn y Tensor Flow-
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Bibliografía Nacional: | Pagina: 2]
   > Materia: Informática y Recursos Humanos Sección: Bibliografía Nacional: Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Condiciones | Pagina: 3]
   > Materia: Inteligencia Artificial Sección: Condiciones de inicialización, problema de saturación prematura. Regiones de Decisión. Modo de operación autoasociativo. Capítulo X Generalización en

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 665 | salida: 14 | total: 679

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

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta. No tengo acceso a información sobre el requisito de regularización en la materia de Redes y Comunicaciones, sólo tengo información sobre las materias de Bases de Datos Avanzadas.

**Tokens:** entrada: 856 | salida: 53 | total: 909

---

### Pregunta 10

> - ¿De qué manera el algoritmo de la ruta más corta de Redes de la unidad 7 se relaciona con los modelos de transporte y transbordo de Investigación Operativa en la Unidad 5?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad VII: -Capa de Red- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad VII: -Capa de Red- ; Algoritmos de enrutamiento (Principio de optimización, Enrutamiento por la ruta más corta, Inundación, Enrutamiento por vector de di
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Análisis | Pagina: 1]
   > Materia: Investigación Operativa Sección: Análisis de dualidad y sensibilidad básica en modelos lineales. Unidad IV: -Modelos de Transporte y Transbordo- El problema del transporte: estructur
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Problemas | Pagina: 1]
   > Materia: Investigación Operativa Sección: Problemas de transbordo y el problema de la asignación
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible vía URL que
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: (Método | Pagina: 1]
   > Materia: Investigación Operativa Sección: (Método Húngaro). Unidad V: -Programación Dinámica- Características de la Programación Dinámica (PD).

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 664 | salida: 14 | total: 678

---

### Pregunta 11

> - Si quiero promocionar todas las materias de 4to año, ¿cuál es la diferencia de promedio exigido entre Investigación Operativa e Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: | Pagina: 1]
   > Materia: Investigación Operativa Sección: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: - ALUMNO PROMOCIONADO: El estudiante logrará la promoción directa si alcanza un prom
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% de asistencia a las clases teóricas y prácticas.
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Diferencias | Pagina: 1]
   > Materia: Investigación Operativa Sección: Diferencias entre
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Composición | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Composición MAX-MIN. Capítulo VII Sistemas Difusos. Consideraciones generales. Representación de conocimiento estructurado mediante reglas lingüísticas.
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas s

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta. No tengo información disponible sobre la materia Inteligencia Artificial ni sobre los requisitos de promedio para promocionar en esa materia. Solo tengo información sobre los requisitos de promedio para promocionar en la materia de Investigación Operativa.

**Tokens:** entrada: 667 | salida: 66 | total: 733

---

### Pregunta 12

> - ¿Qué herramientas de software se recomiendan en la carrera para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas de modelos de optimización y problemas de gestión: - LINDO (Linear, Interactive, and Discrete Optimizer): Software especializado en la resoluci
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: (LP), | Pagina: 2]
   > Materia: Investigación Operativa Sección: (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al análisis
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas Los exámenes se desarrollarán estrictamente en los bloques horarios asignados a la materia. La ausencia no justificada (sin certifica
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible vía URL que
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Problema | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Problema de separación lineal. Aplicaciones.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta. Mis únicos documentos relacionados con la materia son los archivos "PROGRAMA - Investigación Operativa.pdf", cuyos contenidos no proporcionan información sobre herramientas de software recomendadas para resolver problemas de optimización lineal.

**Tokens:** entrada: 761 | salida: 61 | total: 822

---

### Pregunta 13

> - ¿Dónde puedo descargar la materia de Cálculo de 1er año?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS 4- BIBLIOGRAFIA Obligatoria Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Ver
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Visto | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Visto en https://ediciones.ungs.edu.ar/wp-content/uploads/2018/09/9789876301190-completo.pdf
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas s
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Primer | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Primer Orden.
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Bibliografía Nacional: | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Bibliografía Nacional: Ley de Teletrabajo (Ley 27.555).

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 610 | salida: 14 | total: 624

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

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 650 | salida: 14 | total: 664

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
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 9]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Software utilizado PostgreSQL 9.6 o superi

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 922 | salida: 14 | total: 936

---

### Pregunta 16

> - Para la Promoción Directa, se exige la aprobación de la totalidad de los trabajos prácticos (TP 1 al TP 5). ¿Cuál es la calificación numérica mínima que debe obtenerse en cada TP individual para que se considere aprobado?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: | Pagina: 1]
   > Materia: Investigación Operativa Sección: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: - ALUMNO PROMOCIONADO: El estudiante logrará la promoción directa si alcanza un prom
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Visto | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Visto . Guillerón. 2018 Red Privada Virtual (VPM) sobre Protocolo de Internet versión 6 (IPv6) / Rodrigo Paúl Basso, Maximiliano Sebastián Toso; dire
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Asimismo, | Pagina: 1]
   > Materia: Investigación Operativa Sección: Asimismo, deberá acreditar la aprobación de los dos trabajos prácticos de la cátedra y mantener una asistencia mínima del
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Cumplida | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Cumplida exclusivamente en la mesa de examen, junto con la nota correspondiente a la instancia teórica, estableciéndose en ese mome
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Visto | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Visto de revisión y devolución con el equipo docente. El trabajo deberá entregarse con una antelación mínima de diez (10) días há

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 953 | salida: 14 | total: 967

---

### Pregunta 17

> - ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible vía URL que
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas de modelos de optimización y problemas de gestión: - LINDO (Linear, Interactive, and Discrete Optimizer): Software especializado en la resoluci
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex y el
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Problema | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Problema de separación lineal. Aplicaciones.
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Reactivo | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Reactivo Simple.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 479 | salida: 14 | total: 493

---

### Pregunta 18

> - ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mism
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% de asistencia a las clases teóricas y prácticas.
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 13 04 de junio Presencial Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 13 04 de junio Presencial Teoría Marco metodológico I: enfoque y tipo de investigación / muestra 14 11 de junio Virtual Práctica
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Visto | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Visto de revisión y devolución con el equipo docente. El trabajo deberá entregarse con una antelación mínima de diez (10) días há

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 817 | salida: 14 | total: 831

---

## Conversacion 3

**Puntaje evaluado: 11.5 / 18**

**Parametros modificados respecto a la conversacion anterior:**

| Parametro | Valor |
|---|---|
| top_k | 5 |
| retrieval_type | similarity_search |
| chunk_size | 300 |
| chunk_overlap | 30 |
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
   > Materia: Inteligencia Artificial Sección: Métodos y mensajes. Representación de Conocimientos mediante reglas. Estructura básica. Representación de reglas mediante objetos.
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Tópicos | Pagina: 3]
   > Materia: Inteligencia Artificial Sección: Tópicos avanzados en tecnología de
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Integración | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Integración Neuronales Artificiales (RNA). Generalidades, conceptos básicos Reseña Histórica.

**Respuesta:**

De acuerdo a la información del contexto, se puede determinar que los contenidos de la materia "Inteligencia Artificial" se pueden ver en la siguiente sección del Documento:
- Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes (Sección: Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas por el área IA.)
- Descripción de los temas específicos a desarrollarse en la asignatura.
- Métodos y mensajes. Representación de Conocimientos mediante reglas. Estructura básica. Representación de reglas mediante objetos.
- Tópicos avanzados en tecnología de
- Integración Neuronales Artificiales (RNA). Generalidades, conceptos básicos Reseña Histórica.

**Tokens:** entrada: 510 | salida: 179 | total: 689

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
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Estructuras | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Estructuras basadas en Lógica.
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad II: -Capa física concepto y medios- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad II: -Capa física concepto y medios- Protocolo libre de colisiones, Protocolo de LAN Inalámbricas), Ethernet, concepto sobre el Algoritmo de retroceso exp

**Respuesta:**

Según el Contexto, la Lógica Difusa se enseña en la materia de Inteligencia Artificial.

**Tokens:** entrada: 676 | salida: 26 | total: 702

---

### Pregunta 3

> - ¿Cuál es el plan de estudios de Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: SANTA | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: SANTA CRUZ; Año de la carrera a la que pertenece la cátedra: 4 Régimen de la materia: Anual Carga horaria semanal: 3 horas Correlativa: Ingeniería d
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 1 12 de marzo Presencial Teórico/práctico Presentación de la asignatura | 2 19 de marzo Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 1 12 de marzo Presencial Teórico/práctico Presentación de la asignatura | 2 19 de marzo Virtual Teoría Conceptos generales para introducción 3 26 de
3. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 8 30 de abril Presencial (pedir cambio fecha) Práctica | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 8 30 de abril Presencial (pedir cambio fecha) Práctica 9 7 de mayo virtual Teoría Alcances, límites y limitaciones/ Objetivos / Justificación 10 14 d
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Investigación | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Investigación ica desde espacios de reflexión sistemáticos enmarcados en trabajos propios de la disciplina y el campo profesional. Objetivo
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Cronograma de trabajo | METODOLOGÍA DE LA INVESTIGACIÓN- 2026 | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Cronograma de trabajo | METODOLOGÍA DE LA INVESTIGACIÓN- 2026 Clase FECHA Tipo de encuentro Tipo encuentro Tema

**Respuesta:**

Dispongo de información en mis documentos para responder esta consulta.

Cada sección del plan de estudios de Metodología de la Investigación se puede encontrar en diferentes documentos relacionados con la materia. Algunos de los planes de estudios se describen a continuación:

1. **CRUZ;**: Se trata de un fragmento de una sección llamada SANTA CRUZ. No proporciona suficiente información para entender la estructura del plan de estudios.

2. **12 de marzo Presencial Teórico/práctico Presentación de la asignatura**: Comienza un plan de estudios que incluye clases presenciales teórico-prácticas en diferentes fechas. El enfoque es presentar la asignatura.

3. **Cronograma de trabajo | METODOLOGÍA DE LA INVESTIGACIÓN- 2026**: Esto incluye un cronograma de clases, donde se detalla la fecha, el tipo de encuentro, el tipo de tema y el tema específico a tratar. Por ejemplo, se puede ver que hay una clase el **12 de marzo**, **19 de marzo**, **26 de marzo**, etc.

4. **Investigación**: Se describe el plan de estudios relacionado con la investigación, que incluye aspectos metodológicos. Algunos de los objetivos específicos son promover el reconocimiento de aspectos metodológicos de la investigación caracterizando las instancias y fases del proceso de investigación.

El plan de estudios varía según la sección consultada, pero en general, el plan de estudios incluye clases teórico-prácticas que abordan diferentes aspectos de la investigación.

**Tokens:** entrada: 817 | salida: 355 | total: 1172

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

- El alumno accederá a la condición de REGULAR, si cumple con las siguientes condiciones de cátedra:
1 - Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos.
2- Haber realizado y aprobado los dos trabajos Práctico impartido por la cátedra.
3- Asistir al 80% de las clases teóricas y prácticas.

**Tokens:** entrada: 1014 | salida: 98 | total: 1112

---

### Pregunta 5

> - ¿Qué instancias de recuperación nos provee Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% - ALUMNO LIBRE: Revestirá esta condición todo estudiante que no logre cumplimentar alguno de los requisitos de puntaje, trabajos prácticos o as
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mism
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Resolución | Pagina: 1]
   > Materia: Investigación Operativa Sección: Resolución de problemas de diligencia, asignación de recursos y reemplazo de equipos.
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Permite | Pagina: 2]
   > Materia: Investigación Operativa Sección: Permite resolver problemas de programación lineal
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: PLANIFICACIÓN INVESTIGACIÓN OPERATIVA | Pagina: 1]
   > Materia: Investigación Operativa Sección: PLANIFICACIÓN INVESTIGACIÓN OPERATIVA Unidad I: -Introducción y Modelos Matemáticos- Definición y origen de la Investigación Operativa.

**Respuesta:**

La investigación operativa ofrece dos oportunidades de recuperatorio totales. Estas instancias de recuperación pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mismo examen parcial.

**Tokens:** entrada: 600 | salida: 59 | total: 659

---

### Pregunta 6

> - ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: (LP), | Pagina: 2]
   > Materia: Investigación Operativa Sección: (LP), una interfaz basada en menús para la carga de datos. - TORA: Herramienta educativa diseñada específicamente para el aprendizaje de la
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Tamara | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Tamara sarrollará la mayor parte de los contenidos teóricos previstos en el programa, a fin de que el segundo cuatrimestre esté desti
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Incluye | Pagina: 2]
   > Materia: Investigación Operativa Sección: Incluye módulos para el
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: (LP), | Pagina: 2]
   > Materia: Investigación Operativa Sección: (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al análisis
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta. Solo hay información sobre la herramienta TORA en el primer documento relacionado con la Investigación Operativa, donde se especifica que TORA es una herramienta educativa diseñada específicamente para el aprendizaje de la investigación operativa. Sin embargo, no hay mención a qué módulos incluye.

**Tokens:** entrada: 690 | salida: 79 | total: 769

---

### Pregunta 7

> - ¿Qué vinculaciones temáticas existen entre Bases de Datos Avanzadas y Comunicación y Redes que resulten pertinentes para el perfil de un arquitecto de sistemas?

**Chunks de contexto:**

1. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Bases de Datos Avanzadas | Pagina: 2]
   > Materia: Bases de Datos Avanzadas Sección: Bases de Datos Avanzadas Equipo docente Trossero, Sebastián Teoría Trossero.sebastian@uader.edu.ar Schmuckler, Jorge Práctica Schmukler.jorge@uader.edu.ar
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 1- PROGRAMA DE CONTENIDOS | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: 1- PROGRAMA DE CONTENIDOS n la comunicación). La red como plataforma comunicación a través de redes (elementos que intervienen una red, redes convergentes, arqu
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio I. FUNDAMENTACIÓN El avance de las tecnologías de la información y la comunicación (TIC) ha t
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 1- PROGRAMA DE CONTENIDOS | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: 1- PROGRAMA DE CONTENIDOS capas, servicios orientados a la conexión y no orientados a la conexión, primitivas de servicio, relación de servicio a protocolo. Mod
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Unidad IV: Bases de Datos Distribuidas Parcial | Unidad V: Datawarehouse Parcial | Pagina: 6]
   > Materia: Bases de Datos Avanzadas Sección: Unidad IV: Bases de Datos Distribuidas Parcial | Unidad V: Datawarehouse Parcial Unidad VI: Datamining Parcial + TP Unidad VII: Bases de Datos OO Parcial NO

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 783 | salida: 14 | total: 797

---

### Pregunta 8

> - ¿En qué asignaturas de 4to año se analiza el impacto de la Inteligencia Artificial en las personas o las organizaciones, y desde qué enfoque lo aborda cada una?

**Chunks de contexto:**

1. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Unidad 2: Relaciones Humanas en el Contexto Organizacional | Pagina: 2]
   > Materia: Informática y Recursos Humanos Sección: Unidad 2: Relaciones Humanas en el Contexto Organizacional 1. Comunicación interna y cultura organizacional en entornos digitales. 2. Inteligencia emo
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Ventajas | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Ventajas comparativas entre las distintas representaciones. Comportamiento de Agentes Basados en Conocimientos. Capítulo IV Diseño de los Sistemas Expe
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio naria, integrando conceptos de informática, gestión organizacional y derecho informático. Los
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. He
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Unidad 4: Derecho Informático y Mundo Laboral | Pagina: 2]
   > Materia: Informática y Recursos Humanos Sección: Unidad 4: Derecho Informático y Mundo Laboral 1. Protección de datos personales y privacidad en el ámbito laboral. 2. Legislación sobre contratos de t

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 776 | salida: 14 | total: 790

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

**Tokens:** entrada: 803 | salida: 14 | total: 817

---

### Pregunta 10

> - ¿De qué manera el algoritmo de la ruta más corta de Redes de la unidad 7 se relaciona con los modelos de transporte y transbordo de Investigación Operativa en la Unidad 5?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad VII: -Capa de Red- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad VII: -Capa de Red- la conexión, Comparación entre las subredes de circuitos virtuales y las de datagramas); Algoritmos de enrutamiento (Principio de opti
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Análisis | Pagina: 1]
   > Materia: Investigación Operativa Sección: Análisis de dualidad y sensibilidad básica en modelos lineales. Unidad IV: -Modelos de Transporte y Transbordo- El problema del transporte: estructur
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Problemas | Pagina: 1]
   > Materia: Investigación Operativa Sección: Problemas de transbordo y el problema de la asignación
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad VII: -Capa de Red- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad VII: -Capa de Red- y CIDR; Algoritmos de control de congestión (Principios generales del control de congestión, Políticas de prevención de congestión, Co
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad VII: -Capa de Red- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad VII: -Capa de Red- utamiento jerárquico, Enrutamiento por difusión, Enrutamiento por multidifusión, Enrutamiento para hosts móviles, Enrutamiento en rede

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 724 | salida: 14 | total: 738

---

### Pregunta 11

> - Si quiero promocionar todas las materias de 4to año, ¿cuál es la diferencia de promedio exigido entre Investigación Operativa e Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: | Pagina: 1]
   > Materia: Investigación Operativa Sección: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: - ALUMNO PROMOCIONADO: El estudiante logrará la promoción directa si alcanza un prom
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Ventajas | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Ventajas comparativas entre las distintas representaciones. Comportamiento de Agentes Basados en Conocimientos. Capítulo IV Diseño de los Sistemas Expe
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% de asistencia a las clases teóricas y prácticas.
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: (LP), | Pagina: 2]
   > Materia: Investigación Operativa Sección: (LP), una interfaz basada en menús para la carga de datos. - TORA: Herramienta educativa diseñada específicamente para el aprendizaje de la

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 638 | salida: 14 | total: 652

---

### Pregunta 12

> - ¿Qué herramientas de software se recomiendan en la carrera para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas ción de modelos de optimización y problemas de gestión: - LINDO (Linear, Interactive, and Discrete Optimizer): Software especializado en la re
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas ustificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen reprobado. Software de Aplicación - Inv
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: (LP), | Pagina: 2]
   > Materia: Investigación Operativa Sección: (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al análisis
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Definición | Pagina: 1]
   > Materia: Investigación Operativa Sección: Definición de variables de decisión, función objetivo y restricciones de sistema y de no negatividad. Unidad II: -Programación Lineal (PL)- Pro
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Permite | Pagina: 2]
   > Materia: Investigación Operativa Sección: Permite resolver problemas de programación lineal

**Respuesta:**

Dispongo de información en mis documentos para responder esta consulta.

En el contexto proporcionado, se mencionan dos herramientas de software relacionadas con la resolución de problemas de optimización lineal:

1.  **LINDO (Linear, Interactive, and Discrete Optimizer):** Es un software especializado en la resolución de problemas de programación lineal, entera y no lineal. Este software es una herramienta práctica para resolver problemas de optimización lineal.
2.  **Storm:** Es un software orientado al análisis cuantitativo y gestión de operaciones. Además de modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios, Storm facilita el procesamiento de modelos matemáticos y estadísticos mediante una interfaz basada en modelado. Se considera que esta herramienta es útil para resolver problemas de optimización lineal, como los que se estudian en la unidad "Programación Lineal (PL)" del programa de Investigación Operativa. 

Estas herramientas están diseñadas para facilitar el trabajo con modelos de optimización lineal y están relacionadas con las unidades teóricas de la carrera de Investigación Operativa, específicamente la unidad "Programación Lineal (PL)".

**Tokens:** entrada: 660 | salida: 277 | total: 937

---

### Pregunta 13

> - ¿Dónde puedo descargar la materia de Cálculo de 1er año?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 1- PROGRAMA DE CONTENIDOS | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: 1- PROGRAMA DE CONTENIDOS de computadora, aplicaciones de negocios, domésticas, distintos usuarios. Hardware de redes, Sistema Cliente/Servidor, tipos de redes
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Visto | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Visto en https://ediciones.ungs.edu.ar/wp-content/uploads/2018/09/9789876301190-completo.pdf Material audiovisual de la unidad Sobre investigación M
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS istintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] Cisco Systems: Academia de Networking de Cisco Systems: Guí
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas s
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 1- PROGRAMA DE CONTENIDOS | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: 1- PROGRAMA DE CONTENIDOS e estandarización de comunicación y redes.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 739 | salida: 14 | total: 753

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

**Tokens:** entrada: 644 | salida: 14 | total: 658

---

### Pregunta 15

> - ¿Cuál es el costo de la certificación oficial de Cisco que se menciona como opcional en la planificación?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Sitios web sobre normativas, tecnologías y soluciones, opcional: | Pagina: 5]
   > Materia: Comunicacion y Redes Sección: Sitios web sobre normativas, tecnologías y soluciones, opcional: IETF -> www.ietf.org IEEE -> www.ieee.org ISO -> www.iso.org CISCO -> www.cisco.com IANA -> www
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS istintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] Cisco Systems: Academia de Networking de Cisco Systems: Guí
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas s
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Sitios web sobre normativas, tecnologías y soluciones, opcional: | Pagina: 5]
   > Materia: Comunicacion y Redes Sección: Sitios web sobre normativas, tecnologías y soluciones, opcional: ional.html UNDERWRITERS LABORATORIES (UL) -> www.ul.com PANDUIT -> www.panduit.com AMP -> www.t
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Sitios web sobre normativas, tecnologías y soluciones, opcional: | Pagina: 5]
   > Materia: Comunicacion y Redes Sección: Sitios web sobre normativas, tecnologías y soluciones, opcional: -> www.nfpa.org GFI SECURITY AND MESSANGING SOFTWARE -> www.gfi.com Lic. Luciano M. CAISSO.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 851 | salida: 14 | total: 865

---

### Pregunta 16

> - Para la Promoción Directa, se exige la aprobación de la totalidad de los trabajos prácticos (TP 1 al TP 5). ¿Cuál es la calificación numérica mínima que debe obtenerse en cada TP individual para que se considere aprobado?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Visto | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Visto a la condición de Promoción Directa, el/la estudiante deberá cumplir con los siguientes requisitos: - 80 % de asistencia a la cursada. - Aproba
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: | Pagina: 1]
   > Materia: Investigación Operativa Sección: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: - ALUMNO PROMOCIONADO: El estudiante logrará la promoción directa si alcanza un prom
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE El alumno accederá a la condición de PROMOCIÓN si cumple con las siguientes co
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Asimismo, | Pagina: 1]
   > Materia: Investigación Operativa Sección: Asimismo, deberá acreditar la aprobación de los dos trabajos prácticos de la cátedra y mantener una asistencia mínima del
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Es | Pagina: 1]
   > Materia: Investigación Operativa Sección: Es requisito indispensable la entrega y aprobación de los dos trabajos prácticos obligatorios y el cumplimiento del

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 815 | salida: 14 | total: 829

---

### Pregunta 17

> - ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible vía URL que
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: PL: | Pagina: 1]
   > Materia: Investigación Operativa Sección: PL: región factible, búsqueda de la solución óptima en los vértices, análisis de casos especiales (soluciones múltiples, soluciones no acot
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Permite | Pagina: 2]
   > Materia: Investigación Operativa Sección: Permite resolver problemas de programación lineal
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas ción de modelos de optimización y problemas de gestión: - LINDO (Linear, Interactive, and Discrete Optimizer): Software especializado en la re
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex y el

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 570 | salida: 14 | total: 584

---

### Pregunta 18

> - ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas a nota del examen original. Protocolos de Evaluación: Los resultados se publicarán en un plazo de siete días corridos tras la evaluación. Los
3. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 15 18 de junio Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 15 18 de junio Virtual Teoría Marco metodológico II: recolección de datos y análisis de datos RECESO DE INVIERNO/ MESAS DE EXAMENES FINALES 16 06 de
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 15 18 de junio Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 15 18 de junio Virtual Teoría ances proyectos a la cátedra- Grupos Jimena 24 de septiembre Virtual Tutorías 24 01 de octubre Presencial Tutorías Pre
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 15 18 de junio Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 15 18 de junio Virtual Teoría l teoría 19 27 de agosto Virtual Tutorías 03 de septiembre Presencial Tutorías Sugerecia entrevista a expertos en el t

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 794 | salida: 14 | total: 808

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
   > Materia: Inteligencia Artificial Sección: Integración Neuronales Artificiales (RNA). Generalidades, conceptos básicos Reseña Histórica.
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Condiciones | Pagina: 3]
   > Materia: Inteligencia Artificial Sección: Condiciones de inicialización, problema de saturación prematura. Regiones de Decisión. Modo de operación autoasociativo. Capítulo X Generalización en

**Respuesta:**

La respuesta a tu pregunta se puede encontrar en los documentos proporcionados.

Según el documento "IA - Programa de Cátedra (campus).pdf", en la sección "Descripción", se indican los temas específicos que se desarrollarán en la asignatura Inteligencia Artificial.

**Tokens:** entrada: 556 | salida: 64 | total: 620

---

### Pregunta 2

> - ¿En qué materia se enseña el concepto de Lógica Difusa?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Capítulo VI | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Capítulo VI Lógica Difusa (Fuzzy). Consideraciones generales, Conjuntos Difusos, definición.
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Integración | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Estructuras | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Estructuras basadas en Lógica.
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad II: -Capa física concepto y medios- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad II: -Capa física concepto y medios- Protocolo libre de colisiones, Protocolo de LAN Inalámbricas), Ethernet, concepto sobre el Algoritmo de retroceso exp
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Respecto a las clases: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Respecto a las clases: La cátedra implementará el modelo de aula invertida, en el que los estudiantes adquieren los conocimientos teóricos de mane

**Respuesta:**

La materia en la que se enseña el concepto de Lógica Difusa es Inteligencia Artificial.

**Tokens:** entrada: 703 | salida: 25 | total: 728

---

### Pregunta 3

> - ¿Cuál es el plan de estudios de Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: SANTA | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: SANTA CRUZ; Año de la carrera a la que pertenece la cátedra: 4 Régimen de la materia: Anual Carga horaria semanal: 3 horas Correlativa: Ingeniería d
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 1 12 de marzo Presencial Teórico/práctico Presentación de la asignatura | 2 19 de marzo Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 1 12 de marzo Presencial Teórico/práctico Presentación de la asignatura | 2 19 de marzo Virtual Teoría Conceptos generales para introducción 3 26 de
3. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Investigación | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Investigación ica desde espacios de reflexión sistemáticos enmarcados en trabajos propios de la disciplina y el campo profesional. Objetivo
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Cronograma de trabajo | METODOLOGÍA DE LA INVESTIGACIÓN- 2026 | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Cronograma de trabajo | METODOLOGÍA DE LA INVESTIGACIÓN- 2026 Clase FECHA Tipo de encuentro Tipo encuentro Tema
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Estructura del aula virtual: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Estructura del aula virtual: Los materiales educativos estarán alojados en el aula virtual "Metodología de la Investigación" dentro de la plataform

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 817 | salida: 14 | total: 831

---

### Pregunta 4

> - En Comunicaciones y Redes, ¿cómo hago para quedar como alumno regular?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE robado los dos trabajos práctico impartido por la cátedra. 3- Asistir al 80% d
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: SEDE: Oro Verde | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler. AÑO ACADEMICO: 2023 PLAN DE EST
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Visto | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Visto Protocolo de Internet versión 6 (IPv6) / Rodrigo Paúl Basso, Maximiliano Sebastián Toso; director Julio Alberto Aldonate; codirector Luciano Ma
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 8]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Comunicación De rutina y consultas: Lista

**Respuesta:**

Dispongo de información en mis documentos para responder esta consulta.

Para quedar como alumno regular en la materia "Comunicaciones y Redes", debes cumplir con las siguientes condiciones establecidas en el documento "Planificación 2025 - Comunicacion y Redes.pdf":

1. Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos.
2. Asistir al 80% de las clases teóricas y prácticas.
3. No me mencionas si robaste los dos trabajos prácticos, pero si es que los robaste, no me parece que cumplas con las condiciones para ser un estudiante regular.

Espero que esta respuesta te sea útil.

**Tokens:** entrada: 882 | salida: 160 | total: 1042

---

### Pregunta 5

> - ¿Qué instancias de recuperación nos provee Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% - ALUMNO LIBRE: Revestirá esta condición todo estudiante que no logre cumplimentar alguno de los requisitos de puntaje, trabajos prácticos o as
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Permite | Pagina: 2]
   > Materia: Investigación Operativa Sección: Permite resolver problemas de programación lineal
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: PLANIFICACIÓN INVESTIGACIÓN OPERATIVA | Pagina: 1]
   > Materia: Investigación Operativa Sección: PLANIFICACIÓN INVESTIGACIÓN OPERATIVA Unidad I: -Introducción y Modelos Matemáticos- Definición y origen de la Investigación Operativa.
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas ustificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen reprobado. Software de Aplicación - Inv
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: (LP), | Pagina: 2]
   > Materia: Investigación Operativa Sección: (LP), una interfaz basada en menús para la carga de datos. - TORA: Herramienta educativa diseñada específicamente para el aprendizaje de la

**Respuesta:**

La cátedra de Investigación Operativa dispone de dos oportunidades de recuperatorio totales.

**Tokens:** entrada: 588 | salida: 22 | total: 610

---

### Pregunta 6

> - ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: (LP), | Pagina: 2]
   > Materia: Investigación Operativa Sección: (LP), una interfaz basada en menús para la carga de datos. - TORA: Herramienta educativa diseñada específicamente para el aprendizaje de la
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Tamara | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Tamara sarrollará la mayor parte de los contenidos teóricos previstos en el programa, a fin de que el segundo cuatrimestre esté desti
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Incluye | Pagina: 2]
   > Materia: Investigación Operativa Sección: Incluye módulos para el
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas ustificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen reprobado. Software de Aplicación - Inv

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 677 | salida: 14 | total: 691

---

### Pregunta 7

> - ¿Qué vinculaciones temáticas existen entre Bases de Datos Avanzadas y Comunicación y Redes que resulten pertinentes para el perfil de un arquitecto de sistemas?

**Chunks de contexto:**

1. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Bases de Datos Avanzadas | Pagina: 2]
   > Materia: Bases de Datos Avanzadas Sección: Bases de Datos Avanzadas Equipo docente Trossero, Sebastián Teoría Trossero.sebastian@uader.edu.ar Schmuckler, Jorge Práctica Schmukler.jorge@uader.edu.ar
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 1- PROGRAMA DE CONTENIDOS | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: 1- PROGRAMA DE CONTENIDOS n la comunicación). La red como plataforma comunicación a través de redes (elementos que intervienen una red, redes convergentes, arqu
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio I. FUNDAMENTACIÓN El avance de las tecnologías de la información y la comunicación (TIC) ha t
4. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Unidad IV: Bases de Datos Distribuidas Parcial | Unidad V: Datawarehouse Parcial | Pagina: 6]
   > Materia: Bases de Datos Avanzadas Sección: Unidad IV: Bases de Datos Distribuidas Parcial | Unidad V: Datawarehouse Parcial Unidad VI: Datamining Parcial + TP Unidad VII: Bases de Datos OO Parcial NO
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Bases de Datos Avanzadas | Pagina: 1]
   > Materia: Bases de Datos Avanzadas Sección: Bases de Datos Avanzadas PRESENTACIÓN DE LA MATERIA Facultad de Ciencia Y Tecnología Base de Datos Avanzadas

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 718 | salida: 14 | total: 732

---

### Pregunta 8

> - ¿En qué asignaturas de 4to año se analiza el impacto de la Inteligencia Artificial en las personas o las organizaciones, y desde qué enfoque lo aborda cada una?

**Chunks de contexto:**

1. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Unidad 2: Relaciones Humanas en el Contexto Organizacional | Pagina: 2]
   > Materia: Informática y Recursos Humanos Sección: Unidad 2: Relaciones Humanas en el Contexto Organizacional 1. Comunicación interna y cultura organizacional en entornos digitales. 2. Inteligencia emo
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Ventajas | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Ventajas comparativas entre las distintas representaciones. Comportamiento de Agentes Basados en Conocimientos. Capítulo IV Diseño de los Sistemas Expe
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Editorial: Pearson Educación (2004 o versiones posteriores) | Pagina: 4]
   > Materia: Inteligencia Artificial Sección: Editorial: Pearson Educación (2004 o versiones posteriores) Título: Aprendizaje automático y aprendizaje profundo con Python, scikit-learn y Tensor Flow-
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Bibliografía Nacional: | Pagina: 2]
   > Materia: Informática y Recursos Humanos Sección: Bibliografía Nacional: Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio darán aspectos legales fundamentales para comprender el impacto normativo de las TIC en el ám

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 684 | salida: 14 | total: 698

---

### Pregunta 9

> - Los requisitos para regularizar en Bases de Datos Avanzadas y en Redes y Comunicaciones, ¿son iguales? ¿Qué diferencias tienen?

**Chunks de contexto:**

1. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 9]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Software utilizado PostgreSQL 9.6 o superi
2. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Régimen | Regularidad: | Pagina: 7]
   > Materia: Bases de Datos Avanzadas Sección: Régimen | Regularidad: Asistencia: Según norma vigente. Todos los trabajos prácticos aprobados.
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE superior o igual a los 60 puntos. Tener aprobado con 60 puntos los tres parcia
4. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Días de clase | Pagina: 3]
   > Materia: Bases de Datos Avanzadas Sección: Días de clase Lunes: 13:30 a 15:30 -> Teoría Viernes: 17:00 a 19:00 -> Práctica NOTA: Los horarios están en proceso de evaluación y pueden sufrir cambios
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Programa Sintético | Unidad I: Bases de Datos Activas | Unidad II: Bases de Datos Temporales | Unidad III: Bases de Datos Geográficas | Unidad IV: Bases de Datos Distribuidas | Unidad V: Datawarehouse | Unidad VI: Datamining | Unidad VII: Bases de Datos Orientadas a Objetos | Pagina: 6]
   > Materia: Bases de Datos Avanzadas Sección: Programa Sintético | Unidad I: Bases de Datos Activas | Unidad II: Bases de Datos Temporales | Unidad III: Bases de Datos Geográficas | Unidad IV: Bases de D

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 848 | salida: 14 | total: 862

---

### Pregunta 10

> - ¿De qué manera el algoritmo de la ruta más corta de Redes de la unidad 7 se relaciona con los modelos de transporte y transbordo de Investigación Operativa en la Unidad 5?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad VII: -Capa de Red- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad VII: -Capa de Red- la conexión, Comparación entre las subredes de circuitos virtuales y las de datagramas); Algoritmos de enrutamiento (Principio de opti
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Análisis | Pagina: 1]
   > Materia: Investigación Operativa Sección: Análisis de dualidad y sensibilidad básica en modelos lineales. Unidad IV: -Modelos de Transporte y Transbordo- El problema del transporte: estructur
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Problemas | Pagina: 1]
   > Materia: Investigación Operativa Sección: Problemas de transbordo y el problema de la asignación
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible vía URL que
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: (Método | Pagina: 1]
   > Materia: Investigación Operativa Sección: (Método Húngaro). Unidad V: -Programación Dinámica- Características de la Programación Dinámica (PD).

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 619 | salida: 14 | total: 633

---

### Pregunta 11

> - Si quiero promocionar todas las materias de 4to año, ¿cuál es la diferencia de promedio exigido entre Investigación Operativa e Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: | Pagina: 1]
   > Materia: Investigación Operativa Sección: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: - ALUMNO PROMOCIONADO: El estudiante logrará la promoción directa si alcanza un prom
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Ventajas | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Ventajas comparativas entre las distintas representaciones. Comportamiento de Agentes Basados en Conocimientos. Capítulo IV Diseño de los Sistemas Expe
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% de asistencia a las clases teóricas y prácticas.
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Diferencias | Pagina: 1]
   > Materia: Investigación Operativa Sección: Diferencias entre
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas ustificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen reprobado. Software de Aplicación - Inv

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 631 | salida: 14 | total: 645

---

### Pregunta 12

> - ¿Qué herramientas de software se recomiendan en la carrera para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas ción de modelos de optimización y problemas de gestión: - LINDO (Linear, Interactive, and Discrete Optimizer): Software especializado en la re
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas ustificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen reprobado. Software de Aplicación - Inv
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible vía URL que
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Problema | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Problema de separación lineal. Aplicaciones.
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad VII: -Capa de Red- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad VII: -Capa de Red- la conexión, Comparación entre las subredes de circuitos virtuales y las de datagramas); Algoritmos de enrutamiento (Principio de opti

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 673 | salida: 14 | total: 687

---

### Pregunta 13

> - ¿Dónde puedo descargar la materia de Cálculo de 1er año?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 1- PROGRAMA DE CONTENIDOS | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: 1- PROGRAMA DE CONTENIDOS de computadora, aplicaciones de negocios, domésticas, distintos usuarios. Hardware de redes, Sistema Cliente/Servidor, tipos de redes
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Visto | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Visto en https://ediciones.ungs.edu.ar/wp-content/uploads/2018/09/9789876301190-completo.pdf Material audiovisual de la unidad Sobre investigación M
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas s
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: SANTA | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: SANTA CRUZ; Año de la carrera a la que pertenece la cátedra: 4 Régimen de la materia: Anual Carga horaria semanal: 3 horas Correlativa: Ingeniería d
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Primer | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Primer Orden.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 680 | salida: 14 | total: 694

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
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Visto | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Visto de aplicaciones Web escalables / Martín Gerardo Herrlein, Daniel Sebastián Pacheco; director Aldo Daniel Sigura; codirector Pablo Emanuel Goett

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 730 | salida: 14 | total: 744

---

### Pregunta 15

> - ¿Cuál es el costo de la certificación oficial de Cisco que se menciona como opcional en la planificación?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Sitios web sobre normativas, tecnologías y soluciones, opcional: | Pagina: 5]
   > Materia: Comunicacion y Redes Sección: Sitios web sobre normativas, tecnologías y soluciones, opcional: IETF -> www.ietf.org IEEE -> www.ieee.org ISO -> www.iso.org CISCO -> www.cisco.com IANA -> www
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS istintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] Cisco Systems: Academia de Networking de Cisco Systems: Guí
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas s
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: IV. BIBLIOGRAFÍA GENERAL | Bibliografía Básica: | Pagina: 3]
   > Materia: Informática y Recursos Humanos Sección: IV. BIBLIOGRAFÍA GENERAL | Bibliografía Básica: Propiedad intelectual (Ley 11.723) - (modificatoria Ley 25.036) Código Civil y Comercial de la Nación
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 1- PROGRAMA DE CONTENIDOS | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: 1- PROGRAMA DE CONTENIDOS endencia del networking). Explicar el propósito de IOS como Sistema Operativo de red, Explicar cómo acceder al IOS y cómo explorarlo p

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 839 | salida: 14 | total: 853

---

### Pregunta 16

> - Para la Promoción Directa, se exige la aprobación de la totalidad de los trabajos prácticos (TP 1 al TP 5). ¿Cuál es la calificación numérica mínima que debe obtenerse en cada TP individual para que se considere aprobado?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Visto | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Visto a la condición de Promoción Directa, el/la estudiante deberá cumplir con los siguientes requisitos: - 80 % de asistencia a la cursada. - Aproba
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Es | Pagina: 1]
   > Materia: Investigación Operativa Sección: Es requisito indispensable la entrega y aprobación de los dos trabajos prácticos obligatorios y el cumplimiento del
3. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Visto | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Visto Protocolo de Internet versión 6 (IPv6) / Rodrigo Paúl Basso, Maximiliano Sebastián Toso; director Julio Alberto Aldonate; codirector Luciano Ma
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Cumplida | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Cumplida evaluación teórica oral y realizar la defensa oral del trabajo práctico integrador. La calificación del trabajo integrador se
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE sistencia a una de estas evaluaciones se tomará como la reprobación de la mism

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 840 | salida: 14 | total: 854

---

### Pregunta 17

> - ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible vía URL que
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas ción de modelos de optimización y problemas de gestión: - LINDO (Linear, Interactive, and Discrete Optimizer): Software especializado en la re
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Problema | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Problema de separación lineal. Aplicaciones.
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Metodología | Pagina: 1]
   > Materia: Investigación Operativa Sección: Metodología de la construcción de modelos: definición del problema, construcción del modelo matemático, obtención de una solución y validaci
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Reactivo | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Reactivo Simple.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 530 | salida: 14 | total: 544

---

### Pregunta 18

> - ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas a nota del examen original. Protocolos de Evaluación: Los resultados se publicarán en un plazo de siete días corridos tras la evaluación. Los
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% de asistencia a las clases teóricas y prácticas.
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mism
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 13 04 de junio Presencial Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 13 04 de junio Presencial Teoría Marco metodológico I: enfoque y tipo de investigación / muestra 14 11 de junio Virtual Práctica

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 659 | salida: 14 | total: 673

---

## Conversacion 5

**Puntaje evaluado: 10.5 / 18**

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
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Ventajas | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Ventajas comparativas entre las distintas representaciones. Comportamiento de Agentes Basados en Conocimientos. Capítulo IV Diseño de los Sistemas Expe

**Respuesta:**

"Según el Contexto proporcionado, los contenidos de la materia Inteligencia Artificial incluyen: 

1. Inteligencia Artificial Programa de Contenidos | Capítulo I Agentes Inteligentes: 
    - Introducción a la IA.
    - Definiciones y objetivos.
    - Herramientas y técnicas provistas por el área IA.
2. Descripción de los temas específicos a desarrollarse en la asignatura.
3. Métodos y mensajes. Representación de Conocimientos mediante reglas. 
    - Estructura básica.
    - Representación de reglas mediante objetos.
4. Integración de la solución difusa final. 
    - Proceso de Defuzzificación, definición.
    - Método del centroide.
    - Método de máxima.
    - Influencia de la aplicación de los distintos métodos sobre el funcionamiento del sistema.
5. Agentes Basados en Lógica Difusa.
6. Capítulo VIII Redes Neuronales Artificiales (RNA). 
    - Generalidades.
    - Conceptos básicos.
    - Reseña Histórica.
7. Ventajas comparativas entre las distintas representaciones. 
    - Comportamiento de Agentes Basados en Conocimientos.
8. Capítulo IV Diseño de los Sistemas Expertos. 
    - Definición y descripción de sus módulos componentes."

**Tokens:** entrada: 633 | salida: 305 | total: 938

---

### Pregunta 2

> - ¿En qué materia se enseña el concepto de Lógica Difusa?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Capítulo VI | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Capítulo VI Lógica Difusa (Fuzzy). Consideraciones generales, Conjuntos Difusos, definición.
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Integración | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad II: -Capa física concepto y medios- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad II: -Capa física concepto y medios- . Control de enlace lógico, Control de acceso al medio. Implementación de ethernet. Dominios de colisiones - La antig
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Visto | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Visto Deep Learning aplicado al aprendizaje automático de ontologías para la representación del conocimiento a partir de texto no estructurado / Enzo
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Respecto a las clases: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Respecto a las clases: La cátedra implementará el modelo de aula invertida, en el que los estudiantes adquieren los conocimientos teóricos de mane

**Respuesta:**

La respuesta se puede encontrar en el CONTEXTO.

El CONTEXTO establece que el concepto de Lógica Difusa se enseña en la Materia: Inteligencia Artificial.

**Tokens:** entrada: 886 | salida: 42 | total: 928

---

### Pregunta 3

> - ¿Cuál es el plan de estudios de Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: SANTA | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: SANTA CRUZ; Año de la carrera a la que pertenece la cátedra: 4 Régimen de la materia: Anual Carga horaria semanal: 3 horas Correlativa: Ingeniería d
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 1 12 de marzo Presencial Teórico/práctico Presentación de la asignatura | 2 19 de marzo Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 1 12 de marzo Presencial Teórico/práctico Presentación de la asignatura | 2 19 de marzo Virtual Teoría Conceptos generales para introducción 3 26 de
3. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Dicho | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Dicho examen contará con una (1) instancia de recuperación, conforme al cronograma establecido por la cátedra. - Entrega obligatoria de
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Estructura del aula virtual: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Estructura del aula virtual: Los materiales educativos estarán alojados en el aula virtual "Metodología de la Investigación" dentro de la plataform
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Unidad 3: La dimensión de la estrategia general de investigación | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Unidad 3: La dimensión de la estrategia general de investigación ¿Cómo se va a estudiar el problema? Tipo de diseños cuantitativos o cualitativos. La

**Respuesta:**

De acuerdo con la información proporcionada, el plan de estudios de Metodología de la Investigación incluye lo siguiente:

- Un programa de clase que consta de 7 reuniones presenciales y virtuales.
- El calendario del curso de Metodología de la Investigación:

- 1 12 de marzo: Presentación de la asignatura (Presencial, Teórico/práctico)
- 2 19 de marzo: Teoría (Virtual) - Conceptos generales para introducción
- 3 26 de marzo: Virtual - Práctica (Normas APA/ escritura académica)
- 4 2 de abril: Sin clase
- 5 9 de abril: Presencial - Teoría (Tema/problema)
- 6 16 de abril: Virtual - Práctica (Pregunta de investigación, variables, unidad de análisis, contexto, y antecedentes)
- 7 23 de abril: Virtual - Teoría (Pregunta de investigación)
- 8 30 de abril: Examen presencial con una instancia de recuperación.

- Un plan de trabajos prácticos. El primer trabajo es práctico. Los estudiantes deberán seleccionar un artículo de investigación sobre un tema de interés específico relacionado al campo profesional.

- Un aula virtual dentro de la plataforma Moodle con los siguientes apartados: 
  - Inicio del curso: incluye información general de la cátedra, incluyendo el programa, el equipo docente, el cronograma, los objetivos, los materiales utilizados, el enlace de videoconferencia, la descripción de la metodología de trabajo y evaluación, la bibliografía, y un foro de discusión.

**Tokens:** entrada: 1146 | salida: 375 | total: 1521

---

### Pregunta 4

> - En Comunicaciones y Redes, ¿cómo hago para quedar como alumno regular?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE El alumno accederá a la condición de REGULAR, si cumple con las siguientes con
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Visto | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Visto . Guillerón. 2018 Red Privada Virtual (VPM) sobre Protocolo de Internet versión 6 (IPv6) / Rodrigo Paúl Basso, Maximiliano Sebastián Toso; dire
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: SEDE: Oro Verde | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler. AÑO ACADEMICO: 2023 PLAN DE EST
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 8]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Comunicación De rutina y consultas: Lista

**Respuesta:**

Dispongo de información en mis documentos para responder esta consulta. 

De la información proporcionada en el contexto, obtenemos que para quedar como alumno REGULAR en la materia Comunicación y Redes, el estudiante debe cumplir con la condición establecida en el documento "Planificación 2025 - Comunicacion y Redes.pdf". Esta condición establece que el estudiante debe obtener en los 3 parciales una calificación promedio superior o igual a los 60 puntos.

**Tokens:** entrada: 889 | salida: 107 | total: 996

---

### Pregunta 5

> - ¿Qué instancias de recuperación nos provee Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% - ALUMNO LIBRE: Revestirá esta condición todo estudiante que no logre cumplimentar alguno de los requisitos de puntaje, trabajos prácticos o as
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mism
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Permite | Pagina: 2]
   > Materia: Investigación Operativa Sección: Permite resolver problemas de programación lineal
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: PLANIFICACIÓN INVESTIGACIÓN OPERATIVA | Pagina: 1]
   > Materia: Investigación Operativa Sección: PLANIFICACIÓN INVESTIGACIÓN OPERATIVA Unidad I: -Introducción y Modelos Matemáticos- Definición y origen de la Investigación Operativa.
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: (LP), | Pagina: 2]
   > Materia: Investigación Operativa Sección: (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al análisis

**Respuesta:**

La Investigación Operativa ofrece dos oportunidades de recuperatorio totales, lo que significa que los estudiantes tienen dos chances para mejorar su calificación en caso de no haber logrado cumplir con algunos de los requisitos de puntaje, trabajos prácticos o asistencia detallados.

**Tokens:** entrada: 761 | salida: 61 | total: 822

---

### Pregunta 6

> - ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: (LP), | Pagina: 2]
   > Materia: Investigación Operativa Sección: (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al análisis
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Incluye | Pagina: 2]
   > Materia: Investigación Operativa Sección: Incluye módulos para el
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS 4- BIBLIOGRAFIA Obligatoria Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Ver
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 15 18 de junio Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 15 18 de junio Virtual Teoría 10 de septiembre Virtual Tutorías Avances proyectos a la cátedra- Grupos Tamara 17 de septiembre Teoría Coloquio Avanc

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 908 | salida: 14 | total: 922

---

### Pregunta 7

> - ¿Qué vinculaciones temáticas existen entre Bases de Datos Avanzadas y Comunicación y Redes que resulten pertinentes para el perfil de un arquitecto de sistemas?

**Chunks de contexto:**

1. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Bases de Datos Avanzadas | Pagina: 2]
   > Materia: Bases de Datos Avanzadas Sección: Bases de Datos Avanzadas Equipo docente Trossero, Sebastián Teoría Trossero.sebastian@uader.edu.ar Schmuckler, Jorge Práctica Schmukler.jorge@uader.edu.ar
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 1- PROGRAMA DE CONTENIDOS | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: 1- PROGRAMA DE CONTENIDOS . Conceptos usados en Comunicaciones y Redes: Uso de la redes de computadora, aplicaciones de negocios, domésticas, distintos usuarios
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio . FUNDAMENTACIÓN El avance de las tecnologías de la información y la comunicación (TIC) ha tr
4. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Unidad IV: Bases de Datos Distribuidas Parcial | Unidad V: Datawarehouse Parcial | Pagina: 6]
   > Materia: Bases de Datos Avanzadas Sección: Unidad IV: Bases de Datos Distribuidas Parcial | Unidad V: Datawarehouse Parcial Unidad VI: Datamining Parcial + TP Unidad VII: Bases de Datos OO Parcial NO
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Bases de Datos Avanzadas | Pagina: 1]
   > Materia: Bases de Datos Avanzadas Sección: Bases de Datos Avanzadas PRESENTACIÓN DE LA MATERIA Facultad de Ciencia Y Tecnología Base de Datos Avanzadas

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta. Sin embargo, puedo hacer una inferencia sobre la conexión entre ambas materias. 

En la Sección "Conceptos usados en Comunicaciones y Redes" del documento "Planificación 2025 - Comunicacion y Redes.pdf" se menciona el Sistema Cliente/Servidor y redes, que también están relacionados con la gestión de bases de datos. Por otro lado, en la sección "Unidad IV: Bases de Datos Distribuidas Parcial" del documento "BDA Planificacion.pdf", se menciona la distribución de bases de datos, lo que también se relaciona con el concepto de redes. 

Sin embargo, para una respuesta más precisa, te recomendaría consultar los planes de estudio específicos y materiales de las asignaturas "Bases de Datos Avanzadas" y "Comunicación y Redes" para que puedas identificar de manera más precisa las conexiones temáticas que existan entre ambas materias.

**Tokens:** entrada: 771 | salida: 218 | total: 989

---

### Pregunta 8

> - ¿En qué asignaturas de 4to año se analiza el impacto de la Inteligencia Artificial en las personas o las organizaciones, y desde qué enfoque lo aborda cada una?

**Chunks de contexto:**

1. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Unidad 2: Relaciones Humanas en el Contexto Organizacional | Pagina: 2]
   > Materia: Informática y Recursos Humanos Sección: Unidad 2: Relaciones Humanas en el Contexto Organizacional 1. Comunicación interna y cultura organizacional en entornos digitales. 2. Inteligencia emo
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Ventajas | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Ventajas comparativas entre las distintas representaciones. Comportamiento de Agentes Basados en Conocimientos. Capítulo IV Diseño de los Sistemas Expe
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Editorial: Pearson Educación (2004 o versiones posteriores) | Pagina: 4]
   > Materia: Inteligencia Artificial Sección: Editorial: Pearson Educación (2004 o versiones posteriores) Título: Aprendizaje automático y aprendizaje profundo con Python, scikit-learn y Tensor Flow-
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Bibliografía Nacional: | Pagina: 2]
   > Materia: Informática y Recursos Humanos Sección: Bibliografía Nacional: Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Condiciones | Pagina: 3]
   > Materia: Inteligencia Artificial Sección: Condiciones de inicialización, problema de saturación prematura. Regiones de Decisión. Modo de operación autoasociativo. Capítulo X Generalización en

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta. La información proporcionada no incluye detalles sobre la programación curricular de 4to año y como se aborda el impacto de la Inteligencia Artificial en las personas o organizaciones.

**Tokens:** entrada: 665 | salida: 54 | total: 719

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

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 856 | salida: 14 | total: 870

---

### Pregunta 10

> - ¿De qué manera el algoritmo de la ruta más corta de Redes de la unidad 7 se relaciona con los modelos de transporte y transbordo de Investigación Operativa en la Unidad 5?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad VII: -Capa de Red- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad VII: -Capa de Red- ; Algoritmos de enrutamiento (Principio de optimización, Enrutamiento por la ruta más corta, Inundación, Enrutamiento por vector de di
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Análisis | Pagina: 1]
   > Materia: Investigación Operativa Sección: Análisis de dualidad y sensibilidad básica en modelos lineales. Unidad IV: -Modelos de Transporte y Transbordo- El problema del transporte: estructur
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Problemas | Pagina: 1]
   > Materia: Investigación Operativa Sección: Problemas de transbordo y el problema de la asignación
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible vía URL que
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: (Método | Pagina: 1]
   > Materia: Investigación Operativa Sección: (Método Húngaro). Unidad V: -Programación Dinámica- Características de la Programación Dinámica (PD).

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 664 | salida: 14 | total: 678

---

### Pregunta 11

> - Si quiero promocionar todas las materias de 4to año, ¿cuál es la diferencia de promedio exigido entre Investigación Operativa e Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: | Pagina: 1]
   > Materia: Investigación Operativa Sección: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: - ALUMNO PROMOCIONADO: El estudiante logrará la promoción directa si alcanza un prom
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% de asistencia a las clases teóricas y prácticas.
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Diferencias | Pagina: 1]
   > Materia: Investigación Operativa Sección: Diferencias entre
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Composición | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Composición MAX-MIN. Capítulo VII Sistemas Difusos. Consideraciones generales. Representación de conocimiento estructurado mediante reglas lingüísticas.
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas s

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 667 | salida: 14 | total: 681

---

### Pregunta 12

> - ¿Qué herramientas de software se recomiendan en la carrera para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas de modelos de optimización y problemas de gestión: - LINDO (Linear, Interactive, and Discrete Optimizer): Software especializado en la resoluci
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas la evaluación. Los exámenes se desarrollarán estrictamente en los bloques horarios asignados a la materia. La ausencia no justificada
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible vía URL que
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Problema | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Problema de separación lineal. Aplicaciones.
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Sitios web sobre normativas, tecnologías y soluciones, opcional: | Pagina: 5]
   > Materia: Comunicacion y Redes Sección: Sitios web sobre normativas, tecnologías y soluciones, opcional: LACNIC -> http://lacnic.net/sp/ LAC IPV6 TF -> www.lac.ipv6tf.org 3M -> www.3m.com FURUKAWA ->

**Respuesta:**

La herramienta de software recomendada para resolver problemas de optimización lineal es LINDO (Linear, Interactive, and Discrete Optimizer).

**Tokens:** entrada: 818 | salida: 31 | total: 849

---

### Pregunta 13

> - ¿Dónde puedo descargar la materia de Cálculo de 1er año?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS 4- BIBLIOGRAFIA Obligatoria Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Ver
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Visto | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Visto en https://ediciones.ungs.edu.ar/wp-content/uploads/2018/09/9789876301190-completo.pdf
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas s
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Primer | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Primer Orden.
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Bibliografía Nacional: | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Bibliografía Nacional: Ley de Teletrabajo (Ley 27.555).

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 610 | salida: 14 | total: 624

---

### Pregunta 14

> - El profesor Ing. Jorge L. Schmukler da clases en Bases de Datos Avanzadas, en Inteligencia Artificial y en Redes y Comunicaciones.

**Chunks de contexto:**

1. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Bases de Datos Avanzadas | Pagina: 2]
   > Materia: Bases de Datos Avanzadas Sección: Bases de Datos Avanzadas Equipo docente Trossero, Sebastián Teoría Trossero.sebastian@uader.edu.ar Schmuckler, Jorge Práctica Schmukler.jorge@uader.edu.ar
2. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Días de clase | Pagina: 4]
   > Materia: Bases de Datos Avanzadas Sección: Días de clase Cronograma de clases Presenciales/Virtuales A partir de este año la materia será dictada de manera bimodal. El cronograma será definido en su
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Principal (Disponibles en biblioteca) | Pagina: 4]
   > Materia: Inteligencia Artificial Sección: Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig.
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Clases | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Clases e instancias.
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad VII: -Capa de Red- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad VII: -Capa de Red- . Direcciones (especiales, públicas y privadas). Direccionamiento estático y dinámico. Planificación del direccionamiento (segmentació

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 671 | salida: 14 | total: 685

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
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas la evaluación. Los exámenes se desarrollarán estrictamente en los bloques horarios asignados a la materia. La ausencia no justificada

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 971 | salida: 14 | total: 985

---

### Pregunta 16

> - Para la Promoción Directa, se exige la aprobación de la totalidad de los trabajos prácticos (TP 1 al TP 5). ¿Cuál es la calificación numérica mínima que debe obtenerse en cada TP individual para que se considere aprobado?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: | Pagina: 1]
   > Materia: Investigación Operativa Sección: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: - ALUMNO PROMOCIONADO: El estudiante logrará la promoción directa si alcanza un prom
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Visto | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Visto . Guillerón. 2018 Red Privada Virtual (VPM) sobre Protocolo de Internet versión 6 (IPv6) / Rodrigo Paúl Basso, Maximiliano Sebastián Toso; dire
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Asimismo, | Pagina: 1]
   > Materia: Investigación Operativa Sección: Asimismo, deberá acreditar la aprobación de los dos trabajos prácticos de la cátedra y mantener una asistencia mínima del
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Cumplida | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Cumplida integrador se determinará exclusivamente en la mesa de examen, junto con la nota correspondiente a la instancia teórica, e
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Visto | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Visto de revisión y devolución con el equipo docente. El trabajo deberá entregarse con una antelación mínima de diez (10) días há

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 958 | salida: 14 | total: 972

---

### Pregunta 17

> - ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible vía URL que
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas de modelos de optimización y problemas de gestión: - LINDO (Linear, Interactive, and Discrete Optimizer): Software especializado en la resoluci
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex y el
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Problema | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Problema de separación lineal. Aplicaciones.
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Metodología | Pagina: 1]
   > Materia: Investigación Operativa Sección: Metodología de la construcción de modelos: definición del problema, construcción del modelo matemático, obtención de una solución y validaci

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 524 | salida: 14 | total: 538

---

### Pregunta 18

> - ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mism
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% de asistencia a las clases teóricas y prácticas.
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 13 04 de junio Presencial Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 13 04 de junio Presencial Teoría Marco metodológico I: enfoque y tipo de investigación / muestra 14 11 de junio Virtual Práctica
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Visto | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Visto de revisión y devolución con el equipo docente. El trabajo deberá entregarse con una antelación mínima de diez (10) días há

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 805 | salida: 14 | total: 819

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
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Ventajas | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Ventajas comparativas entre las distintas representaciones. Comportamiento de Agentes Basados en Conocimientos. Capítulo IV Diseño de los Sistemas Expe

**Respuesta:**

El contenido del tema es el siguiente:

**Programa de Contenidos | Capítulo I Agentes Inteligentes**

*   Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas por el área IA.

**Descripción**

*   Los temas específicos a desarrollarse en la asignatura son:

1.  Capítulo I Agentes Inteligentes
2.  Capítulo IV Diseño de los Sistemas Expertos
3.  Capítulo VIII Redes Neuronales Artificiales (RNA). Generalidades, conceptos básicos Reseña Histórica.
4.  Comportamiento de Agentes Basados en Conocimientos.
5.  Capítulo VIII Redes Neuronales Artificiales (RNA). Generalidades, conceptos básicos Reseña Histórica.

**Métodos**

*   Representación de Conocimientos mediante reglas. Estructura básica. Representación de reglas mediante objetos.
*   Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación de los distintos métodos sobre el funcionamiento del sistema.

**Integración de la solución difusa final**

*   Agentes Basados en Lógica Difusa.

**Ventajas comparativas entre las distintas representaciones**

**Tokens:** entrada: 633 | salida: 293 | total: 926

---

### Pregunta 2

> - ¿En qué materia se enseña el concepto de Lógica Difusa?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Capítulo VI | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Capítulo VI Lógica Difusa (Fuzzy). Consideraciones generales, Conjuntos Difusos, definición.
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Integración | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Estructuras | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Estructuras basadas en Lógica.
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad VII: -Capa de Red- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad VII: -Capa de Red- . Clase de direccionamiento (clase a, b, c, d y e). Prefijo y Mascara de red. Lógica de and. Calculo de direcciones. División de subre
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Respecto a las clases: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Respecto a las clases: La cátedra implementará el modelo de aula invertida, en el que los estudiantes adquieren los conocimientos teóricos de mane

**Respuesta:**

La respuesta a esta pregunta se encuentra en el Contexto. La Lógica Difusa se enseña en la materia de Inteligencia Artificial.

**Tokens:** entrada: 796 | salida: 32 | total: 828

---

### Pregunta 3

> - ¿Cuál es el plan de estudios de Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: SANTA | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: SANTA CRUZ; Año de la carrera a la que pertenece la cátedra: 4 Régimen de la materia: Anual Carga horaria semanal: 3 horas Correlativa: Ingeniería d
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 1 12 de marzo Presencial Teórico/práctico Presentación de la asignatura | 2 19 de marzo Virtual Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 1 12 de marzo Presencial Teórico/práctico Presentación de la asignatura | 2 19 de marzo Virtual Teoría Conceptos generales para introducción 3 26 de
3. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Investigación | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Investigación brindar conocimientos y herramientas para indagar la realidad en la búsqueda y desnaturalización de problemas, tanto de
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Dicho | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Dicho examen contará con una (1) instancia de recuperación, conforme al cronograma establecido por la cátedra. - Entrega obligatoria de
5. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Estructura del aula virtual: | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Estructura del aula virtual: Los materiales educativos estarán alojados en el aula virtual "Metodología de la Investigación" dentro de la plataform

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1179 | salida: 14 | total: 1193

---

### Pregunta 4

> - En Comunicaciones y Redes, ¿cómo hago para quedar como alumno regular?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE El alumno accederá a la condición de REGULAR, si cumple con las siguientes con
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Visto | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Visto . 2018 Requisitos para rendir como estudiantes regulares, promocionales y libres: a. Promoción Directa Para acceder a la condición de Promoción
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: SEDE: Oro Verde | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler. AÑO ACADEMICO: 2023 PLAN DE EST
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 8]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Comunicación De rutina y consultas: Lista

**Respuesta:**

Dispongo de información en mis documentos para responder esta consulta.

Para quedar como alumno regular en Comunicaciones y Redes, debes obtener una calificación promedio superior o igual a los 60 puntos en los 3 parciales, según se especifica en el Documento "Planificación 2025 - Comunicacion y Redes.pdf" sección "2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE".

**Tokens:** entrada: 906 | salida: 106 | total: 1012

---

### Pregunta 5

> - ¿Qué instancias de recuperación nos provee Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 2]
   > Materia: Investigación Operativa Sección: 80% - ALUMNO LIBRE: Revestirá esta condición todo estudiante que no logre cumplimentar alguno de los requisitos de puntaje, trabajos prácticos o as
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mism
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Permite | Pagina: 2]
   > Materia: Investigación Operativa Sección: Permite resolver problemas de programación lineal
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: PLANIFICACIÓN INVESTIGACIÓN OPERATIVA | Pagina: 1]
   > Materia: Investigación Operativa Sección: PLANIFICACIÓN INVESTIGACIÓN OPERATIVA Unidad I: -Introducción y Modelos Matemáticos- Definición y origen de la Investigación Operativa.
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas a la materia. La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen repr

**Respuesta:**

La investigación operativa nos ofrece dos oportunidades de recuperatorio totales.

**Tokens:** entrada: 829 | salida: 16 | total: 845

---

### Pregunta 6

> - ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: (LP), | Pagina: 2]
   > Materia: Investigación Operativa Sección: (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al análisis
2. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Tamara | Pagina: 1]
   > Materia: Metodología de la Investigación Sección: Tamara los contenidos teóricos previstos en el programa, a fin de que el segundo cuatrimestre esté destinado de manera prioritaria
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Incluye | Pagina: 2]
   > Materia: Investigación Operativa Sección: Incluye módulos para el
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 3- PROGRAMA DE TRABAJOS PRACTICOS | Pagina: 4]
   > Materia: Comunicacion y Redes Sección: 3- PROGRAMA DE TRABAJOS PRACTICOS La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio . Además, se abordarán aspectos legales fundamentales para comprender el impacto normativo de

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 819 | salida: 14 | total: 833

---

### Pregunta 7

> - ¿Qué vinculaciones temáticas existen entre Bases de Datos Avanzadas y Comunicación y Redes que resulten pertinentes para el perfil de un arquitecto de sistemas?

**Chunks de contexto:**

1. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Bases de Datos Avanzadas | Pagina: 2]
   > Materia: Bases de Datos Avanzadas Sección: Bases de Datos Avanzadas Equipo docente Trossero, Sebastián Teoría Trossero.sebastian@uader.edu.ar Schmuckler, Jorge Práctica Schmukler.jorge@uader.edu.ar
2. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Unidad IV: Bases de Datos Distribuidas Parcial | Unidad V: Datawarehouse Parcial | Pagina: 6]
   > Materia: Bases de Datos Avanzadas Sección: Unidad IV: Bases de Datos Distribuidas Parcial | Unidad V: Datawarehouse Parcial Unidad VI: Datamining Parcial + TP Unidad VII: Bases de Datos OO Parcial NO
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 1- PROGRAMA DE CONTENIDOS | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: 1- PROGRAMA DE CONTENIDOS Unidad I: Introducción -Importancia e Influencia de las Redes en Nuestras Vidas: Comunicación en un mundo centrado en la red, herramie
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio I. FUNDAMENTACIÓN El avance de las tecnologías de la información y la comunicación (TIC) ha t
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Editorial: Addison Wesley | Pagina: 10]
   > Materia: Bases de Datos Avanzadas Sección: Editorial: Addison Wesley Libro: Fundamentos de Bases de Datos Autor: Silberschatz / Korth / Sudarshan Editorial: Mc Graw Hill Libro: Introducción a los SIS

**Respuesta:**

La pregunta del usuario plantea una relación entre dos materias distintas, Bases de Datos Avanzadas (BDA) y Comunicación y Redes. Se requiere identificar un enlace lógico relevante.

Para responder la pregunta es necesario encontrar información en los documentos proporcionados que relacionen de alguna manera conceptos de Bases de Datos Avanzadas con Comunicación y Redes.

**Análisis de Contexto:**
1. El Contexto está compuesto por varios documentos que abarcan materias como Bases de Datos Avanzadas, Comunicación y Redes e Informática y Recursos Humanos.
2. El documento BDA Planificacion.pdf destaca la Unidad VI: Datamining Parcial y la Unidad VII: Bases de Datos OO Parcial, que podría relacionarse con el perfil de un arquitecto de sistemas.
3. El contexto del Plan de Estudio de la Materia Informática y Recursos Humanos describe cómo las tecnologías de la información han transformado las relaciones humanas dentro de las organizaciones.

**Relación entre Bases de Datos Avanzadas y Comunicación y Redes**

El contexto proporcionado no brinda información directa sobre una vinculación temática explícita entre Bases de Datos Avanzadas y Comunicación y Redes.

La relación lógica más plausible entre las dos materias puede estar asociada con la transformación tecnológica descrita en el Plan de Estudio de Informática y Recursos Humanos. El avance de las TIC y el desarrollo de redes ha provocado cambios significativos en el mundo laboral y las relaciones humanas. 

Una de las habilidades principales de un arquitecto de sistemas es diseñar y implementar soluciones tecnológicas que aborden estos desafíos.

De manera indirecta, se puede concluir que el perfil de un arquitecto de sistemas debe abordar la intersección de conocimientos técnicos y de tecnologías de la comunicación, así como la necesidad de considerar el impacto de estos cambios tecnológicos en las organizaciones y la sociedad.

La respuesta que se da es la única posible a partir de la información proporcionada.

**Tokens:** entrada: 874 | salida: 474 | total: 1348

---

### Pregunta 8

> - ¿En qué asignaturas de 4to año se analiza el impacto de la Inteligencia Artificial en las personas o las organizaciones, y desde qué enfoque lo aborda cada una?

**Chunks de contexto:**

1. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Unidad 2: Relaciones Humanas en el Contexto Organizacional | Pagina: 2]
   > Materia: Informática y Recursos Humanos Sección: Unidad 2: Relaciones Humanas en el Contexto Organizacional 1. Comunicación interna y cultura organizacional en entornos digitales. 2. Inteligencia emo
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Ventajas | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Ventajas comparativas entre las distintas representaciones. Comportamiento de Agentes Basados en Conocimientos. Capítulo IV Diseño de los Sistemas Expe
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Editorial: Pearson Educación (2004 o versiones posteriores) | Pagina: 4]
   > Materia: Inteligencia Artificial Sección: Editorial: Pearson Educación (2004 o versiones posteriores) Título: Aprendizaje automático y aprendizaje profundo con Python, scikit-learn y Tensor Flow-
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio . Además, se abordarán aspectos legales fundamentales para comprender el impacto normativo de
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Bibliografía Nacional: | Pagina: 2]
   > Materia: Informática y Recursos Humanos Sección: Bibliografía Nacional: Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 690 | salida: 14 | total: 704

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

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 856 | salida: 14 | total: 870

---

### Pregunta 10

> - ¿De qué manera el algoritmo de la ruta más corta de Redes de la unidad 7 se relaciona con los modelos de transporte y transbordo de Investigación Operativa en la Unidad 5?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad VII: -Capa de Red- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad VII: -Capa de Red- ; Algoritmos de enrutamiento (Principio de optimización, Enrutamiento por la ruta más corta, Inundación, Enrutamiento por vector de di
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Análisis | Pagina: 1]
   > Materia: Investigación Operativa Sección: Análisis de dualidad y sensibilidad básica en modelos lineales. Unidad IV: -Modelos de Transporte y Transbordo- El problema del transporte: estructur
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Problemas | Pagina: 1]
   > Materia: Investigación Operativa Sección: Problemas de transbordo y el problema de la asignación
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad VII: -Capa de Red- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad VII: -Capa de Red- . Aspectos de diseño de la capa de red (Conmutación de paquetes de almacenamiento y reenvío, Servicios proporcionados a la capa de tra
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible vía URL que

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 733 | salida: 14 | total: 747

---

### Pregunta 11

> - Si quiero promocionar todas las materias de 4to año, ¿cuál es la diferencia de promedio exigido entre Investigación Operativa e Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: | Pagina: 1]
   > Materia: Investigación Operativa Sección: SISTEMA DE EVALUACIÓN (Investigación Operativa) | Condición del Alumno: - ALUMNO PROMOCIONADO: El estudiante logrará la promoción directa si alcanza un prom
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% de asistencia a las clases teóricas y prácticas.
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Diferencias | Pagina: 1]
   > Materia: Investigación Operativa Sección: Diferencias entre
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Composición | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Composición MAX-MIN. Capítulo VII Sistemas Difusos. Consideraciones generales. Representación de conocimiento estructurado mediante reglas lingüísticas.
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas s

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 667 | salida: 14 | total: 681

---

### Pregunta 12

> - ¿Qué herramientas de software se recomiendan en la carrera para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas a la materia. La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen repr
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: (LP), | Pagina: 2]
   > Materia: Investigación Operativa Sección: (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al análisis
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible vía URL que
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Problema | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Problema de separación lineal. Aplicaciones.
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Unidad VII: -Capa de Red- | Pagina: 2]
   > Materia: Comunicacion y Redes Sección: Unidad VII: -Capa de Red- ; Algoritmos de enrutamiento (Principio de optimización, Enrutamiento por la ruta más corta, Inundación, Enrutamiento por vector de di

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta. Solo tengo disponibles tres documentas, dos de la materia de Investigación Operativa (que solo menciona los nombres de software) y uno de Inteligencia Artificial (que no tiene relación con el tema de optimización lineal), y un documento de Comunicación y Redes (que trata sobre protocolos de enrutamiento).

**Tokens:** entrada: 854 | salida: 82 | total: 936

---

### Pregunta 13

> - ¿Dónde puedo descargar la materia de Cálculo de 1er año?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Visto | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Visto en https://ediciones.ungs.edu.ar/wp-content/uploads/2018/09/9789876301190-completo.pdf
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas s
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 1- PROGRAMA DE CONTENIDOS | Pagina: 1]
   > Materia: Comunicacion y Redes Sección: 1- PROGRAMA DE CONTENIDOS Unidad I: Introducción -Importancia e Influencia de las Redes en Nuestras Vidas: Comunicación en un mundo centrado en la red, herramie
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Primer | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Primer Orden.
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Sitios web sobre normativas, tecnologías y soluciones, opcional: | Pagina: 5]
   > Materia: Comunicacion y Redes Sección: Sitios web sobre normativas, tecnologías y soluciones, opcional: IETF -> www.ietf.org IEEE -> www.ieee.org ISO -> www.iso.org CISCO -> www.cisco.com IANA -> www

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 699 | salida: 14 | total: 713

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

**Respuesta:**

Lo siento, pero no dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 650 | salida: 19 | total: 669

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
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio | Pagina: 1]
   > Materia: Informática y Recursos Humanos Sección: Plan de Estudio: | Docente: Abog. Rodriguez Zanin, Fabio . Además, se abordarán aspectos legales fundamentales para comprender el impacto normativo de

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 956 | salida: 14 | total: 970

---

### Pregunta 16

> - Para la Promoción Directa, se exige la aprobación de la totalidad de los trabajos prácticos (TP 1 al TP 5). ¿Cuál es la calificación numérica mínima que debe obtenerse en cada TP individual para que se considere aprobado?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Visto | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Visto . 2018 Requisitos para rendir como estudiantes regulares, promocionales y libres: a. Promoción Directa Para acceder a la condición de Promoción
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Es | Pagina: 1]
   > Materia: Investigación Operativa Sección: Es requisito indispensable la entrega y aprobación de los dos trabajos prácticos obligatorios y el cumplimiento del
3. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales | Pagina: 9]
   > Materia: Bases de Datos Avanzadas Sección: 6/7 parciales aprobados con más del 50% | Promoción: | Régimen regular Obtener más del 70% en todos los parciales Software utilizado PostgreSQL 9.6 o superi
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Visto | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Visto de revisión y devolución con el equipo docente. El trabajo deberá entregarse con una antelación mínima de diez (10) días há
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Régimen | Regularidad: | Pagina: 7]
   > Materia: Bases de Datos Avanzadas Sección: Régimen | Regularidad: Asistencia: Según norma vigente. Todos los trabajos prácticos aprobados.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 884 | salida: 14 | total: 898

---

### Pregunta 17

> - ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Simplex | Pagina: 2]
   > Materia: Investigación Operativa Sección: Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible vía URL que
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas a la materia. La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen repr
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Problema | Pagina: 2]
   > Materia: Inteligencia Artificial Sección: Problema de separación lineal. Aplicaciones.
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: Reactivo | Pagina: 1]
   > Materia: Inteligencia Artificial Sección: Reactivo Simple.
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE | Pagina: 3]
   > Materia: Comunicacion y Redes Sección: 2- SISTEMA DE EVALUACION | Condición del Alumno: | PROMOCIONADO | REGULAR | LIBRE Evaluación Final: El alumno con condición de REGULAR, deberá rendir un examen

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 724 | salida: 14 | total: 738

---

### Pregunta 18

> - ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: 80% | Pagina: 1]
   > Materia: Investigación Operativa Sección: 80% a los encuentros presenciales. - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de puntos en ambos p
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: Estas | Pagina: 2]
   > Materia: Investigación Operativa Sección: Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mism
3. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: 13 04 de junio Presencial Teoría | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: 13 04 de junio Presencial Teoría Marco metodológico I: enfoque y tipo de investigación / muestra 14 11 de junio Virtual Práctica
4. [Documento: PROGRAMA- Metodología de la Investigación.docx.pdf | Materia: Metodología de la Investigación | Seccion: Cumplida | Pagina: 2]
   > Materia: Metodología de la Investigación Sección: Cumplida en condición libre. Deberá presentar el trabajo práctico integrador con una antelación mínima de veinte (20) días hábiles respecto de
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Días de clase | Pagina: 3]
   > Materia: Bases de Datos Avanzadas Sección: Días de clase Lunes: 13:30 a 15:30 -> Teoría Viernes: 17:00 a 19:00 -> Práctica NOTA: Los horarios están en proceso de evaluación y pueden sufrir cambios

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 872 | salida: 14 | total: 886

---

## Resumen de tokens

| Conversacion | Entrada | Salida | Total |
|---|---|---|---|
| 1 | 14756 | 1330 | 16086 |
| 2 | 14050 | 1403 | 15453 |
| 3 | 13104 | 1227 | 14331 |
| 4 | 12674 | 467 | 13141 |
| 5 | 14203 | 1333 | 15536 |
| 6 | 14621 | 1176 | 15797 |
| **Total** | **83408** | **6936** | **90344** |
