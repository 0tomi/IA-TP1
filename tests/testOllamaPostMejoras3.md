# Evaluacion — testOllamaPostMejoras3

_Iniciada: 2026-04-12 19:22:03_
_Ultima actualizacion: 2026-04-12 19:34:11_

**Estado:** completado
**Archivo de evaluacion:** `tests/evaluaciones/testOllamaPostMejoras.md`
**Preguntas:** 18 | **Conversaciones planificadas:** 5 | **Conversaciones iniciadas:** 5 | **Preguntas procesadas:** 90

## Conversacion 1

**Parametros:**

| Parametro | Valor |
|---|---|
| top_k | 6 |
| retrieval_type | similarity_search |
| threshold | 0.5 |
| max_context_chunks | 6 |
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
| include_metadata_in_embedding | True |
| refresh | True |
| metadata_filter | None |

### Pregunta 1

> - ¿Cuáles son los contenidos de la materia Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos **Capítulo I** **Agentes Inteligentes** Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas p
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > sentación de Conocimientos. Estructuras basadas en Lógica. Lógica de Primer Orden. Reglas de Inferencia. Representación basada en objetos. Definición de objetos y de atributos. Clases e instancias. Co
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > la asignatura. Introducción a los agentes inteligentes. Entorno de Trabajo. Propiedades de los entornos. Estructura de los Agentes. Programas de Agentes. Agente Reactivo Simple. Agentes Reactivos basa
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > os mediante reglas. Estructura básica. Representación de reglas mediante objetos. Ventajas comparativas entre las distintas representaciones. Comportamiento de Agentes Basados en Conocimientos. **Ca
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación de los distintos métodos sobre el funcionamiento del sistema. Agentes Basados en Lógica Dif
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > ralidades, conceptos básicos Reseña Histórica. Clasificación de las RNA. Agentes basados en Proceso de Aprendizaje **Red Perceptron Simple.** Elemento de Procesamiento. Función de Transferencia. Cond

**Respuesta:**

Los contenidos de la materia de Inteligencia Artificial incluyen los siguientes capítulos:

1. **Capítulo I: Agentes Inteligentes**: Introducción a la Inteligencia Artificial, definiciones y objetivos, herramientas y técnicas provistas por el área IA, descripción de los temas específicos a desarrollarse en la asignatura, introducción a la representación de conocimientos mediante reglas y estructuras basadas en lógica.
2. **Capítulo II: Procesos de B** (no se proporciona información adicional sobre el contenido de este capítulo).
3. **Capítulo IV: Diseño de los Sistemas Expertos**: Definición y descripción de sus módulos componentes, proceso de defuzzificación, método del centroide, método de máxima y su influencia en el funcionamiento del sistema.
4. **Capítulo VIII: Redes Neuronales Artificiales (RNA)**: Generalidades, conceptos básicos, reseña histórica, clasificación de las RNA y agentes basados en proceso de aprendizaje.

No se proporciona información sobre el contenido de los capítulos restantes.

**Tokens:** entrada: 1143 | salida: 249 | total: 1392

---

### Pregunta 2

> - ¿En qué materia se enseña el concepto de Lógica Difusa?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Chaining) y Encadenamiento hacia atrás (Backward Chaining). Herramientas para el desarrollo de Sistemas Expertos. **Capítulo VI** **Lógica Difusa (Fuzzy).** Consideraciones generales, Conjuntos Dif
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > eso de Fuzzificación. Influencia de la forma y distribución de los Conjuntos Difusos, en el comportamiento del sistema. Proceso de Inferencia. Tratamiento paralelo de las reglas. Determinación del ap
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > sentación de Conocimientos. Estructuras basadas en Lógica. Lógica de Primer Orden. Reglas de Inferencia. Representación basada en objetos. Definición de objetos y de atributos. Clases e instancias. Co
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación de los distintos métodos sobre el funcionamiento del sistema. Agentes Basados en Lógica Dif
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > s de comunicación (unicast, broadcast (dirigido y limitado), multicast). Direcciones (especiales, públicas y privadas). Direccionamiento estático y dinámico. Planificación del direccionamiento (segmen
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > ón, Igualdad, Complementación, Intersección, Unión. Estructuras FAM (Fuzzy Associative Memories). Composición MAX-MIN. **Capítulo VII** **Sistemas** **Difusos.** Consideraciones generales. Represent

**Respuesta:**

La materia es Inteligencia Artificial.

**Tokens:** entrada: 1156 | salida: 9 | total: 1165

---

### Pregunta 3

> - ¿Cuál es el plan de estudios de Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > **Cronograma de trabajo** |METODOLOGÍA DE LA INVESTIGACIÓN- 2026|Col2|Col3|Col4|Col5| |---|---|---|---|---| |**Clase **|**FECHA**|**Tipo de encuentro**|**Tipo encuentro**|**Tema**| |1|12 de marzo|**P
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: **Equipo docente:** PROFESORA RESPONSABLE ADJUNTO: ALEJANDRA MARǪUESIN; JEFE DE | Pagina: 1]
   > TRABAJOS PRÁCTICOS: TAMARA SUIVA. JEFE DE TRABAJOS PRÁCTICOS: JIMENA SANTA CRUZ; **Año de la carrera a la que pertenece la cátedra:** 4 **Régimen de la materia:** Anual **Carga horaria semanal:** 3
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: dentro de la plataforma Moodle. La organización será la siguiente | Pagina: 5]
   > en tres pestañas temáticas: - Introducción - Dimensión epistemológica - Dimensión estratégica - Dimensión técnica - Cada semana se habilitarán los contenidos planificados, proporcionando a l
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > |12|28 de mayo|Virtual|Teoría|Col5| |---|---|---|---|---| |13|04 de junio|**Presencial**|**Teoría**|Marco metodológico I: enfoque y<br>tipo de investigación / muestra| |14|11 de junio|Virtual|Práctica
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > de marzo|Virtual|Teoría|Conceptos generales para<br>introducción| |3|26 de marzo|Virtual|Práctica|Normas APA/ escritura académica| |4|2 de abril|(sin clase)|(sin clase)|(sin clase)| |5|09 de abril|**P
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: **Equipo docente:** PROFESORA RESPONSABLE ADJUNTO: ALEJANDRA MARǪUESIN; JEFE DE | Pagina: 1]
   > d y Estadística (317). **Fundamentación:** La metodología de la investigación es la ciencia del método. Yuni y Urbano (2016) sostiene que como la epistemología, la metodología de la investigación e

**Respuesta:**

El plan de estudios de Metodología de la Investigación es de 4 años de carrera y pertenece al año 4 de la misma. Se imparte con un régimen anual y una carga horaria semanal de 3 horas.

**Tokens:** entrada: 1315 | salida: 54 | total: 1369

---

### Pregunta 4

> - ¿Qué herramientas de software se recomiendan en la carrera para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > ramación lineal mediante el Método Simplex y el Método Gráfico. Es ideal para validaciones rápidas y visualización de regiones factibles. - **LINGO (64 bits):** Una versión avanzada y más potente d
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > 2.0:** Una suite clásica (dividida en 3 partes) que abarca múltiples módulos de Investigación Operativa. Permite resolver problemas de programación lineal (LP), modelos de transporte, asignación, pr
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > *Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadísticos mediante una interfaz basada en menús para la carga de
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > ara el aprendizaje de la Investigación Operativa. Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - **PHP Simplex:** Herram
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > los: determinísticos y estocásticos. Definición de variables de decisión, función objetivo y restricciones de sistema y de no negatividad. **Unidad II: -Programación Lineal (PL)-** Propiedades de lo

**Respuesta:**

Entre las herramientas de software recomendadas para resolver problemas de optimización lineal se encuentran LINGO (64 bits) y PHP Simplex, ambos capaces de modelar y resolver problemas de gran escala. LINGO es una versión avanzada del motor LINDO y está diseñado para resolver problemas de optimización lineal a gran escala. PHP Simplex es una herramienta en línea accesible vía URL que permite resolver problemas de programación lineal mediante el Método Simplex.

Asimismo, en la Unidad II de la Planificación de la Investigación Operativa se abordan las propiedades de los modelos de Programación Lineal, incluyendo proporcionalidad, aditividad, divisibilidad y certidumbre. Por lo tanto, la relación entre las herramientas de software recomendadas y las unidades teóricas de la Planificación de la Investigación Operativa es que LINGO y PHP Simplex están directamente relacionados con el estudio de la Programación Lineal, siendo esta una de las unidades teóricas que se estudian en la carrera.

Es importante destacar que estas herramientas están diseñadas para apoyar el aprendizaje y la resolución de problemas de optimización lineal, pero no tienen una relación directa con las otras unidades teóricas de la Planificación de la Investigación Operativa como el transporte, redes, teoría de juegos, etc.

**Tokens:** entrada: 1197 | salida: 301 | total: 1498

---

### Pregunta 5

> - ¿Qué instancias de recuperación nos provee Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > one de **dos oportunidades de** **recuperatorio** totales. Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mismo
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > a las clases teóricas y prácticas. - **ALUMNO LIBRE:** Revestirá esta condición todo estudiante que no logre cumplimentar alguno de los requisitos de puntaje, trabajos prácticos o asistencia anter
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > timización de gran escala, permitiendo una integración más fluida con bases de datos y
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > *Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadísticos mediante una interfaz basada en menús para la carga de
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad I: -Introducción y Modelos Matemáticos-** Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del problema, construcción del modelo mate
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > ibilidad y certidumbre. Formulación de problemas de optimización. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en los vértices, análisis de casos especiales

**Respuesta:**

La cátedra dispone de dos oportunidades de instancias de recuperación.

**Tokens:** entrada: 1098 | salida: 18 | total: 1116

---

### Pregunta 6

> - ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > *Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadísticos mediante una interfaz basada en menús para la carga de
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > 2.0:** Una suite clásica (dividida en 3 partes) que abarca múltiples módulos de Investigación Operativa. Permite resolver problemas de programación lineal (LP), modelos de transporte, asignación, pr
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos vertidos en la teoría. Más dos trabajos Prácticos que se realizan en el ho
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: **I. FUNDAMENTACIÓN** | Pagina: 1]
   > conceptos de informática, gestión organizacional y derecho informático. Los estudiantes explorarán los efectos de las nuevas tecnologías en el trabajo, la calidad de vida laboral y la administración
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > ara el aprendizaje de la Investigación Operativa. Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - **PHP Simplex:** Herram

**Respuesta:**

TORA es una herramienta educativa diseñada específicamente para el aprendizaje de la Investigación Operativa. Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos.

**Tokens:** entrada: 1099 | salida: 55 | total: 1154

---

### Pregunta 7

> - ¿Qué profesor forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes?

**Chunks de contexto:**

1. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **EQUIPO DOCENTE** | Pagina: 1]
   > Teoría: Trossero, Sebastián (Trossero.sebastian@uader.edu.ar) Práctica: Schmuckler, Jorge (Schmukler.jorge@uader.edu.ar)
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > **Facultad de Ciencia y Tecnología de la UADER** SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler.
3. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **MODALIDAD DE CLASES** | Pagina: 1]
   > A partir de este año la materia será dictada de manera bimodal. El cronograma será definido en su mayoría por la Facultad. Aún no confirmado. Los links de clases se encuentran en el aula virtual. Las
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > disponible en Biblioteca FCyT- Oro Verde] - Técnico en Redes & Seguridad, Bs. As.: Fox Andina, 2013, ISBN: 9789871857784. - USERS. [Disponible en Biblioteca FCyT- Oro Verde] - Curso visual y prác
5. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **PRESENTACIÓN DE LA MATERIA** | Pagina: 1]
   > Facultad de Ciencia y Tecnología Universidad Autónoma de Entre Ríos (UADER)
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > l, Fred: Redes de computadores e Internet / F. Halsall. - 5a ed. - Madrid: Pearson Educación, 2006. ISBN 9788478290833 [Disponible en Biblioteca FCyT- Oro Verde] - Huidobro Moya, José Manuel: Redes

**Respuesta:**

Jorge L. Schmukler es parte del equipo docente en ambas materias, según el documento "Planificación 2025 - Comunicacion y Redes.pdf".

**Tokens:** entrada: 1100 | salida: 39 | total: 1139

---

### Pregunta 8

> - ¿Qué otra asignatura, además de la propia materia de Inteligencia Artificial, incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos **Capítulo I** **Agentes Inteligentes** Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas p
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > os mediante reglas. Estructura básica. Representación de reglas mediante objetos. Ventajas comparativas entre las distintas representaciones. Comportamiento de Agentes Basados en Conocimientos. **Ca
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 4. El impacto de la inteligencia artificial en la gestión del talento. | Pagina: 2]
   > _**Bibliografía Nacional:**_ Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales. **Uni
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > sentación de Conocimientos. Estructuras basadas en Lógica. Lógica de Primer Orden. Reglas de Inferencia. Representación basada en objetos. Definición de objetos y de atributos. Clases e instancias. Co
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > ón, Igualdad, Complementación, Intersección, Unión. Estructuras FAM (Fuzzy Associative Memories). Composición MAX-MIN. **Capítulo VII** **Sistemas** **Difusos.** Consideraciones generales. Represent
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > la asignatura. Introducción a los agentes inteligentes. Entorno de Trabajo. Propiedades de los entornos. Estructura de los Agentes. Programas de Agentes. Agente Reactivo Simple. Agentes Reactivos basa

**Respuesta:**

La materia de Informática y Recursos Humanos incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) en su sección 4, titualda "El impacto de la inteligencia artificial en la gestión del talento".

**Tokens:** entrada: 1184 | salida: 60 | total: 1244

---

### Pregunta 9

> - Los requisitos para regularizar en Bases de Datos Avanzadas y en Redes y Comunicaciones, ¿son iguales? ¿Qué diferencias tienen?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > n cada parcial. **2-** Haber realizado y aprobado los dos trabajos práctico impartido por la cátedra. **3-** Asistir al 80% de las clases teóricas y prácticas. El alumno accederá a la condición de **
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > (problemas con el crecimiento de la red: escalabilidad, fallas en la red, colisiones). Switches (ancho de banda dedicado a cada puerto, entorno libre de colisiones, operación full-duplex, tabla de con
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > mno con condición de REGULAR, deberá rendir un examen de los temas teóricos y prácticos desarrollados en la materia (prueba escrita). El alumno LIBRE rendirá un examen final sobre el programa vigente
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > ón, Enrutamiento por multidifusión, Enrutamiento para hosts móviles, Enrutamiento en redes ad hoc, Búsqueda de nodos en redes de igual a igual), RIP protocolo de enrutamiento por clase vector de dista
5. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **SOFTWARE REQUERIDO** | Pagina: 2]
   > PostgreSQL: versión 9.6 o superior SQL Server: versión 2016 o superior QGIS: versión compatible con PostgreSQL Anaconda (Python): últimas versiones
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > ** Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos. Tener aprobado con 60 puntos los tres parciales. **2-** Haber realizado y aprobado los dos trabajos Práctico

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1173 | salida: 14 | total: 1187

---

### Pregunta 10

> - ¿Cuál es el porcentaje de asistencia a clases que exigen en común las materias de Investigación Operativa, Comunicaciones y Redes, y Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > **b.** **Alumno Regular** - 60 % de asistencia. - Aprobación del examen parcial teórico con una calificación igual o superior a 60 (sesenta) puntos. - Entrega de todos los trabajos en tiempo y
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > ón. Esta metodología busca facilitar el acceso a los contenidos para aquellos estudiantes que no pueden asistir a todas las clases y, al mismo tiempo, reducir la tasa de abandono. Por ello, los mat
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: **Equipo docente:** PROFESORA RESPONSABLE ADJUNTO: ALEJANDRA MARǪUESIN; JEFE DE | Pagina: 1]
   > TRABAJOS PRÁCTICOS: TAMARA SUIVA. JEFE DE TRABAJOS PRÁCTICOS: JIMENA SANTA CRUZ; **Año de la carrera a la que pertenece la cátedra:** 4 **Régimen de la materia:** Anual **Carga horaria semanal:** 3
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > ias individuales. Asimismo, deberá acreditar la aprobación de los dos trabajos prácticos de la cátedra y mantener una asistencia mínima del 80% a los encuentros presenciales.
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > ** Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos. Tener aprobado con 60 puntos los tres parciales. **2-** Haber realizado y aprobado los dos trabajos Práctico

**Respuesta:**

La asistencia mínima requerida es del 80% en todas las materias mencionadas.

**Tokens:** entrada: 1222 | salida: 22 | total: 1244

---

### Pregunta 11

> - Un proyecto integrador requiere utilizar un software para resolver problemas de optimización a gran escala que pueda conectarse de forma fluida con bases de datos espaciales. Según las herramientas enseñadas en las materias, ¿qué combinación de software visto en Bases de Datos Avanzadas e Investigación Operativa sería la más adecuada para este objetivo?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > timización de gran escala, permitiendo una integración más fluida con bases de datos y
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > 2.0:** Una suite clásica (dividida en 3 partes) que abarca múltiples módulos de Investigación Operativa. Permite resolver problemas de programación lineal (LP), modelos de transporte, asignación, pr
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > *Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadísticos mediante una interfaz basada en menús para la carga de
5. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **SOFTWARE REQUERIDO** | Pagina: 2]
   > PostgreSQL: versión 9.6 o superior SQL Server: versión 2016 o superior QGIS: versión compatible con PostgreSQL Anaconda (Python): últimas versiones
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > ara el aprendizaje de la Investigación Operativa. Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - **PHP Simplex:** Herram

**Respuesta:**

La herramienta más adecuada para resolver problemas de optimización a gran escala que pueda conectarse de forma fluida con bases de datos espaciales es PostgreSQL, versión 9.6 o superior, en combinación con QGIS, versión compatible con PostgreSQL.

Esto se debe a que QGIS es un software de SIG (Sistema de Información Geográfica) que permite trabajar con datos geográficos y espaciales, y PostgreSQL es una base de datos relacional que puede almacenar y manejar grandes cantidades de datos, incluyendo datos espaciales.

La versión compatible de QGIS es necesaria para garantizar que pueda conectarse de forma fluida con PostgreSQL y aprovechar sus características y funcionalidades.

**Tokens:** entrada: 1138 | salida: 153 | total: 1291

---

### Pregunta 12

> - Si un estudiante desea investigar sobre el impacto de los "Agentes que aprenden" y las "Redes Neuronales" en la selección de personal y el teletrabajo en Argentina, ¿qué normativas legales y temas específicos de los programas de Inteligencia Artificial y RRHH debería cruzar en su marco teórico?

