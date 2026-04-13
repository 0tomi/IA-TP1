# Evaluacion — testOllamaPostMejoras1

_Iniciada: 2026-04-12 16:37:28_
_Ultima actualizacion: 2026-04-12 16:43:47_

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
| refresh | True |

### Pregunta 1

> - ¿Cuáles son los contenidos de la materia Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos Capítulo I Agentes Inteligentes Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas por el áre
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > la asignatura. Introducción a los agentes inteligentes. Entorno de Trabajo. Propiedades de los entornos. Estructura de los Agentes. Programas de Agentes. Agente Reactivo Simple.
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 2]
   > entornos digitales. 2. Inteligencia emocional y gestión de equipos en la virtualidad. 3. Liderazgo en tiempos de transformación digital. 4. El impacto de la inteligencia artificial en la gestión del t
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (200
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > nal. Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación de los distintos métodos sobre el funcionamiento del sistema. Agentes Basa
6. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 2]
   > as tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales. Unidad 3: Gestión del Talento en la Era Digital 1. Procesos de selección y r

**Respuesta:**

La materia Inteligencia Artificial incluye los siguientes contenidos: Introducción a los agentes inteligentes, Entorno de Trabajo, Propiedades de los entornos, Estructura de los Agentes, Programas de Agentes, Agente Reactivo Simple, Agentes Reactivos basados en Modelos, Agente basado en Objetivos y Agentes que Aprende.

**Tokens:** entrada: 1102 | salida: 84 | total: 1186

---

### Pregunta 2

> - ¿En qué materia se enseña el concepto de Lógica Difusa?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > ) y Encadenamiento hacia atrás (Backward Chaining). Herramientas para el desarrollo de Sistemas Expertos. Capítulo VI Lógica Difusa (Fuzzy). Consideraciones generales, Conjuntos Difusos, defin
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > nal. Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación de los distintos métodos sobre el funcionamiento del sistema. Agentes Basa
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > s Basados en Conocimientos. Conceptos básicos. Representación de Conocimientos. Estructuras basadas en Lógica. Lógica de Primer Orden. Reglas de Inferencia. Representación basada en obj
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > e Fuzzificación. Influencia de la forma y distribución de los Conjuntos Difusos, en el comportamiento del sistema. Proceso de Inferencia. Tratamiento paralelo de las reglas. Determinación del apor
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > gualdad, Complementación, Intersección, Unión. Estructuras FAM (Fuzzy Associative Memories). Composición MAX-MIN. Capítulo VII Sistemas Difusos. Consideraciones generales. Representación de
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > as. Concepto de herencia. Métodos y mensajes. Representación de Conocimientos mediante reglas. Estructura básica. Representación de reglas mediante objetos. Ventajas comparativas entre la

**Respuesta:**

El concepto de Lógica Difusa se enseña en la materia de "Sistemas Difusos" (Capítulo VII), pero también está relacionado con otras materias como "Lógica Difusa (Fuzzy)" en el Capítulo VI.

**Tokens:** entrada: 1120 | salida: 59 | total: 1179

---

### Pregunta 3

> - ¿Cuál es el plan de estudios de Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > científico - Unidad 2: La dimensión epistemológica - Unidad 3: La dimensión de la estrategia general de investigación - Unidad 4: La Dimensión de las técnicas de obtención y análisis de información em
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 1]
   > tadística (317). Fundamentación: La metodología de la investigación es la ciencia del método. Yuni y Urbano (2016) sostiene que como la epistemología, la metodología de la investigación es una discipl
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 1]
   > nos permite entonces poder conocer. El enfoque que toma esta cátedra se centra en la producción de conocimientos científicos. A los fines de su desarrollo, se entenderá a la Metodología de la Investig
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 1]
   > 2026 - FCYT-ORO VERDE - Licenciatura en Sistemas de Información - Metodología de la Investigación Carrera: Licenciatura en Sistemas de Información Cátedra: Metodología de la Investigación Año Académic
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > PLANIFICACIÓN INVESTIGACIÓN OPERATIVA Unidad I: -Introducción y Modelos Matemáticos- Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del proble
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 11]
   > 11 - Arias, F. (2012). El proyecto de investigación: Introducción a la metodología de la investigación (Sexta edición ampliada y corregida). Caracas: Episteme. - Samaja, Juan (2016) Epistemología y me

**Respuesta:**

La Licenciatura en Sistemas de Información, específicamente la carrera que abarca la Metodología de la Investigación, está programada para el año académico 2026, con la PROFESORA RESPONSABLE ADJUNTO: ALEJANDRA MARǪUESIN.

**Tokens:** entrada: 1083 | salida: 65 | total: 1148

---

### Pregunta 4

> - En Comunicaciones y Redes, ¿cómo hago para quedar como alumno regular?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 3]
   > 80 puntos. Con ninguna nota inferior a 60 puntos en cada parcial. 2- Haber realizado y aprobado los dos trabajos práctico impartido por la cátedra. 3- Asistir al 80% de las clases teóricas y prácticas
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de 60 puntos en ambos parciales. Es requisito indispensable la entrega y aprobación de los dos trabajos prá
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 3]
   > emas de red. 2- SISTEMA DE EVALUACION Condición del Alumno: PROMOCIONADO REGULAR LIBRE El alumno accederá a la condición de PROMOCIÓN si cumple con las siguientes condiciones de cátedra: 1 - Obtener
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 15]
   > ector Julio Alberto Aldonate; codirector Luciano María Caisso. 2018 Requisitos para rendir como estudiantes regulares, promocionales y libres: a. Promoción Directa
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 8]
   > Comunicación De rutina y consultas: Lista de mail. Material académico: aula virtual - Clave de matriculación bda2023 *Único medio oficial. Avisos y notificaciones: Grupo de Telegram https://t.me/+c7PP
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > 17 b. Alumno Regular - 60 % de asistencia. - Aprobación del examen parcial teórico con una calificación igual o superior a 60 (sesenta) puntos. - Entrega de todos los trabajos en tiempo y forma. - Per

**Respuesta:**

Para quedar como alumno regular en Comunicaciones y Redes, debes cumplir con las siguientes condiciones: 

- Obtener una calificación mínima de 60 puntos en ambos parciales.
- Entregar y aprobar los dos trabajos prácticos obligatorios.
- Cumplir con el 80% de asistencia a las clases teóricas y prácticas.

No dispongo de información en mis documentos para saber si hay otras condiciones o requisitos adicionales específicos para la asignatura de Comunicaciones y Redes, por lo que te recomendaría consultar el programa académico o la guía del curso para obtener más información.

**Tokens:** entrada: 1028 | salida: 141 | total: 1169

---

### Pregunta 5

> - ¿Qué instancias de recuperación nos provee Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > PLANIFICACIÓN INVESTIGACIÓN OPERATIVA Unidad I: -Introducción y Modelos Matemáticos- Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del proble
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > do médico o motivo de fuerza mayor validado) se considerará como examen reprobado. Software de Aplicación - Investigación Operativa A continuación, se describen las herramientas informáticas utilizada
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 3]
   > nvestigación caracterizando las instancias y fases del proceso de investigación cualitativa y cuantitativa. - Potenciar el desarrollo de análisis crítico-reflexivo de investigaciones del campo de los
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > rm: Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadísticos mediante una interfaz basada en menús para la carga de datos.
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 20]
   > 20 12 de noviembr e Espacio de recuperación y cierre
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > zaje de la Investigación Operativa. Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 945 | salida: 14 | total: 959

---

### Pregunta 6

> - ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > rm: Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadísticos mediante una interfaz basada en menús para la carga de datos.
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > 3- PROGRAMA DE TRABAJOS PRACTICOS La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos vertidos en la teoría. Más dos trabajos
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 8]
   > tro entre pares: se organizarán espacios de intercambio con estudiantes que ya han cursado la carrera, con el fin de compartir experiencias. Sistema de evaluación: - Un (1) examen parcial teórico, de
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 1]
   > ura busca analizar estos cambios desde una perspectiva multidisciplinaria, integrando conceptos de informática, gestión organizacional y derecho informático. Los estudiantes explorarán los efectos de
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > do médico o motivo de fuerza mayor validado) se considerará como examen reprobado. Software de Aplicación - Investigación Operativa A continuación, se describen las herramientas informáticas utilizada
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 5]
   > urante el primer cuatrimestre se abordará y desarrollará la mayor parte de los contenidos teóricos previstos en el programa, a fin de que el segundo cuatrimestre esté destinado de manera prioritaria y

**Respuesta:**

TORA es una herramienta educativa diseñada específicamente para el aprendizaje de la Investigación Operativa.

**Tokens:** entrada: 1012 | salida: 25 | total: 1037

---

### Pregunta 7

> - ¿Qué profesor forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > Plan de Cátedra de la Carrera Licenciado en Sistemas de Información de la Facultad de Ciencia y Tecnología de la UADER SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE:
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 14]
   > rector Fernando Sato; codirector Sebastián Jorge Trossero. 2022 Modelos vectoriales y redes neuronales artificiales, para la aplicación de procesamiento de lenguaje natural en normativas jurídicas / J
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 1]
   > s semanales Plan de Estudio: Docente: Abog. Rodriguez Zanin, Fabio I. FUNDAMENTACIÓN El avance de las tecnologías de la información y la comunicación (TIC) ha transformado la dinámica del mundo labor
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > es, se trabajarán tanto los fundamentos teóricos de la metodología de la investigación y la escritura académica como aspectos prácticos para avanzar en la elaboración del anteproyecto. Se dispondrá de
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 1]
   > Bases de Datos Avanzadas PRESENTACIÓN DE LA MATERIA Facultad de Ciencia Y Tecnología Base de Datos Avanzadas
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > go de la profesora Alejandra, y de dos enlaces diferenciados para las clases prácticas: uno correspondiente a los grupos asignados a la profesora Tamara y otro destinado a los grupos a cargo de la pro

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1023 | salida: 14 | total: 1037

---

### Pregunta 8

> - ¿Qué otra asignatura, además de la propia materia de Inteligencia Artificial, incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos Capítulo I Agentes Inteligentes Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas por el áre
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 2]
   > as tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales. Unidad 3: Gestión del Talento en la Era Digital 1. Procesos de selección y r
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > la asignatura. Introducción a los agentes inteligentes. Entorno de Trabajo. Propiedades de los entornos. Estructura de los Agentes. Programas de Agentes. Agente Reactivo Simple.
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 1]
   > ura busca analizar estos cambios desde una perspectiva multidisciplinaria, integrando conceptos de informática, gestión organizacional y derecho informático. Los estudiantes explorarán los efectos de
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 2]
   > entornos digitales. 2. Inteligencia emocional y gestión de equipos en la virtualidad. 3. Liderazgo en tiempos de transformación digital. 4. El impacto de la inteligencia artificial en la gestión del t
6. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 3]
   > delitos informáticos en Argentina. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales.

**Respuesta:**

La asignatura que incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas es la mencionada en el Documento "PROGRAMA INFORMATICA Y RRHH.pdf" como "Unidad 4: El impacto de la inteligencia artificial en la gestión del talento" y también la "Unidad 3: Gestión del Talento en la Era Digital" que se refiere a los efectos de las nuevas tecnologías en el trabajo y la administración del talento humano.

**Tokens:** entrada: 1047 | salida: 121 | total: 1168

---

### Pregunta 9

