# Evaluacion — testOllamaPostMejoras2-2

_Iniciada: 2026-04-12 18:45:36_
_Ultima actualizacion: 2026-04-12 18:54:46_

**Estado:** completado
**Archivo de evaluacion:** `tests/evaluaciones/testOllamaPostMejoras.md`
**Preguntas:** 18 | **Conversaciones planificadas:** 4 | **Conversaciones iniciadas:** 4 | **Preguntas procesadas:** 72

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

Los contenidos de la materia Inteligencia Artificial incluyen Agentes Inteligentes, Procesos de B, Representación de Conocimientos mediante reglas, Estructura básica, Comportamiento de Agentes Basados en Conocimientos, Diseño de los Sistemas Expertos y Redes Neuronales Artificiales (RNA).

**Tokens:** entrada: 1143 | salida: 74 | total: 1217

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

La materia en la que se enseña el concepto de Lógica Difusa es Inteligencia Artificial.

**Tokens:** entrada: 1156 | salida: 25 | total: 1181

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

El plan de estudios de Metodología de la Investigación incluye 15 clases repartidas en el período académico, con temas como presentación de la asignatura, concepción de los conceptos generales para introducción, normas APA y escritura académica, tema/problema y más, se divide en presenciales y virtuales.

**Tokens:** entrada: 1315 | salida: 78 | total: 1393

---

### Pregunta 4

> - En Comunicaciones y Redes, ¿cómo hago para quedar como alumno regular?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > n cada parcial. **2-** Haber realizado y aprobado los dos trabajos práctico impartido por la cátedra. **3-** Asistir al 80% de las clases teóricas y prácticas. El alumno accederá a la condición de **
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > PROMOCIONADO REGULAR LIBRE El alumno accederá a la condición de **PROMOCIÓN** si cumple con las siguientes condiciones de cátedra: **1 -** Obtener en los 3 parciales, una calificación promedio sup
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > mno con condición de REGULAR, deberá rendir un examen de los temas teóricos y prácticos desarrollados en la materia (prueba escrita). El alumno LIBRE rendirá un examen final sobre el programa vigente
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > ** Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos. Tener aprobado con 60 puntos los tres parciales. **2-** Haber realizado y aprobado los dos trabajos Práctico
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > peratorios se realizaran en los horarios asignados a la cátedra, y la inasistencia a una de estas evaluaciones se tomará como la reprobación de la misma salvo que se presente justificativo medico o qu
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > s y prácticas. El alumno tendrá condición de **LIBRE** si no cumple con alguna de las condiciones antes nombradas. **Recuperatorio**: El alumno cuenta con dos recuperatorios para cualquiera de los par

**Respuesta:**

Para quedar como alumno regular, debes cumplir con las siguientes condiciones de cátedra: Obtener en los 3 parciales una calificación promedio superior o igual a los 60 puntos. Tener aprobado con 60 puntos los tres parciales. Haber realizado y aprobado los dos trabajos prácticos impartidos por la cátedra. Asistir al 80% de las clases teóricas y prácticas.

**Tokens:** entrada: 1218 | salida: 100 | total: 1318

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

La cátedra dispone de dos oportunidades de recuperación para los estudiantes.

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

El software TORA es una herramienta educativa diseñada para el aprendizaje de la Investigación Operativa. Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos.

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

Schmuckler, Jorge es el profesor que forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes, ya que aparece en ambos documentos.

**Tokens:** entrada: 1100 | salida: 49 | total: 1149

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

La asignatura que incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas es "Informática y Recursos Humanos", específicamente en la sección 4 del documento "PROGRAMA INFORMATICA Y RRHH.pdf", que se refiere al "El impacto de la inteligencia artificial en la gestión del talento".

**Tokens:** entrada: 1184 | salida: 86 | total: 1270

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

Según el contexto, las materias de Investigación Operativa, Comunicaciones y Redes, y Metodología de la Investigación exigen una asistencia mínima del **80%** a las clases teóricas y prácticas.

**Tokens:** entrada: 1222 | salida: 54 | total: 1276

---

### Pregunta 11