**Chunks de contexto:**

1. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: IV. BIBLIOGRAFÍA GENERAL | Pagina: 3]
   > n Argentina. Legislación sobre delitos informáticos en Argentina. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales.
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: **I. FUNDAMENTACIÓN** | Pagina: 1]
   > gales fundamentales para comprender el impacto normativo de las TIC en el ámbito laboral, tomando como base la legislación argentina y los aportes de autores nacionales.
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 3]
   > Legislación sobre delitos informáticos en Argentina. Ley Nacional de Protección de Datos Personales (Ley 25.326). Ley Propiedad Intelectual (Ley 11.723) y su modificatoria. **Unidad 5: Trabajo Autó
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: IV. BIBLIOGRAFÍA GENERAL | Pagina: 3]
   > de Teletrabajo (Ley 27.555). Ley Propiedad intelectual (Ley 11.723) - (modificatoria Ley 25.036) Código Civil y Comercial de la Nación (aspectos relacionados con contratos digitales y firma electrón
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 2]
   > Reglamento de Teletrabajo en Argentina. Nicolás S. Tato, El Derecho Informático - Aspectos Fundamentales. Mariana Nazar, Tecnologías, información y derechos. **Unidad 2:** **Relaciones Humanas en e
6. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 4. El impacto de la inteligencia artificial en la gestión del talento. | Pagina: 2]
   > _**Bibliografía Nacional:**_ Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales. **Uni

**Respuesta:**

El estudiante que investigue sobre el impacto de los "Agentes que aprenden" y las "Redes Neuronales" en la selección de personal y el teletrabajo en Argentina debe tener en cuenta las siguientes normativas legales y temas específicos de los programas de Inteligencia Artificial y RRHH:

- La Ley 25.326 sobre Protección de Datos Personales y su relación con la recopilación y uso de datos en la selección de personal.
- La Ley 11.723 de Propiedad Intelectual y sus modificatorias, que regula la creación, la explotación y la protección de las obras intelectuales.
- El Reglamento de Teletrabajo en Argentina, que establece las normas y condiciones para la prestación de servicios a distancia.
- La Ley 27.555 de Teletrabajo, que regula los derechos y deberes de los trabajadores y empleadores en materia de teletrabajo.
- El Código Civil y Comercial de la Nación, que regula aspectos relacionados con contratos digitales y firma electrónica.
- Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales, como el de Gonzalo Ana Dobratinich sobre el derecho y las nuevas tecnologías.

Es importante destacar que el estudiante debe analizar cómo los "Agentes que aprenden" y las "Redes Neuronales" pueden impactar en la selección de personal y el teletrabajo en Argentina, y cómo estas tecnologías pueden estar reguladas y utilizadas de acuerdo a las normas y leyes citadas.

**Tokens:** entrada: 1129 | salida: 352 | total: 1481

---

### Pregunta 13

> - ¿Dónde puedo descargar la materia de Cálculo de 1er año?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > n de datos y análisis de<br>datos| |||||| |RECESO DE INVIERNO/ MESAS DE EXAMENES FINALES|RECESO DE INVIERNO/ MESAS DE EXAMENES FINALES|RECESO DE INVIERNO/ MESAS DE EXAMENES FINALES|RECESO DE INVIERNO/
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > **Obligatoria** - Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] - Cisco Systems: Academia de Networking de Cisco Systems: Guía del primer añ
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > m de cable, ADSL en comparación con el cable). **Unidad IV**: - **Capa de enlace de dato** - **sub capa** **LLC (control de enlace lógico)** Cuestiones en el diseño de la capa de enlace de dato, servi
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: UNDERWRITERS LABORATORIES (UL) -> www.ul.com | Pagina: 5]
   > PANDUIT -> www.panduit.com AMP -> www.tycoelectronics.com/components/ ETHEREAL -> www.ethereal.com SIEMENS -> www.sea.siemens.com/step/templates/lesson.mason?electricity:2:3:3
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: PROGRAMA DE CÁTEDRA: INFORMÁTICA Y RELACIONES HUMANAS | Pagina: 1]
   > Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas semanales
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > ción de sus módulos componentes. Proceso de Adquisición de Conocimiento. Base de Conocimientos, características generales.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1172 | salida: 14 | total: 1186

---

### Pregunta 14

> - El profesor Ing. Jorge L. Schmukler da clases en Bases de Datos Avanzadas, en Inteligencia Artificial y en Redes y Comunicaciones.

**Chunks de contexto:**

1. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **EQUIPO DOCENTE** | Pagina: 1]
   > Teoría: Trossero, Sebastián (Trossero.sebastian@uader.edu.ar) Práctica: Schmuckler, Jorge (Schmukler.jorge@uader.edu.ar)
2. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **MODALIDAD DE CLASES** | Pagina: 1]
   > A partir de este año la materia será dictada de manera bimodal. El cronograma será definido en su mayoría por la Facultad. Aún no confirmado. Los links de clases se encuentran en el aula virtual. Las
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > sentación de Conocimientos. Estructuras basadas en Lógica. Lógica de Primer Orden. Reglas de Inferencia. Representación basada en objetos. Definición de objetos y de atributos. Clases e instancias. Co
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > **Facultad de Ciencia y Tecnología de la UADER** SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler.
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > Comunicación y coordinación. Protocolos de Interacción. Estándares. Lenguaje ACL. Estándar FIPA. Lenguajes y Herramientas. Tópicos avanzados en tecnología de Agentes
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (2

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1072 | salida: 14 | total: 1086

---

### Pregunta 15

> - ¿Cuál es el costo de la certificación oficial de Cisco que se menciona como opcional en la planificación?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > **Obligatoria** - Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] - Cisco Systems: Academia de Networking de Cisco Systems: Guía del primer añ
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Sitios web sobre normativas, tecnologías y soluciones, opcional** | Pagina: 5]
   > IETF -> www.ietf.org IEEE -> www.ieee.org ISO -> www.iso.org CISCO -> www.cisco.com IANA -> www.iana.org ISOC -> www.isoc.org ARIN -> www.arin.net LACNIC -> http://lacnic.net/sp/ LAC IPV6 TF -> www.la
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > disponible en Biblioteca FCyT- Oro Verde] - Técnico en Redes & Seguridad, Bs. As.: Fox Andina, 2013, ISBN: 9789871857784. - USERS. [Disponible en Biblioteca FCyT- Oro Verde] - Curso visual y prác
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: UNDERWRITERS LABORATORIES (UL) -> www.ul.com | Pagina: 5]
   > PANDUIT -> www.panduit.com AMP -> www.tycoelectronics.com/components/ ETHEREAL -> www.ethereal.com SIEMENS -> www.sea.siemens.com/step/templates/lesson.mason?electricity:2:3:3
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > m de cable, ADSL en comparación con el cable). **Unidad IV**: - **Capa de enlace de dato** - **sub capa** **LLC (control de enlace lógico)** Cuestiones en el diseño de la capa de enlace de dato, servi
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > PROMOCIONADO REGULAR LIBRE El alumno accederá a la condición de **PROMOCIÓN** si cumple con las siguientes condiciones de cátedra: **1 -** Obtener en los 3 parciales, una calificación promedio sup

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1279 | salida: 14 | total: 1293

---

### Pregunta 16

> - Para la Promoción Directa, se exige la aprobación de la totalidad de los trabajos prácticos (TP 1 al TP 5). ¿Cuál es la calificación numérica mínima que debe obtenerse en cada TP individual para que se considere aprobado?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 16]
   > Para acceder a la condición de Promoción Directa, el/la estudiante deberá cumplir con los siguientes requisitos: - 80 % de asistencia a la cursada. - Aprobación del examen parcial teórico con una
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > **Condición del Alumno:** - **ALUMNO PROMOCIONADO:** El estudiante logrará la promoción directa si alcanza un promedio general de **80 puntos** - más entre los **1 parcial** previstos, no pudiendo
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > PROMOCIONADO REGULAR LIBRE El alumno accederá a la condición de **PROMOCIÓN** si cumple con las siguientes condiciones de cátedra: **1 -** Obtener en los 3 parciales, una calificación promedio sup
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 9]
   > **Programa de trabajos prácticos:** Tp 1: Escritura académica. Se solicita a los estudiantes seleccionar un artículo de investigación sobre un tema de interés específico relacionado al campo profesi
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > ias individuales. Asimismo, deberá acreditar la aprobación de los dos trabajos prácticos de la cátedra y mantener una asistencia mínima del 80% a los encuentros presenciales.
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1193 | salida: 14 | total: 1207

---

### Pregunta 17

> - ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > ramación lineal mediante el Método Simplex y el Método Gráfico. Es ideal para validaciones rápidas y visualización de regiones factibles. - **LINGO (64 bits):** Una versión avanzada y más potente d
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > ara el aprendizaje de la Investigación Operativa. Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - **PHP Simplex:** Herram
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > . **Unidad III: -Método SIMPLEX-** Algoritmo del método Simplex: forma estándar, variables de holgura y variables artificiales. Construcción de la tabla inicial, criterios de entrada y salida de va
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > (Código corrección errores y Código detección errores), control de flujo, Protocolos elementales de enlace de datos (Protocolo simplex sin restricciones, Protocolo símplex de parada y espera, Protocol
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > los: determinísticos y estocásticos. Definición de variables de decisión, función objetivo y restricciones de sistema y de no negatividad. **Unidad II: -Programación Lineal (PL)-** Propiedades de lo

**Respuesta:**

Lo siento, pero no dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1199 | salida: 19 | total: 1218

---

### Pregunta 18

> - ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > ión sustituirá automáticamente a la nota del examen original. **Protocolos de Evaluación:** Los resultados se publicarán en un plazo de siete días corridos tras la evaluación. Los exámenes se desar
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > ES| |16|06 de agosto|Virtual|Teoría|Repaso del proceso de| |||||investigación| |17|13 de agosto|Virtual|Tutorías|Tutorías| |18|20 de agosto|**_Presencial (cambio_**<br>**_encuentro)_**|**Teoría**|Parc
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > ias individuales. Asimismo, deberá acreditar la aprobación de los dos trabajos prácticos de la cátedra y mantener una asistencia mínima del 80% a los encuentros presenciales.
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > one de **dos oportunidades de** **recuperatorio** totales. Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mismo
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > |12|28 de mayo|Virtual|Teoría|Col5| |---|---|---|---|---| |13|04 de junio|**Presencial**|**Teoría**|Marco metodológico I: enfoque y<br>tipo de investigación / muestra| |14|11 de junio|Virtual|Práctica

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1184 | salida: 14 | total: 1198

---

## Conversacion 2

**Parametros modificados respecto a la conversacion anterior:**

| Parametro | Valor |
|---|---|
| chunk_size | 500 |
| chunk_overlap | 100 |

### Pregunta 1

> - ¿Cuáles son los contenidos de la materia Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos **Capítulo I** **Agentes Inteligentes** Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas p
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > basada en objetos. Definición de objetos y de atributos. Clases e instancias. Concepto de herencia. Métodos y mensajes. Representación de Conocimientos mediante reglas. Estructura básica. Representac
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > spacio de estados. Recocido Simulado. Búsqueda voraz primero el mejor. Búsqueda A*, Heurísticos admisibles, comparación entre varios heurísticos admisibles. Agentes Basados en Procesos de Búsqueda. *
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > ntos métodos sobre el funcionamiento del sistema. Agentes Basados en Lógica Difusa. **Capítulo VIII** **Redes Neuronales Artificiales (RNA).** Generalidades, conceptos básicos Reseña Histórica. Cla
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Definición y descripción de sus módulos componentes. Proceso de Adquisición de Conocimiento. Base de Conocimientos, características generales.
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (2

**Respuesta:**

Los contenidos de la materia Inteligencia Artificial incluyen:

**Capítulo I: Agentes Inteligentes**

* Introducción a la Inteligencia Artificial (IA) y definiciones de objetivos
* Herramientas y técnicas provistas por el área IA
* Descripción de los temas específicos a desarrollarse en la asignatura
* Introducción a los agentes inteligentes, entornos de trabajo y propiedades de los entornos
* Estructura de los agentes, programas de agentes y agente reactivo simple
* Agentes reactivos basados en modelos y agente basado en objetos
* Definición de objetos y atributos, clases e instancias, concepto de herencia y métodos y mensajes

**Capítulo III: Sistemas Basados en Conocimientos**

* Conceptos básicos y representación de conocimientos
* Estructuras basadas en lógica, lógica de primer orden y reglas de inferencia
* Representación basada en objetos, definición de objetos y atributos, clases e instancias y concepto de herencia
* Métodos sobre el funcionamiento del sistema

**Capítulo IV: Diseño de los Sistemas Expertos**

* Definición y descripción de los módulos componentes
* Proceso de adquisición de conocimiento

**Capítulo VIII: Redes Neuronales Artificiales (RNA)**

* Generalidades, conceptos básicos y reseña histórica
* Clasificación de las RNA y agentes basados en proceso de aprendizaje
* Red Perceptron simple, elemento de procesamiento, función de transferencia, condiciones de convergencia y proceso de entrenamiento

Además, se incluye información sobre la bibliografía recomendada, que consta de dos libros:

* "Inteligencia Artificial - Un Enfoque Moderno" de Stuart J. Rusell y Peter Norvig (edición segunda)
* "Aprendizaje automático y aprendizaje profundo con Python, scikit-learn y Tensor Flow" de S. Raschka y V. Mirjalili (edición segunda)

**Tokens:** entrada: 1337 | salida: 463 | total: 1800

---

### Pregunta 2

> - ¿En qué materia se enseña el concepto de Lógica Difusa?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > * **Lógica Difusa (Fuzzy).** Consideraciones generales, Conjuntos Difusos, definición. Operaciones simples entre conjuntos Difusos: Inclusión, Igualdad, Complementación, Intersección, Unión. Estructu
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > cas. Proceso de Fuzzificación. Influencia de la forma y distribución de los Conjuntos Difusos, en el comportamiento del sistema. Proceso de Inferencia. Tratamiento paralelo de las reglas. Determinac
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > ntos métodos sobre el funcionamiento del sistema. Agentes Basados en Lógica Difusa. **Capítulo VIII** **Redes Neuronales Artificiales (RNA).** Generalidades, conceptos básicos Reseña Histórica. Cla
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Estructura de Control: Procedimientos de Inferencia; Interfase con el usuario. Memoria de Trabajo, Módulo generador de explicaciones al usuario. **Capítulo V** **Funcionalidad de los Sistemas Exper
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > spacio de estados. Recocido Simulado. Búsqueda voraz primero el mejor. Búsqueda A*, Heurísticos admisibles, comparación entre varios heurísticos admisibles. Agentes Basados en Procesos de Búsqueda. *
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > basada en objetos. Definición de objetos y de atributos. Clases e instancias. Concepto de herencia. Métodos y mensajes. Representación de Conocimientos mediante reglas. Estructura básica. Representac

**Respuesta:**

La Lógica Difusa se enseña en la materia de Inteligencia Artificial.

**Tokens:** entrada: 1460 | salida: 20 | total: 1480

---

### Pregunta 3

> - ¿Cuál es el plan de estudios de Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: **Equipo docente:** PROFESORA RESPONSABLE ADJUNTO: ALEJANDRA MARǪUESIN; JEFE DE | Pagina: 1]
   > TRABAJOS PRÁCTICOS: TAMARA SUIVA. JEFE DE TRABAJOS PRÁCTICOS: JIMENA SANTA CRUZ; **Año de la carrera a la que pertenece la cátedra:** 4 **Régimen de la materia:** Anual **Carga horaria semanal:** 3
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > |**FECHA**|**Tipo de encuentro**|**Tipo encuentro**|**Tema**| |1|12 de marzo|**Presencial**|**Teórico/práctico**|Presentación de la asignatura| |2|19 de marzo|Virtual|Teoría|Conceptos generales para<b
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: dentro de la plataforma Moodle. La organización será la siguiente | Pagina: 5]
   > ios de diagnóstico inicial, solicitud de clases de consulta y encuesta de valoración del curso. - Desarrollo de contenidos: distribuidos en tres pestañas temáticas: - Introducción - Dimensión
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > |12|28 de mayo|Virtual|Teoría|Col5| |---|---|---|---|---| |13|04 de junio|**Presencial**|**Teoría**|Marco metodológico I: enfoque y<br>tipo de investigación / muestra| |14|11 de junio|Virtual|Práctica
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 8]
   > al para los estudiantes, con el objetivo de acompañar el desarrollo de sus temas de investigación y brindar orientación especializada. - Encuentro entre pares: se organizarán espacios de intercamb
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: dentro de la plataforma Moodle. La organización será la siguiente | Pagina: 5]
   > - Inicio del curso: contendrá información general de la cátedra, incluyendo el programa, el equipo docente, el cronograma, los objetivos, los materiales utilizados, el enlace de videoconferencia, la

**Respuesta:**

El plan de estudios de Metodología de la Investigación contempla una carga horaria semanal de 3 horas, siendo un régimen anual. Su año corresponde al cuarto año de carrera. La materia tiene como correlativa a Ingeniería del Software I (208) y a Probabilidad y Estadística (317). Se enfoca en la presentación de la asignatura, conceptos generales y la escritura académica, pasando por la introducción de temas relacionados con la epistemología y la estrategia dentro de la investigación.

**Tokens:** entrada: 1583 | salida: 121 | total: 1704

---

### Pregunta 4

> - ¿Qué herramientas de software se recomiendan en la carrera para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > mas de programación lineal (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gest
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > atividad. **Unidad II: -Programación Lineal (PL)-** Propiedades de los modelos de Programación Lineal: proporcionalidad, aditividad, divisibilidad y certidumbre. Formulación de problemas de optimiz
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > egiones factibles. - **LINGO (64 bits):** Una versión avanzada y más potente del motor LINDO. Está diseñado para modelar y resolver problemas de optimización de gran escala, permitiendo una integr
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > icamente para el aprendizaje de la Investigación Operativa. Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - **PHP Simplex
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: pesos. Regiones de Decisión. Problema de separación lineal. Aplicaciones. Limitaciones | Pagina: 2]
   > Problema XOR.

**Respuesta:**