> - Los requisitos para regularizar en Bases de Datos Avanzadas y en Redes y Comunicaciones, ¿son iguales? ¿Qué diferencias tienen?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > full-duplex, tabla de conmutación). Comparación hubs / switch. ARP (protocolo de resolución de direcciones). Mantenimiento de la tabla ARP. ARP proxy. Cableado Estructurado: Selección de dispositivos
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > enlace de datos de alto nivel-, Capa de enlace de datos en Internet -Protocolo PPP (Protocolo Punto a Punto)-). Unidad V: -Capa de enlace de dato -sub capa MAC (control de acceso al medio)- Problema d
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > itiendo una integración más fluida con bases de datos y
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > Enrutamiento por estado del enlace, Enrutamiento jerárquico, Enrutamiento por difusión, Enrutamiento por multidifusión, Enrutamiento para hosts móviles, Enrutamiento en redes ad hoc, Búsqueda de nodos
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > 00base-lx, la ethernet de 10 gigabits (10gbe)). Utilización de hubs como dispositivo intermedio (problemas con el crecimiento de la red: escalabilidad, fallas en la red, colisiones). Switches (ancho d
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > onmutación en la capa de enlace (Repetidores, Concentradores, Puentes, Conmutadores, Enrutadores y Puerta de enlace). Lan Virtuales (VLAN) IEEE 802.1Q. Unidad VI: -Ethernet y Cableado Estructurado- Es

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1026 | salida: 14 | total: 1040

---

### Pregunta 10

> - ¿Cuál es el porcentaje de asistencia a clases que exigen en común las materias de Investigación Operativa, Comunicaciones y Redes, y Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > LAN DE ESTUDIO: 2010 (Resolución No 397/10 UADER) AÑO DE LA CARRERA A LA QUE PERTENECE LA CATEDRA: Cuarto Año RÉGIMEN DE LA MATERIA: Anual CARGA HORARIA SEMANAL: 5 horas 1- PROGRAMA DE CONTENIDOS Uni
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > OLOGÍA DE LA INVESTIGACIÓN- 2026 Clase FECHA Tipo de encuentro Tipo encuentro Tema 1 12 de marzo Presencial Teórico/práctico Presentación de la asignatura 2 19 de marzo Virtual Teoría Conceptos genera
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > ificación menor a 60 puntos en ninguna de las instancias individuales. Asimismo, deberá acreditar la aprobación de los dos trabajos prácticos de la cátedra y mantener una asistencia mínima del 80% a l
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > a facilitar el acceso a los contenidos para aquellos estudiantes que no pueden asistir a todas las clases y, al mismo tiempo, reducir la tasa de abandono. Por ello, los materiales teóricos y las lectu
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > PLANIFICACIÓN INVESTIGACIÓN OPERATIVA Unidad I: -Introducción y Modelos Matemáticos- Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del proble
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > 17 b. Alumno Regular - 60 % de asistencia. - Aprobación del examen parcial teórico con una calificación igual o superior a 60 (sesenta) puntos. - Entrega de todos los trabajos en tiempo y forma. - Per

**Respuesta:**

Un 80% de asistencia a las clases es requisito común para aprobar las materias de Investigación Operativa y Comunicaciones y Redes, pero no tengo información de los requisitos de asistencia para la materia de Metodología de la Investigación.

**Tokens:** entrada: 1098 | salida: 58 | total: 1156

---

### Pregunta 11

> - Si quiero promocionar todas las materias de 4to año, ¿cuál es la diferencia de promedio exigido entre Investigación Operativa e Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > nística y Probabilística. SISTEMA DE EVALUACIÓN (Investigación Operativa) Condición del Alumno: - ALUMNO PROMOCIONADO: El estudiante logrará la promoción directa si alcanza un promedio general de 80 p
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos Capítulo I Agentes Inteligentes Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas por el áre
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > PLANIFICACIÓN INVESTIGACIÓN OPERATIVA Unidad I: -Introducción y Modelos Matemáticos- Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del proble
4. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 7]
   > Régimen Regularidad: Asistencia: Según norma vigente. Todos los trabajos prácticos aprobados. 6/7 parciales aprobados con más del 50% Promoción: Régimen regular Obtener más del 70% en todos los parcia
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > rm: Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadísticos mediante una interfaz basada en menús para la carga de datos.
6. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 1]
   > UNIVERSIDAD AUTÓNOMA DE ENTRE RÍOS FACULTAD DE CIENCIA Y TECNOLOGÍA PROGRAMA DE CÁTEDRA: INFORMÁTICA Y RELACIONES HUMANAS Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectiv

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1080 | salida: 14 | total: 1094

---

### Pregunta 12

> - ¿Qué herramientas de software se recomiendan en la carrera para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > do médico o motivo de fuerza mayor validado) se considerará como examen reprobado. Software de Aplicación - Investigación Operativa A continuación, se describen las herramientas informáticas utilizada
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > mas de gestión: - LINDO (Linear, Interactive, and Discrete Optimizer): Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis se
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > inQSB 2.0: Una suite clásica (dividida en 3 partes) que abarca múltiples módulos de Investigación Operativa. Permite resolver problemas de programación lineal (LP), modelos de transporte, asignación,
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > rm: Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadísticos mediante una interfaz basada en menús para la carga de datos.
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > lidación. Clasificación de modelos: determinísticos y estocásticos. Definición de variables de decisión, función objetivo y restricciones de sistema y de no negatividad. Unidad II: -Programación Linea
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > zaje de la Investigación Operativa. Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible

**Respuesta:**

Las herramientas de software recomendadas para resolver problemas de optimización lineal son:

- LINDO (Linear, Interactive, and Discrete Optimizer): Especializado en la resolución de problemas de programación lineal, entera y no lineal.
- WinQSB 2.0: Una suite clásica que abarca múltiples módulos de Investigación Operativa, incluyendo programación lineal (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios.
- PHP Simplex: Herramienta online que permite resolver problemas de programación lineal mediante el Método Simplex y el Método Primal.

Se relacionan con las unidades teóricas de Programación Lineal (PL) y propiedades de los modelos de Programación Lineal: proporcionalidad, aditividad, divisibilidad, que se encuentran en la Unidad II.

**Tokens:** entrada: 1034 | salida: 201 | total: 1235

---

### Pregunta 13

> - ¿Dónde puedo descargar la materia de Cálculo de 1er año?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 3]
   > hojas de cálculo.
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > puntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] Cisco Systems: Academia de Networking de Cisco Systems: Guía del primer año. -2a ed. - Madrid: Pear
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > LAN DE ESTUDIO: 2010 (Resolución No 397/10 UADER) AÑO DE LA CARRERA A LA QUE PERTENECE LA CATEDRA: Cuarto Año RÉGIMEN DE LA MATERIA: Anual CARGA HORARIA SEMANAL: 5 horas 1- PROGRAMA DE CONTENIDOS Uni
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 12]
   > 12 - Natale, Lucía (Coordinadora) (2013). En carrera: escritura y lectura de textos académicos y profesionales. Argentina. Universidad Nacional de Ǫuilmes. Visto en https://ediciones.ungs.edu.ar/wp-co
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 1]
   > UNIVERSIDAD AUTÓNOMA DE ENTRE RÍOS FACULTAD DE CIENCIA Y TECNOLOGÍA PROGRAMA DE CÁTEDRA: INFORMÁTICA Y RELACIONES HUMANAS Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectiv
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > 2a ed. - Madrid: Pearson Educación, 2004. ISBN 842053921X [Disponible en Biblioteca FCyT- Oro Verde]

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1015 | salida: 14 | total: 1029

---

### Pregunta 14

> - El profesor Ing. Jorge L. Schmukler da clases en Bases de Datos Avanzadas, en Inteligencia Artificial y en Redes y Comunicaciones.

**Chunks de contexto:**

1. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 2]
   > Equipo docente Trossero, Sebastián Teoría Trossero.sebastian@uader.edu.ar Schmuckler, Jorge Práctica Schmukler.jorge@uader.edu.ar
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > la asignatura. Introducción a los agentes inteligentes. Entorno de Trabajo. Propiedades de los entornos. Estructura de los Agentes. Programas de Agentes. Agente Reactivo Simple.
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 14]
   > rector Fernando Sato; codirector Sebastián Jorge Trossero. 2022 Modelos vectoriales y redes neuronales artificiales, para la aplicación de procesamiento de lenguaje natural en normativas jurídicas / J
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > segmentación de red). Clase de direccionamiento (clase a, b, c, d y e). Prefijo y Mascara de red. Lógica de and. Calculo de direcciones. División de subredes (por clase y vlsm (mascara de subred de lo
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > go de la profesora Alejandra, y de dos enlaces diferenciados para las clases prácticas: uno correspondiente a los grupos asignados a la profesora Tamara y otro destinado a los grupos a cargo de la pro
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > Plan de Cátedra de la Carrera Licenciado en Sistemas de Información de la Facultad de Ciencia y Tecnología de la UADER SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE:

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1076 | salida: 14 | total: 1090

---

### Pregunta 15

> - ¿Cuál es el costo de la certificación oficial de Cisco que se menciona como opcional en la planificación?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > puntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] Cisco Systems: Academia de Networking de Cisco Systems: Guía del primer año. -2a ed. - Madrid: Pear
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 5]
   > Sitios web sobre normativas, tecnologías y soluciones, opcional: IETF -> www.ietf.org IEEE -> www.ieee.org ISO -> www.iso.org CISCO -> www.cisco.com IANA -> www.iana.org ISOC -> www.isoc.org ARIN -> w
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 5]
   > on.mason?electricity:2:3:3 NATIONAL FIRE PROTECTION AGENCY (NFPA) -> www.nfpa.org GFI SECURITY AND MESSANGING SOFTWARE -> www.gfi.com Lic. Luciano M. CAISSO.
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 5]
   > 6tf.org 3M -> www.3m.com FURUKAWA -> www.furukawa.com.br/internacional.html UNDERWRITERS LABORATORIES (UL) -> www.ul.com PANDUIT -> www.panduit.com AMP -> www.tycoelectronics.com/components/ ETHEREAL
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > FCyT- Oro Verde] Técnico en Redes & Seguridad, Bs. As.: Fox Andina, 2013, ISBN: 9789871857784. - USERS. [Disponible en Biblioteca FCyT- Oro Verde] Curso visual y práctico: Administrador de Redes Insta
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 8]
   > final, respetando las fechas establecidas en el cronograma académico.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1053 | salida: 14 | total: 1067

---

### Pregunta 16

> - Para la Promoción Directa, se exige la aprobación de la totalidad de los trabajos prácticos (TP 1 al TP 5). ¿Cuál es la calificación numérica mínima que debe obtenerse en cada TP individual para que se considere aprobado?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 16]
   > 16 Para acceder a la condición de Promoción Directa, el/la estudiante deberá cumplir con los siguientes requisitos: - 80 % de asistencia a la cursada. - Aprobación del examen parcial teórico con una c
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > nística y Probabilística. SISTEMA DE EVALUACIÓN (Investigación Operativa) Condición del Alumno: - ALUMNO PROMOCIONADO: El estudiante logrará la promoción directa si alcanza un promedio general de 80 p
3. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 7]
   > Régimen Regularidad: Asistencia: Según norma vigente. Todos los trabajos prácticos aprobados. 6/7 parciales aprobados con más del 50% Promoción: Régimen regular Obtener más del 70% en todos los parcia
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > ificación menor a 60 puntos en ninguna de las instancias individuales. Asimismo, deberá acreditar la aprobación de los dos trabajos prácticos de la cátedra y mantener una asistencia mínima del 80% a l
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 9]
   > 9 Programa de trabajos prácticos: Tp 1: Escritura académica. Se solicita a los estudiantes seleccionar un artículo de investigación sobre un tema de interés específico relacionado al campo profesional
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 9]
   > e resultados. Tp integrador: Presentación formal escrita y oral de todas las partes realizadas en los trabajos anteriores con las sugerencias corregidas y presentación a todos los compañeros que estén

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1020 | salida: 14 | total: 1034

---

### Pregunta 17

> - ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > zaje de la Investigación Operativa. Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > e el Método Simplex y el Método Gráfico. Es ideal para validaciones rápidas y visualización de regiones factibles. - LINGO (64 bits): Una versión avanzada y más potente del motor LINDO. Está diseñado
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > roblemas infactibles). Unidad III: -Método SIMPLEX- Algoritmo del método Simplex: forma estándar, variables de holgura y variables artificiales. Construcción de la tabla inicial, criterios de entrada
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > lidación. Clasificación de modelos: determinísticos y estocásticos. Definición de variables de decisión, función objetivo y restricciones de sistema y de no negatividad. Unidad II: -Programación Linea
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Algoritmo de Modificación de los pesos. Regiones de Decisión. Problema de separación lineal. Aplicaciones. Limitaciones: Problema XOR.
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > mas de gestión: - LINDO (Linear, Interactive, and Discrete Optimizer): Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis se

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1000 | salida: 14 | total: 1014

---

### Pregunta 18

> - ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > RNO/ MESAS DE EXAMENES FINALES 16 06 de agosto Virtual Teoría Repaso del proceso de investigación 17 13 de agosto Virtual Tutorías 18 20 de agosto Presencial (cambio encuentro) Teoría Parcial teoría 1
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > OLOGÍA DE LA INVESTIGACIÓN- 2026 Clase FECHA Tipo de encuentro Tipo encuentro Tema 1 12 de marzo Presencial Teórico/práctico Presentación de la asignatura 2 19 de marzo Virtual Teoría Conceptos genera
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > 19 12 28 de mayo Virtual Teoría 13 04 de junio Presencial Teoría Marco metodológico I: enfoque y tipo de investigación / muestra 14 11 de junio Virtual Práctica 15 18 de junio Virtual Teoría Marco met
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > tura académica 4 2 de abril (sin clase) 5 09 de abril Presencial Teoría Tema/ problema 6 16 de abril Virtual Práctica 7 23 de abril Virtual Teoría Pregunta de investigación (variables, unidad de análi
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > 24 01 de octubre Presencial Tutorías Presentación tesina- ver posibilidad 25 08 de octubre Virtual Tutorías Presentación tesina- ver posibilidad 26 15 de octubre Virtual Tutorías 27 22 de octubre Virt
6. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 3]
   > Días de clase Lunes: 13:30 a 15:30 -> Teoría Viernes: 17:00 a 19:00 -> Práctica NOTA: Los horarios están en proceso de evaluación y pueden sufrir cambios

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1079 | salida: 14 | total: 1093

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
   > Inteligencia Artificial Programa de Contenidos Capítulo I Agentes Inteligentes Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas por el áre
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (200
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > comportamiento del sistema. Proceso de Inferencia. Tratamiento paralelo de las reglas. Determinación del aporte parcial de cada regla. Integración de la solución difusa final. Proceso de D
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 2]
   > . Liderazgo en tiempos de transformación digital. 4. El impacto de la inteligencia artificial en la gestión del talento. Bibliografía Nacional: Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. A
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 5]
   > Programa Sintético Unidad I: Bases de Datos Activas Unidad II: Bases de Datos Temporales Unidad III: Bases de Datos Geográficas Unidad IV: Bases de Datos Distribuidas Unidad V: Datawarehouse Unidad VI

**Respuesta:**

Los contenidos de la materia Inteligencia Artificial se desarrollan en varios capítulos y temas específicos. En el capítulo I, "Agentes Inteligentes", se abordan conceptos fundamentales como la introducción a los agentes inteligentes, los entornos de trabajo, las propiedades de los entornos y la estructura de los agentes.

A continuación, se introducen programas de agentes y se analiza el comportamiento del agente reactivo simple, así como los agentes reactivos basados en reglas.

La bibliografía principal para la materia incluye el libro "Inteligencia Artificial - Un Enfoque Moderno" de Stuart J. Rusell y Peter Norvig, y "Aprendizaje automático y aprendizaje profundo con Python, scikit-learn y Tensor Flow" de S. Raschka y V. Mirjalili. 

Sin embargo, los contenidos detallados de la materia incluyen, entre otros, agentes basados en lógica difusa y redes neuronales artificiales.

**Tokens:** entrada: 1179 | salida: 229 | total: 1408

---

### Pregunta 2

> - ¿En qué materia se enseña el concepto de Lógica Difusa?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Estructura de Control: Procedimientos de Inferencia; Interfase con el usuario. Memoria de Trabajo, Módulo generador de explicaciones al usuario. Capítulo V Funcionalidad de los Sistemas Expertos Proc
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > comportamiento del sistema. Proceso de Inferencia. Tratamiento paralelo de las reglas. Determinación del aporte parcial de cada regla. Integración de la solución difusa final. Proceso de D
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > simples entre conjuntos Difusos: Inclusión, Igualdad, Complementación, Intersección, Unión. Estructuras FAM (Fuzzy Associative Memories). Composición MAX-MIN. Capítulo VII Sistemas Dif
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > ordenada en el espacio de estados. Recocido Simulado. Búsqueda voraz primero el mejor. Búsqueda A*, Heurísticos admisibles, comparación entre varios heurísticos admisibles. Agent
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Reglas de Inferencia. Representación basada en objetos. Definición de objetos y de atributos. Clases e instancias. Concepto de herencia. Métodos y mensajes. Representación de Con

**Respuesta:**

El concepto de Lógica Difusa se enseña en la materia de Sistemas Difusos, específicamente en el Capítulo VI que trata sobre Lógica Difusa (Fuzzy).

**Tokens:** entrada: 1264 | salida: 45 | total: 1309

---

### Pregunta 3

> - ¿Cuál es el plan de estudios de Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > . La comunicación de los resultados Cronograma de trabajo METODOLOGÍA DE LA INVESTIGACIÓN- 2026 Clase FECHA Tipo de encuentro Tipo encuentro Tema 1 12 de marzo Presencial Teórico/práctico Presentación
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 1]
   > . JEFE DE TRABAJOS PRÁCTICOS: JIMENA SANTA CRUZ; Año de la carrera a la que pertenece la cátedra: 4 Régimen de la materia: Anual Carga horaria semanal: 3 horas Correlativa: Ingeniería del Software I (
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 1]
   > . Esto nos permite entonces poder conocer. El enfoque que toma esta cátedra se centra en la producción de conocimientos científicos. A los fines de su desarrollo, se entenderá a la Metodología de la I
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 1]
   > 2026 - FCYT-ORO VERDE - Licenciatura en Sistemas de Información - Metodología de la Investigación Carrera: Licenciatura en Sistemas de Información Cátedra: Metodología de la Investigación Año Académic
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 11]
   > 11 - Arias, F. (2012). El proyecto de investigación: Introducción a la metodología de la investigación (Sexta edición ampliada y corregida). Caracas: Episteme. - Samaja, Juan (2016) Epistemología y me

**Respuesta:**

La cátedra de Metodología de la Investigación es parte del plan de estudios de Licenciatura en Sistemas de Información.

**Tokens:** entrada: 1115 | salida: 31 | total: 1146

---

### Pregunta 4

> - En Comunicaciones y Redes, ¿cómo hago para quedar como alumno regular?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 3]
   > El alumno accederá a la condición de REGULAR, si cumple con las siguientes condiciones de cátedra: 1 - Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de 60 puntos en ambos parciales
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > . Alumno Regular - 60 % de asistencia. - Aprobación del examen parcial teórico con una calificación igual o superior a 60 (sesenta) puntos. - Entrega de todos los trabajos en tiempo y forma. - Pertine
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 15]
   > . Guillerón. 2018 Red Privada Virtual (VPM) sobre Protocolo de Internet versión 6 (IPv6) / Rodrigo Paúl Basso, Maximiliano Sebastián Toso; director Julio Alberto Aldonate; codirector Luciano María Cai
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 3]
   > 2- SISTEMA DE EVALUACION Condición del Alumno: PROMOCIONADO REGULAR LIBRE El alumno accederá a la condición de PROMOCIÓN si cumple con las siguientes condiciones de cátedra: 1 - Obtener en los 3 parc

**Respuesta:**

Para quedar como alumno regular en Comunicaciones y Redes, debes obtener una calificación promedio superior o igual a los 60 puntos en los tres parciales.

**Tokens:** entrada: 958 | salida: 38 | total: 996

---

### Pregunta 5

> - ¿Qué instancias de recuperación nos provee Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > PLANIFICACIÓN INVESTIGACIÓN OPERATIVA Unidad I: -Introducción y Modelos Matemáticos- Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del proble
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > . La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen reprobado. Software de Aplicación - Investigación Operativa A continuación, se descri
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 8]
   > . Dicho examen contará con una (1) instancia de recuperación, conforme al cronograma establecido por la cátedra. - Entrega obligatoria de las actividades prácticas y aprobación del trabajo práctico in
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > . Permite resolver problemas de programación lineal (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al análisis cu
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 20]
   > 20 12 de noviembr e Espacio de recuperación y cierre

**Respuesta:**

La ausencia no justificada se considerará como examen reprobado, pero existen instancias de recuperación. De acuerdo al Documento "PROGRAMA- Metodología de la Investigación.pdf" , hay una instancia de recuperación para el examen. No dispongo de información en mis documentos para saber si hay más de una instancia.

**Tokens:** entrada: 942 | salida: 74 | total: 1016

---

### Pregunta 6

> - ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > . Permite resolver problemas de programación lineal (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al análisis cu
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > . La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen reprobado. Software de Aplicación - Investigación Operativa A continuación, se descri
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 5]
   > complemento de las clases presenciales y remotas. Asimismo, se establece que durante el primer cuatrimestre se abordará y desarrollará la mayor parte de los contenidos teóricos previstos en el program
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > 3- PROGRAMA DE TRABAJOS PRACTICOS La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos vertidos en la teoría. Más dos trabajos
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > : Se propondrán diversas tareas alineadas con los contenidos abordados, las cuales constituirán los componentes del anteproyecto de investigación final. Respecto a las clases: La cátedra implementará

**Respuesta:**

TORA es una herramienta educativa diseñada específicamente para el aprendizaje de la Investigación Operativa. Su propósito es facilitar el procesamiento de modelos matemáticos y estadísticos mediante una interfaz basada en menús para la carga de datos.

**Tokens:** entrada: 1126 | salida: 59 | total: 1185

---

### Pregunta 7

> - ¿Qué profesor forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > Plan de Cátedra de la Carrera Licenciado en Sistemas de Información de la Facultad de Ciencia y Tecnología de la UADER SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE:
2. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 1]
   > Bases de Datos Avanzadas PRESENTACIÓN DE LA MATERIA Facultad de Ciencia Y Tecnología Base de Datos Avanzadas
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > . El análisis de los datos en la investigación: teorías y procedimientos manuales e informáticos. La comunicación de los resultados. Metodología de trabajo y estrategias pedagógicas: La cátedra aborda
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 1]
   > 2026 - FCYT-ORO VERDE - Licenciatura en Sistemas de Información - Metodología de la Investigación Carrera: Licenciatura en Sistemas de Información Cátedra: Metodología de la Investigación Año Académic
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 1]
   > UNIVERSIDAD AUTÓNOMA DE ENTRE RÍOS FACULTAD DE CIENCIA Y TECNOLOGÍA PROGRAMA DE CÁTEDRA: INFORMÁTICA Y RELACIONES HUMANAS Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectiv

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1056 | salida: 14 | total: 1070

---

### Pregunta 8

> - ¿Qué otra asignatura, además de la propia materia de Inteligencia Artificial, incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos Capítulo I Agentes Inteligentes Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas por el áre
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 1]
   > integrando conceptos de informática, gestión organizacional y derecho informático. Los estudiantes explorarán los efectos de las nuevas tecnologías en el trabajo, la calidad de vida laboral y la admin
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 1]
   > . Además, se abordarán aspectos legales fundamentales para comprender el impacto normativo de las TIC en el ámbito laboral, tomando como base la legislación argentina y los aportes de autores nacional
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 2]
   > . Liderazgo en tiempos de transformación digital. 4. El impacto de la inteligencia artificial en la gestión del talento. Bibliografía Nacional: Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. A
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > . El análisis de los datos en la investigación: teorías y procedimientos manuales e informáticos. La comunicación de los resultados. Metodología de trabajo y estrategias pedagógicas: La cátedra aborda

**Respuesta:**

La Unidad 3 de la asignatura "PROGRAMA INFORMATICA Y RRHH" aborda específicamente "El impacto de la inteligencia artificial en la gestión del talento" como uno de sus contenidos.

**Tokens:** entrada: 1113 | salida: 48 | total: 1161

---

### Pregunta 9