> - Si quiero promocionar todas las materias de 4to año, ¿cuál es la diferencia de promedio exigido entre Investigación Operativa e Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > **Condición del Alumno:** - **ALUMNO PROMOCIONADO:** El estudiante logrará la promoción directa si alcanza un promedio general de **80 puntos** - más entre los **1 parcial** previstos, no pudiendo
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > l. Algoritmo SOFM ó SOM (Self-Organizing -Feature-Mapping). Determinación del proceso de adaptación de los pesos. Función de vecindad. Modificación del algoritmo SOM para evitar una excesiva acumulac
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > os mediante reglas. Estructura básica. Representación de reglas mediante objetos. Ventajas comparativas entre las distintas representaciones. Comportamiento de Agentes Basados en Conocimientos. **Ca
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > unto de patrones para el entrenamiento. Algoritmos de reducción (Pruning Algorithms). Deep Learning. Modelos Generativos **Capítulo XI** Redes Autoorganizadas. Características generales. **Red SOM
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Capítulo II** **Procesos de Búsqueda.** Representación en un espacio de estados. Búsqueda Ciega, definición; búsqueda primero en amplitud, búsqueda de costo uniforme; búsqueda primero en profundidad

**Respuesta:**

No dispongo de información en mis documentos para comparar las calificaciones promedio requeridas para promocionar en las materias de Investigación Operativa e Inteligencia Artificial.

**Tokens:** entrada: 1168 | salida: 39 | total: 1207

---

### Pregunta 12

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

Las herramientas de software recomendadas para resolver problemas de optimización lineal se relacionan con las unidades teóricas de la siguiente manera:

- **LINDO (Linear, Interactive, and Discrete Optimizer)**: Utilizado para la resolución de problemas de programación lineal, entera y no lineal. Es compatible con las unidades teóricas de Programación Lineal (PL) como la resolución de problemas de optimización lineal.
- **WinQSB 2.0**: Permite la validación rápida y visualización de regiones factibles mediante el Método Simplex, que es parte de la Unidad II: Programación Lineal (PL).
- **LINGO (64 bits)**: Es una versión avanzada y más potente del motor LINDO, diseñado para modelar y resolver problemas de optimización de gran escala. Está relacionado con la Unidad II: Programación Lineal (PL) en el tratamiento de problemas de optimización lineal.
- **PHP Simplex**: Es una herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el Método Simplex. Está relacionado con la Unidad II: Programación Lineal (PL) en el tratamiento de problemas de optimización lineal.

Estas herramientas están relacionadas con la Unidad II: Programación Lineal (PL) en la resolución de problemas de optimización lineal.

**Tokens:** entrada: 1197 | salida: 304 | total: 1501

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

Lo siento, pero no tengo esa información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1072 | salida: 18 | total: 1090

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

Lo siento, pero no dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1193 | salida: 19 | total: 1212

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

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1199 | salida: 14 | total: 1213

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
| top_k | 5 |
| max_context_chunks | 5 |
| chunk_size | 512 |
| chunk_overlap | 100 |
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

Los contenidos de la materia Inteligencia Artificial incluyen los siguientes capítulos y temas:

Agentes Inteligentes (Capítulo I):
  - Introducción a la Inteligencia Artificial (IA) con definiciones y objetivos.
  - Herramientas y técnicas de IA.
  - Descripción de los temas específicos a desarrollarse en la asignatura.
  - Introducción a los agentes inteligentes.
  - Entorno de Trabajo.
  - Propiedades de los entornos.
  - Estructura de los Agentes.
  - Programas de Agentes.
  - Agente Reactivo Simple.
  - Agentes Reactivos basados en Modelos.
  - Agente basado en objetivos.
  - Agentes que aprenden.

Sistemas Basados en Conocimientos (Capítulo III):
  - Conceptos básicos.
  - Representación de Conocimientos.
  - Estructuras basadas en Lógica.
  - Lógica de Primer Orden.
  - Reglas de Inferencia.
  - Representación basada en objetos.
  - Definición de objetos y de atributos.
  - Clases e instancias.
  - Concepto de herencia.
  - Métodos y mensajes.
  - Representación de Conocimientos mediante reglas.
  - Ventajas comparativas entre las distintas representaciones.