Las herramientas recomendadas para resolver problemas de optimización lineal son LINDO, LINGO (64 bits) y PHP Simplex. Estas herramientas están diseñadas para modelar y resolver problemas de optimización lineal, y se relacionan con las unidades teóricas de la carrera, especialmente con la Unidad II: Programación Lineal (PL), donde se abordan las propiedades de los modelos de Programación Lineal y su resolución gráfica.

Además, se menciona que LINGO (64 bits) es una versión avanzada y más potente del motor LINDO, y que PHP Simplex permite resolver problemas de programación lineal mediante el Método Simplex y el Método Gráfico.

Es importante destacar que las unidades teóricas también incluyen la resolución gráfica de modelos de PL, búsqueda de la solución óptima en los vértices y análisis de casos especiales, lo que sugiere que estas herramientas son herramientas muy útiles para apoyar la comprensión y resolución de problemas de optimización lineal en la carrera.

**Tokens:** entrada: 1332 | salida: 237 | total: 1569

---

### Pregunta 5

> - ¿Qué instancias de recuperación nos provee Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > no de los requisitos de puntaje, trabajos prácticos o asistencia anteriormente detallados. **Instancias de Recuperación:** La cátedra dispone de **dos oportunidades de** **recuperatorio** totales.
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > egiones factibles. - **LINGO (64 bits):** Una versión avanzada y más potente del motor LINDO. Está diseñado para modelar y resolver problemas de optimización de gran escala, permitiendo una integr
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > mas de programación lineal (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gest
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad I: -Introducción y Modelos Matemáticos-** Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del problema, construcción del modelo mate
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > icamente para el aprendizaje de la Investigación Operativa. Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - **PHP Simplex
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par

**Respuesta:**

La cátedra dispone de **dos oportunidades de recuperatorio** totales. Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mismo examen parcial. La calificación obtenida en la instancia de recuperación sustituirá automáticamente a la nota del examen original.

**Tokens:** entrada: 1400 | salida: 82 | total: 1482

---

### Pregunta 6

> - ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > mas de programación lineal (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gest
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > icamente para el aprendizaje de la Investigación Operativa. Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - **PHP Simplex
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: **I. FUNDAMENTACIÓN** | Pagina: 1]
   > ologías en el trabajo, la calidad de vida laboral y la administración del talento humano en la era digital. Además, se abordarán aspectos legales fundamentales para comprender el impacto normativo de
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > 03<br>de<br>septiembr<br>e|**Presencial**|Tutorías|Sugerecia entrevista a expertos<br>en el tema/ recuperatorio parcial<br>teoría| |21|10<br>de<br>septiembr<br>e|Virtual|Tutorías|Avances proyectos a l
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > egiones factibles. - **LINGO (64 bits):** Una versión avanzada y más potente del motor LINDO. Está diseñado para modelar y resolver problemas de optimización de gran escala, permitiendo una integr

**Respuesta:**

El software TORA está diseñado específicamente para el aprendizaje de la Investigación Operativa. Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos.

**Tokens:** entrada: 1305 | salida: 52 | total: 1357

---

### Pregunta 7

> - ¿Qué profesor forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes?

**Chunks de contexto:**

1. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **EQUIPO DOCENTE** | Pagina: 1]
   > Teoría: Trossero, Sebastián (Trossero.sebastian@uader.edu.ar) Práctica: Schmuckler, Jorge (Schmukler.jorge@uader.edu.ar)
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > **Facultad de Ciencia y Tecnología de la UADER** SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler.
3. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **MODALIDAD DE CLASES** | Pagina: 1]
   > A partir de este año la materia será dictada de manera bimodal. El cronograma será definido en su mayoría por la Facultad. Aún no confirmado. Los links de clases se encuentran en el aula virtual. Las
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > **Obligatoria** - Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] - Cisco Systems: Academia de Networking de Cisco Systems: Guía del primer añ
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > ca FCyT- Oro Verde] - Halsall, Fred: Redes de computadores e Internet / F. Halsall. - 5a ed. - Madrid: Pearson Educación, 2006. ISBN 9788478290833 [Disponible en Biblioteca FCyT- Oro Verde] - Huid
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > onible en Biblioteca FCyT- Oro Verde] - Arena, Héctor Facundo: Linux: la guía definitiva / H. F. Arena. - Buenos Aires: Gradi, 2010. ISBN 9789872601386 [Disponible en Biblioteca FCyT- Oro Verde] -

**Respuesta:**

Schmukler, Jorge.

**Tokens:** entrada: 1379 | salida: 8 | total: 1387

---

### Pregunta 8

> - ¿Qué otra asignatura, además de la propia materia de Inteligencia Artificial, incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos **Capítulo I** **Agentes Inteligentes** Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas p
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 4. El impacto de la inteligencia artificial en la gestión del talento. | Pagina: 2]
   > _**Bibliografía Nacional:**_ Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales. **Uni
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > basada en objetos. Definición de objetos y de atributos. Clases e instancias. Concepto de herencia. Métodos y mensajes. Representación de Conocimientos mediante reglas. Estructura básica. Representac
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > n agentes. Metodología Gaia: Modelo de Actividades. Modelo de Roles. Modelo Interacción. Modelo de Agentes. Organizaciones. Interacciones multiagente. Comunicación y coordinación. Protocolos de Intera
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > ntos métodos sobre el funcionamiento del sistema. Agentes Basados en Lógica Difusa. **Capítulo VIII** **Redes Neuronales Artificiales (RNA).** Generalidades, conceptos básicos Reseña Histórica. Cla
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (2

**Respuesta:**

Además de la materia de Inteligencia Artificial, la asignatura de Informática y Recursos Humanos incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas, específicamente en la sección "4. El impacto de la inteligencia artificial en la gestión del talento".

**Tokens:** entrada: 1364 | salida: 77 | total: 1441

---

### Pregunta 9

> - Los requisitos para regularizar en Bases de Datos Avanzadas y en Redes y Comunicaciones, ¿son iguales? ¿Qué diferencias tienen?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > ción Final:** El alumno con condición de REGULAR, deberá rendir un examen de los temas teóricos y prácticos desarrollados en la materia (prueba escrita). El alumno LIBRE rendirá un examen final sobre
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > clases teóricas y prácticas. El alumno accederá a la condición de **REGULAR**, si cumple con las siguientes condiciones de cátedra: **1 -** Obtener en los 3 parciales, una calificación promedio supe
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > * **-VLans-** Definiciones de Vlan, Beneficios de una Vlan, Rangos de ID de la Vlan (rango normal y rango extendido), Tipos de Vlan (Vlan de Datos, Predeterminada, Nativa, Administración, Voz), Config
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > PROMOCIONADO REGULAR LIBRE El alumno accederá a la condición de **PROMOCIÓN** si cumple con las siguientes condiciones de cátedra: **1 -** Obtener en los 3 parciales, una calificación promedio sup
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > ceso múltiple, detección de colisiones, señal de congestión y postergación aleatoria. Tipos de ethernet (10base5, 10base2, 10base-t, 100base-tx, 100base-fx, 1000base-t, 1000base-sx, 1000base-lx, la et
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > a cada puerto, entorno libre de colisiones, operación full-duplex, tabla de conmutación). Comparación hubs / switch. ARP (protocolo de resolución de direcciones). Mantenimiento de la tabla ARP. ARP pr

**Respuesta:**

Los requisitos para regularizar en Redes y Comunicaciones y en bases de datos avanzadas difieren.

En Redes y Comunicaciones, para acceder a la condición de REGULAR, el alumno debe cumplir con las condiciones: obtener una calificación promedio superior o igual a los 60 puntos en los 3 parciales, tener aprobado con 60 puntos los tres parciales, haber realizado y aprobado los dos trabajos prácticos impartidos por la cátedra y asistir al 80% de las clases teóricas y prácticas.

En bases de datos avanzadas no se especifica ningún requisito para regularizar. Por lo tanto, no dispongo de información en mis documentos para describir las diferencias de los requisitos entre ambas materias.

**Tokens:** entrada: 1561 | salida: 173 | total: 1734

---

### Pregunta 10

> - ¿Cuál es el porcentaje de asistencia a clases que exigen en común las materias de Investigación Operativa, Comunicaciones y Redes, y Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > **b.** **Alumno Regular** - 60 % de asistencia. - Aprobación del examen parcial teórico con una calificación igual o superior a 60 (sesenta) puntos. - Entrega de todos los trabajos en tiempo y
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: **Equipo docente:** PROFESORA RESPONSABLE ADJUNTO: ALEJANDRA MARǪUESIN; JEFE DE | Pagina: 1]
   > TRABAJOS PRÁCTICOS: TAMARA SUIVA. JEFE DE TRABAJOS PRÁCTICOS: JIMENA SANTA CRUZ; **Año de la carrera a la que pertenece la cátedra:** 4 **Régimen de la materia:** Anual **Carga horaria semanal:** 3
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > **Condición del Alumno:** - **ALUMNO PROMOCIONADO:** El estudiante logrará la promoción directa si alcanza un promedio general de **80 puntos** - más entre los **1 parcial** previstos, no pudiendo
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > s las clases y, al mismo tiempo, reducir la tasa de abandono. Por ello, los materiales teóricos y las lecturas obligatorias se compartirán con una semana de antelación al encuentro presencial. Ademá
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 16]
   > Para acceder a la condición de Promoción Directa, el/la estudiante deberá cumplir con los siguientes requisitos: - 80 % de asistencia a la cursada. - Aprobación del examen parcial teórico con una

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1557 | salida: 14 | total: 1571

---

### Pregunta 11

> - Un proyecto integrador requiere utilizar un software para resolver problemas de optimización a gran escala que pueda conectarse de forma fluida con bases de datos espaciales. Según las herramientas enseñadas en las materias, ¿qué combinación de software visto en Bases de Datos Avanzadas e Investigación Operativa sería la más adecuada para este objetivo?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > egiones factibles. - **LINGO (64 bits):** Una versión avanzada y más potente del motor LINDO. Está diseñado para modelar y resolver problemas de optimización de gran escala, permitiendo una integr
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > icamente para el aprendizaje de la Investigación Operativa. Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - **PHP Simplex
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > mas de programación lineal (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gest
5. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **SOFTWARE REQUERIDO** | Pagina: 2]
   > PostgreSQL: versión 9.6 o superior SQL Server: versión 2016 o superior QGIS: versión compatible con PostgreSQL Anaconda (Python): últimas versiones
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra

**Respuesta:**

La herramienta más adecuada para resolver problemas de optimización a gran escala que pueda conectarse de forma fluida con bases de datos es LINGO (64 bits), ya que es una versión avanzada y más potente del motor LINDO y está diseñado para modelar y resolver problemas de optimización de gran escala, permitiendo una integración más fluida con bases de datos.

Para conectarse con bases de datos espaciales, necesitaríamos una base de datos compatible con la versión 9.6 o superior de PostgreSQL, que es compatible con QGIS. Además, Anaconda (Python) puede ser útil para procesar datos y realizar análisis cuantitativo y estadísticos mediante una interfaz basada en menús para la carga de datos, pero no es directamente relacionado con la optimización a gran escala.

Por lo tanto, la combinación de software más adecuada sería utilizar LINGO (64 bits) para la resolución de problemas de optimización a gran escala y conectarlo con una base de datos PostgreSQL versión 9.6 o superior, que es compatible con QGIS.

**Tokens:** entrada: 1266 | salida: 240 | total: 1506

---

### Pregunta 12

> - Si un estudiante desea investigar sobre el impacto de los "Agentes que aprenden" y las "Redes Neuronales" en la selección de personal y el teletrabajo en Argentina, ¿qué normativas legales y temas específicos de los programas de Inteligencia Artificial y RRHH debería cruzar en su marco teórico?

**Chunks de contexto:**

1. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: IV. BIBLIOGRAFÍA GENERAL | Pagina: 3]
   > Nación (aspectos relacionados con contratos digitales y firma electrónica). _**Bibliografía Complementaria:**_ Reglamento de Teletrabajo en Argentina. Legislación sobre delitos informáticos en Arge
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 3]
   > Legislación sobre delitos informáticos en Argentina. Ley Nacional de Protección de Datos Personales (Ley 25.326). Ley Propiedad Intelectual (Ley 11.723) y su modificatoria. **Unidad 5: Trabajo Autó
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 2]
   > Reglamento de Teletrabajo en Argentina. Nicolás S. Tato, El Derecho Informático - Aspectos Fundamentales. Mariana Nazar, Tecnologías, información y derechos. **Unidad 2:** **Relaciones Humanas en e
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 4. El impacto de la inteligencia artificial en la gestión del talento. | Pagina: 2]
   > _**Bibliografía Nacional:**_ Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales. **Uni
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: **I. FUNDAMENTACIÓN** | Pagina: 1]
   > ologías en el trabajo, la calidad de vida laboral y la administración del talento humano en la era digital. Además, se abordarán aspectos legales fundamentales para comprender el impacto normativo de
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > ntos métodos sobre el funcionamiento del sistema. Agentes Basados en Lógica Difusa. **Capítulo VIII** **Redes Neuronales Artificiales (RNA).** Generalidades, conceptos básicos Reseña Histórica. Cla

**Respuesta:**

El estudiante debería cruzar los siguientes temas específicos en su marco teórico:

1.  El impacto de la IA en las relaciones laborales, considerando la legislación argentina, en especial los artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales que figuran en la sección 4. El impacto de la inteligencia artificial en la gestión del talento.
2.  El impacto normativo de las TIC en el ámbito laboral, considerando la legislación argentina y los aportes de autores nacionales, en especial la legislación sobre delitos informáticos en Argentina y la Ley Nacional de Protección de Datos Personales.
3.  Los aspectos legales fundamentales relacionados con la selección de personal y el teletrabajo, en especial el Reglamento de Teletrabajo en Argentina.
4.  Los conceptos básicos de Redes Neuronales Artificiales, incluyendo generalidades, clasificación, agentes basados en proceso de aprendizaje y funcionalidad, como por ejemplo el Proceso de Aprendizaje, Clasificación de las RNA y Agentes basados en Proceso de Aprendizaje.

**Tokens:** entrada: 1224 | salida: 270 | total: 1494

---

### Pregunta 13

> - ¿Dónde puedo descargar la materia de Cálculo de 1er año?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: UNDERWRITERS LABORATORIES (UL) -> www.ul.com | Pagina: 5]
   > PANDUIT -> www.panduit.com AMP -> www.tycoelectronics.com/components/ ETHEREAL -> www.ethereal.com SIEMENS -> www.sea.siemens.com/step/templates/lesson.mason?electricity:2:3:3
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: PROGRAMA DE CÁTEDRA: INFORMÁTICA Y RELACIONES HUMANAS | Pagina: 1]
   > Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas semanales
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 12]
   > - Natale, Lucía (Coordinadora) (2013). En carrera: escritura y lectura de textos académicos y profesionales. Argentina. Universidad Nacional de Ǫuilmes. Visto en [https://ediciones.ungs.edu.ar/wp-co
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > **Obligatoria** - Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] - Cisco Systems: Academia de Networking de Cisco Systems: Guía del primer añ
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > spacio de estados. Recocido Simulado. Búsqueda voraz primero el mejor. Búsqueda A*, Heurísticos admisibles, comparación entre varios heurísticos admisibles. Agentes Basados en Procesos de Búsqueda. *
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 12]
   > ría Teresa Sirven Clase 1 Maestría Tecnología Educativa [https://youtu.be/yBL4Hu9n Fic](https://youtu.be/yBL4Hu9n Fic) María Teresa Sirven Clase 2 Maestría Tecnología Educativa [https://youtu.be/dyd

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1378 | salida: 14 | total: 1392

---

### Pregunta 14

> - El profesor Ing. Jorge L. Schmukler da clases en Bases de Datos Avanzadas, en Inteligencia Artificial y en Redes y Comunicaciones.

**Chunks de contexto:**

1. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **EQUIPO DOCENTE** | Pagina: 1]
   > Teoría: Trossero, Sebastián (Trossero.sebastian@uader.edu.ar) Práctica: Schmuckler, Jorge (Schmukler.jorge@uader.edu.ar)
2. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **MODALIDAD DE CLASES** | Pagina: 1]
   > A partir de este año la materia será dictada de manera bimodal. El cronograma será definido en su mayoría por la Facultad. Aún no confirmado. Los links de clases se encuentran en el aula virtual. Las
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > **Facultad de Ciencia y Tecnología de la UADER** SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler.
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Estructura de Control: Procedimientos de Inferencia; Interfase con el usuario. Memoria de Trabajo, Módulo generador de explicaciones al usuario. **Capítulo V** **Funcionalidad de los Sistemas Exper
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (2
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > ntos métodos sobre el funcionamiento del sistema. Agentes Basados en Lógica Difusa. **Capítulo VIII** **Redes Neuronales Artificiales (RNA).** Generalidades, conceptos básicos Reseña Histórica. Cla

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1230 | salida: 14 | total: 1244

---

### Pregunta 15

> - ¿Cuál es el costo de la certificación oficial de Cisco que se menciona como opcional en la planificación?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > **Obligatoria** - Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] - Cisco Systems: Academia de Networking de Cisco Systems: Guía del primer añ
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Sitios web sobre normativas, tecnologías y soluciones, opcional** | Pagina: 5]
   > IETF -> www.ietf.org IEEE -> www.ieee.org ISO -> www.iso.org CISCO -> www.cisco.com IANA -> www.iana.org ISOC -> www.isoc.org ARIN -> www.arin.net LACNIC -> http://lacnic.net/sp/ LAC IPV6 TF -> www.la
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: UNDERWRITERS LABORATORIES (UL) -> www.ul.com | Pagina: 5]
   > PANDUIT -> www.panduit.com AMP -> www.tycoelectronics.com/components/ ETHEREAL -> www.ethereal.com SIEMENS -> www.sea.siemens.com/step/templates/lesson.mason?electricity:2:3:3
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > , topologías. Software de redes, jerarquías de protocolos, aspectos de diseño de las capas, servicios orientados a la conexión y no orientados a la conexión, primitivas de servicio, relación de servic
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > llas, arquitectura de red escalable, calidad de servicio, tendencia del networking). Explicar el **propósito de IOS como Sistema** **Operativo de red**, Explicar cómo acceder al IOS y cómo explorarlo
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 15]
   > cisco Gastón Gregorutti,<br>Dante Emanuel Tortul Cuatrín ; director José Luis Mengarelli.|2019| |Estrategia para planear una migración de software propietario a<br>software librepara la Facultad de Ci

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1483 | salida: 14 | total: 1497

