# Evaluacion — testGeminiPostMejoras2

_Iniciada: 2026-04-12 20:22:31_
_Ultima actualizacion: 2026-04-12 20:24:34_

**Estado:** interrumpido
**Archivo de evaluacion:** `tests/evaluaciones/testGeminiPostMejoras.md`
**Preguntas:** 18 | **Conversaciones planificadas:** 3 | **Conversaciones iniciadas:** 1 | **Preguntas procesadas:** 18
**Interrumpida en:** conversacion 2, antes de la pregunta 1

## Conversacion 1

**Puntaje evaluado: 18 / 18**

**Parametros:**

| Parametro | Valor |
|---|---|
| top_k | 8 |
| retrieval_type | similarity_search |
| threshold | 0.5 |
| max_context_chunks | 8 |
| temperatura | 0.5 |
| debug | False |
| llm_provider | google |
| llm_model | gemini-3.1-flash-lite-preview |
| chunk_size | 800 |
| chunk_overlap | 200 |
| embedding_model | gemini-embedding-001 |
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
   > n espacio de estados. Búsqueda Ciega, definición; búsqueda primero en amplitud, búsqueda de costo uniforme; búsqueda primero en profundidad. Búsqueda Heurística, definición; búsqueda ordenada en el e
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > ntos métodos sobre el funcionamiento del sistema. Agentes Basados en Lógica Difusa. **Capítulo VIII** **Redes Neuronales Artificiales (RNA).** Generalidades, conceptos básicos Reseña Histórica. Cla
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > basada en objetos. Definición de objetos y de atributos. Clases e instancias. Concepto de herencia. Métodos y mensajes. Representación de Conocimientos mediante reglas. Estructura básica. Representac
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > ión (Pruning Algorithms). Deep Learning. Modelos Generativos **Capítulo XI** Redes Autoorganizadas. Características generales. **Red SOM (Kohonen)**. Proceso de aprendizaje competitivo. Realimentac
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > ras FAM (Fuzzy Associative Memories). Composición MAX-MIN. **Capítulo VII** **Sistemas** **Difusos.** Consideraciones generales. Representación de conocimiento estructurado mediante reglas lingüísti
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Estructura de Control: Procedimientos de Inferencia; Interfase con el usuario. Memoria de Trabajo, Módulo generador de explicaciones al usuario. **Capítulo V** **Funcionalidad de los Sistemas Exper
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > n agentes. Metodología Gaia: Modelo de Actividades. Modelo de Roles. Modelo Interacción. Modelo de Agentes. Organizaciones. Interacciones multiagente. Comunicación y coordinación. Protocolos de Intera

**Respuesta:**

Los contenidos de la materia Inteligencia Artificial se organizan en los siguientes capítulos:

*   **Capítulo I: Agentes Inteligentes.** Incluye definiciones, objetivos y herramientas de la IA, el entorno de trabajo y sus propiedades, la estructura y programas de agentes (reactivos simples, basados en modelos, basados en objetivos y que aprenden).
*   **Capítulo II: Procesos de Búsqueda.** Abarca la representación en un espacio de estados, búsqueda ciega (amplitud, costo uniforme, profundidad), búsqueda heurística (ordenada, voraz, A*, recocido simulado), heurísticos admisibles y agentes basados en procesos de búsqueda.
*   **Capítulo III: Sistemas Basados en Conocimientos.** Trata la representación de conocimientos mediante lógica de primer orden, reglas de inferencia, estructuras basadas en objetos (clases, instancias, herencia, métodos, mensajes) y reglas, además del comportamiento de agentes basados en conocimientos.
*   **Capítulo IV y V: Sistemas Expertos.** Incluye el diseño de sus módulos (base de conocimientos, memoria de trabajo, generador de explicaciones, interfase de usuario), proceso de adquisición de conocimiento y procesos de inferencia (encadenamiento hacia adelante y hacia atrás).
*   **Capítulo VI y VII: Lógica y Sistemas Difusos.** Abarca conjuntos difusos, operaciones, estructuras FAM, composición MAX-MIN, representación mediante reglas lingüísticas, procesos de fuzzificación, inferencia, defuzzificación (método del centroide y de máxima) y agentes basados en lógica difusa.
*   **Capítulo VIII: Redes Neuronales Artificiales (RNA).** Comprende generalidades, reseña histórica, clasificación, agentes basados en procesos de aprendizaje, red perceptron simple (elemento de procesamiento, función de transferencia, convergencia, entrenamiento) y algoritmos de modificación.
*   **Capítulo XI: Redes Autoorganizadas.** Incluye características generales, red SOM (Kohonen), proceso de aprendizaje competitivo, realimentación lateral, determinación de pesos, función de vecindad y modificaciones al algoritmo SOM. Adicionalmente, se abordan temas de Deep Learning y modelos generativos.
*   **Capítulo XII: Sistemas Multi Agentes.** Incluye modelos formales, metodologías de diseño (Gaia: modelos de actividades, roles, interacción y agentes), organizaciones, interacciones, comunicación y coordinación, protocolos, estándares (FIPA, lenguaje ACL) y tópicos avanzados en tecnología de agentes.

**Tokens:** entrada: 1968 | salida: 523 | total: 2491

---

### Pregunta 2