Agentes Basados en Lógica Difusa (Sin específicar en qué página se encuentra).

Redes Neuronales Artificiales (RNA) (Capítulo VIII):
  - Generalidades y conceptos básicos.
  - Reseña Histórica.
  - Clasificación de las RNA.
  - Agentes basados en Proceso de Aprendizaje.

Bibliografía (Página 4):
  - Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition.
  - Autores: Stuart J. Rusell, Peter Norvig.
  - Editorial: Pearson Educación (2004 o versiones posteriores).
  - Título: Aprendizaje automático y aprendizaje profundo con Python, scikit-learn y Tensor Flow- Segunda Edition.
  - Autores: S. Raschka, V. Mirjalili.
  - Editorial: Marcombo (2019).

**Tokens:** entrada: 1137 | salida: 498 | total: 1635

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

La materia en la que se enseña el concepto de Lógica Difusa es la Inteligencia Artificial.

**Tokens:** entrada: 1233 | salida: 26 | total: 1259

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

El plan de estudios de Metodología de la Investigación se divide en cuatro unidades, que son:

1. Introducción a la ciencia y conocimiento científico
2. La dimensión epistemológica
3. La dimensión de la estrategia general de investigación
4. La Dimensión de las técnicas de obtención y análisis de información empírica. La comunicación de los resultados.

Además, se menciona un cronograma de trabajo con fechas y temas para cada clase, pero no se proporciona una descripción completa de cada unidad.

**Tokens:** entrada: 1316 | salida: 128 | total: 1444

---

### Pregunta 4

> - En Comunicaciones y Redes, ¿cómo hago para quedar como alumno regular?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > El alumno accederá a la condición de **REGULAR**, si cumple con las siguientes condiciones de cátedra: **1 -** Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos.
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > PROMOCIONADO REGULAR LIBRE El alumno accederá a la condición de **PROMOCIÓN** si cumple con las siguientes condiciones de cátedra: **1 -** Obtener en los 3 parciales, una calificación promedio sup
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > **Evaluación Final:** El alumno con condición de REGULAR, deberá rendir un examen de los temas teóricos y prácticos desarrollados en la materia (prueba escrita). El alumno LIBRE rendirá un examen fina
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > **2-** Haber realizado y aprobado los dos trabajos Práctico impartido por la cátedra. **3-** Asistir al 80% de las clases teóricas y prácticas. El alumno tendrá condición de **LIBRE** si no cumple con
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr

**Respuesta:**

Para quedar como alumno regular en Comunicaciones y Redes, debes cumplir con las condiciones de cátedra establecidas. Primero, debes obtener una calificación promedio superior o igual a los 60 puntos en los tres parciales. Además, es necesario que hayas aprobado con 60 puntos los tres parciales.

Ten en cuenta que la información proporcionada en el otro programa (Investigación Operativa) no es aplicable para esta materia, por lo que solo debes considerar los requisitos establecidos específicamente para Comunicaciones y Redes.

**Tokens:** entrada: 1196 | salida: 127 | total: 1323

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

El software TORA es una herramienta educativa diseñada específicamente para el aprendizaje de la Investigación Operativa. Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos.

**Tokens:** entrada: 1198 | salida: 57 | total: 1255

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

El profesor Ing. Jorge L. Schmukler es parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes.

**Tokens:** entrada: 1115 | salida: 42 | total: 1157

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

La asignatura que además de la propia materia de Inteligencia Artificial, incluye explícitamente el impacto o uso de la 'Inteligencia Artificial' (IA) dentro de sus unidades temáticas es Informática y Recursos Humanos. Se puede ver esto en el "PROGRAMA INFORMATICA Y RRHH.pdf" donde se menciona el "4. El impacto de la inteligencia artificial en la gestión del talento".

**Tokens:** entrada: 1244 | salida: 94 | total: 1338

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

La materia de Investigación Operativa exige el 80% de asistencia a las clases teóricas y prácticas.

**Tokens:** entrada: 1367 | salida: 29 | total: 1396

---

### Pregunta 11