---

### Pregunta 16

> - Para la Promoción Directa, se exige la aprobación de la totalidad de los trabajos prácticos (TP 1 al TP 5). ¿Cuál es la calificación numérica mínima que debe obtenerse en cada TP individual para que se considere aprobado?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 16]
   > Para acceder a la condición de Promoción Directa, el/la estudiante deberá cumplir con los siguientes requisitos: - 80 % de asistencia a la cursada. - Aprobación del examen parcial teórico con una
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > **Condición del Alumno:** - **ALUMNO PROMOCIONADO:** El estudiante logrará la promoción directa si alcanza un promedio general de **80 puntos** - más entre los **1 parcial** previstos, no pudiendo
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > PROMOCIONADO REGULAR LIBRE El alumno accederá a la condición de **PROMOCIÓN** si cumple con las siguientes condiciones de cátedra: **1 -** Obtener en los 3 parciales, una calificación promedio sup
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 15]
   > erto<br>Aldonate ; codirector Luciano María Caisso.|2018| **Requisitos para rendir como estudiantes regulares, promocionales y libres:** **a.** **Promoción Directa**
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 9]
   > a y unidad de muestreo. Tp 5: Elaboración de un escrito en donde presenten: Métodos, técnicas e instrumentos de recolección de datos. Posibles modos de comunicación de resultados. Tp integrador: Pr
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 9]
   > **Programa de trabajos prácticos:** Tp 1: Escritura académica. Se solicita a los estudiantes seleccionar un artículo de investigación sobre un tema de interés específico relacionado al campo profesi

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1409 | salida: 14 | total: 1423

---

### Pregunta 17

> - ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > icamente para el aprendizaje de la Investigación Operativa. Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - **PHP Simplex
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > atividad. **Unidad II: -Programación Lineal (PL)-** Propiedades de los modelos de Programación Lineal: proporcionalidad, aditividad, divisibilidad y certidumbre. Formulación de problemas de optimiz
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > factibles). **Unidad III: -Método SIMPLEX-** Algoritmo del método Simplex: forma estándar, variables de holgura y variables artificiales. Construcción de la tabla inicial, criterios de entrada y sa
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > mas de programación lineal (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gest
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > estructura del modelo y suposiciones. Métodos para obtener una solución básica inicial: Esquina Noroeste, Costo Mínimo y Aproximación de Vogel. Método MODI (Distribución Modificada) para la optimiza

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1491 | salida: 14 | total: 1505

---

### Pregunta 18

> - ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > recuperación sustituirá automáticamente a la nota del examen original. **Protocolos de Evaluación:** Los resultados se publicarán en un plazo de siete días corridos tras la evaluación. Los exámenes
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > Presencial|Tutorías|Presentación tesina- ver<br>posibilidad| |25|08 de octubre|Virtual|Tutorías|Presentación tesina- ver<br>posibilidad| |26|15 de octubre|Virtual|Tutorías|Tutorías| |27|22 de octubre|
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > ril|Virtual|Práctica|| |7|23 de abril|Virtual|Teoría|Pregunta de investigación<br>(variables, unidad de análisis,<br>contexto)/ Antecedentes| |8|30 de abril|**_Presencial (pedir cambio_**<br>**_fecha)
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > **Condición del Alumno:** - **ALUMNO PROMOCIONADO:** El estudiante logrará la promoción directa si alcanza un promedio general de **80 puntos** - más entre los **1 parcial** previstos, no pudiendo
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > no de los requisitos de puntaje, trabajos prácticos o asistencia anteriormente detallados. **Instancias de Recuperación:** La cátedra dispone de **dos oportunidades de** **recuperatorio** totales.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1434 | salida: 14 | total: 1448

---

## Conversacion 3

**Parametros modificados respecto a la conversacion anterior:**

| Parametro | Valor |
|---|---|
| top_k | 5 |
| max_context_chunks | 5 |
| chunk_size | 512 |
| chunking_technique | recursive |

### Pregunta 1

> - ¿Cuáles son los contenidos de la materia Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > **Capítulo I** **Agentes Inteligentes** Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas por el área IA. Descripción de los temas específic
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos **Capítulo I** **Agentes Inteligentes**
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > **Capítulo III** **Sistemas Basados en Conocimientos**. Conceptos básicos. Representación de Conocimientos. Estructuras basadas en Lógica. Lógica de Primer Orden. Reglas de Inferencia. Representación
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Agentes Basados en Lógica Difusa. **Capítulo VIII** **Redes Neuronales Artificiales (RNA).** Generalidades, conceptos básicos Reseña Histórica. Clasificación de las RNA. Agentes basados en Proceso d
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (2

**Respuesta:**

El programa de contenidos de la materia Inteligencia Artificial comprende los siguientes capítulos:

1. **Agentes Inteligentes**: Introducción a los agentes inteligentes, entorno de trabajo, propiedades de los entornos, estructura de los agentes, programas de agentes y tipos de agentes (reactivos simples, basados en modelos, de objetivos y que aprenden).
2. **Sistemas Basados en Conocimientos**: Conceptos básicos, representación de conocimientos mediante estructuras lógicas y representación basada en objetos.
3. **Agentes Basados en Lógica Difusa**: 
4. **Redes Neuronales Artificiales (RNA)**: Generalidades, clasificación de las RNA y agentes basados en proceso de aprendizaje. Se trata específicamente de **Red Perceptron Simple**, incluyendo elemento de procesamiento, función de transferencia, condiciones de convergencia y algoritmo de modificación.

Además, el programa de contenidos incluye una bibliografía con dos títulos recomendados para la materia.

**Tokens:** entrada: 1137 | salida: 238 | total: 1375

---

### Pregunta 2

> - ¿En qué materia se enseña el concepto de Lógica Difusa?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Herramientas para el desarrollo de Sistemas Expertos. **Capítulo VI** **Lógica Difusa (Fuzzy).** Consideraciones generales, Conjuntos Difusos, definición. Operaciones simples entre conjuntos Difusos
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Agentes Basados en Lógica Difusa. **Capítulo VIII** **Redes Neuronales Artificiales (RNA).** Generalidades, conceptos básicos Reseña Histórica. Clasificación de las RNA. Agentes basados en Proceso d
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Proceso de Fuzzificación. Influencia de la forma y distribución de los Conjuntos Difusos, en el comportamiento del sistema. Proceso de Inferencia. Tratamiento paralelo de las reglas. Determinación de
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > **Capítulo III** **Sistemas Basados en Conocimientos**. Conceptos básicos. Representación de Conocimientos. Estructuras basadas en Lógica. Lógica de Primer Orden. Reglas de Inferencia. Representación
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Direccionamiento estático y dinámico. Planificación del direccionamiento (segmentación de red). Clase de direccionamiento (clase a, b, c, d y e). Prefijo y Mascara de red. Lógica de and. Calculo de

**Respuesta:**

La Lógica Difusa se enseña en la materia de Inteligencia Artificial.

**Tokens:** entrada: 1233 | salida: 20 | total: 1253

---

### Pregunta 3

> - ¿Cuál es el plan de estudios de Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > **Plan de estudios resumido** - Unidad 1: Introducción a la ciencia y conocimiento científico - Unidad 2: La dimensión epistemológica - Unidad 3: La dimensión de la estrategia general de investi
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > |METODOLOGÍA DE LA INVESTIGACIÓN- 2026|Col2|Col3|Col4|Col5| |---|---|---|---|---| |**Clase **|**FECHA**|**Tipo de encuentro**|**Tipo encuentro**|**Tema**| |1|12 de marzo|**Presencial**|**Teórico/práct
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: **Equipo docente:** PROFESORA RESPONSABLE ADJUNTO: ALEJANDRA MARǪUESIN; JEFE DE | Pagina: 1]
   > TRABAJOS PRÁCTICOS: TAMARA SUIVA. JEFE DE TRABAJOS PRÁCTICOS: JIMENA SANTA CRUZ; **Año de la carrera a la que pertenece la cátedra:** 4 **Régimen de la materia:** Anual **Carga horaria semanal:** 3
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 8]
   > carrera o profesionales expertos en temáticas de interés general para los estudiantes, con el objetivo de acompañar el desarrollo de sus temas de investigación y brindar orientación especializada.
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: dentro de la plataforma Moodle. La organización será la siguiente | Pagina: 5]
   > diagnóstico inicial, solicitud de clases de consulta y encuesta de valoración del curso. - Desarrollo de contenidos: distribuidos en tres pestañas temáticas: - Introducción - Dimensión epistemo

**Respuesta:**

El plan de estudios de la materia de Metodología de la Investigación se describe en la siguiente manera:

* Se divide en cuatro unidades:
  1. Introducción a la ciencia y conocimiento científico
  2. La dimensión epistemológica
  3. La dimensión de la estrategia general de investigación
  4. La Dimensión de las técnicas de obtención y análisis de información empírica. La comunicación de los resultados

No se proporciona más información sobre el plan de estudios.

**Tokens:** entrada: 1316 | salida: 123 | total: 1439

---

### Pregunta 4

> - ¿Qué herramientas de software se recomiendan en la carrera para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > programación lineal (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de o
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad II: -Programación Lineal (PL)-** Propiedades de los modelos de Programación Lineal: proporcionalidad, aditividad, divisibilidad y certidumbre. Formulación de problemas de optimización. Reso
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINGO (64 bits):** Una versión avanzada y más potente del motor LINDO. Está diseñado para modelar y resolver problemas de optimización de gran escala, permitiendo una integración más fluida con
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > de la Investigación Operativa. Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - **PHP Simplex:** Herramienta online accesib

**Respuesta:**

Según el programa de Investigación Operativa, se recomiendan las herramientas LINGO (64 bits) y LINDO para resolver problemas de optimización lineal. Se menciona que LINGO es una versión avanzada y más potente del motor LINDO, lo que sugiere que ambos se relacionan entre sí, pero no se especifica cómo exactamente. 

En cuanto a la relación con las unidades teóricas, se menciona que el método Simplex se trata en la Unidad III, que coincide con el funcionamiento de LINGO (64 bits) y el motor LINDO, que incluye módulos para el Método Simplex. 

No se mencionan otras herramientas recomendadas específicamente para resolver problemas de optimización lineal relacionadas con la Unidad II de Programación Lineal (PL).

**Tokens:** entrada: 1239 | salida: 181 | total: 1420

---

### Pregunta 5

> - ¿Qué instancias de recuperación nos provee Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > asistencia anteriormente detallados. **Instancias de Recuperación:** La cátedra dispone de **dos oportunidades de** **recuperatorio** totales. Estas pueden utilizarse para cualquiera de los dos parc
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINGO (64 bits):** Una versión avanzada y más potente del motor LINDO. Está diseñado para modelar y resolver problemas de optimización de gran escala, permitiendo una integración más fluida con
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad I: -Introducción y Modelos Matemáticos-** Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del problema, construcción del modelo mate
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > programación lineal (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de o
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > de la Investigación Operativa. Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - **PHP Simplex:** Herramienta online accesib

**Respuesta:**

La cátedra dispone de **dos oportunidades de recuperatorio** totales.

**Tokens:** entrada: 1197 | salida: 19 | total: 1216

---

### Pregunta 6

> - ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > programación lineal (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de o
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > |21|10<br>de<br>septiembr<br>e|Virtual|Tutorías|Avances proyectos a la<br>cátedra-Grupos Tamara| |22|17<br>de<br>septiembr<br>e|Teoría|Coloquio|Avances proyectos a la<br>cátedra-Grupos Jimena| |23|24<
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: **I. FUNDAMENTACIÓN** | Pagina: 1]
   > Los estudiantes explorarán los efectos de las nuevas tecnologías en el trabajo, la calidad de vida laboral y la administración del talento humano en la era digital. Además, se abordarán aspectos legal
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > de la Investigación Operativa. Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - **PHP Simplex:** Herramienta online accesib

**Respuesta:**

TORA es una herramienta educativa diseñada específicamente para el aprendizaje de la Investigación Operativa. Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos.

**Tokens:** entrada: 1198 | salida: 55 | total: 1253

---

### Pregunta 7

> - ¿Qué profesor forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes?

**Chunks de contexto:**

1. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **EQUIPO DOCENTE** | Pagina: 1]
   > Teoría: Trossero, Sebastián (Trossero.sebastian@uader.edu.ar) Práctica: Schmuckler, Jorge (Schmukler.jorge@uader.edu.ar)
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > **Facultad de Ciencia y Tecnología de la UADER** SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler.
3. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **MODALIDAD DE CLASES** | Pagina: 1]
   > A partir de este año la materia será dictada de manera bimodal. El cronograma será definido en su mayoría por la Facultad. Aún no confirmado. Los links de clases se encuentran en el aula virtual. Las
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > **Obligatoria** - Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] - Cisco Systems: Academia de Networking de Cisco Systems: Guía del primer añ
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > - Halsall, Fred: Redes de computadores e Internet / F. Halsall. - 5a ed. - Madrid: Pearson Educación, 2006. ISBN 9788478290833 [Disponible en Biblioteca FCyT- Oro Verde] - Huidobro Moya, José Manuel

**Respuesta:**

Jorge L. Schmukler forma parte del equipo docente en ambas materias, Bases de Datos Avanzadas y Comunicaciones y Redes.

**Tokens:** entrada: 1115 | salida: 36 | total: 1151

---

### Pregunta 8

> - ¿Qué otra asignatura, además de la propia materia de Inteligencia Artificial, incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > **Capítulo I** **Agentes Inteligentes** Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas por el área IA. Descripción de los temas específic
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 4. El impacto de la inteligencia artificial en la gestión del talento. | Pagina: 2]
   > _**Bibliografía Nacional:**_ Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales. **Uni
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Proceso de Fuzzificación. Influencia de la forma y distribución de los Conjuntos Difusos, en el comportamiento del sistema. Proceso de Inferencia. Tratamiento paralelo de las reglas. Determinación de
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (2
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > **Capítulo XII** **Sistemas Multi Agentes** Introducción a los sistemas multiagente, modelos formales. Metodologías de diseño basadas en agentes. Metodología Gaia: Modelo de Actividades. Modelo de R

**Respuesta:**

La asignatura de Informática y Recursos Humanos incluye explícitamente el impacto de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas, específicamente en la Sección 4, El impacto de la inteligencia artificial en la gestión del talento.

**Tokens:** entrada: 1244 | salida: 64 | total: 1308

---

### Pregunta 9

> - Los requisitos para regularizar en Bases de Datos Avanzadas y en Redes y Comunicaciones, ¿son iguales? ¿Qué diferencias tienen?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > **Evaluación Final:** El alumno con condición de REGULAR, deberá rendir un examen de los temas teóricos y prácticos desarrollados en la materia (prueba escrita). El alumno LIBRE rendirá un examen fina
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Tipos de ethernet (10base5, 10base2, 10base-t, 100base-tx, 100base-fx, 1000base-t, 1000base-sx, 1000base-lx, la ethernet de 10 gigabits (10gbe)). Utilización de hubs como dispositivo intermedio (pro
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > ; Algoritmos de enrutamiento (Principio de optimización, Enrutamiento por la ruta más corta, Inundación, Enrutamiento por vector de distancia, Enrutamiento por estado del enlace, Enrutamiento jerárqui
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > El alumno accederá a la condición de **REGULAR**, si cumple con las siguientes condiciones de cátedra: **1 -** Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos.
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > . Protocolo enlace de datos ( **HDLC** -Control de enlace de datos de alto nivel-, Capa de enlace de datos en Internet -Protocolo **PPP** (Protocolo Punto a Punto)-). **Unidad V**: - **Capa de enlace

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1282 | salida: 14 | total: 1296

---

### Pregunta 10

> - ¿Cuál es el porcentaje de asistencia a clases que exigen en común las materias de Investigación Operativa, Comunicaciones y Redes, y Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > **b.** **Alumno Regular** - 60 % de asistencia. - Aprobación del examen parcial teórico con una calificación igual o superior a 60 (sesenta) puntos. - Entrega de todos los trabajos en tiempo y
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > pueden asistir a todas las clases y, al mismo tiempo, reducir la tasa de abandono. Por ello, los materiales teóricos y las lecturas obligatorias se compartirán con una semana de antelación al encuen
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: **Equipo docente:** PROFESORA RESPONSABLE ADJUNTO: ALEJANDRA MARǪUESIN; JEFE DE | Pagina: 1]
   > TRABAJOS PRÁCTICOS: TAMARA SUIVA. JEFE DE TRABAJOS PRÁCTICOS: JIMENA SANTA CRUZ; **Año de la carrera a la que pertenece la cátedra:** 4 **Régimen de la materia:** Anual **Carga horaria semanal:** 3
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > **Condición del Alumno:** - **ALUMNO PROMOCIONADO:** El estudiante logrará la promoción directa si alcanza un promedio general de **80 puntos** - más entre los **1 parcial** previstos, no pudiendo

**Respuesta:**

La información sobre el porcentaje de asistencia a clases común entre las materias de Investigación Operativa, Comunicaciones y Redes y Metodología de la Investigación no se encuentra en el contexto proporcionado.

**Tokens:** entrada: 1367 | salida: 47 | total: 1414

---

### Pregunta 11

> - Un proyecto integrador requiere utilizar un software para resolver problemas de optimización a gran escala que pueda conectarse de forma fluida con bases de datos espaciales. Según las herramientas enseñadas en las materias, ¿qué combinación de software visto en Bases de Datos Avanzadas e Investigación Operativa sería la más adecuada para este objetivo?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINGO (64 bits):** Una versión avanzada y más potente del motor LINDO. Está diseñado para modelar y resolver problemas de optimización de gran escala, permitiendo una integración más fluida con
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > programación lineal (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de o
4. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **SOFTWARE REQUERIDO** | Pagina: 2]
   > PostgreSQL: versión 9.6 o superior SQL Server: versión 2016 o superior QGIS: versión compatible con PostgreSQL Anaconda (Python): últimas versiones
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra

**Respuesta:**

Para resolver problemas de optimización a gran escala que puedan conectarse de forma fluida con bases de datos espaciales, se necesita un software que combine la capacidad de resolver modelos complejos con la capacidad de integrarse con bases de datos. En Investigación Operativa se menciona que LINGO es una versión avanzada del motor LINDO, que está diseñado para modelar y resolver problemas de optimización de gran escala, permitiendo una integración más fluida con bases de datos. Sin embargo, la conexión con bases de datos espaciales es más relevante para el campo de las Bases de Datos Avanzadas. Allí se especifica que se requiere QGIS, versión compatible con PostgreSQL, que es una base de datos gestionable y de código abierto, y PostgreSQL, versión 9.6 o superior. Este software se ajusta a las especificaciones requeridas para la resolución de problemas de optimización en grandes escenarios y la integración con bases de datos espaciales.

**Tokens:** entrada: 1081 | salida: 213 | total: 1294

---

### Pregunta 12

> - Si un estudiante desea investigar sobre el impacto de los "Agentes que aprenden" y las "Redes Neuronales" en la selección de personal y el teletrabajo en Argentina, ¿qué normativas legales y temas específicos de los programas de Inteligencia Artificial y RRHH debería cruzar en su marco teórico?

**Chunks de contexto:**

1. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: **I. FUNDAMENTACIÓN** | Pagina: 1]
   > Los estudiantes explorarán los efectos de las nuevas tecnologías en el trabajo, la calidad de vida laboral y la administración del talento humano en la era digital. Además, se abordarán aspectos legal
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: IV. BIBLIOGRAFÍA GENERAL | Pagina: 3]
   > _**Bibliografía Complementaria:**_ Reglamento de Teletrabajo en Argentina. Legislación sobre delitos informáticos en Argentina. Artículos académicos sobre la transformación del trabajo y el impacto
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 3]
   > Legislación sobre delitos informáticos en Argentina. Ley Nacional de Protección de Datos Personales (Ley 25.326). Ley Propiedad Intelectual (Ley 11.723) y su modificatoria. **Unidad 5: Trabajo Autó
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 2]
   > Reglamento de Teletrabajo en Argentina. Nicolás S. Tato, El Derecho Informático - Aspectos Fundamentales. Mariana Nazar, Tecnologías, información y derechos. **Unidad 2:** **Relaciones Humanas en e
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 4. El impacto de la inteligencia artificial en la gestión del talento. | Pagina: 2]
   > _**Bibliografía Nacional:**_ Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales. **Uni