> - ¿En qué materia se enseña el concepto de Lógica Difusa?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Estructura de Control: Procedimientos de Inferencia; Interfase con el usuario. Memoria de Trabajo, Módulo generador de explicaciones al usuario. **Capítulo V** **Funcionalidad de los Sistemas Exper
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > ras FAM (Fuzzy Associative Memories). Composición MAX-MIN. **Capítulo VII** **Sistemas** **Difusos.** Consideraciones generales. Representación de conocimiento estructurado mediante reglas lingüísti
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > ntos métodos sobre el funcionamiento del sistema. Agentes Basados en Lógica Difusa. **Capítulo VIII** **Redes Neuronales Artificiales (RNA).** Generalidades, conceptos básicos Reseña Histórica. Cla
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > n espacio de estados. Búsqueda Ciega, definición; búsqueda primero en amplitud, búsqueda de costo uniforme; búsqueda primero en profundidad. Búsqueda Heurística, definición; búsqueda ordenada en el e
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > basada en objetos. Definición de objetos y de atributos. Clases e instancias. Concepto de herencia. Métodos y mensajes. Representación de Conocimientos mediante reglas. Estructura básica. Representac
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > ión (Pruning Algorithms). Deep Learning. Modelos Generativos **Capítulo XI** Redes Autoorganizadas. Características generales. **Red SOM (Kohonen)**. Proceso de aprendizaje competitivo. Realimentac
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > n agentes. Metodología Gaia: Modelo de Actividades. Modelo de Roles. Modelo Interacción. Modelo de Agentes. Organizaciones. Interacciones multiagente. Comunicación y coordinación. Protocolos de Intera
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos **Capítulo I** **Agentes Inteligentes** Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas p

**Respuesta:**

El concepto de Lógica Difusa se enseña en la materia Inteligencia Artificial.

**Tokens:** entrada: 1971 | salida: 17 | total: 1988

---

### Pregunta 3

> - ¿Cuál es el plan de estudios de Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > ota correspondiente a la instancia teórica, estableciéndose en ese momento la calificación final y la condición de aprobación o no aprobación. **Plan de estudios resumido** - Unidad 1: Introducci
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: dentro de la plataforma Moodle. La organización será la siguiente | Pagina: 5]
   > - Inicio del curso: contendrá información general de la cátedra, incluyendo el programa, el equipo docente, el cronograma, los objetivos, los materiales utilizados, el enlace de videoconferencia, la
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > preguntas le hago al problema? ¿Cómo construir el marco teórico? ¿Con qué categorías? Definición temporal y de contexto. Relación con los antecedentes relevados. Formulación de las preguntas que se
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: **Equipo docente:** PROFESORA RESPONSABLE ADJUNTO: ALEJANDRA MARǪUESIN; JEFE DE | Pagina: 1]
   > TRABAJOS PRÁCTICOS: TAMARA SUIVA. JEFE DE TRABAJOS PRÁCTICOS: JIMENA SANTA CRUZ; **Año de la carrera a la que pertenece la cátedra:** 4 **Régimen de la materia:** Anual **Carga horaria semanal:** 3
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > análisis y la población. **Unidad 4: La dimensión de las técnicas de obtención y análisis de información empírica. La** **comunicación de los resultados** Análisis de las opciones posibles (entrevi
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 3]
   > tura académica. Normas de citación. **Unidad 2: La dimensión epistemológica** ¿Cómo encauzar la definición del tema de investigación? Lectura de antecedentes, criterios para orientar la búsqueda d
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 3]
   > **Objetivos generales:** - Acercar al campo de la investigación científica desde espacios de reflexión sistemáticos enmarcados en trabajos propios de la disciplina y el campo profesional. **Objeti
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > _remitirá un informe con las observaciones correspondientes y se establecerá un encuentro sincrónico_ _para su devolución y orientación. Cumplida esta instancia de revisión, el/la estudiante quedará_

**Respuesta:**

El plan de estudios de la asignatura Metodología de la Investigación se estructura en cuatro unidades temáticas:

*   **Unidad 1:** Introducción a la ciencia y conocimiento científico.
*   **Unidad 2:** La dimensión epistemológica, que abarca la definición del tema de investigación, búsqueda de antecedentes, construcción del problema objeto de estudio, formulación de preguntas y objetivos, y escritura académica.
*   **Unidad 3:** La dimensión de la estrategia general de investigación, centrada en el diseño de investigación (cuantitativo o cualitativo), estrategias de indagación, universo de análisis y población.
*   **Unidad 4:** La dimensión de las técnicas de obtención y análisis de información empírica y la comunicación de los resultados, incluyendo métodos como entrevistas, observación y análisis documental, así como el análisis de datos y la presentación de resultados.

**Tokens:** entrada: 2136 | salida: 182 | total: 2318

---

### Pregunta 4

> - ¿Qué herramientas de software se recomiendan en la carrera para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > ión de operaciones. Facilita el procesamiento de modelos matemáticos y estadísticos mediante una interfaz basada en menús para la carga de datos. - **TORA:** Herramienta educativa diseñada específ
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > egiones factibles. - **LINGO (64 bits):** Una versión avanzada y más potente del motor LINDO. Está diseñado para modelar y resolver problemas de optimización de gran escala, permitiendo una integr
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > ación. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en los vértices, análisis de casos especiales (soluciones múltiples, soluciones no acotadas y problemas in
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad I: -Introducción y Modelos Matemáticos-** Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del problema, construcción del modelo mate
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > estructura del modelo y suposiciones. Métodos para obtener una solución básica inicial: Esquina Noroeste, Costo Mínimo y Aproximación de Vogel. Método MODI (Distribución Modificada) para la optimiza
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 3]
   > hojas de cálculo.