> - Los requisitos para regularizar en Bases de Datos Avanzadas y en Redes y Comunicaciones, ¿son iguales? ¿Qué diferencias tienen?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . ARP (protocolo de resolución de direcciones). Mantenimiento de la tabla ARP. ARP proxy. Cableado Estructurado: Selección de dispositivos intermedios. Interconexiones de dispositivos intermedios y fi
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Tipos de ethernet (10base5, 10base2, 10base-t, 100base-tx, 100base-fx, 1000base-t, 1000base-sx, 1000base-lx, la ethernet de 10 gigabits (10gbe)). Utilización de hubs como dispositivo intermedio (pro
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > . Protocolo enlace de datos (HDLC -Control de enlace de datos de alto nivel-, Capa de enlace de datos en Internet -Protocolo PPP (Protocolo Punto a Punto)-). Unidad V: -Capa de enlace de dato -sub cap
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > ; Algoritmos de enrutamiento (Principio de optimización, Enrutamiento por la ruta más corta, Inundación, Enrutamiento por vector de distancia, Enrutamiento por estado del enlace, Enrutamiento jerárqui
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Encabezado IP. División de redes, beneficios de la división de host en redes. Limitaciones de IPv4, Paquetes de IPv6 (Mejoras de IPv6, Encapsulación de IPv6, Encabezado del paquete IPv6, Encabezados

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1207 | salida: 14 | total: 1221

---

### Pregunta 10

> - ¿Cuál es el porcentaje de asistencia a clases que exigen en común las materias de Investigación Operativa, Comunicaciones y Redes, y Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 1]
   > . JEFE DE TRABAJOS PRÁCTICOS: JIMENA SANTA CRUZ; Año de la carrera a la que pertenece la cátedra: 4 Régimen de la materia: Anual Carga horaria semanal: 3 horas Correlativa: Ingeniería del Software I (
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > . La comunicación de los resultados Cronograma de trabajo METODOLOGÍA DE LA INVESTIGACIÓN- 2026 Clase FECHA Tipo de encuentro Tipo encuentro Tema 1 12 de marzo Presencial Teórico/práctico Presentación
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 13]
   > . Argentina. Universidad Nacional de Ǫuilmes. Visto en https://ediciones.ungs.edu.ar/wp-content/uploads/2018/09/9789876301190-completo.pdf Unidad 4: La Dimensión de las técnicas de obtención y análisi
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > . Asimismo, deberá acreditar la aprobación de los dos trabajos prácticos de la cátedra y mantener una asistencia mínima del 80% a los encuentros presenciales.
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > . Alumno Regular - 60 % de asistencia. - Aprobación del examen parcial teórico con una calificación igual o superior a 60 (sesenta) puntos. - Entrega de todos los trabajos en tiempo y forma. - Pertine

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1094 | salida: 14 | total: 1108

---

### Pregunta 11

> - Si quiero promocionar todas las materias de 4to año, ¿cuál es la diferencia de promedio exigido entre Investigación Operativa e Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > . Resolución de problemas de diligencia, asignación de recursos y reemplazo de equipos. Diferencias entre Programación Dinámica Determinística y Probabilística. SISTEMA DE EVALUACIÓN (Investigación Op
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos Capítulo I Agentes Inteligentes Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas por el áre
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > PLANIFICACIÓN INVESTIGACIÓN OPERATIVA Unidad I: -Introducción y Modelos Matemáticos- Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del proble
4. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 7]
   > Régimen Regularidad: Asistencia: Según norma vigente. Todos los trabajos prácticos aprobados. 6/7 parciales aprobados con más del 50% Promoción: Régimen regular Obtener más del 70% en todos los parcia
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > . Las clases teóricas se dictarán de manera conjunta para la totalidad del estudiantado, mientras que las instancias

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1020 | salida: 14 | total: 1034

---

### Pregunta 12

> - ¿Qué herramientas de software se recomiendan en la carrera para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > . La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen reprobado. Software de Aplicación - Investigación Operativa A continuación, se descri
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > . Permite resolver problemas de programación lineal (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al análisis cu
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > . Clasificación de modelos: determinísticos y estocásticos. Definición de variables de decisión, función objetivo y restricciones de sistema y de no negatividad. Unidad II: -Programación Lineal (PL)-
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > . Método MODI (Distribución Modificada) para la optimización de la solución. Problemas de transbordo y el problema de la asignación (Método Húngaro). Unidad V: -Programación Dinámica- Características
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > . Formulación de problemas de optimización. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en los vértices, análisis de casos especiales (soluciones múltiples, so

**Respuesta:**

Las herramientas de software recomendadas para resolver problemas de optimización lineal en la carrera son LINDO, Storm y TORA. 

LINDO se utiliza para resolver problemas de programación lineal (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. 

Storm se enfoca en el análisis cuantitativo y gestión de operaciones, permitiendo el procesamiento de modelos matemáticos y estadísticos. 

TORA es una herramienta educativa diseñada para el aprendizaje de la Investigación Operativa.

Las unidades teóricas relacionadas con estas herramientas son:

*   Unidad II: Programación Lineal (PL)
*   Unidad III: Método SIMPLEX
*   Unidad V: Programación Dinámica

Cada una de estas unidades cubre aspectos teóricos relevantes para la resolución de problemas de optimización lineal, y las herramientas de software mencionadas se utilizan en práctica para aplicar y resolver los modelos teóricos aprendidos.

**Tokens:** entrada: 1101 | salida: 236 | total: 1337

---

### Pregunta 13

> - ¿Dónde puedo descargar la materia de Cálculo de 1er año?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 3]
   > hojas de cálculo.
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > 4- BIBLIOGRAFIA Obligatoria Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] Cisco Systems: Academia de Networking de Cisco Systems: Guía del prime
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 12]
   > . Visto en https://ediciones.ungs.edu.ar/wp-content/uploads/2018/09/9789876301190-completo.pdf Material audiovisual de la unidad Sobre investigación María Teresa Sirven Clase 1 Maestría Tecnología Edu
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > . - 2a ed. - Madrid: Pearson Educación, 2004. ISBN 842053921X [Disponible en Biblioteca FCyT- Oro Verde]
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 1]
   > UNIVERSIDAD AUTÓNOMA DE ENTRE RÍOS FACULTAD DE CIENCIA Y TECNOLOGÍA PROGRAMA DE CÁTEDRA: INFORMÁTICA Y RELACIONES HUMANAS Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectiv

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 985 | salida: 14 | total: 999

---

### Pregunta 14

> - El profesor Ing. Jorge L. Schmukler da clases en Bases de Datos Avanzadas, en Inteligencia Artificial y en Redes y Comunicaciones.

**Chunks de contexto:**

1. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 2]
   > Equipo docente Trossero, Sebastián Teoría Trossero.sebastian@uader.edu.ar Schmuckler, Jorge Práctica Schmukler.jorge@uader.edu.ar
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Direccionamiento estático y dinámico. Planificación del direccionamiento (segmentación de red). Clase de direccionamiento (clase a, b, c, d y e). Prefijo y Mascara de red. Lógica de and. Calculo de
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > : Se propondrán diversas tareas alineadas con los contenidos abordados, las cuales constituirán los componentes del anteproyecto de investigación final. Respecto a las clases: La cátedra implementará
4. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 1]
   > Bases de Datos Avanzadas PRESENTACIÓN DE LA MATERIA Facultad de Ciencia Y Tecnología Base de Datos Avanzadas
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > . El análisis de los datos en la investigación: teorías y procedimientos manuales e informáticos. La comunicación de los resultados. Metodología de trabajo y estrategias pedagógicas: La cátedra aborda

**Respuesta:**

Lo siento, pero no dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 917 | salida: 19 | total: 936

---

### Pregunta 15

> - ¿Cuál es el costo de la certificación oficial de Cisco que se menciona como opcional en la planificación?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > 4- BIBLIOGRAFIA Obligatoria Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] Cisco Systems: Academia de Networking de Cisco Systems: Guía del prime
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 5]
   > Sitios web sobre normativas, tecnologías y soluciones, opcional: IETF -> www.ietf.org IEEE -> www.ieee.org ISO -> www.iso.org CISCO -> www.cisco.com IANA -> www.iana.org ISOC -> www.isoc.org ARIN -> w
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 5]
   > LACNIC -> http://lacnic.net/sp/ LAC IPV6 TF -> www.lac.ipv6tf.org 3M -> www.3m.com FURUKAWA -> www.furukawa.com.br/internacional.html UNDERWRITERS LABORATORIES (UL) -> www.ul.com PANDUIT -> www.pandui
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > . Por ello, los materiales teóricos y las lecturas obligatorias se compartirán con una semana de antelación al encuentro presencial
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > Plan de Cátedra de la Carrera Licenciado en Sistemas de Información de la Facultad de Ciencia y Tecnología de la UADER SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE:

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1137 | salida: 14 | total: 1151

---

### Pregunta 16

> - Para la Promoción Directa, se exige la aprobación de la totalidad de los trabajos prácticos (TP 1 al TP 5). ¿Cuál es la calificación numérica mínima que debe obtenerse en cada TP individual para que se considere aprobado?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 16]
   > 16 Para acceder a la condición de Promoción Directa, el/la estudiante deberá cumplir con los siguientes requisitos: - 80 % de asistencia a la cursada. - Aprobación del examen parcial teórico con una c
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > . Resolución de problemas de diligencia, asignación de recursos y reemplazo de equipos. Diferencias entre Programación Dinámica Determinística y Probabilística. SISTEMA DE EVALUACIÓN (Investigación Op
3. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 7]
   > Régimen Regularidad: Asistencia: Según norma vigente. Todos los trabajos prácticos aprobados. 6/7 parciales aprobados con más del 50% Promoción: Régimen regular Obtener más del 70% en todos los parcia
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 3]
   > 2- SISTEMA DE EVALUACION Condición del Alumno: PROMOCIONADO REGULAR LIBRE El alumno accederá a la condición de PROMOCIÓN si cumple con las siguientes condiciones de cátedra: 1 - Obtener en los 3 parc
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 9]
   > 9 Programa de trabajos prácticos: Tp 1: Escritura académica. Se solicita a los estudiantes seleccionar un artículo de investigación sobre un tema de interés específico relacionado al campo profesional

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1150 | salida: 14 | total: 1164

---

### Pregunta 17

> - ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > . Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible vía URL que permite resolver prob
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > . Formulación de problemas de optimización. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en los vértices, análisis de casos especiales (soluciones múltiples, so
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > . Clasificación de modelos: determinísticos y estocásticos. Definición de variables de decisión, función objetivo y restricciones de sistema y de no negatividad. Unidad II: -Programación Lineal (PL)-
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Clasificación de las RNA. Agentes basados en Proceso de Aprendizaje Red Perceptron Simple. Elemento de Procesamiento. Función de Transferencia. Condiciones de Convergencia. Proceso de E
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > . Método MODI (Distribución Modificada) para la optimización de la solución. Problemas de transbordo y el problema de la asignación (Método Húngaro). Unidad V: -Programación Dinámica- Características

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1046 | salida: 14 | total: 1060

---

### Pregunta 18

> - ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > 5 09 de abril Presencial Teoría Tema/ problema 6 16 de abril Virtual Práctica 7 23 de abril Virtual Teoría Pregunta de investigación (variables, unidad de análisis, contexto)/ Antecedentes 8 30 de abr
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > . Por ello, los materiales teóricos y las lecturas obligatorias se compartirán con una semana de antelación al encuentro presencial
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > 19 12 28 de mayo Virtual Teoría 13 04 de junio Presencial Teoría Marco metodológico I: enfoque y tipo de investigación / muestra 14 11 de junio Virtual Práctica 15 18 de junio Virtual Teoría Marco met
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > . Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mismo examen parcial. La calificación obtenida en la instancia de
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > . La comunicación de los resultados Cronograma de trabajo METODOLOGÍA DE LA INVESTIGACIÓN- 2026 Clase FECHA Tipo de encuentro Tipo encuentro Tema 1 12 de marzo Presencial Teórico/práctico Presentación

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1118 | salida: 14 | total: 1132

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
   > Inteligencia Artificial Programa de Contenidos Capítulo I Agentes Inteligentes Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas por el áre
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (200
3. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 5]
   > Programa Sintético Unidad I: Bases de Datos Activas Unidad II: Bases de Datos Temporales Unidad III: Bases de Datos Geográficas Unidad IV: Bases de Datos Distribuidas Unidad V: Datawarehouse Unidad VI
4. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 1]
   > Bases de Datos Avanzadas PRESENTACIÓN DE LA MATERIA Facultad de Ciencia Y Tecnología Base de Datos Avanzadas
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 1]
   > . Además, se abordarán aspectos legales fundamentales para comprender el impacto normativo de las TIC en el ámbito laboral, tomando como base la legislación argentina y los aportes de autores nacional
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > problema de saturación prematura. Regiones de Decisión. Modo de operación autoasociativo. Capítulo X Generalización en las RNA, definición, factores que influyen en la capacidad de Generalización
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > 6 estudiantes los materiales y herramientas necesarios para la construcción autónoma del conocimiento. - Cada clase incluirá uno o más de los siguientes recursos: - Un video explicativo. - Material de
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > Protocolo libre de colisiones, Protocolo de LAN Inalámbricas), Ethernet, concepto sobre el Algoritmo de retroceso exponencial binario, LAN Inalámbricas IEEE 802.11, Banda Ancha Inalámbrica IEEE 802.16

**Respuesta:**

La materia Inteligencia Artificial abarca varios temas específicos que se describen en el capítulo correspondiente. Entre los temas que se desarrollan en esta materia se incluye la introducción a los agentes inteligentes, la descripción de los entornos de trabajo y la estructura de los agentes.

Además, la materia aborda conceptos como la saturación prematura, las regiones de decisión, el modo de operación autoasociativo, la generalización en las redes neuronales y las redes autoorganizadas.

Los autores recomendados para profundizar en la materia son Stuart J. Rusell y Peter Norvig, en su libro "Inteligencia Artificial - Un Enfoque Moderno", así como también se recomienda el libro de S. Raschka y V. Mirjalili, titulado "Aprendizaje automático y aprendizaje profundo con Python, scikit-learn y Tensor Flow".

**Tokens:** entrada: 1500 | salida: 201 | total: 1701

---