> - Si quiero promocionar todas las materias de 4to año, ¿cuál es la diferencia de promedio exigido entre Investigación Operativa e Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > **Condición del Alumno:** - **ALUMNO PROMOCIONADO:** El estudiante logrará la promoción directa si alcanza un promedio general de **80 puntos** - más entre los **1 parcial** previstos, no pudiendo
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > **Capítulo XI** Redes Autoorganizadas. Características generales. **Red SOM (Kohonen)**. Proceso de aprendizaje competitivo. Realimentación lateral. Algoritmo SOFM ó SOM (Self-Organizing -Feature-Ma
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > **Capítulo II** **Procesos de Búsqueda.** Representación en un espacio de estados. Búsqueda Ciega, definición; búsqueda primero en amplitud, búsqueda de costo uniforme; búsqueda primero en profundid
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Agentes Basados en Lógica Difusa. **Capítulo VIII** **Redes Neuronales Artificiales (RNA).** Generalidades, conceptos básicos Reseña Histórica. Clasificación de las RNA. Agentes basados en Proceso d

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1265 | salida: 14 | total: 1279

---

### Pregunta 12

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

La respuesta a esta pregunta se basa en la información proporcionada en el contexto sobre herramientas de software recomendadas para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas de la carrera de Investigación Operativa.

Se recomiendan las siguientes herramientas:

1. **LINDO (Linear, Interactive, and Discrete Optimizer)**: Un software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla para ingresar ecuaciones y restricciones de manera directa.
2. **WinQSB 2.0**: Una suite clásica que abarca múltiples módulos de Investigación Operativa, incluyendo la resolución de problemas de programación lineal, transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios.
3. **LINGO (64 bits)**: Una versión avanzada y más potente del motor LINDO, diseñado para modelar y resolver problemas de optimización de gran escala.
4. **PHP Simplex**: Herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el Método Simplex y el Método Gráfico.

Estas herramientas se relacionan con las unidades teóricas de la carrera de la siguiente manera:

- **Unidad II: Programación Lineal (PL)**: Estas herramientas pueden ser utilizadas para resolver problemas de optimización lineal, como la búsqueda de la solución óptima en los vértices y el análisis de casos especiales (soluciones múltiples, soluciones no acotadas y problemas infactibles).
- **Unidad III: Método SIMPLEX**: Las herramientas LINGO y PHP Simplex incluyen módulos para el Método Simplex, lo que permite resolver problemas de optimización lineal mediante este algoritmo.

Es importante mencionar que estas herramientas pueden ser utilizadas para resolver problemas de optimización lineal y se relacionan con las unidades teóricas de la carrera de Investigación Operativa.

**Tokens:** entrada: 1239 | salida: 456 | total: 1695

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

Lo siento, pero no dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 987 | salida: 19 | total: 1006

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

## Conversacion 3

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

La materia de Inteligencia Artificial cubre varios temas en los capítulos proporcionados. El capítulo I se centra en los agentes inteligentes, presentando conceptos básicos sobre Inteligencia Artificial, entornos de trabajo, estructura de los agentes y tipos de agentes (reactivos simples, basados en modelos, de objetivos y que aprenden). 

El Capítulo II trata los Sistemas Basados en Conocimientos, con un enfoque en la representación de conocimientos a través de lógica de primer orden, reglas de inferencia y representación basada en objetos. 

Los capítulos III a X se enfocan en distintos aspectos de la Inteligencia Artificial: Lógica Difusa, Sistemas Difusos, Redes Perceptron Multicapa, Proceso de Entrenamiento (Backpropagation), Herramientas para el Desarrollo de Sistemas Expertos, y Capa de enlace de Dato.

**Tokens:** entrada: 1649 | salida: 214 | total: 1863

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

La Lógica Difusa se menciona en la materia Inteligencia Artificial, específicamente en el Capítulo VI del contenido de la primera página del documento de IA - Programa de Cátedra (campus).pdf.

**Tokens:** entrada: 1683 | salida: 50 | total: 1733

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

El plan de estudios de la asignatura de Metodología de la Investigación se compone de varias unidades y se encuentra resumido en la siguiente descripción:

 - Unidad 1: Introducción a la ciencia y conocimiento científico
 - Unidad 2: La dimensión epistemológica
 - Unidad 3: La dimensión de la estrategia general de investigación
 - Unidad 4: La Dimensión de las técnicas de obtención y análisis de información empírica. La comunicación de los resultados

Estas unidades forman parte del plan de estudios resumido de la materia de Metodología de la Investigación.

**Tokens:** entrada: 1800 | salida: 149 | total: 1949

---

### Pregunta 4

> - En Comunicaciones y Redes, ¿cómo hago para quedar como alumno regular?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > El alumno accederá a la condición de **REGULAR**, si cumple con las siguientes condiciones de cátedra: **1 -** Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos.
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > **Evaluación Final:** El alumno con condición de REGULAR, deberá rendir un examen de los temas teóricos y prácticos desarrollados en la materia (prueba escrita). El alumno LIBRE rendirá un examen fina
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > **2-** Haber realizado y aprobado los dos trabajos Práctico impartido por la cátedra. **3-** Asistir al 80% de las clases teóricas y prácticas. El alumno tendrá condición de **LIBRE** si no cumple con
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > . La nota obtenida en este reemplaza a la obtenida en el parcial que se recupera La cátedra dará el resultado de cada una de las evaluaciones parciales y recuperatorios una semana después de que estas
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > **Facultad de Ciencia y Tecnología de la UADER** SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler.
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 15]
   > **Requisitos para rendir como estudiantes regulares, promocionales y libres:** **a.** **Promoción Directa**
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > . Explicar el **propósito de IOS como Sistema** **Operativo de red**, Explicar cómo acceder al IOS y cómo explorarlo para configurar los dispositivos de red, Describir la estructura de comandos, Confi