**Respuesta:**

Para la resolución de problemas de optimización lineal y otros modelos de gestión, la cátedra utiliza un conjunto de herramientas informáticas con capacidades específicas que se vinculan directamente con los contenidos teóricos de la materia:

*   **Herramientas para Programación Lineal (Unidad II y III):**
    *   **PHP Simplex:** Es una herramienta online ideal para realizar validaciones rápidas y visualizar regiones factibles, siendo útil para la resolución gráfica (Unidad II) y el Método Simplex (Unidad III).
    *   **LINDO:** Se especializa en programación lineal, entera y no lineal. Su ventaja principal es la sintaxis sencilla para ingresar ecuaciones y restricciones.
    *   **LINGO (64 bits):** Evolución del motor LINDO, está diseñado para problemas de optimización de gran escala, permitiendo una integración fluida con bases de datos y hojas de cálculo.

*   **Herramientas para Modelos de Transporte, Asignación y otros (Unidad IV y V):**
    *   **WinQSB 2.0:** Es una suite integral que permite resolver problemas de programación lineal, transporte, asignación (Unidad IV), programación dinámica (Unidad V), teoría de colas y gestión de inventarios.
    *   **TORA:** Es una herramienta de carácter educativo que incluye módulos específicos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos.

*   **Herramientas para Análisis Cuantitativo y Gestión:**
    *   **Storm:** Está orientado al procesamiento de modelos matemáticos y estadísticos mediante una interfaz basada en menús para la carga de datos, facilitando las tareas de gestión de operaciones mencionadas en la sección general de la materia.

La relación entre estas herramientas y la teoría es directa: mientras que herramientas como **PHP Simplex** y **TORA** ofrecen soporte visual y pedagógico para el aprendizaje de los algoritmos (como el Simplex o la resolución gráfica), **LINDO**, **LINGO** y **WinQSB** proporcionan la potencia necesaria para abordar la resolución de los problemas complejos de optimización, transporte y programación dinámica planteados en las unidades programáticas.

**Tokens:** entrada: 1672 | salida: 462 | total: 2134

---

### Pregunta 5

> - ¿Qué instancias de recuperación nos provee Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mismo examen parcial. La calificación obtenida en la instancia de
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > ión de operaciones. Facilita el procesamiento de modelos matemáticos y estadísticos mediante una interfaz basada en menús para la carga de datos. - **TORA:** Herramienta educativa diseñada específ
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad I: -Introducción y Modelos Matemáticos-** Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del problema, construcción del modelo mate
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > egiones factibles. - **LINGO (64 bits):** Una versión avanzada y más potente del motor LINDO. Está diseñado para modelar y resolver problemas de optimización de gran escala, permitiendo una integr
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > ación. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en los vértices, análisis de casos especiales (soluciones múltiples, soluciones no acotadas y problemas in

**Respuesta:**

La cátedra dispone de dos oportunidades de recuperatorio totales. Estas instancias pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no es posible aplicar ambos recuperatorios a un mismo examen parcial. La calificación obtenida en la instancia de recuperación sustituirá automáticamente a la nota del examen original.

**Tokens:** entrada: 1784 | salida: 64 | total: 1848

---

### Pregunta 6

> - ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > ión de operaciones. Facilita el procesamiento de modelos matemáticos y estadísticos mediante una interfaz basada en menús para la carga de datos. - **TORA:** Herramienta educativa diseñada específ
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > egiones factibles. - **LINGO (64 bits):** Una versión avanzada y más potente del motor LINDO. Está diseñado para modelar y resolver problemas de optimización de gran escala, permitiendo una integr
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 3]
   > hojas de cálculo.
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > estructura del modelo y suposiciones. Métodos para obtener una solución básica inicial: Esquina Noroeste, Costo Mínimo y Aproximación de Vogel. Método MODI (Distribución Modificada) para la optimiza
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > n agentes. Metodología Gaia: Modelo de Actividades. Modelo de Roles. Modelo Interacción. Modelo de Agentes. Organizaciones. Interacciones multiagente. Comunicación y coordinación. Protocolos de Intera
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad I: -Introducción y Modelos Matemáticos-** Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del problema, construcción del modelo mate

**Respuesta:**

TORA es una herramienta educativa diseñada específicamente para el aprendizaje de la Investigación Operativa. Incluye módulos para el Método Simplex, el cual permite la visualización paso a paso, así como módulos para modelos de transporte, redes y teoría de juegos.

**Tokens:** entrada: 1590 | salida: 50 | total: 1640

---

### Pregunta 7

> - ¿Qué profesor forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > **Facultad de Ciencia y Tecnología de la UADER** SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler.
2. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **EQUIPO DOCENTE** | Pagina: 1]
   > Teoría: Trossero, Sebastián (Trossero.sebastian@uader.edu.ar) Práctica: Schmuckler, Jorge (Schmukler.jorge@uader.edu.ar)
3. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **CANALES DE COMUNICACIÓN** | Pagina: 2]
   > Correo: Lista de mail (consultas y comunicación de rutina) Aula virtual: Material académico - Clave de matriculación: bda2023 (ÚNICO MEDIO OFICIAL) Telegram: https://t.me/+c7PPIrc9nQM4MzEx (avisos y n
4. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **BIBLIOGRAFÍA BASE** | Pagina: 2]
   > Elmasri, R. / Navathe, S. - Fundamentos de Sistemas de Bases de Datos (Addison Wesley) Silberschatz / Korth / Sudarshan - Fundamentos de Bases de Datos (Mc Graw Hill) Date, C.J. - Introducción a los S
5. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **MODALIDAD DE CLASES** | Pagina: 1]
   > A partir de este año la materia será dictada de manera bimodal. El cronograma será definido en su mayoría por la Facultad. Aún no confirmado. Los links de clases se encuentran en el aula virtual. Las
6. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **HORARIOS DE CLASE** | Pagina: 1]
   > Lunes: 13:30 a 15:30 (Teoría) Viernes: 17:00 a 19:00 (Práctica) Nota: Los horarios están en proceso de evaluación y pueden sufrir cambios
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > s de enrutamiento. Aspectos de diseño de la capa de red (Conmutación de paquetes de almacenamiento y reenvío, Servicios proporcionados a la capa de transporte, Implementación del servicio no orientado
8. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **PRESENTACIÓN DE LA MATERIA** | Pagina: 1]
   > Facultad de Ciencia y Tecnología Universidad Autónoma de Entre Ríos (UADER)

**Respuesta:**

El profesor que forma parte del equipo docente en ambas materias es el Ingeniero Jorge L. Schmukler (o Schmuckler).

**Tokens:** entrada: 1346 | salida: 27 | total: 1373

---

### Pregunta 8

> - ¿Qué otra asignatura, además de la propia materia de Inteligencia Artificial, incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > n agentes. Metodología Gaia: Modelo de Actividades. Modelo de Roles. Modelo Interacción. Modelo de Agentes. Organizaciones. Interacciones multiagente. Comunicación y coordinación. Protocolos de Intera
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 4. El impacto de la inteligencia artificial en la gestión del talento. | Pagina: 2]
   > _**Bibliografía Nacional:**_ Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales. **Uni
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (2
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos **Capítulo I** **Agentes Inteligentes** Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas p
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > ión (Pruning Algorithms). Deep Learning. Modelos Generativos **Capítulo XI** Redes Autoorganizadas. Características generales. **Red SOM (Kohonen)**. Proceso de aprendizaje competitivo. Realimentac
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > ntos métodos sobre el funcionamiento del sistema. Agentes Basados en Lógica Difusa. **Capítulo VIII** **Redes Neuronales Artificiales (RNA).** Generalidades, conceptos básicos Reseña Histórica. Cla
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > basada en objetos. Definición de objetos y de atributos. Clases e instancias. Concepto de herencia. Métodos y mensajes. Representación de Conocimientos mediante reglas. Estructura básica. Representac
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > n espacio de estados. Búsqueda Ciega, definición; búsqueda primero en amplitud, búsqueda de costo uniforme; búsqueda primero en profundidad. Búsqueda Heurística, definición; búsqueda ordenada en el e

**Respuesta:**

La asignatura de Informática y Recursos Humanos incluye explícitamente el impacto de la inteligencia artificial en su unidad temática número 3, titulada "Gestión del Talento en la Era Digital", y cuenta con una sección específica dedicada al "impacto de la inteligencia artificial en la gestión del talento".

**Tokens:** entrada: 1796 | salida: 60 | total: 1856

---

### Pregunta 9

> - Los requisitos para regularizar en Bases de Datos Avanzadas y en Redes y Comunicaciones, ¿son iguales? ¿Qué diferencias tienen?

**Chunks de contexto:**

1. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **RÉGIMEN DE CURSADA** | Pagina: 2]
   > **Regularidad:** Asistencia: Según norma vigente Todos los trabajos prácticos aprobados 6/7 parciales aprobados con más del 50% **Promoción:** Régimen regular Obtener más del 70% en todos los parci
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > PROMOCIONADO REGULAR LIBRE El alumno accederá a la condición de **PROMOCIÓN** si cumple con las siguientes condiciones de cátedra: **1 -** Obtener en los 3 parciales, una calificación promedio sup
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > erior o igual a los 60 puntos. Tener aprobado con 60 puntos los tres parciales. **2-** Haber realizado y aprobado los dos trabajos Práctico impartido por la cátedra. **3-** Asistir al 80% de las clas
4. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **CANALES DE COMUNICACIÓN** | Pagina: 2]
   > Correo: Lista de mail (consultas y comunicación de rutina) Aula virtual: Material académico - Clave de matriculación: bda2023 (ÚNICO MEDIO OFICIAL) Telegram: https://t.me/+c7PPIrc9nQM4MzEx (avisos y n
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > una de las evaluaciones parciales y recuperatorios una semana después de que estas se hayan realizado. Tanto las evaluaciones parciales como los recuperatorios se realizaran en los horarios asignados
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos vertidos en la teoría. Más dos trabajos Prácticos que se realizan en el ho
7. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **SOFTWARE REQUERIDO** | Pagina: 2]
   > PostgreSQL: versión 9.6 o superior SQL Server: versión 2016 o superior QGIS: versión compatible con PostgreSQL Anaconda (Python): últimas versiones
8. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **MODALIDAD DE CLASES** | Pagina: 1]
   > A partir de este año la materia será dictada de manera bimodal. El cronograma será definido en su mayoría por la Facultad. Aún no confirmado. Los links de clases se encuentran en el aula virtual. Las