**Respuesta:**

Para investigar sobre el impacto de los "Agentes que aprenden" y las "Redes Neuronales" en la selección de personal y el teletrabajo en Argentina, el estudiante debería cruzar los siguientes aspectos en su marco teórico:

- Normativa legal: El estudiante debería estudiar el Reglamento de Teletrabajo en Argentina, ya que es un tema específico mencionado en la Bibliografía Complementaria y en el contexto del Programa.
- Temas específicos de Inteligencia Artificial (IA) y RRHH: El estudiante debería profundizar en los artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales. Además, consideraría la obra de Nicolás S. Tato, "El Derecho Informático - Aspectos Fundamentales", así como los artículos de Mariana Nazar, "Tecnologías, información y derechos" y "Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías".
- Relación con la Inteligencia Artificial: Consideraría el artículo "Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías" para entender el impacto de la IA en las relaciones laborales.
- Relación con el Teletrabajo: Revisaría el "Reglamento de Teletrabajo en Argentina" para comprender las implicaciones legales del teletrabajo en el país.

Por lo tanto, para una investigación integral sobre el impacto de los "Agentes que aprenden" y las "Redes Neuronales" en la selección de personal y el teletrabajo en Argentina, el estudiante debería tener en cuenta estos aspectos y cruce de conceptos para formar un marco teórico sólido.

**Tokens:** entrada: 1056 | salida: 384 | total: 1440

---

### Pregunta 13

> - ¿Dónde puedo descargar la materia de Cálculo de 1er año?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > **Obligatoria** - Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] - Cisco Systems: Academia de Networking de Cisco Systems: Guía del primer añ
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: UNDERWRITERS LABORATORIES (UL) -> www.ul.com | Pagina: 5]
   > PANDUIT -> www.panduit.com AMP -> www.tycoelectronics.com/components/ ETHEREAL -> www.ethereal.com SIEMENS -> www.sea.siemens.com/step/templates/lesson.mason?electricity:2:3:3
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: PROGRAMA DE CÁTEDRA: INFORMÁTICA Y RELACIONES HUMANAS | Pagina: 1]
   > Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas semanales
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 12]
   > - Natale, Lucía (Coordinadora) (2013). En carrera: escritura y lectura de textos académicos y profesionales. Argentina. Universidad Nacional de Ǫuilmes. Visto en [https://ediciones.ungs.edu.ar/wp-co
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos **Capítulo I** **Agentes Inteligentes**

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1088 | salida: 14 | total: 1102

---

### Pregunta 14

> - El profesor Ing. Jorge L. Schmukler da clases en Bases de Datos Avanzadas, en Inteligencia Artificial y en Redes y Comunicaciones.

**Chunks de contexto:**

1. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **EQUIPO DOCENTE** | Pagina: 1]
   > Teoría: Trossero, Sebastián (Trossero.sebastian@uader.edu.ar) Práctica: Schmuckler, Jorge (Schmukler.jorge@uader.edu.ar)
2. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **MODALIDAD DE CLASES** | Pagina: 1]
   > A partir de este año la materia será dictada de manera bimodal. El cronograma será definido en su mayoría por la Facultad. Aún no confirmado. Los links de clases se encuentran en el aula virtual. Las
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > **Facultad de Ciencia y Tecnología de la UADER** SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler.
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Estructura de Control: Procedimientos de Inferencia; Interfase con el usuario. Memoria de Trabajo, Módulo generador de explicaciones al usuario. **Capítulo V** **Funcionalidad de los Sistemas Exper
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Comportamiento de Agentes Basados en Conocimientos. **Capítulo IV** **Diseño de los Sistemas Expertos**. Definición y descripción de sus módulos componentes. Proceso de Adquisición de Conocimiento.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 987 | salida: 14 | total: 1001

---

### Pregunta 15

> - ¿Cuál es el costo de la certificación oficial de Cisco que se menciona como opcional en la planificación?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > **Obligatoria** - Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] - Cisco Systems: Academia de Networking de Cisco Systems: Guía del primer añ
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Sitios web sobre normativas, tecnologías y soluciones, opcional** | Pagina: 5]
   > IETF -> www.ietf.org IEEE -> www.ieee.org ISO -> www.iso.org CISCO -> www.cisco.com IANA -> www.iana.org ISOC -> www.isoc.org ARIN -> www.arin.net LACNIC -> http://lacnic.net/sp/ LAC IPV6 TF -> www.la
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: UNDERWRITERS LABORATORIES (UL) -> www.ul.com | Pagina: 5]
   > PANDUIT -> www.panduit.com AMP -> www.tycoelectronics.com/components/ ETHEREAL -> www.ethereal.com SIEMENS -> www.sea.siemens.com/step/templates/lesson.mason?electricity:2:3:3
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > . Modelo de referencia OSI, Modelo de protocolo TCP/IP, comparación modelo OSI y TCP/IP, critica al modelo OSI y los protocolos; Organismos de estandarización de comunicación y redes. **Unidad II**: -
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > : - **Capa de enlace de dato** - **sub capa** **LLC (control de enlace lógico)** Cuestiones en el diseño de la capa de enlace de dato, servicios proporcionados por la capa de red, entramado, control d

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1293 | salida: 14 | total: 1307

---

### Pregunta 16

> - Para la Promoción Directa, se exige la aprobación de la totalidad de los trabajos prácticos (TP 1 al TP 5). ¿Cuál es la calificación numérica mínima que debe obtenerse en cada TP individual para que se considere aprobado?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 16]
   > Para acceder a la condición de Promoción Directa, el/la estudiante deberá cumplir con los siguientes requisitos: - 80 % de asistencia a la cursada. - Aprobación del examen parcial teórico con una
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > **Condición del Alumno:** - **ALUMNO PROMOCIONADO:** El estudiante logrará la promoción directa si alcanza un promedio general de **80 puntos** - más entre los **1 parcial** previstos, no pudiendo
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 15]
   > **Requisitos para rendir como estudiantes regulares, promocionales y libres:** **a.** **Promoción Directa**
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > PROMOCIONADO REGULAR LIBRE El alumno accederá a la condición de **PROMOCIÓN** si cumple con las siguientes condiciones de cátedra: **1 -** Obtener en los 3 parciales, una calificación promedio sup
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > _El trabajo práctico integrador será recepcionado y revisado por el equipo docente. En caso de_ _requerirse ajustes, se remitirá un informe con las observaciones correspondientes y se_ _establecerá

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1214 | salida: 14 | total: 1228

---

### Pregunta 17

> - ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > de la Investigación Operativa. Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - **PHP Simplex:** Herramienta online accesib
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad II: -Programación Lineal (PL)-** Propiedades de los modelos de Programación Lineal: proporcionalidad, aditividad, divisibilidad y certidumbre. Formulación de problemas de optimización. Reso
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad III: -Método SIMPLEX-** Algoritmo del método Simplex: forma estándar, variables de holgura y variables artificiales. Construcción de la tabla inicial, criterios de entrada y salida de varia
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > programación lineal (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de o

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1268 | salida: 14 | total: 1282

---

### Pregunta 18

> - ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > **Protocolos de Evaluación:** Los resultados se publicarán en un plazo de siete días corridos tras la evaluación. Los exámenes se desarrollarán estrictamente en los bloques horarios asignados a la m
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > asistencia anteriormente detallados. **Instancias de Recuperación:** La cátedra dispone de **dos oportunidades de** **recuperatorio** totales. Estas pueden utilizarse para cualquiera de los dos parc
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > |5|09 de abril|**Presencial**|**Teoría**|Tema/ problema| |6|16 de abril|Virtual|Práctica|| |7|23 de abril|Virtual|Teoría|Pregunta de investigación<br>(variables, unidad de análisis,<br>contexto)/ Ante
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > |16|06 de agosto|Virtual|Teoría|Repaso del proceso de| |||||investigación| |17|13 de agosto|Virtual|Tutorías|Tutorías| |18|20 de agosto|**_Presencial (cambio_**<br>**_encuentro)_**|**Teoría**|Parcial

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1324 | salida: 14 | total: 1338

---

## Conversacion 4

**Parametros modificados respecto a la conversacion anterior:**

| Parametro | Valor |
|---|---|
| top_k | 8 |
| retrieval_type | mmr |
| max_context_chunks | 8 |

### Pregunta 1

> - ¿Cuáles son los contenidos de la materia Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > **Capítulo I** **Agentes Inteligentes** Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas por el área IA. Descripción de los temas específic
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > **Capítulo III** **Sistemas Basados en Conocimientos**. Conceptos básicos. Representación de Conocimientos. Estructuras basadas en Lógica. Lógica de Primer Orden. Reglas de Inferencia. Representación
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (2
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > **Capítulo IX** **Redes** **Perceptron** **Multicapa**, estructura básica. Proceso de Entrenamiento Backpropagation (BP). Interpretación heurística y matemática del procedimiento BP. Término de Momen
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Herramientas para el desarrollo de Sistemas Expertos. **Capítulo VI** **Lógica Difusa (Fuzzy).** Consideraciones generales, Conjuntos Difusos, definición. Operaciones simples entre conjuntos Difusos
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: pesos. Regiones de Decisión. Problema de separación lineal. Aplicaciones. Limitaciones | Pagina: 2]
   > Problema XOR.
7. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: **I. FUNDAMENTACIÓN** | Pagina: 1]
   > Los estudiantes explorarán los efectos de las nuevas tecnologías en el trabajo, la calidad de vida laboral y la administración del talento humano en la era digital. Además, se abordarán aspectos legal
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > : - **Capa de enlace de dato** - **sub capa** **LLC (control de enlace lógico)** Cuestiones en el diseño de la capa de enlace de dato, servicios proporcionados por la capa de red, entramado, control d

**Respuesta:**

Los contenidos de la materia Inteligencia Artificial incluyen:

* Agentes Inteligentes: Introducción a la Inteligencia Artificial, definiciones y objetivos, herramientas y técnicas, entorno de trabajo, propiedades de los entornos, estructura de los agentes, programas de agentes, agente reactivo simple, agentes reactivos basados en modelos, agente basado en objetivos y agentes que aprenden.
* Sistemas Basados en Conocimientos: Conceptos básicos, representación de conocimientos, estructuras basadas en lógica, lógica de primer orden, reglas de inferencia, representación basada en objetos, definición de objetos y de atributos, clases e instancias, concepto de herencia, métodos y mensajes, representación de conocimientos mediante reglas y estructura básica.
* Redes Perceptron Multicapa: estructura básica, proceso de entrenamiento backpropagation (BP), interpretación heurística y matemática del procedimiento BP, término de momento, superficies de error, mínimos locales y mínimo global, función de transferencia, condiciones de inicialización y problema de saturación prematura.
* Lógica Difusa (Fuzzy): consideraciones generales, conjuntos difusos, definición, operaciones simples entre conjuntos difusos y estructuras FAM (Fuzzy Associative Memories).
* Sistemas Difusos: consideraciones generales, representación de conocimiento estructurado mediante reglas lingüísticas, regiones de decisión y problema de separación lineal.

Además, se incluyen herramientas para el desarrollo de Sistemas Expertos y el tema de Aprendizaje Automático y Aprendizaje Profundo con Python, scikit-learn y TensorFlow.

**Tokens:** entrada: 1649 | salida: 389 | total: 2038

---

### Pregunta 2

> - ¿En qué materia se enseña el concepto de Lógica Difusa?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Herramientas para el desarrollo de Sistemas Expertos. **Capítulo VI** **Lógica Difusa (Fuzzy).** Consideraciones generales, Conjuntos Difusos, definición. Operaciones simples entre conjuntos Difusos
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Agentes Basados en Lógica Difusa. **Capítulo VIII** **Redes Neuronales Artificiales (RNA).** Generalidades, conceptos básicos Reseña Histórica. Clasificación de las RNA. Agentes basados en Proceso d
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Direccionamiento estático y dinámico. Planificación del direccionamiento (segmentación de red). Clase de direccionamiento (clase a, b, c, d y e). Prefijo y Mascara de red. Lógica de and. Calculo de
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > final. _**Respecto a las clases:**_ La cátedra implementará el modelo de aula invertida, en el que los estudiantes adquieren los conocimientos teóricos de manera previa a la clase, a través de vide
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 3]
   > Conocimiento Científico. Concepto de ciencia. Diferentes modos de conocer y explicar la realidad: conocimiento vulgar, conocimiento científico. Clasificación de las ciencias. Diferencias entre cienc
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 15]
   > ; director Aldo Daniel Sigura ;<br>codirector Pablo Emanuel Goette.|2019| |Deep Learning aplicado al aprendizaje automático de ontologías para la<br>representación del conocimiento a partir de texto n
7. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: **I. FUNDAMENTACIÓN** | Pagina: 1]
   > Los estudiantes explorarán los efectos de las nuevas tecnologías en el trabajo, la calidad de vida laboral y la administración del talento humano en la era digital. Además, se abordarán aspectos legal
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par

**Respuesta:**

La Lógica Difusa se aborda en la materia de Inteligencia Artificial.

**Tokens:** entrada: 1683 | salida: 20 | total: 1703

---

### Pregunta 3

> - ¿Cuál es el plan de estudios de Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > **Plan de estudios resumido** - Unidad 1: Introducción a la ciencia y conocimiento científico - Unidad 2: La dimensión epistemológica - Unidad 3: La dimensión de la estrategia general de investi
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > |METODOLOGÍA DE LA INVESTIGACIÓN- 2026|Col2|Col3|Col4|Col5| |---|---|---|---|---| |**Clase **|**FECHA**|**Tipo de encuentro**|**Tipo encuentro**|**Tema**| |1|12 de marzo|**Presencial**|**Teórico/práct
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: **Equipo docente:** PROFESORA RESPONSABLE ADJUNTO: ALEJANDRA MARǪUESIN; JEFE DE | Pagina: 1]
   > TRABAJOS PRÁCTICOS: TAMARA SUIVA. JEFE DE TRABAJOS PRÁCTICOS: JIMENA SANTA CRUZ; **Año de la carrera a la que pertenece la cátedra:** 4 **Régimen de la materia:** Anual **Carga horaria semanal:** 3
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 8]
   > carrera o profesionales expertos en temáticas de interés general para los estudiantes, con el objetivo de acompañar el desarrollo de sus temas de investigación y brindar orientación especializada.
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: dentro de la plataforma Moodle. La organización será la siguiente | Pagina: 5]
   > diagnóstico inicial, solicitud de clases de consulta y encuesta de valoración del curso. - Desarrollo de contenidos: distribuidos en tres pestañas temáticas: - Introducción - Dimensión epistemo
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > **comunicación de los resultados** Análisis de las opciones posibles (entrevistas, observación, análisis documental, etc). El análisis de los datos en la investigación: teorías y procedimientos manu
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > anteproyecto, mientras que el resto de las clases se desarrollarán de manera presencial mediadas por tecnología a través de Google Meet. En estos encuentros virtuales, se trabajarán tanto los fundam
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 5]
   > parte de los contenidos teóricos previstos en el programa, a fin de que el segundo cuatrimestre esté destinado de manera prioritaria y exclusiva a instancias de tutorías, acompañamiento personalizad

**Respuesta:**

El plan de estudios de Metodología de la Investigación está resumido en las unidades que se detallan a continuación: 

 - Unidad 1: Introducción a la ciencia y conocimiento científico
 - Unidad 2: La dimensión epistemológica
 - Unidad 3: La dimensión de la estrategia general de investigación
 - Unidad 4: La Dimensión de las técnicas de obtención y análisis de información empírica. La comunicación de los resultados.

Además, se menciona que la cátedra abordará tanto aspectos teóricos como prácticos y que el objetivo principal es la elaboración de un Anteproyecto de Investigación.

**Tokens:** entrada: 1800 | salida: 163 | total: 1963

---

### Pregunta 4

> - ¿Qué herramientas de software se recomiendan en la carrera para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: pesos. Regiones de Decisión. Problema de separación lineal. Aplicaciones. Limitaciones | Pagina: 2]
   > Problema XOR.
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > Naturaleza recursiva de los cálculos: etapas, estados, decisiones y principio de optimalidad de Bellman. Resolución de problemas de diligencia, asignación de recursos y reemplazo de equipos. Diferen
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: PROGRAMA DE CÁTEDRA: INFORMÁTICA Y RELACIONES HUMANAS | Pagina: 1]
   > Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas semanales
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 7]
   > Durante los encuentros sincrónicos orientados a la práctica, se trabajará bajo modalidad de taller, con instancias de escritura guiada, revisión de avances y discusión de decisiones metodológicas, f
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: UNDERWRITERS LABORATORIES (UL) -> www.ul.com | Pagina: 5]
   > PANDUIT -> www.panduit.com AMP -> www.tycoelectronics.com/components/ ETHEREAL -> www.ethereal.com SIEMENS -> www.sea.siemens.com/step/templates/lesson.mason?electricity:2:3:3
8. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: **I. FUNDAMENTACIÓN** | Pagina: 1]
   > Los estudiantes explorarán los efectos de las nuevas tecnologías en el trabajo, la calidad de vida laboral y la administración del talento humano en la era digital. Además, se abordarán aspectos legal

**Respuesta:**

LINDO (Linear, Interactive, and Discrete Optimizer) es una herramienta de software especializada en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla para ingresar ecuaciones y restricciones de manera directa.

Además, en la Unidad IV del programa de Investigación Operativa se estudia el problema del transporte, que es un modelo de optimización lineal.

La relación de estas herramientas de software con las unidades teóricas de la carrera se encuentra descrita en el programa de Investigación Operativa.

**Tokens:** entrada: 1387 | salida: 130 | total: 1517

---

### Pregunta 5

> - ¿Qué instancias de recuperación nos provee Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > asistencia anteriormente detallados. **Instancias de Recuperación:** La cátedra dispone de **dos oportunidades de** **recuperatorio** totales. Estas pueden utilizarse para cualquiera de los dos parc
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > programación lineal (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de o
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad III: -Método SIMPLEX-** Algoritmo del método Simplex: forma estándar, variables de holgura y variables artificiales. Construcción de la tabla inicial, criterios de entrada y salida de varia
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > Naturaleza recursiva de los cálculos: etapas, estados, decisiones y principio de optimalidad de Bellman. Resolución de problemas de diligencia, asignación de recursos y reemplazo de equipos. Diferen
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 3]
   > hojas de cálculo.
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 16]
   > durante el proceso. - 80 % de los cuestionarios de autoevaluación respondidos. - Presentación y defensa oral del trabajo práctico integrador, previamente aprobado, en instancia de coloquio. Es r

**Respuesta:**

La cátedra de Investigación Operativa dispone de dos oportunidades de recuperatorio totales, que pueden utilizarse para cualquiera de los dos parciales con la restricción de que no se pueden aplicar ambos recuperatorios al mismo examen parcial.

**Tokens:** entrada: 1554 | salida: 59 | total: 1613

---

### Pregunta 6

> - ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > programación lineal (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de o
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > |21|10<br>de<br>septiembr<br>e|Virtual|Tutorías|Avances proyectos a la<br>cátedra-Grupos Tamara| |22|17<br>de<br>septiembr<br>e|Teoría|Coloquio|Avances proyectos a la<br>cátedra-Grupos Jimena| |23|24<
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: **I. FUNDAMENTACIÓN** | Pagina: 1]
   > Los estudiantes explorarán los efectos de las nuevas tecnologías en el trabajo, la calidad de vida laboral y la administración del talento humano en la era digital. Además, se abordarán aspectos legal
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos vertidos en la teoría. Más dos trabajos Prácticos que se realizan en el ho
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > **Capítulo IX** **Redes** **Perceptron** **Multicapa**, estructura básica. Proceso de Entrenamiento Backpropagation (BP). Interpretación heurística y matemática del procedimiento BP. Término de Momen
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: pesos. Regiones de Decisión. Problema de separación lineal. Aplicaciones. Limitaciones | Pagina: 2]
   > Problema XOR.
7. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: IV. BIBLIOGRAFÍA GENERAL | Pagina: 3]
   > _**Bibliografía Básica:**_ Nicolás S. Tato, El Derecho Informático - Aspectos Fundamentales. Mariana Nazar, Tecnologías, información y derechos. Gonzalo Ana Dobratinich, derecho y nuevas tecnología
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > final. _**Respecto a las clases:**_ La cátedra implementará el modelo de aula invertida, en el que los estudiantes adquieren los conocimientos teóricos de manera previa a la clase, a través de vide

**Respuesta:**

El software TORA es una herramienta educativa diseñada específicamente para el aprendizaje de la Investigación Operativa. Incluye módulos para el Método Simplex (con capacidad de resolver problemas de optimización lineal), lo que sugiere que se utiliza para ayudar a los estudiantes a comprender y aplicar técnicas de resolución de modelos de optimización y problemas de gestión a través de un enfoque interactivo y práctico.

**Tokens:** entrada: 1705 | salida: 99 | total: 1804

---

### Pregunta 7

> - ¿Qué profesor forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes?

**Chunks de contexto:**

1. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **EQUIPO DOCENTE** | Pagina: 1]
   > Teoría: Trossero, Sebastián (Trossero.sebastian@uader.edu.ar) Práctica: Schmuckler, Jorge (Schmukler.jorge@uader.edu.ar)
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > **Facultad de Ciencia y Tecnología de la UADER** SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler.
3. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **MODALIDAD DE CLASES** | Pagina: 1]
   > A partir de este año la materia será dictada de manera bimodal. El cronograma será definido en su mayoría por la Facultad. Aún no confirmado. Los links de clases se encuentran en el aula virtual. Las
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > - Arena, Héctor Facundo: Linux: la guía definitiva / H. F. Arena. - Buenos Aires: Gradi, 2010. ISBN 9789872601386 [Disponible en Biblioteca FCyT- Oro Verde] - Graziani, Rick: Conceptos y protocolos
5. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **HORARIOS DE CLASE** | Pagina: 1]
   > Lunes: 13:30 a 15:30 (Teoría) Viernes: 17:00 a 19:00 (Práctica) Nota: Los horarios están en proceso de evaluación y pueden sufrir cambios
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > . Modelo de referencia OSI, Modelo de protocolo TCP/IP, comparación modelo OSI y TCP/IP, critica al modelo OSI y los protocolos; Organismos de estandarización de comunicación y redes. **Unidad II**: -
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos vertidos en la teoría. Más dos trabajos Prácticos que se realizan en el ho
8. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **BIBLIOGRAFÍA BASE** | Pagina: 2]
   > Elmasri, R. / Navathe, S. - Fundamentos de Sistemas de Bases de Datos (Addison Wesley) Silberschatz / Korth / Sudarshan - Fundamentos de Bases de Datos (Mc Graw Hill) Date, C.J. - Introducción a los S

**Respuesta:**

Jorge L. Schmukler forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes.

**Tokens:** entrada: 1483 | salida: 38 | total: 1521

---

### Pregunta 8

> - ¿Qué otra asignatura, además de la propia materia de Inteligencia Artificial, incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > **Capítulo I** **Agentes Inteligentes** Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas por el área IA. Descripción de los temas específic
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 4. El impacto de la inteligencia artificial en la gestión del talento. | Pagina: 2]
   > _**Bibliografía Nacional:**_ Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales. **Uni
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (2
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > **Capítulo IX** **Redes** **Perceptron** **Multicapa**, estructura básica. Proceso de Entrenamiento Backpropagation (BP). Interpretación heurística y matemática del procedimiento BP. Término de Momen
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Herramientas para el desarrollo de Sistemas Expertos. **Capítulo VI** **Lógica Difusa (Fuzzy).** Consideraciones generales, Conjuntos Difusos, definición. Operaciones simples entre conjuntos Difusos
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: pesos. Regiones de Decisión. Problema de separación lineal. Aplicaciones. Limitaciones | Pagina: 2]
   > Problema XOR.
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > **Capítulo XI** Redes Autoorganizadas. Características generales. **Red SOM (Kohonen)**. Proceso de aprendizaje competitivo. Realimentación lateral. Algoritmo SOFM ó SOM (Self-Organizing -Feature-Ma
8. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: **I. FUNDAMENTACIÓN** | Pagina: 1]
   > Los estudiantes explorarán los efectos de las nuevas tecnologías en el trabajo, la calidad de vida laboral y la administración del talento humano en la era digital. Además, se abordarán aspectos legal

**Respuesta:**

Además de la materia de Inteligencia Artificial, la asignatura de Informática y Recursos Humanos incluye explícitamente el impacto o uso de la Inteligencia Artificial dentro de sus unidades temáticas. Esto se puede observar en la sección "4. El impacto de la inteligencia artificial en la gestión del talento" del documento "PROGRAMA INFORMATICA Y RRHH.pdf".

**Tokens:** entrada: 1601 | salida: 88 | total: 1689

---

### Pregunta 9

> - Los requisitos para regularizar en Bases de Datos Avanzadas y en Redes y Comunicaciones, ¿son iguales? ¿Qué diferencias tienen?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > **Evaluación Final:** El alumno con condición de REGULAR, deberá rendir un examen de los temas teóricos y prácticos desarrollados en la materia (prueba escrita). El alumno LIBRE rendirá un examen fina
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Tipos de ethernet (10base5, 10base2, 10base-t, 100base-tx, 100base-fx, 1000base-t, 1000base-sx, 1000base-lx, la ethernet de 10 gigabits (10gbe)). Utilización de hubs como dispositivo intermedio (pro
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > ; Algoritmos de enrutamiento (Principio de optimización, Enrutamiento por la ruta más corta, Inundación, Enrutamiento por vector de distancia, Enrutamiento por estado del enlace, Enrutamiento jerárqui
4. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **SOFTWARE REQUERIDO** | Pagina: 2]
   > PostgreSQL: versión 9.6 o superior SQL Server: versión 2016 o superior QGIS: versión compatible con PostgreSQL Anaconda (Python): últimas versiones
5. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **CANALES DE COMUNICACIÓN** | Pagina: 2]
   > Correo: Lista de mail (consultas y comunicación de rutina) Aula virtual: Material académico - Clave de matriculación: bda2023 (ÚNICO MEDIO OFICIAL) Telegram: https://t.me/+c7PPIrc9nQM4MzEx (avisos y n
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > : - **Capa de enlace de dato** - **sub capa** **LLC (control de enlace lógico)** Cuestiones en el diseño de la capa de enlace de dato, servicios proporcionados por la capa de red, entramado, control d
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Sitios web sobre normativas, tecnologías y soluciones, opcional** | Pagina: 5]
   > IETF -> www.ietf.org IEEE -> www.ieee.org ISO -> www.iso.org CISCO -> www.cisco.com IANA -> www.iana.org ISOC -> www.isoc.org ARIN -> www.arin.net LACNIC -> http://lacnic.net/sp/ LAC IPV6 TF -> www.la
8. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **RÉGIMEN DE CURSADA** | Pagina: 2]
   > **Regularidad:** Asistencia: Según norma vigente Todos los trabajos prácticos aprobados 6/7 parciales aprobados con más del 50% **Promoción:** Régimen regular Obtener más del 70% en todos los parci

**Respuesta:**

No dispongo de información en mis documentos para comparar los requisitos de regularidad en Bases de Datos Avanzadas y Redes y Comunicaciones.

**Tokens:** entrada: 1629 | salida: 34 | total: 1663

---

### Pregunta 10

> - ¿Cuál es el porcentaje de asistencia a clases que exigen en común las materias de Investigación Operativa, Comunicaciones y Redes, y Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > **b.** **Alumno Regular** - 60 % de asistencia. - Aprobación del examen parcial teórico con una calificación igual o superior a 60 (sesenta) puntos. - Entrega de todos los trabajos en tiempo y
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > pueden asistir a todas las clases y, al mismo tiempo, reducir la tasa de abandono. Por ello, los materiales teóricos y las lecturas obligatorias se compartirán con una semana de antelación al encuen
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: **Equipo docente:** PROFESORA RESPONSABLE ADJUNTO: ALEJANDRA MARǪUESIN; JEFE DE | Pagina: 1]
   > TRABAJOS PRÁCTICOS: TAMARA SUIVA. JEFE DE TRABAJOS PRÁCTICOS: JIMENA SANTA CRUZ; **Año de la carrera a la que pertenece la cátedra:** 4 **Régimen de la materia:** Anual **Carga horaria semanal:** 3
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: Dr Roberto Hernández Sampieri Charla enfoques cuantitativo, cualitativo, mixto | Pagina: 13]
   > [https://youtu.be/CfjSC_pp8o0](https://youtu.be/CfjSC_pp8o0) _Bibliografía obligatoria sobre escritura académica_ - Natale, Lucía (Coordinadora) (2013). En carrera: escritura y lectura de textos ac
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > asistencia anteriormente detallados. **Instancias de Recuperación:** La cátedra dispone de **dos oportunidades de** **recuperatorio** totales. Estas pueden utilizarse para cualquiera de los dos parc
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > final. _**Respecto a las clases:**_ La cátedra implementará el modelo de aula invertida, en el que los estudiantes adquieren los conocimientos teóricos de manera previa a la clase, a través de vide
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > . Modelo de referencia OSI, Modelo de protocolo TCP/IP, comparación modelo OSI y TCP/IP, critica al modelo OSI y los protocolos; Organismos de estandarización de comunicación y redes. **Unidad II**: -

**Respuesta:**

La materia de Investigación Operativa pide una asistencia del 80%, mientras que las materias de Metodología de la Investigación y Comunicaciones y Redes no especifican una asistencia requerida.

**Tokens:** entrada: 1903 | salida: 46 | total: 1949

---

### Pregunta 11

> - Un proyecto integrador requiere utilizar un software para resolver problemas de optimización a gran escala que pueda conectarse de forma fluida con bases de datos espaciales. Según las herramientas enseñadas en las materias, ¿qué combinación de software visto en Bases de Datos Avanzadas e Investigación Operativa sería la más adecuada para este objetivo?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINGO (64 bits):** Una versión avanzada y más potente del motor LINDO. Está diseñado para modelar y resolver problemas de optimización de gran escala, permitiendo una integración más fluida con
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > programación lineal (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de o
3. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **SOFTWARE REQUERIDO** | Pagina: 2]
   > PostgreSQL: versión 9.6 o superior SQL Server: versión 2016 o superior QGIS: versión compatible con PostgreSQL Anaconda (Python): últimas versiones
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad III: -Método SIMPLEX-** Algoritmo del método Simplex: forma estándar, variables de holgura y variables artificiales. Construcción de la tabla inicial, criterios de entrada y salida de varia
6. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Unidad VII: Bases de Datos Orientadas a Objetos - Parcial | Pagina: 1]
   > Nota: Los parciales serán agrupados en 2 o 3 instancias durante el cursado
7. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **EQUIPO DOCENTE** | Pagina: 1]
   > Teoría: Trossero, Sebastián (Trossero.sebastian@uader.edu.ar) Práctica: Schmuckler, Jorge (Schmukler.jorge@uader.edu.ar)
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > Deberá presentar el trabajo práctico integrador con una antelación mínima de veinte (20) días hábiles respecto de la fecha de la mesa de examen. En caso contrario, su evaluación se trasladará al tur

**Respuesta:**

La combinación de software que sería más adecuada para resolver problemas de optimización a gran escala y conectarse con bases de datos espaciales es utilizar **Lindo (Lingo)** de la materia Investigación Operativa, ya que está diseñado para modelar y resolver problemas de gran escala, permitiendo una integración más fluida con bases de datos.

En la materia Bases de Datos Avanzadas no se encontró un software específico que se relacione directamente con la conectividad con bases de datos espaciales, pero en la sección de software requerido, se menciona que se necesita QGIS, que es compatible con PostgreSQL, y se menciona la necesidad de utilizar Anaconda (Python) con versiones recientes. Sin embargo, no se ha encontrado evidencia de que el software de QGIS o Anaconda esté relacionado con problemas de optimización a gran escala.

Sin embargo, no tengo información específica sobre la conectividad de Lingo con bases de datos espaciales. 

En cuanto a la opción de conectividad de bases de datos, se podría considerar utilizar la versión 9.6 o superior de PostgreSQL, que se menciona en la sección de software requerido de la materia Bases de Datos Avanzadas. 

**Nota**: No dispongo de información en mis documentos para determinar si el software QGIS o Anaconda (Python) están diseñados para resolver problemas de optimización a gran escala y si se pueden conectar con bases de datos espaciales.

**Tokens:** entrada: 1329 | salida: 320 | total: 1649

---

### Pregunta 12

> - Si un estudiante desea investigar sobre el impacto de los "Agentes que aprenden" y las "Redes Neuronales" en la selección de personal y el teletrabajo en Argentina, ¿qué normativas legales y temas específicos de los programas de Inteligencia Artificial y RRHH debería cruzar en su marco teórico?

**Chunks de contexto:**

1. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: **I. FUNDAMENTACIÓN** | Pagina: 1]
   > Los estudiantes explorarán los efectos de las nuevas tecnologías en el trabajo, la calidad de vida laboral y la administración del talento humano en la era digital. Además, se abordarán aspectos legal
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: IV. BIBLIOGRAFÍA GENERAL | Pagina: 3]
   > _**Bibliografía Complementaria:**_ Reglamento de Teletrabajo en Argentina. Legislación sobre delitos informáticos en Argentina. Artículos académicos sobre la transformación del trabajo y el impacto
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 4. El impacto de la inteligencia artificial en la gestión del talento. | Pagina: 2]
   > _**Bibliografía Nacional:**_ Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales. **Uni
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Agentes Basados en Lógica Difusa. **Capítulo VIII** **Redes Neuronales Artificiales (RNA).** Generalidades, conceptos básicos Reseña Histórica. Clasificación de las RNA. Agentes basados en Proceso d
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 4. Derecho a la desconexión digital y equilibrio entre vida personal y laboral. | Pagina: 2]
   > _**Bibliografía Nacional:**_ Ley Nacional de Protección de Datos Personales (Ley 25.326). Código Civil y Comercial de la Nación (aspectos relacionados con contratos digitales y firma electrónica).
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > **Capítulo XI** Redes Autoorganizadas. Características generales. **Red SOM (Kohonen)**. Proceso de aprendizaje competitivo. Realimentación lateral. Algoritmo SOFM ó SOM (Self-Organizing -Feature-Ma
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 14]
   > ; director Fernando Sato ;<br>codirector Sebastián Jorge Trossero.|2022| |Modelos vectoriales y redes neuronales artifciales, para la aplicación de<br>procesamiento de lenguaje natural en normativas j
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > . **Conceptos** **usados en Comunicaciones y Redes:** Uso de la redes de computadora, aplicaciones de negocios, domésticas, distintos usuarios. Hardware de redes, Sistema Cliente/Servidor, tipos de re