### Pregunta 2

> - ¿En qué materia se enseña el concepto de Lógica Difusa?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Estructura de Control: Procedimientos de Inferencia; Interfase con el usuario. Memoria de Trabajo, Módulo generador de explicaciones al usuario. Capítulo V Funcionalidad de los Sistemas Expertos Proc
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > . Las clases teóricas se dictarán de manera conjunta para la totalidad del estudiantado, mientras que las instancias
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 15]
   > . 2019 Deep Learning aplicado al aprendizaje automático de ontologías para la representación del conocimiento a partir de texto no estructurado / Enzo Javier Andreetto; director Alejandro Javier Hadad
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 16]
   > : la primera correspondiente a la dimensión epistemológica y la segunda integrando las dimensiones epistemológica, estratégica y técnica.
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Clasificación de las RNA. Agentes basados en Proceso de Aprendizaje Red Perceptron Simple. Elemento de Procesamiento. Función de Transferencia. Condiciones de Convergencia. Proceso de E
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > . La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen reprobado. Software de Aplicación - Investigación Operativa A continuación, se descri
7. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 1]
   > . FUNDAMENTACIÓN El avance de las tecnologías de la información y la comunicación (TIC) ha transformado la dinámica del mundo laboral y las relaciones humanas dentro de las organizaciones. Esta asigna
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 5]
   > Lic. Luciano M. CAISSO.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1246 | salida: 14 | total: 1260

---

### Pregunta 3

> - ¿Cuál es el plan de estudios de Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > . La comunicación de los resultados Cronograma de trabajo METODOLOGÍA DE LA INVESTIGACIÓN- 2026 Clase FECHA Tipo de encuentro Tipo encuentro Tema 1 12 de marzo Presencial Teórico/práctico Presentación
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 1]
   > . JEFE DE TRABAJOS PRÁCTICOS: JIMENA SANTA CRUZ; Año de la carrera a la que pertenece la cátedra: 4 Régimen de la materia: Anual Carga horaria semanal: 3 horas Correlativa: Ingeniería del Software I (
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > PLANIFICACIÓN INVESTIGACIÓN OPERATIVA Unidad I: -Introducción y Modelos Matemáticos- Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del proble
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 1]
   > . Yuni y Urbano (2016) sostiene que como la epistemología, la metodología de la investigación es una disciplina meta teórica porque toma como objeto de estudio a la ciencia. En este sentido los autore
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > . La calificación del trabajo integrador se determinará exclusivamente en la mesa de examen, junto con la nota correspondiente a la instancia teórica, estableciéndose en ese momento la calificación fi
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 1]
   > . No obstante, se considera necesario, antes de recibir el título de Licenciado/a en Sistemas de Información, que el/la estudiante cuente con herramientas conceptuales y prácticas para encarar los des
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 12]
   > : https://youtu.be/eHjUqHcVBA4 -> BÚSǪUEDA AVANZADA GOOGLE - BÚSǪUEDA GOOGLE AVANZADA - 3RA PARTE APRENDER A INVESTIGAR: https://youtu.be/NJby_1x178I -> BÚSǪUEDA AVANZADA GOOGLE - BÚSǪUEDA GOOGLE AVAN
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 5]
   > Estructura del aula virtual: Los materiales educativos estarán alojados en el aula virtual "Metodología de la Investigación" dentro de la plataforma Moodle

**Respuesta:**

El plan de estudios de Metodología de la Investigación está dividido en cuatro unidades:

* Unidad 1: Introducción a la ciencia y conocimiento científico
* Unidad 2: La dimensión epistemológica
* Unidad 3: La dimensión de la estrategia general de investigación
* Unidad 4: (sin detalles específicos)

Además, se menciona que se considera necesario que los estudiantes cuenten con herramientas conceptuales y prácticas para encarar los desafíos de la investigación científica y el ejercicio de la profesión.

**Tokens:** entrada: 1508 | salida: 135 | total: 1643

---

### Pregunta 4

> - En Comunicaciones y Redes, ¿cómo hago para quedar como alumno regular?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 3]
   > El alumno accederá a la condición de REGULAR, si cumple con las siguientes condiciones de cátedra: 1 - Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 15]
   > . Guillerón. 2018 Red Privada Virtual (VPM) sobre Protocolo de Internet versión 6 (IPv6) / Rodrigo Paúl Basso, Maximiliano Sebastián Toso; director Julio Alberto Aldonate; codirector Luciano María Cai
3. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 8]
   > Comunicación De rutina y consultas: Lista de mail. Material académico: aula virtual - Clave de matriculación bda2023 *Único medio oficial. Avisos y notificaciones: Grupo de Telegram https://t.me/+c7PP
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > Plan de Cátedra de la Carrera Licenciado en Sistemas de Información de la Facultad de Ciencia y Tecnología de la UADER SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE:
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > 1- PROGRAMA DE CONTENIDOS Unidad I: Introducción -Importancia e Influencia de las Redes en Nuestras Vidas: Comunicación en un mundo centrado en la red, herramientas de comunicación. La comunicación (d
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > . Por ello, los materiales teóricos y las lecturas obligatorias se compartirán con una semana de antelación al encuentro presencial
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Direccionamiento estático y dinámico. Planificación del direccionamiento (segmentación de red). Clase de direccionamiento (clase a, b, c, d y e). Prefijo y Mascara de red. Lógica de and. Calculo de
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > Esta metodología busca facilitar el acceso a los contenidos para aquellos estudiantes que no pueden asistir a todas las clases y, al mismo tiempo, reducir la tasa de abandono

**Respuesta:**

Para quedar como alumno regular en Comunicaciones y Redes, debes obtener en los tres parciales una calificación promedio superior o igual a los 60 puntos.

**Tokens:** entrada: 1273 | salida: 38 | total: 1311

---

### Pregunta 5

> - ¿Qué instancias de recuperación nos provee Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > PLANIFICACIÓN INVESTIGACIÓN OPERATIVA Unidad I: -Introducción y Modelos Matemáticos- Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del proble
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > . La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen reprobado. Software de Aplicación - Investigación Operativa A continuación, se descri
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 20]
   > 20 12 de noviembr e Espacio de recuperación y cierre
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 3]
   > 3 Objetivos generales: - Acercar al campo de la investigación científica desde espacios de reflexión sistemáticos enmarcados en trabajos propios de la disciplina y el campo profesional. Objetivos espe
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > . Es requisito indispensable la entrega y aprobación de los dos trabajos prácticos obligatorios y el cumplimiento del 80% de asistencia a las clases teóricas y prácticas. - ALUMNO LIBRE: Revestirá est
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 12]
   > -> Paula Espeche Trayecto 2 Google académico y operadores booleanos: https://youtu.be/fiSJ4bDb Nwrc -> BÚSǪUEDA AVANZADA con GOOGLE - PRIMERA PARTE - APRENDER A INVESTIGAR: https://youtu.be/9oWM50RDsL
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 1]
   > 2026 - FCYT-ORO VERDE - Licenciatura en Sistemas de Información - Metodología de la Investigación Carrera: Licenciatura en Sistemas de Información Cátedra: Metodología de la Investigación Año Académic
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > 03 de septiembr e Presencial Tutorías Sugerecia entrevista a expertos en el tema/ recuperatorio parcial teoría 10 de septiembr e Virtual Tutorías Avances proyectos a la cátedra-Grupos Tamara 17 de s

**Respuesta:**

La cátedra de Investigación Operativa dispone de dos oportunidades de recuperatorio totales.

**Tokens:** entrada: 1373 | salida: 22 | total: 1395

---

### Pregunta 6

> - ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > . Permite resolver problemas de programación lineal (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al análisis cu
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > . La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen reprobado. Software de Aplicación - Investigación Operativa A continuación, se descri
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > 3- PROGRAMA DE TRABAJOS PRACTICOS La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos vertidos en la teoría. Más dos trabajos
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > 4- BIBLIOGRAFIA Obligatoria Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] Cisco Systems: Academia de Networking de Cisco Systems: Guía del prime
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 1]
   > integrando conceptos de informática, gestión organizacional y derecho informático. Los estudiantes explorarán los efectos de las nuevas tecnologías en el trabajo, la calidad de vida laboral y la admin
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 12]
   > . Visto en https://ediciones.ungs.edu.ar/wp-content/uploads/2018/09/9789876301190-completo.pdf Material audiovisual de la unidad Sobre investigación María Teresa Sirven Clase 1 Maestría Tecnología Edu
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > . Por ello, los materiales teóricos y las lecturas obligatorias se compartirán con una semana de antelación al encuentro presencial
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 15]
   > . 2019 Deep Learning aplicado al aprendizaje automático de ontologías para la representación del conocimiento a partir de texto no estructurado / Enzo Javier Andreetto; director Alejandro Javier Hadad

**Respuesta:**

El software TORA es una herramienta educativa diseñada específicamente para el aprendizaje de la Investigación Operativa.

**Tokens:** entrada: 1440 | salida: 27 | total: 1467

---

### Pregunta 7

> - ¿Qué profesor forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > Plan de Cátedra de la Carrera Licenciado en Sistemas de Información de la Facultad de Ciencia y Tecnología de la UADER SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE:
2. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 1]
   > Bases de Datos Avanzadas PRESENTACIÓN DE LA MATERIA Facultad de Ciencia Y Tecnología Base de Datos Avanzadas
3. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 2]
   > Equipo docente Trossero, Sebastián Teoría Trossero.sebastian@uader.edu.ar Schmuckler, Jorge Práctica Schmukler.jorge@uader.edu.ar
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > . En estos encuentros virtuales, se trabajarán tanto los fundamentos teóricos de la metodología de la investigación y la escritura académica como aspectos prácticos para avanzar en la elaboración del
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > . Halsall. - 5a ed. - Madrid: Pearson Educación, 2006. ISBN 9788478290833 [Disponible en Biblioteca FCyT- Oro Verde] Huidobro Moya, José Manuel: Redes de datos y convergencia IP / J. M. Huidobro Moya,
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 15]
   > 15 Sistemas de detección de intrusos para mejorar la seguridad de la FCyT / Emiliano Teodoro Herber, Luciano Nahuel Zapata; director Julio Aldonate. 2020 Medidas de seguridad para la información en te
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 14]
   > . 2022 Modelos vectoriales y redes neuronales artificiales, para la aplicación de procesamiento de lenguaje natural en normativas jurídicas / Julián Lanfranco; director Alejandro Javier Hadad
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 14]
   > . 2021 Diseño de una base de datos espacio-temporal para la modelización hidrológica y geomorfológica de la cuenca del río Paraná, Entre Ríos / Lucas Leonel Barreto López, Juan Cruz Mantovani; directo

**Respuesta:**

El profesor Jorge Schmukler forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes.

**Tokens:** entrada: 1437 | salida: 38 | total: 1475

---

### Pregunta 8

> - ¿Qué otra asignatura, además de la propia materia de Inteligencia Artificial, incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos Capítulo I Agentes Inteligentes Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas por el áre
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 1]
   > integrando conceptos de informática, gestión organizacional y derecho informático. Los estudiantes explorarán los efectos de las nuevas tecnologías en el trabajo, la calidad de vida laboral y la admin
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 3]
   > Bibliografía Complementaria: Reglamento de Teletrabajo en Argentina. Legislación sobre delitos informáticos en Argentina. Artículos académicos sobre la transformación del trabajo y el impacto de la IA
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > : Se propondrán diversas tareas alineadas con los contenidos abordados, las cuales constituirán los componentes del anteproyecto de investigación final. Respecto a las clases: La cátedra implementará
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > 5 09 de abril Presencial Teoría Tema/ problema 6 16 de abril Virtual Práctica 7 23 de abril Virtual Teoría Pregunta de investigación (variables, unidad de análisis, contexto)/ Antecedentes 8 30 de abr
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (200
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 3]
   > . Los sistemas de información como objeto de estudio. Escritura académica. Normas de citación. Unidad 2: La dimensión epistemológica ¿Cómo encauzar la definición del tema de investigación? Lectura de
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > comportamiento del sistema. Proceso de Inferencia. Tratamiento paralelo de las reglas. Determinación del aporte parcial de cada regla. Integración de la solución difusa final. Proceso de D

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1530 | salida: 14 | total: 1544

---

### Pregunta 9