**Respuesta:**

Para quedar como alumno regular en la materia de Comunicaciones y Redes, debes cumplir con las siguientes condiciones de cátedra, según se establece en el Planificación 2025 para esa materia:

1. Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos. Tener aprobado con 60 puntos los tres parciales.
2. Haber realizado y aprobado los dos trabajos Práctico impartidos por la cátedra.
3. Asistir al 80% de las clases teóricas y prácticas.

Si cumple con estas condiciones, tendrás la condición de **REGULAR**.

**Tokens:** entrada: 1544 | salida: 150 | total: 1694

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

La cátedra de Investigación Operativa ofrece dos oportunidades de recuperatorio totales, que pueden utilizarse para cualquiera de los dos parciales, siempre que no se apliquen ambos recuperatorios al mismo examen parcial. La calificación obtenida en la instancia de recuperación sustituirá automáticamente a la nota del examen original.

**Tokens:** entrada: 1554 | salida: 77 | total: 1631

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

El software TORA sirve para el aprendizaje de la Investigación Operativa. Incluye módulos para el Método Simplex (con interfaz gráfica).

**Tokens:** entrada: 1705 | salida: 38 | total: 1743

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

Schmukler, Jorge es el profesor que forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes, según los documentos proporcionados.

**Tokens:** entrada: 1483 | salida: 47 | total: 1530

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

La asignatura "Informática y Recursos Humanos" incluye el impacto de la inteligencia artificial en la gestión del talento dentro de sus unidades temáticas, específicamente en la "Unidad 3: Gestión del Talento en la Era Digital".

**Tokens:** entrada: 1601 | salida: 57 | total: 1658

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

Los requisitos para regularizar en Bases de Datos Avanzadas y en Redes y Comunicaciones no son iguales.

En Bases de Datos Avanzadas, para regularidad se requiere asistencia según norma vigente, aprobación de todos los trabajos prácticos y 6 de 7 parciales aprobados con más del 50%.

En Redes y Comunicaciones, para ser regular, el alumno con condición de regular deberá rendir un examen de los temas teóricos y prácticos desarrollados en la materia, esto es, una prueba escrita.

**Tokens:** entrada: 1629 | salida: 131 | total: 1760

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

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1903 | salida: 14 | total: 1917

---

### Pregunta 11