**Respuesta:**

En primer lugar, es importante mencionar que "Agentes que aprenden" y "Redes Neuronales" son conceptos estrechamente relacionados entre sí, como lo describen en el "IA - Programa de Cátedra (campus)".

Para la selección de personal y el teletrabajo en Argentina, el estudiante podría cruzar los siguientes temas en su marco teórico:

*   "Derecho a la desconexión digital y equilibrio entre vida personal y laboral" (sección 4 del programa de Informática y RRHH), especialmente la "Ley Nacional de Protección de Datos Personales (Ley 25.326)" y el "Código Civil y Comercial de la Nación" (aspectos relacionados con contratos digitales y firma electrónica).
*   El "Reglamento de Teletrabajo en Argentina" (en la sección de Bibliografía Complementaria del programa de Informática y RRHH).
*   Aspectos legales fundamentales para comprender el impacto normativo de las TIC en el ámbito laboral, tomando como base la legislación argentina y los aportes de autores nacionales (mencionado en la sección I. Fundamentación del programa de Informática y RRHH).
*   "Modelos vectoriales y redes neuronales artifciales, para la aplicación de procesamiento de lenguaje natural en normativas jurídicas / Julián Lanfranco" y "Diseño de una base de datos espacio-temporal para la modelización hidrológica y geomorfológica de la cuenca del río Paraná, Entre Ríos / Lucas Leonel Barreto López, Juan Cruz Mantovani" (publicaciones en el programa de Metodología de la Investigación)

**Tokens:** entrada: 1650 | salida: 392 | total: 2042

---

### Pregunta 13

> - ¿Dónde puedo descargar la materia de Cálculo de 1er año?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > **Obligatoria** - Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] - Cisco Systems: Academia de Networking de Cisco Systems: Guía del primer añ
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 12]
   > - Natale, Lucía (Coordinadora) (2013). En carrera: escritura y lectura de textos académicos y profesionales. Argentina. Universidad Nacional de Ǫuilmes. Visto en [https://ediciones.ungs.edu.ar/wp-co
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos **Capítulo I** **Agentes Inteligentes**
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio | Pagina: 1]
   > Docente: Abog. Rodriguez Zanin, Fabio
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > : - **Capa de enlace de dato** - **sub capa** **LLC (control de enlace lógico)** Cuestiones en el diseño de la capa de enlace de dato, servicios proporcionados por la capa de red, entramado, control d
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: pesos. Regiones de Decisión. Problema de separación lineal. Aplicaciones. Limitaciones | Pagina: 2]
   > Problema XOR.
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > : enfoque y<br>tipo de investigación / muestra| |14|11 de junio|Virtual|Práctica|| |15|18 de junio|Virtual|Teoría|Marco metodológico II:<br>recolección de datos y análisis de<br>datos| |||||| |RECESO
8. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **PRESENTACIÓN DE LA MATERIA** | Pagina: 1]
   > Facultad de Ciencia y Tecnología Universidad Autónoma de Entre Ríos (UADER)

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1461 | salida: 14 | total: 1475

---

### Pregunta 14

> - El profesor Ing. Jorge L. Schmukler da clases en Bases de Datos Avanzadas, en Inteligencia Artificial y en Redes y Comunicaciones.

**Chunks de contexto:**

1. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **EQUIPO DOCENTE** | Pagina: 1]
   > Teoría: Trossero, Sebastián (Trossero.sebastian@uader.edu.ar) Práctica: Schmuckler, Jorge (Schmukler.jorge@uader.edu.ar)
2. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **MODALIDAD DE CLASES** | Pagina: 1]
   > A partir de este año la materia será dictada de manera bimodal. El cronograma será definido en su mayoría por la Facultad. Aún no confirmado. Los links de clases se encuentran en el aula virtual. Las
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > **Facultad de Ciencia y Tecnología de la UADER** SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler.
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (2
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > **Capítulo XI** Redes Autoorganizadas. Características generales. **Red SOM (Kohonen)**. Proceso de aprendizaje competitivo. Realimentación lateral. Algoritmo SOFM ó SOM (Self-Organizing -Feature-Ma
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Herramientas para el desarrollo de Sistemas Expertos. **Capítulo VI** **Lógica Difusa (Fuzzy).** Consideraciones generales, Conjuntos Difusos, definición. Operaciones simples entre conjuntos Difusos
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > . Protocolo enlace de datos ( **HDLC** -Control de enlace de datos de alto nivel-, Capa de enlace de datos en Internet -Protocolo **PPP** (Protocolo Punto a Punto)-). **Unidad V**: - **Capa de enlace
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > final. _**Respecto a las clases:**_ La cátedra implementará el modelo de aula invertida, en el que los estudiantes adquieren los conocimientos teóricos de manera previa a la clase, a través de vide

**Respuesta:**

El profesor Ing. Jorge L. Schmukler da clases en Bases de Datos Avanzadas.

**Tokens:** entrada: 1580 | salida: 24 | total: 1604

---

### Pregunta 15

> - ¿Cuál es el costo de la certificación oficial de Cisco que se menciona como opcional en la planificación?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > **Obligatoria** - Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] - Cisco Systems: Academia de Networking de Cisco Systems: Guía del primer añ
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Sitios web sobre normativas, tecnologías y soluciones, opcional** | Pagina: 5]
   > IETF -> www.ietf.org IEEE -> www.ieee.org ISO -> www.iso.org CISCO -> www.cisco.com IANA -> www.iana.org ISOC -> www.isoc.org ARIN -> www.arin.net LACNIC -> http://lacnic.net/sp/ LAC IPV6 TF -> www.la
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > PROMOCIONADO REGULAR LIBRE El alumno accederá a la condición de **PROMOCIÓN** si cumple con las siguientes condiciones de cátedra: **1 -** Obtener en los 3 parciales, una calificación promedio sup
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: PROGRAMA DE CÁTEDRA: INFORMÁTICA Y RELACIONES HUMANAS | Pagina: 1]
   > Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas semanales
5. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **SOFTWARE REQUERIDO** | Pagina: 2]
   > PostgreSQL: versión 9.6 o superior SQL Server: versión 2016 o superior QGIS: versión compatible con PostgreSQL Anaconda (Python): últimas versiones
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Utilización de medios según dispositivo a conectar. Conexiones WAN. **Unidad VII**: - **Capa de Red** Capa de Internet - Protocolo IPv4 (Protocolo de Internet versión 4), protocolos de la capa de re
7. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 5. comercio electrónico, manifestación del consentimiento en internet | Pagina: 3]
   > _**Bibliografía Nacional:**_ Ley de Teletrabajo (Ley 27.555) Código Civil y Comercial de la Nación (aspectos relacionados con contratos digitales). Artículos académicos sobre la economía gig y el t
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1583 | salida: 14 | total: 1597

---

### Pregunta 16

> - Para la Promoción Directa, se exige la aprobación de la totalidad de los trabajos prácticos (TP 1 al TP 5). ¿Cuál es la calificación numérica mínima que debe obtenerse en cada TP individual para que se considere aprobado?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 16]
   > Para acceder a la condición de Promoción Directa, el/la estudiante deberá cumplir con los siguientes requisitos: - 80 % de asistencia a la cursada. - Aprobación del examen parcial teórico con una
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > PROMOCIONADO REGULAR LIBRE El alumno accederá a la condición de **PROMOCIÓN** si cumple con las siguientes condiciones de cátedra: **1 -** Obtener en los 3 parciales, una calificación promedio sup
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > Deberá presentar el trabajo práctico integrador con una antelación mínima de veinte (20) días hábiles respecto de la fecha de la mesa de examen. En caso contrario, su evaluación se trasladará al tur
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 9]
   > **Programa de trabajos prácticos:** Tp 1: Escritura académica. Se solicita a los estudiantes seleccionar un artículo de investigación sobre un tema de interés específico relacionado al campo profesi
6. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **RÉGIMEN DE CURSADA** | Pagina: 2]
   > **Regularidad:** Asistencia: Según norma vigente Todos los trabajos prácticos aprobados 6/7 parciales aprobados con más del 50% **Promoción:** Régimen regular Obtener más del 70% en todos los parci
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > **Evaluación Final:** El alumno con condición de REGULAR, deberá rendir un examen de los temas teóricos y prácticos desarrollados en la materia (prueba escrita). El alumno LIBRE rendirá un examen fina
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > asistencia anteriormente detallados. **Instancias de Recuperación:** La cátedra dispone de **dos oportunidades de** **recuperatorio** totales. Estas pueden utilizarse para cualquiera de los dos parc

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1656 | salida: 14 | total: 1670

---

### Pregunta 17

> - ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > de la Investigación Operativa. Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - **PHP Simplex:** Herramienta online accesib
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad III: -Método SIMPLEX-** Algoritmo del método Simplex: forma estándar, variables de holgura y variables artificiales. Construcción de la tabla inicial, criterios de entrada y salida de varia
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > Naturaleza recursiva de los cálculos: etapas, estados, decisiones y principio de optimalidad de Bellman. Resolución de problemas de diligencia, asignación de recursos y reemplazo de equipos. Diferen
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > _remitirá un informe con las observaciones correspondientes y se establecerá un encuentro sincrónico_ _para su devolución y orientación. Cumplida esta instancia de revisión, el/la estudiante quedará_
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: pesos. Regiones de Decisión. Problema de separación lineal. Aplicaciones. Limitaciones | Pagina: 2]
   > Problema XOR.
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 14]
   > ; director Fernando Sato ; codirector<br>Carlos Fernando<br>Sosa.|2020| |Big Data como modelo de solución para la Administración Tributaria de Entre Ríos<br>/ Agustín Alorda, César Aníbal Sarchioni ;
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > preguntas le hago al problema? ¿Cómo construir el marco teórico? ¿Con qué categorías? Definición temporal y de contexto. Relación con los antecedentes relevados. Formulación de las preguntas que se
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > : - **Capa de enlace de dato** - **sub capa** **LLC (control de enlace lógico)** Cuestiones en el diseño de la capa de enlace de dato, servicios proporcionados por la capa de red, entramado, control d

**Respuesta:**

Lo siento, pero no dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1524 | salida: 19 | total: 1543

---

### Pregunta 18

> - ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > **Protocolos de Evaluación:** Los resultados se publicarán en un plazo de siete días corridos tras la evaluación. Los exámenes se desarrollarán estrictamente en los bloques horarios asignados a la m
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > asistencia anteriormente detallados. **Instancias de Recuperación:** La cátedra dispone de **dos oportunidades de** **recuperatorio** totales. Estas pueden utilizarse para cualquiera de los dos parc
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > |16|06 de agosto|Virtual|Teoría|Repaso del proceso de| |||||investigación| |17|13 de agosto|Virtual|Tutorías|Tutorías| |18|20 de agosto|**_Presencial (cambio_**<br>**_encuentro)_**|**Teoría**|Parcial
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > **-** Presentación y defensa oral del trabajo práctico integrador en la mesa de examen final, previa instancia de revisión y devolución con el equipo docente. El trabajo deberá entregarse con una an
6. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **HORARIOS DE CLASE** | Pagina: 1]
   > Lunes: 13:30 a 15:30 (Teoría) Viernes: 17:00 a 19:00 (Práctica) Nota: Los horarios están en proceso de evaluación y pueden sufrir cambios
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > de la Investigación Operativa. Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - **PHP Simplex:** Herramienta online accesib
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > anteproyecto, mientras que el resto de las clases se desarrollarán de manera presencial mediadas por tecnología a través de Google Meet. En estos encuentros virtuales, se trabajarán tanto los fundam

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1682 | salida: 14 | total: 1696

---

## Conversacion 5

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

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas por el área IA. Descripción de los temas específicos a desarrollarse en la asignatura. Intro
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos **Capítulo I** **Agentes Inteligentes**
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > **Sistemas Basados en Conocimientos**. Conceptos básicos. Representación de Conocimientos. Estructuras basadas en Lógica. Lógica de Primer Orden. Reglas de Inferencia. Representación basada en objetos
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > **Capítulo VIII** **Redes Neuronales Artificiales (RNA).** Generalidades, conceptos básicos Reseña Histórica. Clasificación de las RNA. Agentes basados en Proceso de Aprendizaje
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > . Clases e instancias. Concepto de herencia. Métodos y mensajes.

**Respuesta:**

El programa de contenidos de la materia Inteligencia Artificial se estructura a través de diferentes capítulos, destacando el contenido de los capítulos "Agentes Inteligentes" y "Redes Neuronales Artificiales (RNA)", así como la introducción a conceptos básicos como la representación de conocimientos, la lógica de primer orden y la inferencia, la representación basada en objetos, la herencia y la definición de objetos y atributos.

**Tokens:** entrada: 872 | salida: 104 | total: 976

---

### Pregunta 2

> - ¿En qué materia se enseña el concepto de Lógica Difusa?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > **Capítulo VI** **Lógica Difusa (Fuzzy).** Consideraciones generales, Conjuntos Difusos, definición. Operaciones simples entre conjuntos Difusos: Inclusión, Igualdad, Complementación, Intersección, U
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > **Capítulo VII** **Sistemas** **Difusos.** Consideraciones generales. Representación de conocimiento estructurado mediante reglas lingüísticas. Proceso de Fuzzificación. Influencia de la forma y dis
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación de los distintos métodos sobre el funcionamiento del sistema. Agentes Basados en Lógica Dif
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > **Sistemas Basados en Conocimientos**. Conceptos básicos. Representación de Conocimientos. Estructuras basadas en Lógica. Lógica de Primer Orden. Reglas de Inferencia. Representación basada en objetos
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Proceso de Inferencia. Tratamiento paralelo de las reglas. Determinación del aporte parcial de cada regla. Integración de la solución difusa final.

**Respuesta:**

La materia en la que se enseña el concepto de Lógica Difusa es la Inteligencia Artificial.

**Tokens:** entrada: 955 | salida: 26 | total: 981

---

### Pregunta 3

> - ¿Cuál es el plan de estudios de Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > **Plan de estudios resumido** - Unidad 1: Introducción a la ciencia y conocimiento científico - Unidad 2: La dimensión epistemológica - Unidad 3: La dimensión de la estrategia general de investi
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > |METODOLOGÍA DE LA INVESTIGACIÓN- 2026|Col2|Col3|Col4|Col5| |---|---|---|---|---| |**Clase **|**FECHA**|**Tipo de encuentro**|**Tipo encuentro**|**Tema**| |1|12 de marzo|**Presencial**|**Teórico/práct
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: dentro de la plataforma Moodle. La organización será la siguiente | Pagina: 5]
   > - Introducción - Dimensión epistemológica - Dimensión estratégica - Dimensión técnica - Cada semana se habilitarán los contenidos planificados, proporcionando a los
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: **Equipo docente:** PROFESORA RESPONSABLE ADJUNTO: ALEJANDRA MARǪUESIN; JEFE DE | Pagina: 1]
   > TRABAJOS PRÁCTICOS: TAMARA SUIVA. JEFE DE TRABAJOS PRÁCTICOS: JIMENA SANTA CRUZ; **Año de la carrera a la que pertenece la cátedra:** 4 **Régimen de la materia:** Anual **Carga horaria semanal:** 3
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > |2|19 de marzo|Virtual|Teoría|Conceptos generales para<br>introducción| |3|26 de marzo|Virtual|Práctica|Normas APA/ escritura académica| |4|2 de abril|(sin clase)|(sin clase)|(sin clase)| |5|09 de abr

**Respuesta:**

El plan de estudios resumido de Metodología de la Investigación se encuentra en la sección "Plan de estudios resumido" y está dividido en tres unidades:

1. Introducción a la ciencia y conocimiento científico
2. La dimensión epistemológica
3. La dimensión de la estrategia general de investigación

**Tokens:** entrada: 1076 | salida: 81 | total: 1157

---

### Pregunta 4

> - ¿Qué herramientas de software se recomiendan en la carrera para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > problemas de programación lineal mediante el Método Simplex y el Método Gráfico. Es ideal para validaciones rápidas y visualización de regiones factibles. - **LINGO (64 bits):** Una versión avanzad
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > manera directa. - **WinQSB 2.0:** Una suite clásica (dividida en 3 partes) que abarca múltiples módulos de Investigación Operativa. Permite resolver problemas de programación lineal (LP), modelos
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadísticos mediante una interfaz basada en menús para la carga
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > Lineal: proporcionalidad, aditividad, divisibilidad y certidumbre. Formulación de problemas de optimización. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en l

**Respuesta:**

Entre las herramientas mencionadas se incluyen:

- LINDO: especializado en la resolución de problemas de programación lineal, entera y no lineal, reconocido por su sintaxis sencilla para ingresar ecuaciones y restricciones.
- LINGO: una versión avanzada y más potente del motor LINDO, ideal para validaciones rápidas y visualización de regiones factibles.
- WinQSB 2.0: una suite clásica que abarca múltiples módulos de Investigación Operativa y permite resolver problemas de programación lineal (LP) y modelos de transporte.

Sin embargo, no tengo suficiente información para relacionar las herramientas con unidades teóricas específicas de la carrera.

**Tokens:** entrada: 1026 | salida: 164 | total: 1190

---

### Pregunta 5

> - ¿Qué instancias de recuperación nos provee Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > asistencia anteriormente detallados. **Instancias de Recuperación:** La cátedra dispone de **dos oportunidades de** **recuperatorio** totales. Estas pueden utilizarse para cualquiera de los dos parc
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > parcial. La calificación obtenida en la instancia de recuperación sustituirá automáticamente a la nota del examen original. **Protocolos de Evaluación:** Los resultados se publicarán en un plazo de
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > manera directa. - **WinQSB 2.0:** Una suite clásica (dividida en 3 partes) que abarca múltiples módulos de Investigación Operativa. Permite resolver problemas de programación lineal (LP), modelos
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > Está diseñado para modelar y resolver problemas de optimización de gran escala, permitiendo una integración más fluida con bases de datos y
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadísticos mediante una interfaz basada en menús para la carga

**Respuesta:**

Investigación Operativa proporciona **dos oportunidades de recuperatorio** totales. Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mismo examen.

**Tokens:** entrada: 968 | salida: 56 | total: 1024

---

### Pregunta 6

> - ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadísticos mediante una interfaz basada en menús para la carga
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos vertidos en la teoría
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > |19|27 de agosto|Virtual|Tutorías|Tutorías| |20|03<br>de<br>septiembr<br>e|**Presencial**|Tutorías|Sugerecia entrevista a expertos<br>en el tema/ recuperatorio parcial<br>teoría| |21|10<br>de<br>septi