> - Los requisitos para regularizar en Bases de Datos Avanzadas y en Redes y Comunicaciones, ¿son iguales? ¿Qué diferencias tienen?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . ARP (protocolo de resolución de direcciones). Mantenimiento de la tabla ARP. ARP proxy. Cableado Estructurado: Selección de dispositivos intermedios. Interconexiones de dispositivos intermedios y fi
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 3]
   > . Tato, El Derecho Informático - Aspectos Fundamentales. Mariana Nazar, Tecnologías, información y derechos. Gonzalo Ana Dobratinich, derecho y nuevas tecnologías. Ley Nacional de Protección de Datos
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > . Halsall. - 5a ed. - Madrid: Pearson Educación, 2006. ISBN 9788478290833 [Disponible en Biblioteca FCyT- Oro Verde] Huidobro Moya, José Manuel: Redes de datos y convergencia IP / J. M. Huidobro Moya,
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 14]
   > . 2022 Modelos vectoriales y redes neuronales artificiales, para la aplicación de procesamiento de lenguaje natural en normativas jurídicas / Julián Lanfranco; director Alejandro Javier Hadad
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 5]
   > Programa Sintético Unidad I: Bases de Datos Activas Unidad II: Bases de Datos Temporales Unidad III: Bases de Datos Geográficas Unidad IV: Bases de Datos Distribuidas Unidad V: Datawarehouse Unidad VI
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > problema de saturación prematura. Regiones de Decisión. Modo de operación autoasociativo. Capítulo X Generalización en las RNA, definición, factores que influyen en la capacidad de Generalización
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 14]
   > . 2023 Caracterización de usuarios conforme a datos recolectados del proceso de user experience: caso de estudio: sistemas web del Ministerio de Salud de la provincia de Entre Ríos / Wilfredo Ariel Be
8. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 7]
   > Régimen Regularidad: Asistencia: Según norma vigente. Todos los trabajos prácticos aprobados. 6/7 parciales aprobados con más del 50% Promoción: Régimen regular Obtener más del 70% en todos los parcia

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1493 | salida: 14 | total: 1507

---

### Pregunta 10

> - ¿Cuál es el porcentaje de asistencia a clases que exigen en común las materias de Investigación Operativa, Comunicaciones y Redes, y Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 1]
   > . JEFE DE TRABAJOS PRÁCTICOS: JIMENA SANTA CRUZ; Año de la carrera a la que pertenece la cátedra: 4 Régimen de la materia: Anual Carga horaria semanal: 3 horas Correlativa: Ingeniería del Software I (
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > . La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen reprobado. Software de Aplicación - Investigación Operativa A continuación, se descri
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > . Por ello, los materiales teóricos y las lecturas obligatorias se compartirán con una semana de antelación al encuentro presencial
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > Esta metodología busca facilitar el acceso a los contenidos para aquellos estudiantes que no pueden asistir a todas las clases y, al mismo tiempo, reducir la tasa de abandono
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 8]
   > 8 - Articulación con la cátedra Tesina de Grado: se organizarán encuentros conjuntos en los que los estudiantes presentarán los avances de sus proyectos, promoviendo un trabajo coordinado entre Metodo
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > . Resolución de problemas de diligencia, asignación de recursos y reemplazo de equipos. Diferencias entre Programación Dinámica Determinística y Probabilística. SISTEMA DE EVALUACIÓN (Investigación Op
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > 1- PROGRAMA DE CONTENIDOS Unidad I: Introducción -Importancia e Influencia de las Redes en Nuestras Vidas: Comunicación en un mundo centrado en la red, herramientas de comunicación. La comunicación (d
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > - 60 % de los cuestionarios de autoevaluación respondidos. - Presentación y defensa oral del trabajo práctico integrador en la mesa de examen final, previa instancia de revisión y devolución con el eq

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1261 | salida: 14 | total: 1275

---

### Pregunta 11

> - Si quiero promocionar todas las materias de 4to año, ¿cuál es la diferencia de promedio exigido entre Investigación Operativa e Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > . Resolución de problemas de diligencia, asignación de recursos y reemplazo de equipos. Diferencias entre Programación Dinámica Determinística y Probabilística. SISTEMA DE EVALUACIÓN (Investigación Op
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos Capítulo I Agentes Inteligentes Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas por el áre
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > . Las clases teóricas se dictarán de manera conjunta para la totalidad del estudiantado, mientras que las instancias
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 1]
   > . No obstante, se considera necesario, antes de recibir el título de Licenciado/a en Sistemas de Información, que el/la estudiante cuente con herramientas conceptuales y prácticas para encarar los des
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > . El objetivo principal será la elaboración de un Anteproyecto de Investigación, el cual podrá retomarse en el espacio curricular de Tesina de Grado. Dado que se trata de una asignatura de cuarto año,
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > . Permite resolver problemas de programación lineal (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al análisis cu
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > Plan de Cátedra de la Carrera Licenciado en Sistemas de Información de la Facultad de Ciencia y Tecnología de la UADER SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE:
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 12]
   > : https://youtu.be/eHjUqHcVBA4 -> BÚSǪUEDA AVANZADA GOOGLE - BÚSǪUEDA GOOGLE AVANZADA - 3RA PARTE APRENDER A INVESTIGAR: https://youtu.be/NJby_1x178I -> BÚSǪUEDA AVANZADA GOOGLE - BÚSǪUEDA GOOGLE AVAN

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1640 | salida: 14 | total: 1654

---

### Pregunta 12

> - ¿Qué herramientas de software se recomiendan en la carrera para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > . La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen reprobado. Software de Aplicación - Investigación Operativa A continuación, se descri
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > . Permite resolver problemas de programación lineal (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm: Software orientado al análisis cu
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > . Clasificación de modelos: determinísticos y estocásticos. Definición de variables de decisión, función objetivo y restricciones de sistema y de no negatividad. Unidad II: -Programación Lineal (PL)-
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > . Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible vía URL que permite resolver prob
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 7]
   > 7 Durante los encuentros sincrónicos orientados a la práctica, se trabajará bajo modalidad de taller, con instancias de escritura guiada, revisión de avances y discusión de decisiones metodológicas, f
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 5]
   > LACNIC -> http://lacnic.net/sp/ LAC IPV6 TF -> www.lac.ipv6tf.org 3M -> www.3m.com FURUKAWA -> www.furukawa.com.br/internacional.html UNDERWRITERS LABORATORIES (UL) -> www.ul.com PANDUIT -> www.pandui
7. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 1]
   > UNIVERSIDAD AUTÓNOMA DE ENTRE RÍOS FACULTAD DE CIENCIA Y TECNOLOGÍA PROGRAMA DE CÁTEDRA: INFORMÁTICA Y RELACIONES HUMANAS Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectiv
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 3]
   > hojas de cálculo.

**Respuesta:**

Se recomiendan las herramientas LINDO y PHP Simplex para resolver problemas de optimización lineal. 

LINDO (Linear, Interactive, and Discrete Optimizer) se destaca por su capacidad para resolver problemas de programación lineal, entera y no lineal. 

PHP Simplex es una herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el Método Simplex y el Método Gráfico.

La unidad II del programa, llamada Programación Lineal (PL), se enfoca en las propiedades de los modelos de Programación Lineal, lo cual es relevante para el uso de estas herramientas de software.

**Tokens:** entrada: 1381 | salida: 142 | total: 1523

---

### Pregunta 13

> - ¿Dónde puedo descargar la materia de Cálculo de 1er año?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 3]
   > hojas de cálculo.
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > 4- BIBLIOGRAFIA Obligatoria Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] Cisco Systems: Academia de Networking de Cisco Systems: Guía del prime
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 12]
   > . Visto en https://ediciones.ungs.edu.ar/wp-content/uploads/2018/09/9789876301190-completo.pdf Material audiovisual de la unidad Sobre investigación María Teresa Sirven Clase 1 Maestría Tecnología Edu
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 1]
   > . JEFE DE TRABAJOS PRÁCTICOS: JIMENA SANTA CRUZ; Año de la carrera a la que pertenece la cátedra: 4 Régimen de la materia: Anual Carga horaria semanal: 3 horas Correlativa: Ingeniería del Software I (
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 12]
   > 12 - Natale, Lucía (Coordinadora) (2013). En carrera: escritura y lectura de textos académicos y profesionales. Argentina. Universidad Nacional de Ǫuilmes
6. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 8]
   > Comunicación De rutina y consultas: Lista de mail. Material académico: aula virtual - Clave de matriculación bda2023 *Único medio oficial. Avisos y notificaciones: Grupo de Telegram https://t.me/+c7PP
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > 1- PROGRAMA DE CONTENIDOS Unidad I: Introducción -Importancia e Influencia de las Redes en Nuestras Vidas: Comunicación en un mundo centrado en la red, herramientas de comunicación. La comunicación (d
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > . Formulación de problemas de optimización. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en los vértices, análisis de casos especiales (soluciones múltiples, so

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1320 | salida: 14 | total: 1334

---

### Pregunta 14

> - El profesor Ing. Jorge L. Schmukler da clases en Bases de Datos Avanzadas, en Inteligencia Artificial y en Redes y Comunicaciones.

**Chunks de contexto:**

1. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 2]
   > Equipo docente Trossero, Sebastián Teoría Trossero.sebastian@uader.edu.ar Schmuckler, Jorge Práctica Schmukler.jorge@uader.edu.ar
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Direccionamiento estático y dinámico. Planificación del direccionamiento (segmentación de red). Clase de direccionamiento (clase a, b, c, d y e). Prefijo y Mascara de red. Lógica de and. Calculo de
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > : Se propondrán diversas tareas alineadas con los contenidos abordados, las cuales constituirán los componentes del anteproyecto de investigación final. Respecto a las clases: La cátedra implementará
4. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 1]
   > Bases de Datos Avanzadas PRESENTACIÓN DE LA MATERIA Facultad de Ciencia Y Tecnología Base de Datos Avanzadas
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos Capítulo I Agentes Inteligentes Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas por el áre
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > Plan de Cátedra de la Carrera Licenciado en Sistemas de Información de la Facultad de Ciencia y Tecnología de la UADER SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE:
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (200
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 15]
   > . 2019 Deep Learning aplicado al aprendizaje automático de ontologías para la representación del conocimiento a partir de texto no estructurado / Enzo Javier Andreetto; director Alejandro Javier Hadad

**Respuesta:**

Lo siento, pero la afirmación de que el profesor Ing. Jorge L. Schmukler da clases en Bases de Datos Avanzadas no está respaldada en el Contexto proporcionado.

**Tokens:** entrada: 1463 | salida: 45 | total: 1508

---

### Pregunta 15

> - ¿Cuál es el costo de la certificación oficial de Cisco que se menciona como opcional en la planificación?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > 4- BIBLIOGRAFIA Obligatoria Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] Cisco Systems: Academia de Networking de Cisco Systems: Guía del prime
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 5]
   > LACNIC -> http://lacnic.net/sp/ LAC IPV6 TF -> www.lac.ipv6tf.org 3M -> www.3m.com FURUKAWA -> www.furukawa.com.br/internacional.html UNDERWRITERS LABORATORIES (UL) -> www.ul.com PANDUIT -> www.pandui
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > . Por ello, los materiales teóricos y las lecturas obligatorias se compartirán con una semana de antelación al encuentro presencial
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > . La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen reprobado. Software de Aplicación - Investigación Operativa A continuación, se descri
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > : -Capa de enlace de dato -sub capa LLC (control de enlace lógico)- Cuestiones en el diseño de la capa de enlace de dato, servicios proporcionados por la capa de red, entramado, control de errores (Có
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 15]
   > . 2019 Estrategia para planear una migración de software propietario a software libre para la Facultad de Ciencia y Tecnología (FCyT) Sede Oro Verde en el año 2018 / Emanuel Antonio Wasinger; director
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > . Explicar el propósito de IOS como Sistema Operativo de red, Explicar cómo acceder al IOS y cómo explorarlo para configurar los dispositivos de red, Describir la estructura de comandos, Configurar no
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 3]
   > 2- SISTEMA DE EVALUACION Condición del Alumno: PROMOCIONADO REGULAR LIBRE El alumno accederá a la condición de PROMOCIÓN si cumple con las siguientes condiciones de cátedra: 1 - Obtener en los 3 parc

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1534 | salida: 14 | total: 1548

---

### Pregunta 16