> - Si quiero promocionar todas las materias de 4to año, ¿cuál es la diferencia de promedio exigido entre Investigación Operativa e Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > **Condición del Alumno:** - **ALUMNO PROMOCIONADO:** El estudiante logrará la promoción directa si alcanza un promedio general de **80 puntos** - más entre los **1 parcial** previstos, no pudiendo
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > **Capítulo XI** Redes Autoorganizadas. Características generales. **Red SOM (Kohonen)**. Proceso de aprendizaje competitivo. Realimentación lateral. Algoritmo SOFM ó SOM (Self-Organizing -Feature-Ma
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > **Capítulo II** **Procesos de Búsqueda.** Representación en un espacio de estados. Búsqueda Ciega, definición; búsqueda primero en amplitud, búsqueda de costo uniforme; búsqueda primero en profundid
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > **Capítulo IX** **Redes** **Perceptron** **Multicapa**, estructura básica. Proceso de Entrenamiento Backpropagation (BP). Interpretación heurística y matemática del procedimiento BP. Término de Momen
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: pesos. Regiones de Decisión. Problema de separación lineal. Aplicaciones. Limitaciones | Pagina: 2]
   > Problema XOR.
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Herramientas para el desarrollo de Sistemas Expertos. **Capítulo VI** **Lógica Difusa (Fuzzy).** Consideraciones generales, Conjuntos Difusos, definición. Operaciones simples entre conjuntos Difusos
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > Naturaleza recursiva de los cálculos: etapas, estados, decisiones y principio de optimalidad de Bellman. Resolución de problemas de diligencia, asignación de recursos y reemplazo de equipos. Diferen
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > programación lineal (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de o

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1631 | salida: 14 | total: 1645

---

### Pregunta 12

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

LINDO (Linear, Interactive, and Discrete Optimizer) es una herramienta de software especializada en resolver problemas de programación lineal, entera y no lineal, reconocida por su sintaxis sencilla para ingresar ecuaciones y restricciones de manera directa.

Es importante señalar que en el contexto de la materia de Investigación Operativa, específicamente en la unidad IV sobre modelos de transporte y transbordo, se menciona la naturaleza recursiva de los cálculos, lo que implica que los estudiantes deben familiarizarse con técnicas de resolución de problemas dinámicos.

No dispongo de información en mis documentos para relacionar específicamente las unidades teóricas con la recomendación de herramientas de software para resolver problemas de optimización lineal, por lo que no puedo responder con certeza qué unidad o unidades teóricas se relacionan con la recomendación de LINDO como herramienta de software.

**Tokens:** entrada: 1387 | salida: 202 | total: 1589

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

Sí, según la información disponible, el profesor Ing. Jorge L. Schmukler da clases en Bases de Datos Avanzadas y en Redes y Comunicaciones.

**Tokens:** entrada: 1580 | salida: 40 | total: 1620

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

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1524 | salida: 14 | total: 1538

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

## Conversacion 4

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

Los contenidos de la materia Inteligencia Artificial incluyen:

**Capítulo I: Agentes Inteligentes**, que abarca conceptos básicos de sistemas basados en conocimientos, representación de conocimientos, estructuras basadas en lógica, lógica de primer orden, reglas de inferencia, representación basada en objetos, clases e instancias, concepto de herencia y definición de objetos y atributos.

**Capítulo VIII: Redes Neuronales Artificiales (RNA)**, que se centra en generalidades, conceptos básicos, reseña histórica, clasificación de las RNA y agentes basados en proceso de aprendizaje.

No se proporciona información específica sobre los demás capítulos y contenidos que podrían estar incluidos en el programa de la materia.

**Tokens:** entrada: 872 | salida: 179 | total: 1051

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

La Lógica Difusa se enseña en la materia de Inteligencia Artificial.

**Tokens:** entrada: 955 | salida: 20 | total: 975

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

El plan de estudios resumido de Metodología de la Investigación consta de tres unidades: Introducción a la ciencia y conocimiento científico, La dimensión epistemológica y La dimensión de la estrategia general de investigación.

**Tokens:** entrada: 1076 | salida: 59 | total: 1135

---

### Pregunta 4

> - En Comunicaciones y Redes, ¿cómo hago para quedar como alumno regular?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > El alumno accederá a la condición de **REGULAR**, si cumple con las siguientes condiciones de cátedra: **1 -** Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos.
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > **Evaluación Final:** El alumno con condición de REGULAR, deberá rendir un examen de los temas teóricos y prácticos desarrollados en la materia (prueba escrita)
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > PROMOCIONADO REGULAR LIBRE El alumno accederá a la condición de **PROMOCIÓN** si cumple con las siguientes condiciones de cátedra:
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > **1 -** Obtener en los 3 parciales, una calificación promedio superior o igual a los 80 puntos. Con ninguna nota inferior a 60 puntos en cada parcial. **2-** Haber realizado y aprobado los dos trabajo
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > **2-** Haber realizado y aprobado los dos trabajos Práctico impartido por la cátedra. **3-** Asistir al 80% de las clases teóricas y prácticas. El alumno tendrá condición de **LIBRE** si no cumple con

**Respuesta:**

Para quedar como alumno regular en Comunicaciones y Redes, debes cumplir con las siguientes condiciones de cátedra:

1. Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos. Debes tener aprobado con 60 puntos los tres parciales.

No dispongo de información en mis documentos para determinar si hay otras condiciones que debes cumplir para obtener la condición de Regular.

**Tokens:** entrada: 974 | salida: 98 | total: 1072

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

La cátedra dispone de dos oportunidades de recuperatorio totales. Estas pueden utilizarse para cualquiera de los dos parciales.

**Tokens:** entrada: 968 | salida: 33 | total: 1001

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

TORA es una herramienta educativa diseñada específicamente para el aprendizaje y no se proporciona información sobre los módulos incluidos.

**Tokens:** entrada: 952 | salida: 33 | total: 985

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

El profesor Jorge L. Schmukler forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes.

**Tokens:** entrada: 881 | salida: 40 | total: 921

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

La asignatura Informática y Recursos Humanos, más específicamente en su sección 4, se refiere explícitamente al "Impacto de la inteligencia artificial en la gestión del talento" en su contenido.

**Tokens:** entrada: 948 | salida: 50 | total: 998

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

> - Si quiero promocionar todas las materias de 4to año, ¿cuál es la diferencia de promedio exigido entre Investigación Operativa e Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > **Condición del Alumno:** - **ALUMNO PROMOCIONADO:** El estudiante logrará la promoción directa si alcanza un promedio general de **80 puntos** - más entre los **1 parcial** previstos, no pudiendo
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > y el cumplimiento del 80% de asistencia a las clases teóricas y prácticas. - **ALUMNO LIBRE:** Revestirá esta condición todo estudiante que no logre cumplimentar alguno de los requisitos de puntaje
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Representación de Conocimientos mediante reglas. Estructura básica. Representación de reglas mediante objetos. Ventajas comparativas entre las distintas representaciones. Comportamiento de Agentes Ba
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > Modificación del algoritmo SOM para evitar una excesiva acumulación de información, por parte de una misma neurona. **Capítulo XII** **Sistemas Multi Agentes**

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 945 | salida: 14 | total: 959

---

### Pregunta 12

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

Según el documento, las herramientas recomendadas para resolver problemas de optimización lineal son:

*   LINDO (Linear, Interactive, and Discrete Optimizer), que es software especializado en la resolución de problemas de programación lineal, entera y no lineal.
*   LINGO (64 bits), una versión avanzada del motor LINDO.
*   WinQSB 2.0, una suite que incluye múltiples módulos de Investigación Operativa para resolver problemas de programación lineal, transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios.
*   Storm, software orientado al análisis cuantitativo y gestión de operaciones.

Estas herramientas están relacionadas con las unidades teóricas de la materia de Investigación Operativa, ya que permiten resolver problemas de optimización y gestión de manera práctica.

**Tokens:** entrada: 1026 | salida: 199 | total: 1225

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

Lo siento, pero no dispongo de información en mis documentos para confirmar que el profesor Ing. Jorge L. Schmukler da clases en Redes y Comunicaciones. En el contexto proporcionado, se menciona que da clases en Bases de Datos Avanzadas y en Inteligencia Artificial.

**Tokens:** entrada: 965 | salida: 67 | total: 1032

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
| 1 | 21172 | 989 | 22161 |
| 2 | 21963 | 1593 | 23556 |
| 3 | 29055 | 1253 | 30308 |
| 4 | 17686 | 890 | 18576 |
| **Total** | **89876** | **4725** | **94601** |