**Respuesta:**

TORA es una herramienta educativa diseñada para el aprendizaje, pero no se proporciona información sobre qué módulos incluye. No dispongo de información en mis documentos para describir con precisión qué funcionalidades o módulos incluye el software TORA.

**Tokens:** entrada: 952 | salida: 60 | total: 1012

---

### Pregunta 7

> - ¿Qué profesor forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes?

**Chunks de contexto:**

1. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **EQUIPO DOCENTE** | Pagina: 1]
   > Teoría: Trossero, Sebastián (Trossero.sebastian@uader.edu.ar) Práctica: Schmuckler, Jorge (Schmukler.jorge@uader.edu.ar)
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > **Facultad de Ciencia y Tecnología de la UADER** SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler.
3. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **MODALIDAD DE CLASES** | Pagina: 1]
   > A partir de este año la materia será dictada de manera bimodal. El cronograma será definido en su mayoría por la Facultad. Aún no confirmado. Los links de clases se encuentran en el aula virtual. Las
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos vertidos en la teoría
5. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **PRESENTACIÓN DE LA MATERIA** | Pagina: 1]
   > Facultad de Ciencia y Tecnología Universidad Autónoma de Entre Ríos (UADER)

**Respuesta:**

El profesor que forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes es Jorge L. Schmukler.

**Tokens:** entrada: 881 | salida: 42 | total: 923

---

### Pregunta 8

> - ¿Qué otra asignatura, además de la propia materia de Inteligencia Artificial, incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas por el área IA. Descripción de los temas específicos a desarrollarse en la asignatura. Intro
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 4. El impacto de la inteligencia artificial en la gestión del talento. | Pagina: 2]
   > _**Bibliografía Nacional:**_ Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales. **Uni
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > Introducción a los sistemas multiagente, modelos formales. Metodologías de diseño basadas en agentes. Metodología Gaia: Modelo de Actividades. Modelo de Roles. Modelo Interacción. Modelo de Agentes. O
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Estructura de Control: Procedimientos de Inferencia; Interfase con el usuario. Memoria de Trabajo, Módulo generador de explicaciones al usuario. **Capítulo V**
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > . Clases e instancias. Concepto de herencia. Métodos y mensajes.

**Respuesta:**

La asignatura de Informática y Recursos Humanos incluye explícitamente el impacto de la inteligencia artificial (IA) en la gestión del talento en la Unidad 3: Gestión del Talento en la Era Digital.

**Tokens:** entrada: 948 | salida: 53 | total: 1001

---

### Pregunta 9

> - Los requisitos para regularizar en Bases de Datos Avanzadas y en Redes y Comunicaciones, ¿son iguales? ¿Qué diferencias tienen?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > **Evaluación Final:** El alumno con condición de REGULAR, deberá rendir un examen de los temas teóricos y prácticos desarrollados en la materia (prueba escrita)
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > . Señalización y Codificación (señalización de bits, codificación agrupación de bits, capacidad para transportar datos (ancho de banda, rendimiento, capacidad de transferencia útil))
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > El alumno accederá a la condición de **REGULAR**, si cumple con las siguientes condiciones de cátedra: **1 -** Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos.
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > difusión, Enrutamiento por multidifusión, Enrutamiento para hosts móviles, Enrutamiento en redes ad hoc, Búsqueda de nodos en redes de igual a igual), RIP protocolo de enrutamiento por clase vector de
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > **1 -** Obtener en los 3 parciales, una calificación promedio superior o igual a los 80 puntos. Con ninguna nota inferior a 60 puntos en cada parcial. **2-** Haber realizado y aprobado los dos trabajo

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 996 | salida: 14 | total: 1010

---

### Pregunta 10

> - ¿Cuál es el porcentaje de asistencia a clases que exigen en común las materias de Investigación Operativa, Comunicaciones y Redes, y Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > y el cumplimiento del 80% de asistencia a las clases teóricas y prácticas. - **ALUMNO LIBRE:** Revestirá esta condición todo estudiante que no logre cumplimentar alguno de los requisitos de puntaje
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > pueden asistir a todas las clases y, al mismo tiempo, reducir la tasa de abandono. Por ello, los materiales teóricos y las lecturas obligatorias se compartirán con una semana de antelación al encuen
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > **b.** **Alumno Regular** - 60 % de asistencia. - Aprobación del examen parcial teórico con una calificación igual o superior a 60 (sesenta) puntos. - Entrega de todos los trabajos en tiempo y
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: **Equipo docente:** PROFESORA RESPONSABLE ADJUNTO: ALEJANDRA MARǪUESIN; JEFE DE | Pagina: 1]
   > TRABAJOS PRÁCTICOS: TAMARA SUIVA. JEFE DE TRABAJOS PRÁCTICOS: JIMENA SANTA CRUZ; **Año de la carrera a la que pertenece la cátedra:** 4 **Régimen de la materia:** Anual **Carga horaria semanal:** 3
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1064 | salida: 14 | total: 1078

---

### Pregunta 11

> - Un proyecto integrador requiere utilizar un software para resolver problemas de optimización a gran escala que pueda conectarse de forma fluida con bases de datos espaciales. Según las herramientas enseñadas en las materias, ¿qué combinación de software visto en Bases de Datos Avanzadas e Investigación Operativa sería la más adecuada para este objetivo?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > Está diseñado para modelar y resolver problemas de optimización de gran escala, permitiendo una integración más fluida con bases de datos y
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadísticos mediante una interfaz basada en menús para la carga
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > manera directa. - **WinQSB 2.0:** Una suite clásica (dividida en 3 partes) que abarca múltiples módulos de Investigación Operativa. Permite resolver problemas de programación lineal (LP), modelos
5. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **SOFTWARE REQUERIDO** | Pagina: 2]
   > PostgreSQL: versión 9.6 o superior SQL Server: versión 2016 o superior QGIS: versión compatible con PostgreSQL Anaconda (Python): últimas versiones

**Respuesta:**

La combinación de software más adecuada para resolver problemas de optimización a gran escala que pueda conectarse de forma fluida con bases de datos espaciales es utilizando **PostgreSQL** (versión 9.6 o superior) como base de datos y **LINDO (Linear, Interactive, and Discrete Optimizer)** como software de resolución de problemas de optimización. LINDO se destaca por su capacidad para resolver problemas de programación lineal, entera y no lineal, y su sintaxis sencilla para ingresar ecuaciones y restricciones. Además, PostgreSQL es compatible con bases de datos espaciales, lo que permite la integración con QGIS.

**Tokens:** entrada: 1008 | salida: 146 | total: 1154

---

### Pregunta 12

> - Si un estudiante desea investigar sobre el impacto de los "Agentes que aprenden" y las "Redes Neuronales" en la selección de personal y el teletrabajo en Argentina, ¿qué normativas legales y temas específicos de los programas de Inteligencia Artificial y RRHH debería cruzar en su marco teórico?

**Chunks de contexto:**

1. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: IV. BIBLIOGRAFÍA GENERAL | Pagina: 3]
   > Reglamento de Teletrabajo en Argentina. Legislación sobre delitos informáticos en Argentina. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laboral
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: **I. FUNDAMENTACIÓN** | Pagina: 1]
   > . Además, se abordarán aspectos legales fundamentales para comprender el impacto normativo de las TIC en el ámbito laboral, tomando como base la legislación argentina y los aportes de autores nacional
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: IV. BIBLIOGRAFÍA GENERAL | Pagina: 3]
   > Ley de Teletrabajo (Ley 27.555). Ley Propiedad intelectual (Ley 11.723) - (modificatoria Ley 25.036) Código Civil y Comercial de la Nación (aspectos relacionados con contratos digitales y firma elec
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 3]
   > Legislación sobre delitos informáticos en Argentina. Ley Nacional de Protección de Datos Personales (Ley 25.326). Ley Propiedad Intelectual (Ley 11.723) y su modificatoria. **Unidad 5: Trabajo Autó
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 2]
   > Reglamento de Teletrabajo en Argentina. Nicolás S. Tato, El Derecho Informático - Aspectos Fundamentales. Mariana Nazar, Tecnologías, información y derechos. **Unidad 2:** **Relaciones Humanas en e

**Respuesta:**

Para investigar sobre el impacto de los "Agentes que aprenden" y las "Redes Neuronales" en la selección de personal y el teletrabajo en Argentina, te recomendaría incluir las siguientes normativas legales y temas específicos en tu marco teórico:

1.  **Ley 27.555 de Teletrabajo**: Al considerar el contexto de trabajo remoto en Argentina, es importante abordar la regulación legal que rige este tipo de trabajo. La Ley 27.555 ofrece información sobre los derechos y obligaciones tanto del empleador como del trabajador en el ámbito del teletrabajo.

2.  **Ley de Protección de Datos Personales (Ley 25.326)**: Al investigar sobre la selección de personal y el teletrabajo en el contexto de la Inteligencia Artificial, es crucial considerar las implicaciones de la privacidad y la protección de datos personales. La Ley de Protección de Datos Personales es fundamental en este sentido, ya que regula cómo se pueden recopilar, utilizar y proteger los datos personales, especialmente en entornos de selección de personal y teletrabajo.

3.  **Código Civil y Comercial de la Nación (aspectos relacionados con contratos digitales y firma electrónica)**: La adopción de "Agentes que aprenden" y "Redes Neuronales" en procesos de selección y teletrabajo podría estar sujeta a las normas sobre contratos digitales y firma electrónica. El Código Civil y Comercial proporciona la base legal para entender cómo se aplican estas tecnologías en el ámbito contractual.

4.  **Aspectos relacionados con la privacidad y la seguridad de la información**: El uso de la Inteligencia Artificial en selección y teletrabajo plantea preocupaciones sobre la privacidad y la seguridad de la información. Te recomendaría incluir recursos que aborden estas cuestiones, particularmente en relación con la Ley de Protección de Datos Personales.

5.  **Bibliografía Complementaria**: Para una exploración más profunda, la **Bibliografía Complementaria** incluye el Reglamento de Teletrabajo en Argentina, lo que podría ofrecer detalles prácticos y específicos sobre cómo se aplica la ley en el contexto del teletrabajo.

6.  **Nicolás S. Tato, El Derecho Informático - Aspectos Fundamentales**: Como parte de tu marco teórico, considera incluir obras como la de Nicolás S. Tato, que abordan aspectos fundamentales del derecho informático. Esta obra podría proporcionar contexto sobre cómo las tecnologías de la información y la comunicación influyen en el derecho y la sociedad.

7.  **Mariana Nazar, Tecnologías, información y derechos**: La obra de Mariana Nazar también es relevante para comprender cómo las tecnologías influyen en los derechos y las relaciones sociales. Te recomendaría incluir esta obra para una comprensión más completa de los impactos de la Inteligencia Artificial en la sociedad.

Recuerda que la inclusión de estas normativas legales y recursos bibliográficos te permitirá crear un marco teórico robusto y bien fundamentado para tu investigación sobre el impacto de los "Agentes que aprenden" y las "Redes Neuronales" en la selección de personal y el teletrabajo en Argentina.

**Tokens:** entrada: 1019 | salida: 749 | total: 1768

---

### Pregunta 13

> - ¿Dónde puedo descargar la materia de Cálculo de 1er año?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: UNDERWRITERS LABORATORIES (UL) -> www.ul.com | Pagina: 5]
   > PANDUIT -> www.panduit.com AMP -> www.tycoelectronics.com/components/ ETHEREAL -> www.ethereal.com SIEMENS -> www.sea.siemens.com/step/templates/lesson.mason?electricity:2:3:3
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: PROGRAMA DE CÁTEDRA: INFORMÁTICA Y RELACIONES HUMANAS | Pagina: 1]
   > Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas semanales
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > - Cisco Systems: Academia de Networking de Cisco Systems: Guía del primer año. -2a ed. - Madrid: Pearson Educación, 2002. ISBN 8420532967 [ Copia disponible en Biblioteca FCyT- Oro Verde] - Técnico
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > : - **Capa de enlace de dato** - **sub capa** **MAC (control de acceso al medio)** Problema de asignación del canal, Asignación estática de canal, Asignación dinámica de canal
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > : - **Capa de enlace de dato** - **sub capa** **LLC (control de enlace lógico)** Cuestiones en el diseño de la capa de enlace de dato, servicios proporcionados por la capa de red, entramado, control d

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1055 | salida: 14 | total: 1069

---

### Pregunta 14

> - El profesor Ing. Jorge L. Schmukler da clases en Bases de Datos Avanzadas, en Inteligencia Artificial y en Redes y Comunicaciones.

**Chunks de contexto:**

1. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **EQUIPO DOCENTE** | Pagina: 1]
   > Teoría: Trossero, Sebastián (Trossero.sebastian@uader.edu.ar) Práctica: Schmuckler, Jorge (Schmukler.jorge@uader.edu.ar)
2. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **MODALIDAD DE CLASES** | Pagina: 1]
   > A partir de este año la materia será dictada de manera bimodal. El cronograma será definido en su mayoría por la Facultad. Aún no confirmado. Los links de clases se encuentran en el aula virtual. Las
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > **Capítulo V** **Funcionalidad de los Sistemas Expertos** Procesos de inferencia: Encadenamiento hacia adelante (Fordward Chaining) y Encadenamiento hacia atrás (Backward Chaining). Herramientas par
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > **Facultad de Ciencia y Tecnología de la UADER** SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler.
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > **Sistemas Basados en Conocimientos**. Conceptos básicos. Representación de Conocimientos. Estructuras basadas en Lógica. Lógica de Primer Orden. Reglas de Inferencia. Representación basada en objetos

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 965 | salida: 14 | total: 979

---

### Pregunta 15

> - ¿Cuál es el costo de la certificación oficial de Cisco que se menciona como opcional en la planificación?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Sitios web sobre normativas, tecnologías y soluciones, opcional** | Pagina: 5]
   > IETF -> www.ietf.org IEEE -> www.ieee.org ISO -> www.iso.org CISCO -> www.cisco.com IANA -> www.iana.org ISOC -> www.isoc.org ARIN -> www.arin.net LACNIC -> http://lacnic.net/sp/ LAC IPV6 TF -> www.la
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > - Cisco Systems: Academia de Networking de Cisco Systems: Guía del primer año. -2a ed. - Madrid: Pearson Educación, 2002. ISBN 8420532967 [ Copia disponible en Biblioteca FCyT- Oro Verde] - Técnico
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: UNDERWRITERS LABORATORIES (UL) -> www.ul.com | Pagina: 5]
   > PANDUIT -> www.panduit.com AMP -> www.tycoelectronics.com/components/ ETHEREAL -> www.ethereal.com SIEMENS -> www.sea.siemens.com/step/templates/lesson.mason?electricity:2:3:3
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > [Disponible en Biblioteca FCyT- Oro Verde] - Curso visual y práctico: Administrador de Redes Instalación y configuración de hardware y software. - USERS-CISCO. [Disponible en Biblioteca FCyT- Oro
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > : - **Capa de enlace de dato** - **sub capa** **LLC (control de enlace lógico)** Cuestiones en el diseño de la capa de enlace de dato, servicios proporcionados por la capa de red, entramado, control d

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1098 | salida: 14 | total: 1112

---

### Pregunta 16

> - Para la Promoción Directa, se exige la aprobación de la totalidad de los trabajos prácticos (TP 1 al TP 5). ¿Cuál es la calificación numérica mínima que debe obtenerse en cada TP individual para que se considere aprobado?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 16]
   > Para acceder a la condición de Promoción Directa, el/la estudiante deberá cumplir con los siguientes requisitos: - 80 % de asistencia a la cursada. - Aprobación del examen parcial teórico con una
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > **Condición del Alumno:** - **ALUMNO PROMOCIONADO:** El estudiante logrará la promoción directa si alcanza un promedio general de **80 puntos** - más entre los **1 parcial** previstos, no pudiendo
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 15]
   > **Requisitos para rendir como estudiantes regulares, promocionales y libres:** **a.** **Promoción Directa**
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 9]
   > **Programa de trabajos prácticos:** Tp 1: Escritura académica. Se solicita a los estudiantes seleccionar un artículo de investigación sobre un tema de interés específico relacionado al campo profesi
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 970 | salida: 14 | total: 984

---

### Pregunta 17

> - ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > problemas de programación lineal mediante el Método Simplex y el Método Gráfico. Es ideal para validaciones rápidas y visualización de regiones factibles. - **LINGO (64 bits):** Una versión avanzad
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > de la Investigación Operativa. Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - **PHP Simplex:** Herramienta online accesib
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > (soluciones múltiples, soluciones no acotadas y problemas infactibles). **Unidad III: -Método SIMPLEX-** Algoritmo del método Simplex: forma estándar, variables de holgura y variables artificiales.
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > elementales de enlace de datos (Protocolo simplex sin restricciones, Protocolo símplex de parada y espera, Protocolo símplex para un canal con ruido, Protocolo de ventana corrediza)

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 974 | salida: 14 | total: 988

---

### Pregunta 18

> - ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > parcial. La calificación obtenida en la instancia de recuperación sustituirá automáticamente a la nota del examen original. **Protocolos de Evaluación:** Los resultados se publicarán en un plazo de
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > instancias individuales. Asimismo, deberá acreditar la aprobación de los dos trabajos prácticos de la cátedra y mantener una asistencia mínima del 80% a los encuentros presenciales.
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > y el cumplimiento del 80% de asistencia a las clases teóricas y prácticas. - **ALUMNO LIBRE:** Revestirá esta condición todo estudiante que no logre cumplimentar alguno de los requisitos de puntaje
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > |6|16 de abril|Virtual|Práctica|| |7|23 de abril|Virtual|Teoría|Pregunta de investigación<br>(variables, unidad de análisis,<br>contexto)/ Antecedentes| |8|30 de abril|**_Presencial (pedir cambio_**<b

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 967 | salida: 14 | total: 981

---

## Resumen de tokens

| Conversacion | Entrada | Salida | Total |
|---|---|---|---|
| 1 | 21053 | 1415 | 22468 |
| 2 | 25193 | 1841 | 27034 |
| 3 | 21639 | 1478 | 23117 |
| 4 | 28859 | 1877 | 30736 |
| 5 | 17794 | 1593 | 19387 |
| **Total** | **114538** | **8204** | **122742** |