> - Para la Promoción Directa, se exige la aprobación de la totalidad de los trabajos prácticos (TP 1 al TP 5). ¿Cuál es la calificación numérica mínima que debe obtenerse en cada TP individual para que se considere aprobado?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 16]
   > 16 Para acceder a la condición de Promoción Directa, el/la estudiante deberá cumplir con los siguientes requisitos: - 80 % de asistencia a la cursada. - Aprobación del examen parcial teórico con una c
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > . Resolución de problemas de diligencia, asignación de recursos y reemplazo de equipos. Diferencias entre Programación Dinámica Determinística y Probabilística. SISTEMA DE EVALUACIÓN (Investigación Op
3. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 7]
   > Régimen Regularidad: Asistencia: Según norma vigente. Todos los trabajos prácticos aprobados. 6/7 parciales aprobados con más del 50% Promoción: Régimen regular Obtener más del 70% en todos los parcia
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 9]
   > 9 Programa de trabajos prácticos: Tp 1: Escritura académica. Se solicita a los estudiantes seleccionar un artículo de investigación sobre un tema de interés específico relacionado al campo profesional
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > . El trabajo deberá entregarse con una antelación mínima de diez (10) días hábiles respecto de la fecha de la mesa; en caso contrario, su evaluación se trasladará al turno siguiente. El trabajo prácti
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 9]
   > . Posibles modos de comunicación de resultados. Tp integrador: Presentación formal escrita y oral de todas las partes realizadas en los trabajos anteriores con las sugerencias corregidas y presentació
7. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 6]
   > Evaluaciones (tentativo) Unidad I: Bases de Datos Activas Parcial + TP Unidad II: Bases de Datos Temporales Parcial Unidad III: Bases de Datos Geográficas Parcial + TP Unidad IV: Bases de Datos Distri
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 15]
   > . Guillerón. 2018 Red Privada Virtual (VPM) sobre Protocolo de Internet versión 6 (IPv6) / Rodrigo Paúl Basso, Maximiliano Sebastián Toso; director Julio Alberto Aldonate; codirector Luciano María Cai

**Respuesta:**

Lo siento, pero no dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1455 | salida: 19 | total: 1474

---

### Pregunta 17

> - ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > . Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible vía URL que permite resolver prob
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > . Formulación de problemas de optimización. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en los vértices, análisis de casos especiales (soluciones múltiples, so
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Clasificación de las RNA. Agentes basados en Proceso de Aprendizaje Red Perceptron Simple. Elemento de Procesamiento. Función de Transferencia. Condiciones de Convergencia. Proceso de E
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > . La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen reprobado. Software de Aplicación - Investigación Operativa A continuación, se descri
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 3]
   > hojas de cálculo.
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > . Resolución de problemas de diligencia, asignación de recursos y reemplazo de equipos. Diferencias entre Programación Dinámica Determinística y Probabilística. SISTEMA DE EVALUACIÓN (Investigación Op
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 7]
   > 7 Durante los encuentros sincrónicos orientados a la práctica, se trabajará bajo modalidad de taller, con instancias de escritura guiada, revisión de avances y discusión de decisiones metodológicas, f
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > . Es reconocido por su sintaxis sencilla para ingresar ecuaciones y restricciones de manera directa. - WinQSB 2.0: Una suite clásica (dividida en 3 partes) que abarca múltiples módulos de Investigació

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1319 | salida: 14 | total: 1333

---

### Pregunta 18

> - ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > 5 09 de abril Presencial Teoría Tema/ problema 6 16 de abril Virtual Práctica 7 23 de abril Virtual Teoría Pregunta de investigación (variables, unidad de análisis, contexto)/ Antecedentes 8 30 de abr
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > . Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mismo examen parcial. La calificación obtenida en la instancia de
3. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 4]
   > Cronograma de clases Presenciales/Virtuales A partir de este año la materia será dictada de manera bimodal. El cronograma será definido en su mayoría por la Facultad. Aún no confirmado. Los links de c
4. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 6]
   > Evaluaciones (tentativo) Unidad I: Bases de Datos Activas Parcial + TP Unidad II: Bases de Datos Temporales Parcial Unidad III: Bases de Datos Geográficas Parcial + TP Unidad IV: Bases de Datos Distri
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > . El trabajo deberá entregarse con una antelación mínima de diez (10) días hábiles respecto de la fecha de la mesa; en caso contrario, su evaluación se trasladará al turno siguiente. El trabajo prácti
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > . Las clases teóricas se dictarán de manera conjunta para la totalidad del estudiantado, mientras que las instancias
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > . Resolución de problemas de diligencia, asignación de recursos y reemplazo de equipos. Diferencias entre Programación Dinámica Determinística y Probabilística. SISTEMA DE EVALUACIÓN (Investigación Op
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > . La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen reprobado. Software de Aplicación - Investigación Operativa A continuación, se descri

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1417 | salida: 14 | total: 1431

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
   > Inteligencia Artificial Programa de Contenidos Capítulo I Agentes Inteligentes Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas por el áre
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > a desarrollarse en la asignatura. Introducción a los agentes inteligentes. Entorno de Trabajo. Propiedades de los entornos. Estructura de los Agentes. Programas de Agentes. Age
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > del sistema. Agentes Basados en Lógica Difusa. Capítulo VIII Redes Neuronales Artificiales (RNA). Generalidades, conceptos básicos Reseña Histórica. Clasificación de las RNA. Agentes basados
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 2]
   > . Protección de datos personales y privacidad en el ámbito laboral. 2. Legislación sobre contratos de trabajo en plataformas digitales. 3. Responsabilidad legal de las empresas en el uso de IA y algor
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (200

**Respuesta:**

El Programa de Contenidos de la materia Inteligencia Artificial incluye los temas: Introducción a la Inteligencia Artificial (IA), Definiciones y objetivos, Herramientas y técnicas provistas por el área IA, Descripción de los temas específicos a desarrollarse en la asignatura, Introducción a los agentes inteligentes, Entorno de Trabajo, Propiedades de los entornos, Estructura de los Agentes, Programas de Agentes, Agentes Reactivo Simple, Agentes Reactivos basados en Modelos, Agente basado en objetivos, Agentes Basados en Lógica Difusa y Capítulo VIII Redes Neuronales Artificiales (RNA), Generalidades, conceptos básicos Reseña Histórica, Clasificación de las RNA y Agentes basados en Proceso de Aprendizaje.

**Tokens:** entrada: 944 | salida: 190 | total: 1134

---

### Pregunta 2

> - ¿En qué materia se enseña el concepto de Lógica Difusa?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > (Fordward Chaining) y Encadenamiento hacia atrás (Backward Chaining). Herramientas para el desarrollo de Sistemas Expertos. Capítulo VI Lógica Difusa (Fuzzy). Consideraciones generales, Conju
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > cada regla. Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación de los distintos métodos
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > del sistema. Agentes Basados en Lógica Difusa. Capítulo VIII Redes Neuronales Artificiales (RNA). Generalidades, conceptos básicos Reseña Histórica. Clasificación de las RNA. Agentes basados
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > conjuntos Difusos: Inclusión, Igualdad, Complementación, Intersección, Unión. Estructuras FAM (Fuzzy Associative Memories). Composición MAX-MIN. Capítulo VII Sistemas Difusos. Considerac
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > mediante reglas lingüísticas. Proceso de Fuzzificación. Influencia de la forma y distribución de los Conjuntos Difusos, en el comportamiento del sistema. Proceso de Inferencia. Tratamiento para

**Respuesta:**

La Lógica Difusa se enseña en el capítulo VI del programa de cátedra de IA.

**Tokens:** entrada: 984 | salida: 25 | total: 1009

---

### Pregunta 3

> - ¿Cuál es el plan de estudios de Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 1]
   > ; Año de la carrera a la que pertenece la cátedra: 4 Régimen de la materia: Anual Carga horaria semanal: 3 horas Correlativa: Ingeniería del Software I (208) - Probabilidad y Estadística (317). Fundam
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 1]
   > A los fines de su desarrollo, se entenderá a la Metodología de la Investigación como el conjunto de estrategias, reflexiones y decisiones que configuran los procesos de investigación científica.
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > . La comunicación de los resultados Cronograma de trabajo METODOLOGÍA DE LA INVESTIGACIÓN- 2026 Clase FECHA Tipo de encuentro Tipo encuentro Tema 1 12 de marzo Presencial Teórico/práctico Presentación
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 1]
   > . De este modo, se propone desde la cátedra de Metodología de la Investigación brindar conocimientos y herramientas para indagar la realidad en la búsqueda y desnaturalización de
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 1]
   > 2026 - FCYT-ORO VERDE - Licenciatura en Sistemas de Información - Metodología de la Investigación Carrera: Licenciatura en Sistemas de Información Cátedra: Metodología de la Investigación Año Académic

**Respuesta:**

El plan de estudios de Metodología de la Investigación se refiere a la carrera de Licenciatura en Sistemas de Información, dentro del Año Académico 2026 en la Universidad FCYT-ORO VERDE.

**Tokens:** entrada: 888 | salida: 52 | total: 940

---

### Pregunta 4

> - En Comunicaciones y Redes, ¿cómo hago para quedar como alumno regular?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 3]
   > El alumno accederá a la condición de REGULAR, si cumple con las siguientes condiciones de cátedra: 1 - Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - ALUMNO REGULAR: Obtendrá la regularidad aquel estudiante que logre una calificación mínima de 60 puntos en ambos parciales
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > . Alumno Regular - 60 % de asistencia. - Aprobación del examen parcial teórico con una calificación igual o superior a 60 (sesenta) puntos. - Entrega de todos los trabajos en tiempo y forma.
4. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 8]
   > Comunicación De rutina y consultas: Lista de mail. Material académico: aula virtual - Clave de matriculación bda2023 *Único medio oficial. Avisos y notificaciones: Grupo de Telegram https://t.me/+c7PP
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 15]
   > . Guillerón. 2018 Red Privada Virtual (VPM) sobre Protocolo de Internet versión 6 (IPv6) / Rodrigo Paúl Basso, Maximiliano Sebastián Toso; director Julio Alberto Aldonate; codirector Luciano María Cai

**Respuesta:**

Para quedar como alumno regular en la cátedra de Comunicaciones y Redes, necesitarás obtener una calificación promedio superior o igual a los 60 puntos en los 3 parciales, según el Documento "Planificación 2025 - Comunicacion y Redes.pdf".

**Tokens:** entrada: 839 | salida: 64 | total: 903

---

### Pregunta 5

> - ¿Qué instancias de recuperación nos provee Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > : Herramienta educativa diseñada específicamente para el aprendizaje de la Investigación Operativa
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > PLANIFICACIÓN INVESTIGACIÓN OPERATIVA Unidad I: -Introducción y Modelos Matemáticos- Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del proble
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 3]
   > caracterizando las instancias y fases del proceso de investigación cualitativa y cuantitativa. - Potenciar el desarrollo de análisis crítico-reflexivo de investigaciones del campo de los sistemas de i
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 8]
   > . Dicho examen contará con una (1) instancia de recuperación, conforme al cronograma establecido por la cátedra. - Entrega obligatoria de las actividades prácticas y aprobación del trabajo práctico in
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > Software de Aplicación - Investigación Operativa A continuación, se describen las herramientas informáticas utilizadas en la cátedra para la resolución de modelos de optimización y problemas de gestió

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 809 | salida: 14 | total: 823

---

### Pregunta 6

> - ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > : Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadísticos mediante una interfaz basada en menús para la carga de datos. -
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > Software de Aplicación - Investigación Operativa A continuación, se describen las herramientas informáticas utilizadas en la cátedra para la resolución de modelos de optimización y problemas de gestió
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > 3- PROGRAMA DE TRABAJOS PRACTICOS La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos vertidos en la teoría
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > . Permite resolver problemas de programación lineal (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > . Se dispondrá de un enlace específico para el desarrollo de las clases teóricas, a cargo de la profesora Alejandra, y de dos enlaces diferenciados para las clases prácticas: uno correspondiente a los

**Respuesta:**

El software TORA facilita el procesamiento de modelos matemáticos y estadísticos mediante una interfaz basada en menús para la carga de datos. No se mencionan específicamente los módulos que incluye el software TORA según la cátedra.

**Tokens:** entrada: 822 | salida: 59 | total: 881

---

### Pregunta 7

> - ¿Qué profesor forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > . Se dispondrá de un enlace específico para el desarrollo de las clases teóricas, a cargo de la profesora Alejandra, y de dos enlaces diferenciados para las clases prácticas: uno correspondiente a los
3. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 1]
   > Bases de Datos Avanzadas PRESENTACIÓN DE LA MATERIA Facultad de Ciencia Y Tecnología Base de Datos Avanzadas
4. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 2]
   > Equipo docente Trossero, Sebastián Teoría Trossero.sebastian@uader.edu.ar Schmuckler, Jorge Práctica Schmukler.jorge@uader.edu.ar
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > conocimientos teóricos de manera previa a la clase, a través de videos elaborados por la cátedra, lecturas y otros materiales interactivos

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 780 | salida: 14 | total: 794

---

### Pregunta 8