**Respuesta:**

Los requisitos para regularizar las materias Bases de Datos Avanzadas y Comunicación y Redes no son iguales; presentan diferencias significativas en cuanto a la exigencia de asistencia, la aprobación de trabajos prácticos y el rendimiento en los exámenes parciales.

Las diferencias principales son las siguientes:

*   **Asistencia:** En Bases de Datos Avanzadas, la asistencia se rige según la norma vigente, mientras que en Comunicación y Redes se exige obligatoriamente un 80% de asistencia a las clases teóricas y prácticas.
*   **Trabajos Prácticos:** Bases de Datos Avanzadas requiere tener aprobados "todos" los trabajos prácticos. Por su parte, Comunicación y Redes especifica la aprobación de dos trabajos prácticos realizados en horario de clase.
*   **Evaluaciones Parciales:** 
    *   En **Bases de Datos Avanzadas**, se requiere aprobar 6 de los 7 parciales con una nota superior al 50%.
    *   En **Comunicación y Redes**, se deben aprobar los 3 parciales con una calificación de al menos 60 puntos cada uno, obteniendo un promedio general superior o igual a 60 puntos. 

En resumen, mientras que Bases de Datos Avanzadas se enfoca en un volumen mayor de evaluaciones parciales con un umbral de aprobación del 50%, Comunicación y Redes establece un sistema de tres instancias con un piso de nota más elevado (60 puntos) y un control de asistencia estricto.

**Tokens:** entrada: 1676 | salida: 319 | total: 1995

---

### Pregunta 10

> - ¿Cuál es el porcentaje de asistencia a clases que exigen en común las materias de Investigación Operativa, Comunicaciones y Redes, y Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > **Condición del Alumno:** - **ALUMNO PROMOCIONADO:** El estudiante logrará la promoción directa si alcanza un promedio general de **80 puntos** - más entre los **1 parcial** previstos, no pudiendo
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > erior o igual a los 60 puntos. Tener aprobado con 60 puntos los tres parciales. **2-** Haber realizado y aprobado los dos trabajos Práctico impartido por la cátedra. **3-** Asistir al 80% de las clas
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > PROMOCIONADO REGULAR LIBRE El alumno accederá a la condición de **PROMOCIÓN** si cumple con las siguientes condiciones de cátedra: **1 -** Obtener en los 3 parciales, una calificación promedio sup
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mismo examen parcial. La calificación obtenida en la instancia de
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > **b.** **Alumno Regular** - 60 % de asistencia. - Aprobación del examen parcial teórico con una calificación igual o superior a 60 (sesenta) puntos. - Entrega de todos los trabajos en tiempo y
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 16]
   > Para acceder a la condición de Promoción Directa, el/la estudiante deberá cumplir con los siguientes requisitos: - 80 % de asistencia a la cursada. - Aprobación del examen parcial teórico con una
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 3]
   > hojas de cálculo.

**Respuesta:**

No existe un porcentaje de asistencia común para las tres materias.

Las condiciones de asistencia varían según la asignatura:

*   **Investigación Operativa y Comunicaciones y Redes:** Ambas exigen una asistencia mínima del **80%** a las clases teóricas y prácticas para alcanzar las condiciones de regularidad y promoción.
*   **Metodología de la Investigación:** Los requisitos de asistencia son distintos dependiendo de la condición del alumno: se exige un **60%** para la condición de alumno regular y un **80%** para acceder a la promoción directa.

**Tokens:** entrada: 1957 | salida: 122 | total: 2079

---

### Pregunta 11

> - Un proyecto integrador requiere utilizar un software para resolver problemas de optimización a gran escala que pueda conectarse de forma fluida con bases de datos espaciales. Según las herramientas enseñadas en las materias, ¿qué combinación de software visto en Bases de Datos Avanzadas e Investigación Operativa sería la más adecuada para este objetivo?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > egiones factibles. - **LINGO (64 bits):** Una versión avanzada y más potente del motor LINDO. Está diseñado para modelar y resolver problemas de optimización de gran escala, permitiendo una integr
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > ión de operaciones. Facilita el procesamiento de modelos matemáticos y estadísticos mediante una interfaz basada en menús para la carga de datos. - **TORA:** Herramienta educativa diseñada específ
3. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **SOFTWARE REQUERIDO** | Pagina: 2]
   > PostgreSQL: versión 9.6 o superior SQL Server: versión 2016 o superior QGIS: versión compatible con PostgreSQL Anaconda (Python): últimas versiones
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
6. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **BIBLIOGRAFÍA BASE** | Pagina: 2]
   > Elmasri, R. / Navathe, S. - Fundamentos de Sistemas de Bases de Datos (Addison Wesley) Silberschatz / Korth / Sudarshan - Fundamentos de Bases de Datos (Mc Graw Hill) Date, C.J. - Introducción a los S
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > ación. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en los vértices, análisis de casos especiales (soluciones múltiples, soluciones no acotadas y problemas in
8. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **PRESENTACIÓN DE LA MATERIA** | Pagina: 1]
   > Facultad de Ciencia y Tecnología Universidad Autónoma de Entre Ríos (UADER)

**Respuesta:**

Para abordar un proyecto de optimización a gran escala con integración fluida en bases de datos, la combinación más adecuada consiste en utilizar **LINGO (64 bits)** junto con **PostgreSQL**.

La elección se fundamenta en las capacidades específicas de cada herramienta:

*   **Para el motor de optimización:** **LINGO (64 bits)** es la herramienta diseñada específicamente para modelar y resolver problemas de optimización de gran escala. A diferencia de otras opciones orientadas a la enseñanza o al análisis cuantitativo básico, LINGO destaca por permitir una integración más fluida con bases de datos.
*   **Para la gestión de datos espaciales:** **PostgreSQL** (versión 9.6 o superior) es el software de base de datos requerido en la materia Bases de Datos Avanzadas. Su integración es complementaria con **QGIS**, que es el software compatible para el manejo de información espacial.

Esta combinación permite aprovechar la potencia de cálculo de LINGO para modelos complejos y la infraestructura de datos robusta de PostgreSQL, la cual puede ser gestionada mediante las herramientas de análisis espacial requeridas en el plan de estudios.

**Tokens:** entrada: 1501 | salida: 235 | total: 1736

---

### Pregunta 12

> - Si un estudiante desea investigar sobre el impacto de los "Agentes que aprenden" y las "Redes Neuronales" en la selección de personal y el teletrabajo en Argentina, ¿qué normativas legales y temas específicos de los programas de Inteligencia Artificial y RRHH debería cruzar en su marco teórico?

**Chunks de contexto:**

1. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 4. El impacto de la inteligencia artificial en la gestión del talento. | Pagina: 2]
   > _**Bibliografía Nacional:**_ Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales. **Uni
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: IV. BIBLIOGRAFÍA GENERAL | Pagina: 3]
   > _**Bibliografía Básica:**_ Nicolás S. Tato, El Derecho Informático - Aspectos Fundamentales. Mariana Nazar, Tecnologías, información y derechos. Gonzalo Ana Dobratinich, derecho y nuevas tecnología
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 2]
   > Reglamento de Teletrabajo en Argentina. Nicolás S. Tato, El Derecho Informático - Aspectos Fundamentales. Mariana Nazar, Tecnologías, información y derechos. **Unidad 2:** **Relaciones Humanas en e
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 6. Desafíos éticos y sociales de la tecnología en el ámbito laboral. | Pagina: 1]
   > _**Bibliografía Nacional:**_ Ley de Teletrabajo (Ley 27.555).
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 5. comercio electrónico, manifestación del consentimiento en internet | Pagina: 3]
   > _**Bibliografía Nacional:**_ Ley de Teletrabajo (Ley 27.555) Código Civil y Comercial de la Nación (aspectos relacionados con contratos digitales). Artículos académicos sobre la economía gig y el t
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > ntos métodos sobre el funcionamiento del sistema. Agentes Basados en Lógica Difusa. **Capítulo VIII** **Redes Neuronales Artificiales (RNA).** Generalidades, conceptos básicos Reseña Histórica. Cla
7. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: **I. FUNDAMENTACIÓN** | Pagina: 1]
   > El avance de las tecnologías de la información y la comunicación (TIC) ha transformado la dinámica del mundo laboral y las relaciones humanas dentro de las organizaciones. Esta asignatura busca analiz
8. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 3]
   > Legislación sobre delitos informáticos en Argentina. Ley Nacional de Protección de Datos Personales (Ley 25.326). Ley Propiedad Intelectual (Ley 11.723) y su modificatoria. **Unidad 5: Trabajo Autó

**Respuesta:**

Para estructurar un marco teórico que vincule el uso de agentes inteligentes y redes neuronales con la gestión de personal y el teletrabajo en Argentina, el estudiante debe integrar los siguientes ejes normativos y temáticos:

### Marco Normativo (Base Legal Argentina)
El análisis del impacto de estas tecnologías debe fundamentarse en el marco legal vigente, que regula tanto la protección de la información como las modalidades laborales:

*   **Protección de Datos Personales:** La **Ley 25.326** es fundamental para abordar cómo los agentes basados en procesos de aprendizaje gestionan la información sensible de los candidatos y empleados.
*   **Regulación del Teletrabajo:** La **Ley 27.555** y su reglamento son los pilares para analizar el impacto de la IA en el trabajo remoto y la calidad de vida laboral.
*   **Derechos y Contratos:** El **Código Civil y Comercial de la Nación** debe ser consultado para los aspectos relacionados con contratos digitales y firma electrónica, mientras que la **Ley 11.723** (y su modificatoria 25.036) es necesaria para tratar la propiedad intelectual en el entorno digital.
*   **Seguridad:** La legislación sobre delitos informáticos en Argentina constituye el marco de referencia para la seguridad de los sistemas que emplean IA.

### Ejes Temáticos de Intersección
Para conectar los aspectos técnicos de la Inteligencia Artificial con la gestión de Recursos Humanos, el estudiante debe cruzar los siguientes temas:

1.  **Tecnología y Aprendizaje:**
    *   **Redes Neuronales Artificiales (RNA):** Estudiar sus generalidades, clasificación y, específicamente, los **agentes basados en procesos de aprendizaje** y el **Perceptron Simple** (incluyendo su función de transferencia y entrenamiento).
    *   **Lógica Difusa:** Analizar el uso de agentes basados en esta metodología como herramienta para la toma de decisiones en la gestión del talento.