> - ¿Qué otra asignatura, además de la propia materia de Inteligencia Artificial, incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos Capítulo I Agentes Inteligentes Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas por el áre
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 2]
   > . El impacto de la inteligencia artificial en la gestión del talento. Bibliografía Nacional: Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del tra
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > a desarrollarse en la asignatura. Introducción a los agentes inteligentes. Entorno de Trabajo. Propiedades de los entornos. Estructura de los Agentes. Programas de Agentes. Age
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 1]
   > integrando conceptos de informática, gestión organizacional y derecho informático. Los estudiantes explorarán los efectos de las nuevas tecnologías en el trabajo, la calidad de vida laboral y la admin
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 1]
   > . Además, se abordarán aspectos legales fundamentales para comprender el impacto normativo de las TIC en el ámbito laboral, tomando como base la legislación argentina y los aportes de autores nacional

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 962 | salida: 14 | total: 976

---

### Pregunta 9

> - Los requisitos para regularizar en Bases de Datos Avanzadas y en Redes y Comunicaciones, ¿son iguales? ¿Qué diferencias tienen?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Switches (ancho de banda dedicado a cada puerto, entorno libre de colisiones, operación full-duplex, tabla de conmutación). Comparación hubs / switch. ARP (protocolo de resolución de direcciones). M
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > de Adquisición de Conocimiento. Base de Conocimientos, características generales.
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > . Señalización y Codificación (señalización de bits, codificación agrupación de bits, capacidad para transportar datos (ancho de banda, rendimiento, capacidad de transferencia útil))
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > . Protocolo enlace de datos (HDLC -Control de enlace de datos de alto nivel-, Capa de enlace de datos en Internet -Protocolo PPP (Protocolo Punto a Punto)-). Unidad V
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Lan Virtuales (VLAN) IEEE 802.1Q. Unidad VI: -Ethernet y Cableado Estructurado- Estándares de Ethernet IEE 802.3. Control de enlace lógico, Control de acceso al medio. Implementación de ethernet. Do

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 824 | salida: 14 | total: 838

---

### Pregunta 10

> - ¿Cuál es el porcentaje de asistencia a clases que exigen en común las materias de Investigación Operativa, Comunicaciones y Redes, y Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 1]
   > ; Año de la carrera a la que pertenece la cátedra: 4 Régimen de la materia: Anual Carga horaria semanal: 3 horas Correlativa: Ingeniería del Software I (208) - Probabilidad y Estadística (317). Fundam
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > . Asimismo, deberá acreditar la aprobación de los dos trabajos prácticos de la cátedra y mantener una asistencia mínima del 80% a los encuentros presenciales.
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > . La comunicación de los resultados Cronograma de trabajo METODOLOGÍA DE LA INVESTIGACIÓN- 2026 Clase FECHA Tipo de encuentro Tipo encuentro Tema 1 12 de marzo Presencial Teórico/práctico Presentación
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > . Alumno Regular - 60 % de asistencia. - Aprobación del examen parcial teórico con una calificación igual o superior a 60 (sesenta) puntos. - Entrega de todos los trabajos en tiempo y forma.
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > . Por ello, los materiales teóricos y las lecturas obligatorias se compartirán con una semana de antelación al encuentro presencial

**Respuesta:**

El porcentaje de asistencia a clases que exigen las materias de Investigación Operativa y Metodología de la Investigación es del 80%. No dispongo de información en mis documentos para comparar este dato con el de la materia de Comunicaciones y Redes.

**Tokens:** entrada: 867 | salida: 59 | total: 926

---

### Pregunta 11

> - Si quiero promocionar todas las materias de 4to año, ¿cuál es la diferencia de promedio exigido entre Investigación Operativa e Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > : Herramienta educativa diseñada específicamente para el aprendizaje de la Investigación Operativa
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > . Diferencias entre Programación Dinámica Determinística y Probabilística. SISTEMA DE EVALUACIÓN (Investigación Operativa) Condición del Alumno: - ALUMNO PROMOCIONADO
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 1]
   > ; Año de la carrera a la que pertenece la cátedra: 4 Régimen de la materia: Anual Carga horaria semanal: 3 horas Correlativa: Ingeniería del Software I (208) - Probabilidad y Estadística (317). Fundam
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos Capítulo I Agentes Inteligentes Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas por el áre
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > : El estudiante logrará la promoción directa si alcanza un promedio general de 80 puntos o más entre los 1 parcial previstos, no pudiendo obtener una calificación menor a 60 puntos en ninguna de las i

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 849 | salida: 14 | total: 863

---

### Pregunta 12

> - ¿Qué herramientas de software se recomiendan en la carrera para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > Software de Aplicación - Investigación Operativa A continuación, se describen las herramientas informáticas utilizadas en la cátedra para la resolución de modelos de optimización y problemas de gestió
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > : Software especializado en la resolución de problemas de programación lineal, entera y no lineal
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > . Definición de variables de decisión, función objetivo y restricciones de sistema y de no negatividad. Unidad II: -Programación Lineal (PL)- Propiedades de los modelos de Programación Lineal: proporc
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > . Permite resolver problemas de programación lineal (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. - Storm
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > . Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible vía URL que permite resolver prob

**Respuesta:**

Se recomiendan las herramientas LINDO, Storm y PHP Simplex para resolver problemas de optimización lineal, ya que se menciona que LINDO es un software especializado en la resolución de problemas de programación lineal, entera y no lineal, mientras que Storm incluye módulos para el Método Simplex y modelos de transporte, redes y teoría de juegos.

LINDO se relaciona con la Unidad II de la carrera, específicamente con la sección de propiedades de los modelos de Programación Lineal, que incluye proporcionalidad, aditividad, divisibilidad y certidumbre.

Storm y PHP Simplex se relacionan con la misma unidad, específicamente con la sección de formulación de problemas de optimización y los módulos incluidos en Storm para el Método Simplex y otros modelos.

**Tokens:** entrada: 809 | salida: 184 | total: 993

---

### Pregunta 13

> - ¿Dónde puedo descargar la materia de Cálculo de 1er año?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 3]
   > hojas de cálculo.
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 13]
   > . En carrera: escritura y lectura de textos académicos y profesionales. Argentina. Universidad Nacional de Ǫuilmes. Visto en https://ediciones.ungs.edu.ar/wp-content/uploads/2018/09/9789876301190-comp
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > 4- BIBLIOGRAFIA Obligatoria Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] Cisco Systems: Academia de Networking de Cisco Systems: Guía del prime
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 12]
   > . Visto en https://ediciones.ungs.edu.ar/wp-content/uploads/2018/09/9789876301190-completo.pdf Material audiovisual de la unidad Sobre investigación
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 7]
   > Para facilitar este proceso, cada estudiante o grupo deberá crear una carpeta en la nube (Drive) con el nombre de la materia

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 787 | salida: 14 | total: 801

---

### Pregunta 14

> - El profesor Ing. Jorge L. Schmukler da clases en Bases de Datos Avanzadas, en Inteligencia Artificial y en Redes y Comunicaciones.

**Chunks de contexto:**

1. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 2]
   > Equipo docente Trossero, Sebastián Teoría Trossero.sebastian@uader.edu.ar Schmuckler, Jorge Práctica Schmukler.jorge@uader.edu.ar
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > . Se dispondrá de un enlace específico para el desarrollo de las clases teóricas, a cargo de la profesora Alejandra, y de dos enlaces diferenciados para las clases prácticas: uno correspondiente a los
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > a desarrollarse en la asignatura. Introducción a los agentes inteligentes. Entorno de Trabajo. Propiedades de los entornos. Estructura de los Agentes. Programas de Agentes. Age
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > . Luciano M. Caisso, Ing. Jorge L. Schmukler. AÑO ACADEMICO: 2023 PLAN DE ESTUDIO: 2010 (Resolución No 397/10 UADER) AÑO DE LA CARRERA A LA QUE PERTENECE LA CATEDRA: Cuarto Año RÉGIMEN DE LA MATERIA:

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 930 | salida: 14 | total: 944

---

### Pregunta 15

> - ¿Cuál es el costo de la certificación oficial de Cisco que se menciona como opcional en la planificación?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > 4- BIBLIOGRAFIA Obligatoria Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] Cisco Systems: Academia de Networking de Cisco Systems: Guía del prime
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 5]
   > Sitios web sobre normativas, tecnologías y soluciones, opcional: IETF -> www.ietf.org IEEE -> www.ieee.org ISO -> www.iso.org CISCO -> www.cisco.com IANA -> www.iana.org ISOC -> www.isoc.org ARIN -> w
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 1]
   > Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas semanales Plan de Estudio: Docente: Abog. Rodriguez
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > . As.: Fox Andina, 2013, ISBN: 9789871857784. - USERS. [Disponible en Biblioteca FCyT- Oro Verde] Curso visual y práctico: Administrador de Redes Instalación y configuración de hardware y software. -
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 5]
   > NATIONAL FIRE PROTECTION AGENCY (NFPA) -> www.nfpa.org GFI SECURITY AND MESSANGING SOFTWARE -> www.gfi.com

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 901 | salida: 14 | total: 915

---

### Pregunta 16

> - Para la Promoción Directa, se exige la aprobación de la totalidad de los trabajos prácticos (TP 1 al TP 5). ¿Cuál es la calificación numérica mínima que debe obtenerse en cada TP individual para que se considere aprobado?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 16]
   > 16 Para acceder a la condición de Promoción Directa, el/la estudiante deberá cumplir con los siguientes requisitos: - 80 % de asistencia a la cursada. - Aprobación del examen parcial teórico con una c
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > : El estudiante logrará la promoción directa si alcanza un promedio general de 80 puntos o más entre los 1 parcial previstos, no pudiendo obtener una calificación menor a 60 puntos en ninguna de las i
3. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 7]
   > Régimen Regularidad: Asistencia: Según norma vigente. Todos los trabajos prácticos aprobados. 6/7 parciales aprobados con más del 50% Promoción: Régimen regular Obtener más del 70% en todos los parcia
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 16]
   > cinco) puntos. - Entrega de la totalidad de los trabajos prácticos en tiempo y forma. - Pertinencia, coherencia y calidad académica en las producciones escritas y orales presentadas durante el proceso
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 3]
   > . Con ninguna nota inferior a 60 puntos en cada parcial. 2- Haber realizado y aprobado los dos trabajos práctico impartido por la cátedra. 3- Asistir al 80% de las clases teóricas y prácticas.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 907 | salida: 14 | total: 921

---

### Pregunta 17

> - ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > . Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos. - PHP Simplex: Herramienta online accesible vía URL que permite resolver prob
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > . Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en los vértices, análisis de casos especiales (soluciones múltiples, soluciones no acotadas y problemas infactibl
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > : -Método SIMPLEX- Algoritmo del método Simplex: forma estándar, variables de holgura y variables artificiales
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 1]
   > . Definición de variables de decisión, función objetivo y restricciones de sistema y de no negatividad. Unidad II: -Programación Lineal (PL)- Propiedades de los modelos de Programación Lineal: proporc
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > : Software especializado en la resolución de problemas de programación lineal, entera y no lineal

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 801 | salida: 14 | total: 815

---

### Pregunta 18

> - ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > : enfoque y tipo de investigación / muestra 14 11 de junio Virtual Práctica 15 18 de junio Virtual Teoría Marco metodológico II: recolección de datos y análisis de datos RECESO DE INVIERNO/ MESAS DE E
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > . Por ello, los materiales teóricos y las lecturas obligatorias se compartirán con una semana de antelación al encuentro presencial
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > investigación 17 13 de agosto Virtual Tutorías 18 20 de agosto Presencial (cambio encuentro) Teoría Parcial teoría 19 27 de agosto Virtual Tutorías
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > 24 de septiembr e Virtual Tutorías 24 01 de octubre Presencial Tutorías Presentación tesina- ver posibilidad 25 08 de octubre Virtual Tutorías Presentación tesina- ver posibilidad 26 15 de octubre Vir
5. [Documento: BDA Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: General | Pagina: 3]
   > Días de clase Lunes: 13:30 a 15:30 -> Teoría Viernes: 17:00 a 19:00 -> Práctica NOTA: Los horarios están en proceso de evaluación y pueden sufrir cambios

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 849 | salida: 14 | total: 863

---

## Resumen de tokens

| Conversacion | Entrada | Salida | Total |
|---|---|---|---|
| 1 | 18841 | 894 | 19735 |
| 2 | 19528 | 905 | 20433 |
| 3 | 25590 | 793 | 26383 |
| 4 | 15552 | 787 | 16339 |
| **Total** | **79511** | **3379** | **82890** |