2.  **Gestión del Talento y Transformación Laboral:**
    *   **Impacto de la IA:** Investigar la transformación del trabajo y las relaciones laborales bajo la influencia de la inteligencia artificial, utilizando los artículos académicos sugeridos en el programa.
    *   **Nuevas Dinámicas:** Analizar la gestión del talento en la era digital y los desafíos éticos y sociales que plantea la tecnología en el ámbito laboral.
    *   **Economía Gig:** Integrar el estudio del trabajo autónomo y las plataformas digitales, los cuales suelen ser entornos donde se aplican algoritmos de aprendizaje.

### Autores y Referencias
Para consolidar este marco, se recomienda integrar la bibliografía nacional específica:
*   **Gonzalo Ana Dobratinich:** *Derecho y nuevas tecnologías*.
*   **Nicolás S. Tato:** *El Derecho Informático - Aspectos Fundamentales*.
*   **Mariana Nazar:** *Tecnologías, información y derechos*.

El cruce de estos puntos permite analizar cómo la capacidad de aprendizaje de los agentes (técnica) se ve limitada o regulada por el marco de protección de datos y los derechos laborales (normativa) en el contexto de las organizaciones argentinas.

**Tokens:** entrada: 1487 | salida: 675 | total: 2162

---

### Pregunta 13

> - ¿Dónde puedo descargar la materia de Cálculo de 1er año?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: -> BÚSǪUEDA AVANZADA con GOOGLE - PRIMERA PARTE - APRENDER A INVESTIGAR **:** | Pagina: 12]
   > **[https://youtu.be/9oWM50RDsLǪ](https://youtu.be/9oWM50RDsLQ)**
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 3]
   > hojas de cálculo.
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: -> BÚSǪUEDA AVANZADA GOOGLE - BÚSǪUEDA GOOGLE AVANZADA - 3RA PARTE | Pagina: 12]
   > [APRENDER A INVESTIGAR: https://youtu.be/NJby_1x178I](https://youtu.be/NJby_1x178I)
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: -> Paula Espeche Trayecto 2 Google académico y operadores booleanos | Pagina: 12]
   > **[https://youtu.be/fiSJ4bDb Nwrc](https://youtu.be/1SJ4bDb Nwrc)**
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: -> BÚSǪUEDA AVANZADA GOOGLE - BÚSǪUEDA GOOGLE AVANZADA - 2DA PARTE | Pagina: 12]
   > [APRENDER A INVESTIGAR: https://youtu.be/eHjUqHcVBA4](https://youtu.be/eHjUqHcVBA4)
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: AÑO ACADEMICO: 2023 | Pagina: 1]
   > PLAN DE ESTUDIO: 2010 (Resolución No 397/10 UADER)
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 12]
   > - Natale, Lucía (Coordinadora) (2013). En carrera: escritura y lectura de textos académicos y profesionales. Argentina. Universidad Nacional de Ǫuilmes. Visto en [https://ediciones.ungs.edu.ar/wp-co
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 13]
   > - Yuni, J y Urbano, C (2016) Técnicas para investigar 2: Recursos metodológicos para la preparación de proyectos de investigación. Editorial Brujas: Argentina _Material audiovisual de la unidad_

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1298 | salida: 13 | total: 1311

---

### Pregunta 14

> - El profesor Ing. Jorge L. Schmukler da clases en Bases de Datos Avanzadas, en Inteligencia Artificial y en Redes y Comunicaciones.

**Chunks de contexto:**

1. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **EQUIPO DOCENTE** | Pagina: 1]
   > Teoría: Trossero, Sebastián (Trossero.sebastian@uader.edu.ar) Práctica: Schmuckler, Jorge (Schmukler.jorge@uader.edu.ar)
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > **Facultad de Ciencia y Tecnología de la UADER** SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler.
3. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **HORARIOS DE CLASE** | Pagina: 1]
   > Lunes: 13:30 a 15:30 (Teoría) Viernes: 17:00 a 19:00 (Práctica) Nota: Los horarios están en proceso de evaluación y pueden sufrir cambios
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > basada en objetos. Definición de objetos y de atributos. Clases e instancias. Concepto de herencia. Métodos y mensajes. Representación de Conocimientos mediante reglas. Estructura básica. Representac
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > ntos métodos sobre el funcionamiento del sistema. Agentes Basados en Lógica Difusa. **Capítulo VIII** **Redes Neuronales Artificiales (RNA).** Generalidades, conceptos básicos Reseña Histórica. Cla
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > ión (Pruning Algorithms). Deep Learning. Modelos Generativos **Capítulo XI** Redes Autoorganizadas. Características generales. **Red SOM (Kohonen)**. Proceso de aprendizaje competitivo. Realimentac
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos **Capítulo I** **Agentes Inteligentes** Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas p
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > **Capítulo IX** **Redes** **Perceptron** **Multicapa**, estructura básica. Proceso de Entrenamiento Backpropagation (BP). Interpretación heurística y matemática del procedimiento BP. Término de Momen

**Respuesta:**

El Ing. Jorge L. Schmukler forma parte del equipo docente en las siguientes materias:

*   **Bases de Datos Avanzadas:** Se desempeña como docente de la parte práctica.
*   **Comunicaciones y Redes:** Integra el equipo docente de la cátedra.

Respecto a la materia **Inteligencia Artificial**, no dispongo de información en mis documentos que confirme que el Ing. Jorge L. Schmukler forme parte de su equipo docente.

**Tokens:** entrada: 1699 | salida: 99 | total: 1798

---

### Pregunta 15

> - ¿Cuál es el costo de la certificación oficial de Cisco que se menciona como opcional en la planificación?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > **Obligatoria** - Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] - Cisco Systems: Academia de Networking de Cisco Systems: Guía del primer añ
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > ma 802.1Q, Operación de enlace troncal, Configuración de las VLAN y de los enlaces troncales, Administración de las VLAN, Resolución de problemas de las VLAN y de los enlaces troncales. **Unidad X** *
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Sitios web sobre normativas, tecnologías y soluciones, opcional** | Pagina: 5]
   > IETF -> www.ietf.org IEEE -> www.ieee.org ISO -> www.iso.org CISCO -> www.cisco.com IANA -> www.iana.org ISOC -> www.isoc.org ARIN -> www.arin.net LACNIC -> http://lacnic.net/sp/ LAC IPV6 TF -> www.la
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > Comunicación en un mundo centrado en la red, herramientas de comunicación. La comunicación (definición, establecimiento de reglas, calidad de la comunicación, factores internos y externos en la comuni
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > ca FCyT- Oro Verde] - Halsall, Fred: Redes de computadores e Internet / F. Halsall. - 5a ed. - Madrid: Pearson Educación, 2006. ISBN 9788478290833 [Disponible en Biblioteca FCyT- Oro Verde] - Huid
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > (Internet Control Message Protocol - Protocolo de mensajes de control de Internet), IGMP (Internet Group Management Protocol). Proveedores de servicio de internet (ISP), descripción Ipv6. **Unidad IX*
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > s de enrutamiento. Aspectos de diseño de la capa de red (Conmutación de paquetes de almacenamiento y reenvío, Servicios proporcionados a la capa de transporte, Implementación del servicio no orientado
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: UNDERWRITERS LABORATORIES (UL) -> www.ul.com | Pagina: 5]
   > PANDUIT -> www.panduit.com AMP -> www.tycoelectronics.com/components/ ETHEREAL -> www.ethereal.com SIEMENS -> www.sea.siemens.com/step/templates/lesson.mason?electricity:2:3:3

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta. El material menciona a CISCO como un sitio web de referencia sobre tecnologías y soluciones, e incluye bibliografía relacionada con la Academia de Networking de Cisco, pero no contiene datos sobre costos de certificaciones.

**Tokens:** entrada: 2195 | salida: 53 | total: 2248

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
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > **b.** **Alumno Regular** - 60 % de asistencia. - Aprobación del examen parcial teórico con una calificación igual o superior a 60 (sesenta) puntos. - Entrega de todos los trabajos en tiempo y
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > erior o igual a los 60 puntos. Tener aprobado con 60 puntos los tres parciales. **2-** Haber realizado y aprobado los dos trabajos Práctico impartido por la cátedra. **3-** Asistir al 80% de las clas
6. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **RÉGIMEN DE CURSADA** | Pagina: 2]
   > **Regularidad:** Asistencia: Según norma vigente Todos los trabajos prácticos aprobados 6/7 parciales aprobados con más del 50% **Promoción:** Régimen regular Obtener más del 70% en todos los parci
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > de diez (10) días hábiles respecto de la fecha de la mesa; en caso contrario, su evaluación se trasladará al turno siguiente. _El trabajo práctico integrador será recepcionado y revisado por el equi

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta, ya que los fragmentos proporcionados no especifican una calificación numérica mínima individual para la aprobación de los trabajos prácticos en ninguna de las materias mencionadas.

**Tokens:** entrada: 2103 | salida: 44 | total: 2147

---

### Pregunta 17

> - ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > ación. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en los vértices, análisis de casos especiales (soluciones múltiples, soluciones no acotadas y problemas in
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > ión de operaciones. Facilita el procesamiento de modelos matemáticos y estadísticos mediante una interfaz basada en menús para la carga de datos. - **TORA:** Herramienta educativa diseñada específ
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad I: -Introducción y Modelos Matemáticos-** Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del problema, construcción del modelo mate
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 3]
   > hojas de cálculo.
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > egiones factibles. - **LINGO (64 bits):** Una versión avanzada y más potente del motor LINDO. Está diseñado para modelar y resolver problemas de optimización de gran escala, permitiendo una integr
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > estructura del modelo y suposiciones. Métodos para obtener una solución básica inicial: Esquina Noroeste, Costo Mínimo y Aproximación de Vogel. Método MODI (Distribución Modificada) para la optimiza
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1661 | salida: 13 | total: 1674

---

### Pregunta 18 [ERROR]

> - ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

**Error:** Error calling model 'gemini-3.1-flash-lite-preview' (RESOURCE_EXHAUSTED): 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 15, model: gemini-3.1-flash-lite\nPlease retry in 26.01630179s.', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_content_free_tier_requests', 'quotaId': 'GenerateRequestsPerMinutePerProjectPerModel-FreeTier', 'quotaDimensions': {'model': 'gemini-3.1-flash-lite', 'location': 'global'}, 'quotaValue': '15'}]}, {'@type': 'type.googleapis.com/google.rpc.RetryInfo', 'retryDelay': '26s'}]}}

---

## Resumen de tokens

| Conversacion | Entrada | Salida | Total |
|---|---|---|---|
| 1 | 29840 | 2958 | 32798 |
| **Total** | **29840** | **2958** | **32798** |
