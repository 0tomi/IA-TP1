# Evaluacion — testGeminiPostMejoras1

_Iniciada: 2026-04-12 20:04:52_
_Ultima actualizacion: 2026-04-12 20:15:23_

**Estado:** completado
**Archivo de evaluacion:** `tests/evaluaciones/testGeminiPostMejoras.md`
**Preguntas:** 18 | **Conversaciones planificadas:** 3 | **Conversaciones iniciadas:** 3 | **Preguntas procesadas:** 54

## Conversacion 1

**Puntaje evaluado: 18 / 18**

**Parametros:**

| Parametro | Valor |
|---|---|
| top_k | 10 |
| retrieval_type | similarity_search |
| threshold | 0.5 |
| max_context_chunks | 10 |
| temperatura | 0.5 |
| debug | False |
| llm_provider | google |
| llm_model | gemini-3.1-flash-lite-preview |
| chunk_size | 600 |
| chunk_overlap | 100 |
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
   > en objetivos. Agentes que aprenden. **Capítulo II** **Procesos de Búsqueda.** Representación en un espacio de estados. Búsqueda Ciega, definición; búsqueda primero en amplitud, búsqueda de costo un
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > amiento de Agentes Basados en Conocimientos. **Capítulo IV** **Diseño de los Sistemas Expertos**. Definición y descripción de sus módulos componentes. Proceso de Adquisición de Conocimiento. Base d
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > ión del aporte parcial de cada regla. Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación de los disti
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Estructura de Control: Procedimientos de Inferencia; Interfase con el usuario. Memoria de Trabajo, Módulo generador de explicaciones al usuario. **Capítulo V** **Funcionalidad de los Sistemas Exper
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > a acumulación de información, por parte de una misma neurona. **Capítulo XII** **Sistemas Multi Agentes** Introducción a los sistemas multiagente, modelos formales. Metodologías de diseño basadas e
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > o de Procesamiento. Función de Transferencia. Condiciones de Convergencia. Proceso de Entrenamiento. Algoritmo de Modificación de los
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > cidad de Generalización. Tamaño del conjunto de patrones para el entrenamiento. Algoritmos de reducción (Pruning Algorithms). Deep Learning. Modelos Generativos **Capítulo XI** Redes Autoorganizadas
9. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > *Capítulo III** **Sistemas Basados en Conocimientos**. Conceptos básicos. Representación de Conocimientos. Estructuras basadas en Lógica. Lógica de Primer Orden. Reglas de Inferencia. Representación
10. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > simples entre conjuntos Difusos: Inclusión, Igualdad, Complementación, Intersección, Unión. Estructuras FAM (Fuzzy Associative Memories). Composición MAX-MIN. **Capítulo VII** **Sistemas** **Difusos

**Respuesta:**

Los contenidos de la asignatura Inteligencia Artificial se organizan en los siguientes capítulos:

*   **Capítulo I: Agentes Inteligentes.** Incluye definiciones, objetivos, herramientas y técnicas de IA. Se aborda el entorno de trabajo, propiedades de los entornos, estructura y programas de agentes (reactivos simples, basados en modelos, basados en objetivos y agentes que aprenden).
*   **Capítulo II: Procesos de Búsqueda.** Abarca la representación en un espacio de estados, búsqueda ciega (amplitud, costo uniforme, profundidad), búsqueda heurística (ordenada, recocido simulado, voraz primero el mejor, A* y comparación de heurísticos admisibles) y agentes basados en procesos de búsqueda.
*   **Capítulo III: Sistemas Basados en Conocimientos.** Trata conceptos básicos, representación basada en lógica (primer orden y reglas de inferencia), representación basada en objetos (clases, instancias, herencia, métodos y mensajes), representación mediante reglas y el comportamiento de agentes basados en conocimientos.
*   **Capítulo IV: Diseño de los Sistemas Expertos.** Incluye la definición y módulos componentes (base de conocimientos, estructura de control, procedimientos de inferencia, interfase con el usuario y memoria de trabajo), el módulo generador de explicaciones y el proceso de adquisición de conocimiento.
*   **Capítulo V: Funcionalidad de los Sistemas Expertos.** Se centra en los procesos de inferencia (encadenamiento hacia adelante y hacia atrás) y herramientas para su desarrollo.
*   **Capítulo VI y VII: Lógica Difusa (Fuzzy) y Sistemas Difusos.** Incluye conjuntos difusos, operaciones simples, estructuras FAM, composición MAX-MIN, representación mediante reglas lingüísticas, procesos de fuzzificación, inferencia (tratamiento paralelo, aporte parcial de reglas e integración de solución final), defuzzificación (métodos del centroide y máxima) y agentes basados en lógica difusa.
*   **Capítulo VIII: Redes Neuronales Artificiales (RNA).** Abarca generalidades, reseña histórica, clasificación, agentes basados en aprendizaje, el Perceptron Simple (elemento de procesamiento, función de transferencia, condiciones de convergencia y entrenamiento) y algoritmos de modificación de pesos.
*   **Capítulo XI: Redes Autoorganizadas.** Incluye características generales, la Red SOM (Kohonen), proceso de aprendizaje competitivo, realimentación lateral, algoritmo SOFM/SOM, función de vecindad, determinación de adaptación de pesos y modificaciones para evitar la acumulación excesiva de información. También se tratan la capacidad de generalización, tamaño del conjunto de entrenamiento, algoritmos de reducción (pruning), Deep Learning y modelos generativos.
*   **Capítulo XII: Sistemas Multi Agentes.** Comprende modelos formales, metodologías de diseño (Gaia: actividades, roles, interacción, agentes), organizaciones, comunicación y coordinación, protocolos de interacción, estándares (FIPA, lenguaje ACL) y tópicos avanzados.

**Tokens:** entrada: 2011 | salida: 622 | total: 2633

---

### Pregunta 2

> - ¿En qué materia se enseña el concepto de Lógica Difusa?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Estructura de Control: Procedimientos de Inferencia; Interfase con el usuario. Memoria de Trabajo, Módulo generador de explicaciones al usuario. **Capítulo V** **Funcionalidad de los Sistemas Exper
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > simples entre conjuntos Difusos: Inclusión, Igualdad, Complementación, Intersección, Unión. Estructuras FAM (Fuzzy Associative Memories). Composición MAX-MIN. **Capítulo VII** **Sistemas** **Difusos
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > ión del aporte parcial de cada regla. Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación de los disti
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > *Capítulo III** **Sistemas Basados en Conocimientos**. Conceptos básicos. Representación de Conocimientos. Estructuras basadas en Lógica. Lógica de Primer Orden. Reglas de Inferencia. Representación
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > amiento de Agentes Basados en Conocimientos. **Capítulo IV** **Diseño de los Sistemas Expertos**. Definición y descripción de sus módulos componentes. Proceso de Adquisición de Conocimiento. Base d
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > o de Procesamiento. Función de Transferencia. Condiciones de Convergencia. Proceso de Entrenamiento. Algoritmo de Modificación de los
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > en objetivos. Agentes que aprenden. **Capítulo II** **Procesos de Búsqueda.** Representación en un espacio de estados. Búsqueda Ciega, definición; búsqueda primero en amplitud, búsqueda de costo un
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos **Capítulo I** **Agentes Inteligentes** Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas p
9. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > cidad de Generalización. Tamaño del conjunto de patrones para el entrenamiento. Algoritmos de reducción (Pruning Algorithms). Deep Learning. Modelos Generativos **Capítulo XI** Redes Autoorganizadas
10. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > a acumulación de información, por parte de una misma neurona. **Capítulo XII** **Sistemas Multi Agentes** Introducción a los sistemas multiagente, modelos formales. Metodologías de diseño basadas e

**Respuesta:**

El concepto de Lógica Difusa se enseña en la materia Inteligencia Artificial.

**Tokens:** entrada: 2014 | salida: 17 | total: 2031

---

### Pregunta 3

> - ¿Cuál es el plan de estudios de Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > ificación del trabajo integrador se determinará exclusivamente en la mesa de examen, junto con la nota correspondiente a la instancia teórica, estableciéndose en ese momento la calificación final y
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: dentro de la plataforma Moodle. La organización será la siguiente | Pagina: 5]
   > - Inicio del curso: contendrá información general de la cátedra, incluyendo el programa, el equipo docente, el cronograma, los objetivos, los materiales utilizados, el enlace de videoconferencia, la
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: dentro de la plataforma Moodle. La organización será la siguiente | Pagina: 5]
   > - Desarrollo de contenidos: distribuidos en tres pestañas temáticas: - Introducción - Dimensión epistemológica - Dimensión estratégica - Dimensión técnica - Cada semana se habilitarán los co
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 3]
   > reseñas, resúmenes e informes de lectura. Características y organización de la escritura de los antecedentes. ¿Cómo construir un problema objeto de estudio?, ¿Ǫué
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: **Equipo docente:** PROFESORA RESPONSABLE ADJUNTO: ALEJANDRA MARǪUESIN; JEFE DE | Pagina: 1]
   > TRABAJOS PRÁCTICOS: TAMARA SUIVA. JEFE DE TRABAJOS PRÁCTICOS: JIMENA SANTA CRUZ; **Año de la carrera a la que pertenece la cátedra:** 4 **Régimen de la materia:** Anual **Carga horaria semanal:** 3
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > btención y análisis de información empírica. La comunicación de los resultados **Cronograma de trabajo** |METODOLOGÍA DE LA INVESTIGACIÓN- 2026|Col2|Col3|Col4|Col5| |---|---|---|---|---| |**Clase **
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > tivos. Las estrategias de indagación según la perspectiva metodológica seleccionada. El universo de análisis y la población. **Unidad 4: La dimensión de las técnicas de obtención y análisis de inform
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > preguntas le hago al problema? ¿Cómo construir el marco teórico? ¿Con qué categorías? Definición temporal y de contexto. Relación con los antecedentes relevados. Formulación de las preguntas que se
9. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > estudiantes los materiales y herramientas necesarios para la construcción autónoma del conocimiento. - Cada clase incluirá uno o más de los siguientes recursos: - Un video explicativo. - Materi
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 5]
   > prácticas se desarrollarán en grupos diferenciados bajo la coordinación de las docentes responsables. Además, se dispondrá de un espacio en la plataforma Moodle de la FCyT, que servirá como complem

**Respuesta:**

El plan de estudios de la asignatura Metodología de la Investigación se estructura en cuatro unidades temáticas:

*   **Unidad 1:** Introducción a la ciencia y conocimiento científico.
*   **Unidad 2:** La dimensión epistemológica.
*   **Unidad 3:** La dimensión de la estrategia general de investigación, que incluye el diseño de la investigación (cuantitativo o cualitativo), estrategias de indagación, universo de análisis y población.
*   **Unidad 4:** La dimensión de las técnicas de obtención y análisis de información empírica y la comunicación de los resultados, abordando procedimientos manuales e informáticos, análisis de datos y técnicas como entrevistas, observación y análisis documental.

Adicionalmente, el programa contempla el desarrollo de competencias para la escritura académica, tales como la elaboración de reseñas, resúmenes, informes de lectura y la construcción de antecedentes, el problema de investigación, el marco teórico, la formulación de preguntas y la definición de objetivos.

**Tokens:** entrada: 2096 | salida: 207 | total: 2303

---

### Pregunta 4

> - ¿Qué herramientas de software se recomiendan en la carrera para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > :** Herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el Método Simplex y el Método Gráfico. Es ideal para validaciones rápidas y visualización de r
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadísticos mediante una i
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > eal: proporcionalidad, aditividad, divisibilidad y certidumbre. Formulación de problemas de optimización. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en los
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad I: -Introducción y Modelos Matemáticos-** Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del problema, construcción del modelo mate
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > lida de variables. Interpretación de la tabla óptima. Aplicación del método de la "M Grande" y método de las "Dos Fases". Análisis de dualidad y sensibilidad básica en modelos lineales.
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > estructura del modelo y suposiciones. Métodos para obtener una solución básica inicial: Esquina Noroeste, Costo Mínimo y Aproximación de Vogel. Método MODI (Distribución Modificada) para la optimiza
9. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 3]
   > hojas de cálculo.
10. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > n de problemas de diligencia, asignación de recursos y reemplazo de equipos. Diferencias entre Programación Dinámica Determinística y Probabilística.

**Respuesta:**

Para la resolución de problemas de optimización lineal y otros modelos de gestión, la cátedra utiliza diversas herramientas informáticas, cada una con capacidades específicas que se vinculan con los contenidos de las unidades teóricas:

**Herramientas para Programación Lineal (Unidad II y III):**
*   **PHP Simplex:** Herramienta online ideal para validaciones rápidas y visualización de regiones factibles. Permite resolver problemas de programación lineal mediante el Método Gráfico (vinculado a la Unidad II) y el Método Simplex (Unidad III).
*   **TORA:** Diseñado con fines educativos, incluye módulos específicos para el Método Simplex, ofreciendo visualización paso a paso, lo cual facilita el aprendizaje de la construcción de tablas y criterios de entrada/salida de variables.
*   **LINDO:** Especializado en programación lineal, entera y no lineal, destaca por su sintaxis sencilla para ingresar ecuaciones y restricciones.
*   **LINGO:** Versión avanzada del motor LINDO, orientada a problemas de gran escala con capacidad de integración fluida con bases de datos y hojas de cálculo.

**Herramientas para Modelos de Gestión y Optimización (Unidades IV y V):**
*   **WinQSB 2.0:** Suite integral que abarca múltiples módulos. Además de programación lineal, permite abordar modelos de transporte, asignación (Unidad IV), programación dinámica y teoría de colas/gestión de inventarios (Unidad V).
*   **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadísticos mediante una interfaz basada en menús, cubriendo áreas como teoría de colas y gestión de inventarios.
*   **TORA:** Complementa los contenidos de la Unidad IV al incluir módulos específicos para modelos de transporte, redes y teoría de juegos.

En resumen, mientras herramientas como **PHP Simplex** y **TORA** se enfocan en el soporte didáctico para los algoritmos básicos (Simplex y Gráfico), **LINDO** y **LINGO** están orientados a la resolución técnica de modelos lineales. Por su parte, **WinQSB** y **Storm** actúan como soluciones integrales que cubren el espectro más amplio de la materia, incluyendo transporte, asignación, programación dinámica y gestión de inventarios.

**Tokens:** entrada: 1748 | salida: 496 | total: 2244

---

### Pregunta 5

> - ¿Qué instancias de recuperación nos provee Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > ncias de Recuperación:** La cátedra dispone de **dos oportunidades de** **recuperatorio** totales. Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se puede
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadísticos mediante una i
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > :** Herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el Método Simplex y el Método Gráfico. Es ideal para validaciones rápidas y visualización de r
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad I: -Introducción y Modelos Matemáticos-** Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del problema, construcción del modelo mate
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > eal: proporcionalidad, aditividad, divisibilidad y certidumbre. Formulación de problemas de optimización. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en los
9. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > **Condición del Alumno:** - **ALUMNO PROMOCIONADO:** El estudiante logrará la promoción directa si alcanza un promedio general de **80 puntos** - más entre los **1 parcial** previstos, no pudiendo
10. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > estructura del modelo y suposiciones. Métodos para obtener una solución básica inicial: Esquina Noroeste, Costo Mínimo y Aproximación de Vogel. Método MODI (Distribución Modificada) para la optimiza

**Respuesta:**

La cátedra de Investigación Operativa dispone de dos oportunidades de recuperatorio totales. Estas instancias pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no es posible aplicar ambos recuperatorios a un mismo examen parcial. La calificación obtenida en la instancia de recuperación sustituye automáticamente a la nota del examen original.

**Tokens:** entrada: 2005 | salida: 67 | total: 2072

---

### Pregunta 6

> - ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadísticos mediante una i
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > :** Herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el Método Simplex y el Método Gráfico. Es ideal para validaciones rápidas y visualización de r
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 3]
   > hojas de cálculo.
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > estructura del modelo y suposiciones. Métodos para obtener una solución básica inicial: Esquina Noroeste, Costo Mínimo y Aproximación de Vogel. Método MODI (Distribución Modificada) para la optimiza
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > lida de variables. Interpretación de la tabla óptima. Aplicación del método de la "M Grande" y método de las "Dos Fases". Análisis de dualidad y sensibilidad básica en modelos lineales.
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > n de problemas de diligencia, asignación de recursos y reemplazo de equipos. Diferencias entre Programación Dinámica Determinística y Probabilística.
9. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad I: -Introducción y Modelos Matemáticos-** Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del problema, construcción del modelo mate
10. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > a acumulación de información, por parte de una misma neurona. **Capítulo XII** **Sistemas Multi Agentes** Introducción a los sistemas multiagente, modelos formales. Metodologías de diseño basadas e

**Respuesta:**

El software TORA es una herramienta educativa diseñada específicamente para el aprendizaje de la Investigación Operativa. Incluye módulos para el Método Simplex —el cual permite una visualización paso a paso—, así como módulos para modelos de transporte, redes y teoría de juegos.

**Tokens:** entrada: 1713 | salida: 53 | total: 1766

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
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > reenvío, Servicios proporcionados a la capa de transporte, Implementación del servicio no orientado a la conexión, Implementación del servicio orientado a la conexión, Comparación entre las subredes d
5. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **BIBLIOGRAFÍA BASE** | Pagina: 2]
   > Elmasri, R. / Navathe, S. - Fundamentos de Sistemas de Bases de Datos (Addison Wesley) Silberschatz / Korth / Sudarshan - Fundamentos de Bases de Datos (Mc Graw Hill) Date, C.J. - Introducción a los S
6. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **MODALIDAD DE CLASES** | Pagina: 1]
   > A partir de este año la materia será dictada de manera bimodal. El cronograma será definido en su mayoría por la Facultad. Aún no confirmado. Los links de clases se encuentran en el aula virtual. Las
7. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **HORARIOS DE CLASE** | Pagina: 1]
   > Lunes: 13:30 a 15:30 (Teoría) Viernes: 17:00 a 19:00 (Práctica) Nota: Los horarios están en proceso de evaluación y pueden sufrir cambios
8. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **PRESENTACIÓN DE LA MATERIA** | Pagina: 1]
   > Facultad de Ciencia y Tecnología Universidad Autónoma de Entre Ríos (UADER)
9. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > sión, Enrutamiento para hosts móviles, Enrutamiento en redes ad hoc, Búsqueda de nodos en redes de igual a igual), RIP protocolo de enrutamiento por clase vector de distancia, configuración, VLSM y CI
10. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos vertidos en la teoría. Más dos trabajos Prácticos que se realizan en el ho

**Respuesta:**

Jorge L. Schmukler es el docente que integra el equipo de ambas cátedras. En la materia Comunicaciones y Redes figura como parte del equipo docente, mientras que en Bases de Datos Avanzadas es el responsable de la parte práctica.

**Tokens:** entrada: 1628 | salida: 51 | total: 1679

---

### Pregunta 8

> - ¿Qué otra asignatura, además de la propia materia de Inteligencia Artificial, incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas?

**Chunks de contexto:**

1. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 4. El impacto de la inteligencia artificial en la gestión del talento. | Pagina: 2]
   > _**Bibliografía Nacional:**_ Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales. **Uni
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > amiento de Agentes Basados en Conocimientos. **Capítulo IV** **Diseño de los Sistemas Expertos**. Definición y descripción de sus módulos componentes. Proceso de Adquisición de Conocimiento. Base d
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos **Capítulo I** **Agentes Inteligentes** Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas p
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (2
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > a acumulación de información, por parte de una misma neurona. **Capítulo XII** **Sistemas Multi Agentes** Introducción a los sistemas multiagente, modelos formales. Metodologías de diseño basadas e
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > en objetivos. Agentes que aprenden. **Capítulo II** **Procesos de Búsqueda.** Representación en un espacio de estados. Búsqueda Ciega, definición; búsqueda primero en amplitud, búsqueda de costo un
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > o de Procesamiento. Función de Transferencia. Condiciones de Convergencia. Proceso de Entrenamiento. Algoritmo de Modificación de los
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > cidad de Generalización. Tamaño del conjunto de patrones para el entrenamiento. Algoritmos de reducción (Pruning Algorithms). Deep Learning. Modelos Generativos **Capítulo XI** Redes Autoorganizadas
9. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > *Capítulo III** **Sistemas Basados en Conocimientos**. Conceptos básicos. Representación de Conocimientos. Estructuras basadas en Lógica. Lógica de Primer Orden. Reglas de Inferencia. Representación
10. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > ión del aporte parcial de cada regla. Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación de los disti

**Respuesta:**

La asignatura de Informática y Recursos Humanos incluye explícitamente el impacto de la inteligencia artificial en su unidad temática "Gestión del Talento en la Era Digital", específicamente bajo el apartado "El impacto de la inteligencia artificial en la gestión del talento".

**Tokens:** entrada: 1930 | salida: 51 | total: 1981

---

### Pregunta 9

> - Los requisitos para regularizar en Bases de Datos Avanzadas y en Redes y Comunicaciones, ¿son iguales? ¿Qué diferencias tienen?

**Chunks de contexto:**

1. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **RÉGIMEN DE CURSADA** | Pagina: 2]
   > **Regularidad:** Asistencia: Según norma vigente Todos los trabajos prácticos aprobados 6/7 parciales aprobados con más del 50% **Promoción:** Régimen regular Obtener más del 70% en todos los parci
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > PROMOCIONADO REGULAR LIBRE El alumno accederá a la condición de **PROMOCIÓN** si cumple con las siguientes condiciones de cátedra: **1 -** Obtener en los 3 parciales, una calificación promedio sup
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > iguientes condiciones de cátedra: **1 -** Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos. Tener aprobado con 60 puntos los tres parciales. **2-** Haber realiz
4. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **CANALES DE COMUNICACIÓN** | Pagina: 2]
   > Correo: Lista de mail (consultas y comunicación de rutina) Aula virtual: Material académico - Clave de matriculación: bda2023 (ÚNICO MEDIO OFICIAL) Telegram: https://t.me/+c7PPIrc9nQM4MzEx (avisos y n
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos vertidos en la teoría. Más dos trabajos Prácticos que se realizan en el ho
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > ma salvo que se presente justificativo medico o que sea entendida justificada la ausencia. **Evaluación Final:** El alumno con condición de REGULAR, deberá rendir un examen de los temas teóricos y pr
7. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **SOFTWARE REQUERIDO** | Pagina: 2]
   > PostgreSQL: versión 9.6 o superior SQL Server: versión 2016 o superior QGIS: versión compatible con PostgreSQL Anaconda (Python): últimas versiones
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > reenvío, Servicios proporcionados a la capa de transporte, Implementación del servicio no orientado a la conexión, Implementación del servicio orientado a la conexión, Comparación entre las subredes d
9. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > de los parciales, no pudiéndose utilizar en un mismo parcial los dos recuperatorios. La nota obtenida en este reemplaza a la obtenida en el parcial que se recupera La cátedra dará el resultado de cada
10. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **MODALIDAD DE CLASES** | Pagina: 1]
   > A partir de este año la materia será dictada de manera bimodal. El cronograma será definido en su mayoría por la Facultad. Aún no confirmado. Los links de clases se encuentran en el aula virtual. Las

**Respuesta:**

Los requisitos para regularizar en Bases de Datos Avanzadas y en Comunicación y Redes no son iguales; presentan diferencias significativas en cuanto a la exigencia de asistencia, la aprobación de trabajos prácticos y el rendimiento en las evaluaciones.

Las diferencias y puntos clave son los siguientes:

*   **Asistencia:** En Bases de Datos Avanzadas, la asistencia se rige según la norma vigente de la facultad. En Comunicación y Redes, se exige un porcentaje específico del 80% de asistencia a las clases teóricas y prácticas.
*   **Trabajos Prácticos:** En Bases de Datos Avanzadas, el alumno debe tener aprobados todos los trabajos prácticos. En Comunicación y Redes, el requisito es haber realizado y aprobado los dos trabajos prácticos impartidos por la cátedra.
*   **Evaluaciones Parciales:**
    *   **Bases de Datos Avanzadas:** Se requiere tener aprobados 6 de los 7 parciales con una calificación superior al 50%.
    *   **Comunicación y Redes:** Se requiere obtener un promedio superior o igual a 60 puntos en los 3 parciales, debiendo aprobar cada uno de ellos con una nota mínima de 60 puntos.

En resumen, mientras que Bases de Datos Avanzadas se enfoca en un volumen mayor de evaluaciones (6 de 7) con un umbral de aprobación del 50%, Comunicación y Redes establece un sistema de promedios y notas mínimas para sus 3 parciales, sumado a un control de asistencia porcentual estricto.

**Tokens:** entrada: 1885 | salida: 333 | total: 2218

---

### Pregunta 10

> - ¿Cuál es el porcentaje de asistencia a clases que exigen en común las materias de Investigación Operativa, Comunicaciones y Redes, y Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > iguientes condiciones de cátedra: **1 -** Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos. Tener aprobado con 60 puntos los tres parciales. **2-** Haber realiz
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > **Condición del Alumno:** - **ALUMNO PROMOCIONADO:** El estudiante logrará la promoción directa si alcanza un promedio general de **80 puntos** - más entre los **1 parcial** previstos, no pudiendo
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > s se desarrollarán estrictamente en los bloques horarios asignados a la materia. La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen repr
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > PROMOCIONADO REGULAR LIBRE El alumno accederá a la condición de **PROMOCIÓN** si cumple con las siguientes condiciones de cátedra: **1 -** Obtener en los 3 parciales, una calificación promedio sup
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > **b.** **Alumno Regular** - 60 % de asistencia. - Aprobación del examen parcial teórico con una calificación igual o superior a 60 (sesenta) puntos. - Entrega de todos los trabajos en tiempo y
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 16]
   > Para acceder a la condición de Promoción Directa, el/la estudiante deberá cumplir con los siguientes requisitos: - 80 % de asistencia a la cursada. - Aprobación del examen parcial teórico con una
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > de los parciales, no pudiéndose utilizar en un mismo parcial los dos recuperatorios. La nota obtenida en este reemplaza a la obtenida en el parcial que se recupera La cátedra dará el resultado de cada
9. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > ncias de Recuperación:** La cátedra dispone de **dos oportunidades de** **recuperatorio** totales. Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se puede
10. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > ma salvo que se presente justificativo medico o que sea entendida justificada la ausencia. **Evaluación Final:** El alumno con condición de REGULAR, deberá rendir un examen de los temas teóricos y pr

**Respuesta:**

No existe un porcentaje de asistencia común para las tres materias.

Los requisitos de asistencia son los siguientes:

*   **Investigación Operativa:** Exige un **80%** de asistencia a las clases teóricas y prácticas para obtener la regularidad y para la promoción directa.
*   **Comunicación y Redes:** Exige un **80%** de asistencia a las clases teóricas y prácticas para todas sus condiciones (promoción, regularidad y libre).
*   **Metodología de la Investigación:** Los requisitos varían según la condición:
    *   Para **Alumno Regular**, se exige un **60%** de asistencia.
    *   Para **Promoción Directa**, se exige un **80%** de asistencia.

**Tokens:** entrada: 2109 | salida: 162 | total: 2271

---

### Pregunta 11

> - Un proyecto integrador requiere utilizar un software para resolver problemas de optimización a gran escala que pueda conectarse de forma fluida con bases de datos espaciales. Según las herramientas enseñadas en las materias, ¿qué combinación de software visto en Bases de Datos Avanzadas e Investigación Operativa sería la más adecuada para este objetivo?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > :** Herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el Método Simplex y el Método Gráfico. Es ideal para validaciones rápidas y visualización de r
2. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **SOFTWARE REQUERIDO** | Pagina: 2]
   > PostgreSQL: versión 9.6 o superior SQL Server: versión 2016 o superior QGIS: versión compatible con PostgreSQL Anaconda (Python): últimas versiones
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadísticos mediante una i
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > lida de variables. Interpretación de la tabla óptima. Aplicación del método de la "M Grande" y método de las "Dos Fases". Análisis de dualidad y sensibilidad básica en modelos lineales.
7. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **BIBLIOGRAFÍA BASE** | Pagina: 2]
   > Elmasri, R. / Navathe, S. - Fundamentos de Sistemas de Bases de Datos (Addison Wesley) Silberschatz / Korth / Sudarshan - Fundamentos de Bases de Datos (Mc Graw Hill) Date, C.J. - Introducción a los S
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > eal: proporcionalidad, aditividad, divisibilidad y certidumbre. Formulación de problemas de optimización. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en los
9. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > estructura del modelo y suposiciones. Métodos para obtener una solución básica inicial: Esquina Noroeste, Costo Mínimo y Aproximación de Vogel. Método MODI (Distribución Modificada) para la optimiza
10. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **PRESENTACIÓN DE LA MATERIA** | Pagina: 1]
   > Facultad de Ciencia y Tecnología Universidad Autónoma de Entre Ríos (UADER)

**Respuesta:**

Para resolver problemas de optimización a gran escala con integración fluida a bases de datos, la combinación más adecuada es **LINGO** y **PostgreSQL** (complementado con **QGIS**).

Esta elección se fundamenta en las capacidades específicas de cada herramienta:

*   **Para la optimización:** **LINGO** es la herramienta diseñada específicamente para modelar y resolver problemas de optimización de gran escala, destacándose por permitir una integración fluida con bases de datos, superando en potencia al motor LINDO.
*   **Para la gestión de datos y componentes espaciales:** **PostgreSQL** (versión 9.6 o superior) es el software de base de datos requerido, y su integración con **QGIS** permite el manejo de datos espaciales, proporcionando el entorno necesario para la gestión de la información que requiere el proyecto.

Otras herramientas de Investigación Operativa mencionadas, como WinQSB, Storm, TORA o PHP Simplex, están orientadas al análisis cuantitativo, la educación o la resolución de problemas de menor escala, pero no cuentan con la capacidad de integración avanzada con bases de datos que ofrece LINGO.

**Tokens:** entrada: 1743 | salida: 241 | total: 1984

---

### Pregunta 12

> - Si un estudiante desea investigar sobre el impacto de los "Agentes que aprenden" y las "Redes Neuronales" en la selección de personal y el teletrabajo en Argentina, ¿qué normativas legales y temas específicos de los programas de Inteligencia Artificial y RRHH debería cruzar en su marco teórico?

**Chunks de contexto:**

1. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: IV. BIBLIOGRAFÍA GENERAL | Pagina: 3]
   > entaria:**_ Reglamento de Teletrabajo en Argentina. Legislación sobre delitos informáticos en Argentina. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relac
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 4. El impacto de la inteligencia artificial en la gestión del talento. | Pagina: 2]
   > _**Bibliografía Nacional:**_ Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales. **Uni
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 2]
   > Reglamento de Teletrabajo en Argentina. Nicolás S. Tato, El Derecho Informático - Aspectos Fundamentales. Mariana Nazar, Tecnologías, información y derechos. **Unidad 2:** **Relaciones Humanas en e
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 6. Desafíos éticos y sociales de la tecnología en el ámbito laboral. | Pagina: 1]
   > _**Bibliografía Nacional:**_ Ley de Teletrabajo (Ley 27.555).
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: IV. BIBLIOGRAFÍA GENERAL | Pagina: 3]
   > _**Bibliografía Básica:**_ Nicolás S. Tato, El Derecho Informático - Aspectos Fundamentales. Mariana Nazar, Tecnologías, información y derechos. Gonzalo Ana Dobratinich, derecho y nuevas tecnología
6. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 5. comercio electrónico, manifestación del consentimiento en internet | Pagina: 3]
   > _**Bibliografía Nacional:**_ Ley de Teletrabajo (Ley 27.555) Código Civil y Comercial de la Nación (aspectos relacionados con contratos digitales). Artículos académicos sobre la economía gig y el t
7. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: **I. FUNDAMENTACIÓN** | Pagina: 1]
   > igital. Además, se abordarán aspectos legales fundamentales para comprender el impacto normativo de las TIC en el ámbito laboral, tomando como base la legislación argentina y los aportes de autores na
8. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 3]
   > Legislación sobre delitos informáticos en Argentina. Ley Nacional de Protección de Datos Personales (Ley 25.326). Ley Propiedad Intelectual (Ley 11.723) y su modificatoria. **Unidad 5: Trabajo Autó
9. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 4. Derecho a la desconexión digital y equilibrio entre vida personal y laboral. | Pagina: 2]
   > _**Bibliografía Nacional:**_ Ley Nacional de Protección de Datos Personales (Ley 25.326). Código Civil y Comercial de la Nación (aspectos relacionados con contratos digitales y firma electrónica).
10. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > ión del aporte parcial de cada regla. Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación de los disti

**Respuesta:**

Para investigar el impacto de los agentes que aprenden y las redes neuronales en la selección de personal y el teletrabajo en Argentina, el marco teórico debe integrar los siguientes componentes normativos y temáticos:

### Normativa Legal Aplicable
Para analizar el impacto legal de estas tecnologías en el ámbito laboral argentino, deben considerarse los siguientes instrumentos:
*   **Protección de datos y derechos digitales:** La **Ley Nacional de Protección de Datos Personales (Ley 25.326)** y la obra de Mariana Nazar, *Tecnologías, información y derechos*, son fundamentales para abordar el tratamiento de datos en procesos automatizados.
*   **Marco contractual y propiedad intelectual:** El **Código Civil y Comercial de la Nación** (específicamente en lo referente a contratos digitales y firma electrónica) y la **Ley de Propiedad Intelectual (Ley 11.723 y su modificatoria 25.036)**.
*   **Regulación del teletrabajo:** La **Ley de Teletrabajo (Ley 27.555)** y su reglamento asociado, que establecen el marco normativo para las relaciones laborales a distancia.
*   **Seguridad jurídica:** La legislación sobre delitos informáticos en Argentina y los aportes de Nicolás S. Tato en *El Derecho Informático - Aspectos Fundamentales*, junto con la obra de Gonzalo Ana Dobratinich, *Derecho y nuevas tecnologías*.

### Temas Específicos de Inteligencia Artificial y RRHH
El estudiante debe cruzar la normativa anterior con los siguientes núcleos temáticos:

1.  **Fundamentos técnicos de IA:**
    *   **Redes Neuronales Artificiales (RNA):** Conceptos básicos, clasificación y agentes basados en procesos de aprendizaje.
    *   **Perceptron Simple:** Entrenamiento, funciones de transferencia y condiciones de convergencia.
    *   **Sistemas Difusos:** Agentes basados en lógica difusa, procesos de defuzzificación y métodos de integración de soluciones.

2.  **Impacto en la gestión laboral:**
    *   **Gestión del Talento:** Análisis de la transformación del trabajo y el impacto de la IA en las relaciones laborales.
    *   **Derecho a la desconexión:** Equilibrio entre la vida personal y laboral en entornos digitales.
    *   **Nuevas formas de trabajo:** Economía gig, trabajo autónomo y plataformas digitales, considerando la manifestación del consentimiento en internet y los desafíos éticos y sociales de la tecnología en el ámbito laboral.

La integración de estos elementos permite abordar cómo la capacidad de aprendizaje de los agentes y las redes neuronales interactúa con la legislación argentina vigente, especialmente en lo que respecta a la validez de los contratos digitales, la protección de la información del candidato o trabajador y el cumplimiento de las condiciones laborales en la era digital.

**Tokens:** entrada: 1622 | salida: 596 | total: 2218

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
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 12]
   > tu.be/yBL4Hu9n Fic) María Teresa Sirven Clase 2 Maestría Tecnología Educativa [https://youtu.be/dydibttPBGU](https://youtu.be/dydibttPBGU) **Operadores Booleanos para búsquedas**
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: AÑO ACADEMICO: 2023 | Pagina: 1]
   > PLAN DE ESTUDIO: 2010 (Resolución No 397/10 UADER)
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 13]
   > - Yuni, J y Urbano, C (2016) Técnicas para investigar 2: Recursos metodológicos para la preparación de proyectos de investigación. Editorial Brujas: Argentina _Material audiovisual de la unidad_
9. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 12]
   > - Natale, Lucía (Coordinadora) (2013). En carrera: escritura y lectura de textos académicos y profesionales. Argentina. Universidad Nacional de Ǫuilmes. Visto en [https://ediciones.ungs.edu.ar/wp-co

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1433 | salida: 13 | total: 1446

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
   > amiento de Agentes Basados en Conocimientos. **Capítulo IV** **Diseño de los Sistemas Expertos**. Definición y descripción de sus módulos componentes. Proceso de Adquisición de Conocimiento. Base d
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > *Capítulo III** **Sistemas Basados en Conocimientos**. Conceptos básicos. Representación de Conocimientos. Estructuras basadas en Lógica. Lógica de Primer Orden. Reglas de Inferencia. Representación
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > **Capítulo IX** **Redes** **Perceptron** **Multicapa**, estructura básica. Proceso de Entrenamiento Backpropagation (BP). Interpretación heurística y matemática del procedimiento BP. Término de Momen
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > a acumulación de información, por parte de una misma neurona. **Capítulo XII** **Sistemas Multi Agentes** Introducción a los sistemas multiagente, modelos formales. Metodologías de diseño basadas e
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos **Capítulo I** **Agentes Inteligentes** Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas p
9. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > en objetivos. Agentes que aprenden. **Capítulo II** **Procesos de Búsqueda.** Representación en un espacio de estados. Búsqueda Ciega, definición; búsqueda primero en amplitud, búsqueda de costo un
10. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > ión del aporte parcial de cada regla. Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación de los disti

**Respuesta:**

El Ing. Jorge L. Schmukler forma parte del equipo docente en las siguientes materias:

*   **Bases de Datos Avanzadas:** Se desempeña en el área de Práctica.
*   **Comunicaciones y Redes:** Integra el equipo docente junto al Lic. Luciano M. Caisso.

Respecto a la materia **Inteligencia Artificial**, no dispongo de información en mis documentos que confirme que el Ing. Jorge L. Schmukler forme parte de su equipo docente.

**Tokens:** entrada: 1886 | salida: 105 | total: 1991

---

### Pregunta 15

> - ¿Cuál es el costo de la certificación oficial de Cisco que se menciona como opcional en la planificación?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > **Obligatoria** - Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] - Cisco Systems: Academia de Networking de Cisco Systems: Guía del primer añ
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > rid: Pearson Educación, 2006. ISBN 9788478290833 [Disponible en Biblioteca FCyT- Oro Verde] - Huidobro Moya, José Manuel: Redes de datos y convergencia IP / J. M. Huidobro Moya, Ramón Jesús Millán T
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > e de direccionamiento (clase a, b, c, d y e). Prefijo y Mascara de red. Lógica de and. Calculo de direcciones. División de subredes (por clase y vlsm (mascara de subred de longitud variable)), icmpv4
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Sitios web sobre normativas, tecnologías y soluciones, opcional** | Pagina: 5]
   > IETF -> www.ietf.org IEEE -> www.ieee.org ISO -> www.iso.org CISCO -> www.cisco.com IANA -> www.iana.org ISOC -> www.isoc.org ARIN -> www.arin.net LACNIC -> http://lacnic.net/sp/ LAC IPV6 TF -> www.la
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > Comunicación en un mundo centrado en la red, herramientas de comunicación. La comunicación (definición, establecimiento de reglas, calidad de la comunicación, factores internos y externos en la comuni
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > nstalación y configuración de hardware y software. - USERS-CISCO. [Disponible en Biblioteca FCyT- Oro Verde] - Comer, Douglas E.: Redes de computadoras, Internet e Interredes / D. E. Comer. - Méxi
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > rango extendido), Tipos de Vlan (Vlan de Datos, Predeterminada, Nativa, Administración, Voz), Configuración de Vlan, Modos de puertos de switch de VLAN (Vlan Estática, Dinámica y Voz), Control de los
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > ropósito de IOS como Sistema** **Operativo de red**, Explicar cómo acceder al IOS y cómo explorarlo para configurar los dispositivos de red, Describir la estructura de comandos, Configurar nombres de
9. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > retroceso exponencial binario, LAN Inalámbricas IEEE 802.11, Banda Ancha Inalámbrica IEEE 802.16, Comparación entre el estándar IEEE 802.11 y IEEE 802.16, Bluetooh, Conmutación en la capa de enlace (R
10. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: UNDERWRITERS LABORATORIES (UL) -> www.ul.com | Pagina: 5]
   > PANDUIT -> www.panduit.com AMP -> www.tycoelectronics.com/components/ ETHEREAL -> www.ethereal.com SIEMENS -> www.sea.siemens.com/step/templates/lesson.mason?electricity:2:3:3

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta. La planificación menciona a Cisco como una organización dentro de los sitios web opcionales sobre normativas, tecnologías y soluciones, y lista bibliografía relacionada con la Academia de Networking de Cisco, pero no proporciona detalles ni costos sobre certificaciones oficiales.

**Tokens:** entrada: 2479 | salida: 61 | total: 2540

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
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > iguientes condiciones de cátedra: **1 -** Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos. Tener aprobado con 60 puntos los tres parciales. **2-** Haber realiz
5. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **RÉGIMEN DE CURSADA** | Pagina: 2]
   > **Regularidad:** Asistencia: Según norma vigente Todos los trabajos prácticos aprobados 6/7 parciales aprobados con más del 50% **Promoción:** Régimen regular Obtener más del 70% en todos los parci
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > **b.** **Alumno Regular** - 60 % de asistencia. - Aprobación del examen parcial teórico con una calificación igual o superior a 60 (sesenta) puntos. - Entrega de todos los trabajos en tiempo y
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos vertidos en la teoría. Más dos trabajos Prácticos que se realizan en el ho
9. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 9]
   > **Programa de trabajos prácticos:** Tp 1: Escritura académica. Se solicita a los estudiantes seleccionar un artículo de investigación sobre un tema de interés específico relacionado al campo profesi
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > instancia_ _de revisión, el/la estudiante quedará habilitado/a para presentarse a la mesa de examen final._ _No se realizarán nuevas instancias de corrección previas a la mesa. La evaluación definit

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta, ya que los textos proporcionados no especifican una calificación numérica mínima individual para cada trabajo práctico en ninguna de las materias mencionadas.

**Tokens:** entrada: 2139 | salida: 39 | total: 2178

---

### Pregunta 17

> - ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > :** Herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el Método Simplex y el Método Gráfico. Es ideal para validaciones rápidas y visualización de r
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > eal: proporcionalidad, aditividad, divisibilidad y certidumbre. Formulación de problemas de optimización. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en los
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadísticos mediante una i
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > lida de variables. Interpretación de la tabla óptima. Aplicación del método de la "M Grande" y método de las "Dos Fases". Análisis de dualidad y sensibilidad básica en modelos lineales.
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 3]
   > hojas de cálculo.
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad I: -Introducción y Modelos Matemáticos-** Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del problema, construcción del modelo mate
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > estructura del modelo y suposiciones. Métodos para obtener una solución básica inicial: Esquina Noroeste, Costo Mínimo y Aproximación de Vogel. Método MODI (Distribución Modificada) para la optimiza
9. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
10. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > n de problemas de diligencia, asignación de recursos y reemplazo de equipos. Diferencias entre Programación Dinámica Determinística y Probabilística.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1737 | salida: 13 | total: 1750

---

### Pregunta 18

> - ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > s se desarrollarán estrictamente en los bloques horarios asignados a la materia. La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen repr
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > ncias de Recuperación:** La cátedra dispone de **dos oportunidades de** **recuperatorio** totales. Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se puede
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > **Condición del Alumno:** - **ALUMNO PROMOCIONADO:** El estudiante logrará la promoción directa si alcanza un promedio general de **80 puntos** - más entre los **1 parcial** previstos, no pudiendo
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > ESO DE INVIERNO/ MESAS DE EXAMENES FINALES| |16|06 de agosto|Virtual|Teoría|Repaso del proceso de| |||||investigación| |17|13 de agosto|Virtual|Tutorías|Tutorías| |18|20 de agosto|**_Presencial (cambi
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > |12|28 de mayo|Virtual|Teoría|Col5| |---|---|---|---|---| |13|04 de junio|**Presencial**|**Teoría**|Marco metodológico I: enfoque y<br>tipo de investigación / muestra| |14|11 de junio|Virtual|Práctica
7. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **HORARIOS DE CLASE** | Pagina: 1]
   > Lunes: 13:30 a 15:30 (Teoría) Viernes: 17:00 a 19:00 (Práctica) Nota: Los horarios están en proceso de evaluación y pueden sufrir cambios
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad I: -Introducción y Modelos Matemáticos-** Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del problema, construcción del modelo mate
9. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > eal: proporcionalidad, aditividad, divisibilidad y certidumbre. Formulación de problemas de optimización. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en los
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > **b.** **Alumno Regular** - 60 % de asistencia. - Aprobación del examen parcial teórico con una calificación igual o superior a 60 (sesenta) puntos. - Entrega de todos los trabajos en tiempo y

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 2204 | salida: 13 | total: 2217

---

## Conversacion 2

**Puntaje evaluado: 18 / 18**

**Parametros modificados respecto a la conversacion anterior:**

| Parametro | Valor |
|---|---|
| chunking_technique | recursive |

### Pregunta 1

> - ¿Cuáles son los contenidos de la materia Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos **Capítulo I** **Agentes Inteligentes** Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas p
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > **Capítulo II** **Procesos de Búsqueda.** Representación en un espacio de estados. Búsqueda Ciega, definición; búsqueda primero en amplitud, búsqueda de costo uniforme; búsqueda primero en profundid
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Estructura de Control: Procedimientos de Inferencia; Interfase con el usuario. Memoria de Trabajo, Módulo generador de explicaciones al usuario. **Capítulo V** **Funcionalidad de los Sistemas Exper
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Proceso de Inferencia. Tratamiento paralelo de las reglas. Determinación del aporte parcial de cada regla. Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Comportamiento de Agentes Basados en Conocimientos. **Capítulo IV** **Diseño de los Sistemas Expertos**. Definición y descripción de sus módulos componentes. Proceso de Adquisición de Conocimiento.
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > **Capítulo III** **Sistemas Basados en Conocimientos**. Conceptos básicos. Representación de Conocimientos. Estructuras basadas en Lógica. Lógica de Primer Orden. Reglas de Inferencia. Representación
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > **Red Perceptron Simple.** Elemento de Procesamiento. Función de Transferencia. Condiciones de Convergencia. Proceso de Entrenamiento. Algoritmo de Modificación de los
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > Modificación del algoritmo SOM para evitar una excesiva acumulación de información, por parte de una misma neurona. **Capítulo XII** **Sistemas Multi Agentes** Introducción a los sistemas multiagen
9. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > Regiones de Decisión. Modo de operación autoasociativo. **Capítulo X** **Generalización en las RNA,** definición, factores que influyen en la capacidad de Generalización. Tamaño del conjunto de pat
10. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > **Capítulo IX** **Redes** **Perceptron** **Multicapa**, estructura básica. Proceso de Entrenamiento Backpropagation (BP). Interpretación heurística y matemática del procedimiento BP. Término de Momen

**Respuesta:**

La materia Inteligencia Artificial se estructura en los siguientes contenidos:

*   **Agentes Inteligentes:** Introducción a la IA, definiciones, objetivos, herramientas y técnicas. Se aborda el entorno de trabajo, sus propiedades, la estructura y programas de agentes (reactivos simples, basados en modelos, basados en objetivos y agentes que aprenden).
*   **Procesos de Búsqueda:** Representación en espacio de estados. Incluye búsqueda ciega (amplitud, costo uniforme, profundidad), búsqueda heurística (ordenada, recocido simulado, voraz primero el mejor, A* y comparación de heurísticos admisibles) y agentes basados en procesos de búsqueda.
*   **Sistemas Basados en Conocimientos:** Conceptos, representación (lógica de primer orden, basada en objetos con clases, instancias, herencia, métodos y mensajes, y representación mediante reglas) y comportamiento de agentes basados en conocimientos.
*   **Sistemas Expertos:** Diseño y módulos (base de conocimientos, procesos de inferencia, estructura de control, interfaz con el usuario y módulo generador de explicaciones). Incluye procesos de inferencia (encadenamiento hacia adelante y hacia atrás) y herramientas de desarrollo.
*   **Lógica Difusa:** Procesos de inferencia, tratamiento paralelo de reglas, integración de la solución difusa, defuzzificación (método del centroide y de máxima) y agentes basados en lógica difusa.
*   **Redes Neuronales Artificiales (RNA):** Reseña histórica, clasificación y agentes basados en aprendizaje.
    *   **Perceptron Simple:** Elemento de procesamiento, función de transferencia, condiciones de convergencia, entrenamiento y regiones de decisión.
    *   **Perceptron Multicapa:** Estructura, entrenamiento mediante Backpropagation (BP), superficies de error, mínimos locales/globales, saturación prematura y modo autoasociativo.
    *   **Redes Autoorganizadas:** Red SOM (Kohonen), aprendizaje competitivo, realimentación lateral, función de vecindad y modificación del algoritmo SOM.
    *   **Generalización:** Factores que influyen, tamaño del conjunto de entrenamiento, algoritmos de reducción (pruning), Deep Learning y modelos generativos.
*   **Sistemas Multiagente:** Introducción y modelos formales. Incluye metodologías de diseño (Gaia: modelos de actividades, roles, interacción y agentes), organizaciones, interacciones, comunicación, coordinación, protocolos, estándares (FIPA, lenguaje ACL) y tópicos avanzados.

**Tokens:** entrada: 1868 | salida: 528 | total: 2396

---

### Pregunta 2

> - ¿En qué materia se enseña el concepto de Lógica Difusa?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Herramientas para el desarrollo de Sistemas Expertos. **Capítulo VI** **Lógica Difusa (Fuzzy).** Consideraciones generales, Conjuntos Difusos, definición. Operaciones simples entre conjuntos Difusos
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Proceso de Inferencia. Tratamiento paralelo de las reglas. Determinación del aporte parcial de cada regla. Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > **Capítulo III** **Sistemas Basados en Conocimientos**. Conceptos básicos. Representación de Conocimientos. Estructuras basadas en Lógica. Lógica de Primer Orden. Reglas de Inferencia. Representación
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Estructura de Control: Procedimientos de Inferencia; Interfase con el usuario. Memoria de Trabajo, Módulo generador de explicaciones al usuario. **Capítulo V** **Funcionalidad de los Sistemas Exper
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos **Capítulo I** **Agentes Inteligentes** Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas p
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Comportamiento de Agentes Basados en Conocimientos. **Capítulo IV** **Diseño de los Sistemas Expertos**. Definición y descripción de sus módulos componentes. Proceso de Adquisición de Conocimiento.
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > **Capítulo II** **Procesos de Búsqueda.** Representación en un espacio de estados. Búsqueda Ciega, definición; búsqueda primero en amplitud, búsqueda de costo uniforme; búsqueda primero en profundid
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > Modificación del algoritmo SOM para evitar una excesiva acumulación de información, por parte de una misma neurona. **Capítulo XII** **Sistemas Multi Agentes** Introducción a los sistemas multiagen
9. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > **Red Perceptron Simple.** Elemento de Procesamiento. Función de Transferencia. Condiciones de Convergencia. Proceso de Entrenamiento. Algoritmo de Modificación de los
10. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > **Capítulo IX** **Redes** **Perceptron** **Multicapa**, estructura básica. Proceso de Entrenamiento Backpropagation (BP). Interpretación heurística y matemática del procedimiento BP. Término de Momen

**Respuesta:**

El concepto de Lógica Difusa se enseña en la materia Inteligencia Artificial.

**Tokens:** entrada: 1872 | salida: 17 | total: 1889

---

### Pregunta 3

> - ¿Cuál es el plan de estudios de Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > integrador se determinará exclusivamente en la mesa de examen, junto con la nota correspondiente a la instancia teórica, estableciéndose en ese momento la calificación final y la condición de aproba
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: dentro de la plataforma Moodle. La organización será la siguiente | Pagina: 5]
   > - Inicio del curso: contendrá información general de la cátedra, incluyendo el programa, el equipo docente, el cronograma, los objetivos, los materiales utilizados, el enlace de videoconferencia, la
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: dentro de la plataforma Moodle. La organización será la siguiente | Pagina: 5]
   > curso. - Desarrollo de contenidos: distribuidos en tres pestañas temáticas: - Introducción - Dimensión epistemológica - Dimensión estratégica - Dimensión técnica - Cada semana se habilitar
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > objetivos y relación de los objetivos con las preguntas de la investigación. **Unidad 3: La dimensión de la estrategia general de investigación** ¿Cómo se va a estudiar el problema? Tipo de diseños c
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 3]
   > orientar la búsqueda de información relevante. Tipo de fuentes, obras y producciones que pueden consultarse. Escritura de reseñas, resúmenes e informes de lectura. Características y organización de
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: **Equipo docente:** PROFESORA RESPONSABLE ADJUNTO: ALEJANDRA MARǪUESIN; JEFE DE | Pagina: 1]
   > TRABAJOS PRÁCTICOS: TAMARA SUIVA. JEFE DE TRABAJOS PRÁCTICOS: JIMENA SANTA CRUZ; **Año de la carrera a la que pertenece la cátedra:** 4 **Régimen de la materia:** Anual **Carga horaria semanal:** 3
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > los datos en la investigación: teorías y procedimientos manuales e informáticos. La comunicación de los resultados. **Metodología de trabajo y estrategias pedagógicas:** La cátedra abordará tanto a
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > estudiantes los materiales y herramientas necesarios para la construcción autónoma del conocimiento. - Cada clase incluirá uno o más de los siguientes recursos: - Un video explicativo. - Materi
9. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 5]
   > prácticas se desarrollarán en grupos diferenciados bajo la coordinación de las docentes responsables. Además, se dispondrá de un espacio en la plataforma Moodle de la FCyT, que servirá como complem
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 3]
   > conocimiento vulgar, conocimiento científico. Clasificación de las ciencias. Diferencias entre ciencia, técnica, tecnología, ingeniería e intervención profesional. La ciencia y los sistemas de infor

**Respuesta:**

El plan de estudios de la asignatura Metodología de la Investigación se organiza en cuatro unidades temáticas:

*   **Unidad 1: Introducción a la ciencia y conocimiento científico.** Incluye el estudio del conocimiento vulgar y científico, la clasificación de las ciencias y las diferencias entre ciencia, técnica, tecnología, ingeniería e intervención profesional. También aborda la ciencia y los sistemas de información como objeto de estudio, la escritura académica y las normas de citación.
*   **Unidad 2: La dimensión epistemológica.** Se enfoca en cómo encauzar la definición del tema de investigación, la lectura de antecedentes, los criterios para la búsqueda de información relevante, el uso de fuentes y la elaboración de reseñas, resúmenes e informes de lectura. Asimismo, trata la construcción del problema objeto de estudio y la relación entre objetivos y preguntas de investigación.
*   **Unidad 3: La dimensión de la estrategia general de investigación.** Analiza cómo estudiar el problema, incluyendo los tipos de diseños cuantitativos o cualitativos, las estrategias de indagación según la perspectiva metodológica, el universo de análisis y la población.
*   **Unidad 4: La dimensión de las técnicas de obtención y análisis de información empírica. La comunicación de los resultados.** Comprende el análisis de opciones como entrevistas, observación y análisis documental, así como el tratamiento de datos mediante procedimientos manuales e informáticos y la comunicación final de los resultados.

**Tokens:** entrada: 1958 | salida: 296 | total: 2254

---

### Pregunta 4

> - ¿Qué herramientas de software se recomiendan en la carrera para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **PHP Simplex:** Herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el Método Simplex y el Método Gráfico. Es ideal para validaciones rápidas y vis
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadístico
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > Lineal: proporcionalidad, aditividad, divisibilidad y certidumbre. Formulación de problemas de optimización. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en l
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad I: -Introducción y Modelos Matemáticos-** Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del problema, construcción del modelo mate
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > entrada y salida de variables. Interpretación de la tabla óptima. Aplicación del método de la "M Grande" y método de las "Dos Fases". Análisis de dualidad y sensibilidad básica en modelos lineales.
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > estructura del modelo y suposiciones. Métodos para obtener una solución básica inicial: Esquina Noroeste, Costo Mínimo y Aproximación de Vogel. Método MODI (Distribución Modificada) para la optimiza
9. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 3]
   > hojas de cálculo.
10. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > optimalidad de Bellman. Resolución de problemas de diligencia, asignación de recursos y reemplazo de equipos. Diferencias entre Programación Dinámica Determinística y Probabilística.

**Respuesta:**

Para la resolución de problemas de optimización lineal y otros modelos de gestión en la cátedra, se utilizan diversas herramientas de software que se vinculan con los contenidos teóricos de la siguiente manera:

*   **Programación Lineal (Unidad II y III):**
    *   **PHP Simplex:** Herramienta online diseñada para la resolución mediante el Método Simplex y el Método Gráfico, permitiendo la visualización de regiones factibles y validaciones rápidas.
    *   **LINDO:** Especializado en programación lineal, entera y no lineal, destacando por su sintaxis sencilla para ingresar ecuaciones y restricciones.
    *   **LINGO:** Versión avanzada del motor LINDO, orientada a problemas de optimización de gran escala con capacidad de integración con bases de datos.
    *   **WinQSB 2.0:** Suite que incluye módulos específicos para programación lineal (LP).
    *   **TORA:** Herramienta educativa que permite aplicar el Método Simplex con visualización paso a paso, facilitando el aprendizaje de los algoritmos de la Unidad III.

*   **Modelos de Transporte, Asignación y Redes (Unidad IV):**
    *   **WinQSB 2.0:** Contiene módulos dedicados a resolver modelos de transporte y asignación.
    *   **TORA:** Incluye módulos específicos para modelos de transporte y redes, alineándose con los métodos de resolución (como Esquina Noroeste, Costo Mínimo, Vogel, MODI y Húngaro) abordados en la unidad.

*   **Programación Dinámica, Inventarios y Gestión (Unidad V y gestión operativa):**
    *   **WinQSB 2.0:** Abarca módulos para programación dinámica, teoría de colas y gestión de inventarios.
    *   **TORA:** Ofrece soporte para teoría de juegos.
    *   **Storm:** Orientado al análisis cuantitativo y gestión de operaciones, facilita el procesamiento de modelos matemáticos y estadísticos mediante una interfaz de menús.

Adicionalmente, se menciona el uso de hojas de cálculo para el procesamiento de modelos. La relación principal radica en que el software actúa como soporte práctico para los algoritmos y métodos estudiados en las unidades teóricas, permitiendo desde la visualización pedagógica (TORA, PHP Simplex) hasta la resolución de problemas complejos de gran escala (LINGO, WinQSB, Storm).

**Tokens:** entrada: 1718 | salida: 515 | total: 2233

---

### Pregunta 5

> - ¿Qué instancias de recuperación nos provee Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > **Instancias de Recuperación:** La cátedra dispone de **dos oportunidades de** **recuperatorio** totales. Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no s
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadístico
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **PHP Simplex:** Herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el Método Simplex y el Método Gráfico. Es ideal para validaciones rápidas y vis
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > Lineal: proporcionalidad, aditividad, divisibilidad y certidumbre. Formulación de problemas de optimización. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en l
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad I: -Introducción y Modelos Matemáticos-** Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del problema, construcción del modelo mate
9. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > entrada y salida de variables. Interpretación de la tabla óptima. Aplicación del método de la "M Grande" y método de las "Dos Fases". Análisis de dualidad y sensibilidad básica en modelos lineales.
10. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > **Condición del Alumno:** - **ALUMNO PROMOCIONADO:** El estudiante logrará la promoción directa si alcanza un promedio general de **80 puntos** - más entre los **1 parcial** previstos, no pudiendo

**Respuesta:**

La cátedra dispone de dos oportunidades de recuperación en total. Estas pueden utilizarse para cualquiera de los dos exámenes parciales, con la restricción de que no es posible aplicar ambos recuperatorios a un mismo examen parcial. La calificación obtenida en la instancia de recuperación sustituye automáticamente a la nota del examen original.

**Tokens:** entrada: 1852 | salida: 63 | total: 1915

---

### Pregunta 6

> - ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadístico
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **PHP Simplex:** Herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el Método Simplex y el Método Gráfico. Es ideal para validaciones rápidas y vis
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > entrada y salida de variables. Interpretación de la tabla óptima. Aplicación del método de la "M Grande" y método de las "Dos Fases". Análisis de dualidad y sensibilidad básica en modelos lineales.
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 3]
   > hojas de cálculo.
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > estructura del modelo y suposiciones. Métodos para obtener una solución básica inicial: Esquina Noroeste, Costo Mínimo y Aproximación de Vogel. Método MODI (Distribución Modificada) para la optimiza
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > optimalidad de Bellman. Resolución de problemas de diligencia, asignación de recursos y reemplazo de equipos. Diferencias entre Programación Dinámica Determinística y Probabilística.
9. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad I: -Introducción y Modelos Matemáticos-** Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del problema, construcción del modelo mate
10. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Estructura de Control: Procedimientos de Inferencia; Interfase con el usuario. Memoria de Trabajo, Módulo generador de explicaciones al usuario. **Capítulo V** **Funcionalidad de los Sistemas Exper

**Respuesta:**

El software TORA es una herramienta educativa diseñada específicamente para facilitar el aprendizaje de la Investigación Operativa. Incluye módulos para el Método Simplex (que permite una visualización paso a paso), modelos de transporte, redes y teoría de juegos.

**Tokens:** entrada: 1662 | salida: 48 | total: 1710

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
7. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **PRESENTACIÓN DE LA MATERIA** | Pagina: 1]
   > Facultad de Ciencia y Tecnología Universidad Autónoma de Entre Ríos (UADER)
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos vertidos en la teoría. Más dos trabajos Prácticos que se realizan en el ho
9. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Aspectos de diseño de la capa de red (Conmutación de paquetes de almacenamiento y reenvío, Servicios proporcionados a la capa de transporte, Implementación del servicio no orientado a la conexión, I
10. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > - Terán Pérez, David Moisés: Redes convergentes: diseño e implementación / D. M. Terán Pérez. - México: Alfaomega, 2010. ISBN 9786077854890 [Disponible en Biblioteca FCyT- Oro Verde] **Opcional y amp

**Respuesta:**

El profesor que forma parte del equipo docente en ambas materias es Jorge L. Schmukler (también identificado como Jorge Schmuckler).

**Tokens:** entrada: 1605 | salida: 27 | total: 1632

---

### Pregunta 8

> - ¿Qué otra asignatura, además de la propia materia de Inteligencia Artificial, incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas?

**Chunks de contexto:**

1. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 4. El impacto de la inteligencia artificial en la gestión del talento. | Pagina: 2]
   > _**Bibliografía Nacional:**_ Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales. **Uni
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos **Capítulo I** **Agentes Inteligentes** Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas p
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (2
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Comportamiento de Agentes Basados en Conocimientos. **Capítulo IV** **Diseño de los Sistemas Expertos**. Definición y descripción de sus módulos componentes. Proceso de Adquisición de Conocimiento.
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > Modificación del algoritmo SOM para evitar una excesiva acumulación de información, por parte de una misma neurona. **Capítulo XII** **Sistemas Multi Agentes** Introducción a los sistemas multiagen
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > **Capítulo II** **Procesos de Búsqueda.** Representación en un espacio de estados. Búsqueda Ciega, definición; búsqueda primero en amplitud, búsqueda de costo uniforme; búsqueda primero en profundid
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > **Red Perceptron Simple.** Elemento de Procesamiento. Función de Transferencia. Condiciones de Convergencia. Proceso de Entrenamiento. Algoritmo de Modificación de los
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Estructura de Control: Procedimientos de Inferencia; Interfase con el usuario. Memoria de Trabajo, Módulo generador de explicaciones al usuario. **Capítulo V** **Funcionalidad de los Sistemas Exper
9. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > **Capítulo III** **Sistemas Basados en Conocimientos**. Conceptos básicos. Representación de Conocimientos. Estructuras basadas en Lógica. Lógica de Primer Orden. Reglas de Inferencia. Representación
10. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Proceso de Inferencia. Tratamiento paralelo de las reglas. Determinación del aporte parcial de cada regla. Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del

**Respuesta:**

La asignatura de Informática y Recursos Humanos incluye explícitamente el impacto de la inteligencia artificial dentro de sus contenidos, específicamente en la Unidad 3, denominada "Gestión del Talento en la Era Digital", donde se aborda el impacto de la inteligencia artificial en la gestión del talento.

**Tokens:** entrada: 1831 | salida: 59 | total: 1890

---

### Pregunta 9

> - Los requisitos para regularizar en Bases de Datos Avanzadas y en Redes y Comunicaciones, ¿son iguales? ¿Qué diferencias tienen?

**Chunks de contexto:**

1. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **RÉGIMEN DE CURSADA** | Pagina: 2]
   > **Regularidad:** Asistencia: Según norma vigente Todos los trabajos prácticos aprobados 6/7 parciales aprobados con más del 50% **Promoción:** Régimen regular Obtener más del 70% en todos los parci
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > PROMOCIONADO REGULAR LIBRE El alumno accederá a la condición de **PROMOCIÓN** si cumple con las siguientes condiciones de cátedra: **1 -** Obtener en los 3 parciales, una calificación promedio sup
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > **2-** Haber realizado y aprobado los dos trabajos Práctico impartido por la cátedra. **3-** Asistir al 80% de las clases teóricas y prácticas. El alumno tendrá condición de **LIBRE** si no cumple con
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > **1 -** Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos. Tener aprobado con 60 puntos los tres parciales.
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > **Evaluación Final:** El alumno con condición de REGULAR, deberá rendir un examen de los temas teóricos y prácticos desarrollados en la materia (prueba escrita). El alumno LIBRE rendirá un examen fina
6. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **CANALES DE COMUNICACIÓN** | Pagina: 2]
   > Correo: Lista de mail (consultas y comunicación de rutina) Aula virtual: Material académico - Clave de matriculación: bda2023 (ÚNICO MEDIO OFICIAL) Telegram: https://t.me/+c7PPIrc9nQM4MzEx (avisos y n
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos vertidos en la teoría. Más dos trabajos Prácticos que se realizan en el ho
8. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **SOFTWARE REQUERIDO** | Pagina: 2]
   > PostgreSQL: versión 9.6 o superior SQL Server: versión 2016 o superior QGIS: versión compatible con PostgreSQL Anaconda (Python): últimas versiones
9. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Aspectos de diseño de la capa de red (Conmutación de paquetes de almacenamiento y reenvío, Servicios proporcionados a la capa de transporte, Implementación del servicio no orientado a la conexión, I
10. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **MODALIDAD DE CLASES** | Pagina: 1]
   > A partir de este año la materia será dictada de manera bimodal. El cronograma será definido en su mayoría por la Facultad. Aún no confirmado. Los links de clases se encuentran en el aula virtual. Las

**Respuesta:**

Los requisitos para regularizar las materias Bases de Datos Avanzadas y Comunicación y Redes presentan diferencias significativas en cuanto a exigencias académicas y criterios de evaluación:

**Bases de Datos Avanzadas:**
*   **Asistencia:** Se rige según la norma vigente.
*   **Trabajos Prácticos:** Es obligatorio tener aprobados todos los trabajos prácticos.
*   **Parciales:** Se requiere aprobar 6 de los 7 parciales, cada uno con una calificación superior al 50%.

**Comunicación y Redes:**
*   **Asistencia:** Es obligatorio asistir al 80% de las clases teóricas y prácticas.
*   **Trabajos Prácticos:** Se deben realizar y aprobar los dos trabajos prácticos impartidos por la cátedra.
*   **Parciales:** Se requiere obtener un promedio superior o igual a 60 puntos en los 3 parciales, debiendo aprobar cada uno de ellos con al menos 60 puntos.
*   **Recuperatorios:** La cátedra permite dos instancias de recuperación para cualquiera de los parciales, con la restricción de no utilizar ambos recuperatorios en un mismo parcial.

**Puntos en común y diferencias:**
Ambas materias exigen la aprobación de trabajos prácticos y el cumplimiento de instancias de evaluación parcial para alcanzar la regularidad. Sin embargo, difieren en la estructura de evaluación: mientras que Bases de Datos Avanzadas exige un alto volumen de exámenes parciales (6 de 7), Comunicación y Redes se centra en 3 parciales con promedios específicos y un control de asistencia porcentual estricto (80%). Además, Comunicación y Redes especifica explícitamente el régimen de recuperatorios, información que no se detalla para Bases de Datos Avanzadas.

**Tokens:** entrada: 1619 | salida: 380 | total: 1999

---

### Pregunta 10

> - ¿Cuál es el porcentaje de asistencia a clases que exigen en común las materias de Investigación Operativa, Comunicaciones y Redes, y Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > **2-** Haber realizado y aprobado los dos trabajos Práctico impartido por la cátedra. **3-** Asistir al 80% de las clases teóricas y prácticas. El alumno tendrá condición de **LIBRE** si no cumple con
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > **Condición del Alumno:** - **ALUMNO PROMOCIONADO:** El estudiante logrará la promoción directa si alcanza un promedio general de **80 puntos** - más entre los **1 parcial** previstos, no pudiendo
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > corridos tras la evaluación. Los exámenes se desarrollarán estrictamente en los bloques horarios asignados a la materia. La ausencia no justificada (sin certificado médico o motivo de fuerza mayor v
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > PROMOCIONADO REGULAR LIBRE El alumno accederá a la condición de **PROMOCIÓN** si cumple con las siguientes condiciones de cátedra: **1 -** Obtener en los 3 parciales, una calificación promedio sup
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > **b.** **Alumno Regular** - 60 % de asistencia. - Aprobación del examen parcial teórico con una calificación igual o superior a 60 (sesenta) puntos. - Entrega de todos los trabajos en tiempo y
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > **1 -** Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos. Tener aprobado con 60 puntos los tres parciales.
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 16]
   > Para acceder a la condición de Promoción Directa, el/la estudiante deberá cumplir con los siguientes requisitos: - 80 % de asistencia a la cursada. - Aprobación del examen parcial teórico con una
9. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > . La nota obtenida en este reemplaza a la obtenida en el parcial que se recupera La cátedra dará el resultado de cada una de las evaluaciones parciales y recuperatorios una semana después de que estas
10. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > Lineal: proporcionalidad, aditividad, divisibilidad y certidumbre. Formulación de problemas de optimización. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en l

**Respuesta:**

Las materias de Investigación Operativa, Comunicaciones y Redes, y Metodología de la Investigación no comparten un único porcentaje de asistencia exigido para todas sus condiciones de alumno.

Al comparar los requisitos de las tres asignaturas, se observa lo siguiente:

*   **Investigación Operativa y Comunicaciones y Redes:** Ambas exigen una asistencia mínima del **80%** a las clases teóricas y prácticas para alcanzar las condiciones de regularidad y promoción.
*   **Metodología de la Investigación:** Esta materia presenta requisitos diferenciados según la condición:
    *   Para la **Promoción Directa**, exige un **80%** de asistencia.
    *   Para la condición de **Alumno Regular**, exige un **60%** de asistencia.

En conclusión, no existe un porcentaje de asistencia común que aplique de forma uniforme a todas las materias y a todas sus condiciones de cursada, ya que mientras las dos primeras mantienen el 80% como estándar, Metodología de la Investigación reduce el requisito al 60% para los alumnos regulares.

**Tokens:** entrada: 1941 | salida: 228 | total: 2169

---

### Pregunta 11

> - Un proyecto integrador requiere utilizar un software para resolver problemas de optimización a gran escala que pueda conectarse de forma fluida con bases de datos espaciales. Según las herramientas enseñadas en las materias, ¿qué combinación de software visto en Bases de Datos Avanzadas e Investigación Operativa sería la más adecuada para este objetivo?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **PHP Simplex:** Herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el Método Simplex y el Método Gráfico. Es ideal para validaciones rápidas y vis
2. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **SOFTWARE REQUERIDO** | Pagina: 2]
   > PostgreSQL: versión 9.6 o superior SQL Server: versión 2016 o superior QGIS: versión compatible con PostgreSQL Anaconda (Python): últimas versiones
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadístico
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
6. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **BIBLIOGRAFÍA BASE** | Pagina: 2]
   > Elmasri, R. / Navathe, S. - Fundamentos de Sistemas de Bases de Datos (Addison Wesley) Silberschatz / Korth / Sudarshan - Fundamentos de Bases de Datos (Mc Graw Hill) Date, C.J. - Introducción a los S
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > entrada y salida de variables. Interpretación de la tabla óptima. Aplicación del método de la "M Grande" y método de las "Dos Fases". Análisis de dualidad y sensibilidad básica en modelos lineales.
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > estructura del modelo y suposiciones. Métodos para obtener una solución básica inicial: Esquina Noroeste, Costo Mínimo y Aproximación de Vogel. Método MODI (Distribución Modificada) para la optimiza
9. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **PRESENTACIÓN DE LA MATERIA** | Pagina: 1]
   > Facultad de Ciencia y Tecnología Universidad Autónoma de Entre Ríos (UADER)
10. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > Lineal: proporcionalidad, aditividad, divisibilidad y certidumbre. Formulación de problemas de optimización. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en l

**Respuesta:**

Para abordar un proyecto que requiere la resolución de problemas de optimización a gran escala con integración fluida a bases de datos espaciales, la combinación más adecuada consiste en utilizar **LINGO (64 bits)** junto con **PostgreSQL** y **QGIS**.

Esta selección se fundamenta en las capacidades específicas de cada herramienta:

*   **Optimización a gran escala:** **LINGO (64 bits)** es el software diseñado específicamente para modelar y resolver problemas de optimización de gran escala, ofreciendo una potencia superior a otros motores.
*   **Integración con bases de datos:** LINGO permite una integración fluida con bases de datos, lo cual es esencial para el flujo de información del proyecto.
*   **Gestión de datos espaciales:** **PostgreSQL** (en su versión 9.6 o superior) y **QGIS** (en una versión compatible con PostgreSQL) son las herramientas requeridas para el manejo de datos, siendo QGIS el software especializado para el trabajo con componentes espaciales en conjunto con la base de datos.

Esta combinación articula la potencia de cálculo matemático de LINGO con la infraestructura de gestión de datos y capacidades geoespaciales proporcionadas por el entorno de Bases de Datos Avanzadas.

**Tokens:** entrada: 1713 | salida: 260 | total: 1973

---

### Pregunta 12

> - Si un estudiante desea investigar sobre el impacto de los "Agentes que aprenden" y las "Redes Neuronales" en la selección de personal y el teletrabajo en Argentina, ¿qué normativas legales y temas específicos de los programas de Inteligencia Artificial y RRHH debería cruzar en su marco teórico?

**Chunks de contexto:**

1. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: **I. FUNDAMENTACIÓN** | Pagina: 1]
   > Los estudiantes explorarán los efectos de las nuevas tecnologías en el trabajo, la calidad de vida laboral y la administración del talento humano en la era digital. Además, se abordarán aspectos legal
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 4. El impacto de la inteligencia artificial en la gestión del talento. | Pagina: 2]
   > _**Bibliografía Nacional:**_ Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales. **Uni
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: IV. BIBLIOGRAFÍA GENERAL | Pagina: 3]
   > _**Bibliografía Complementaria:**_ Reglamento de Teletrabajo en Argentina. Legislación sobre delitos informáticos en Argentina. Artículos académicos sobre la transformación del trabajo y el impacto
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 2]
   > Reglamento de Teletrabajo en Argentina. Nicolás S. Tato, El Derecho Informático - Aspectos Fundamentales. Mariana Nazar, Tecnologías, información y derechos. **Unidad 2:** **Relaciones Humanas en e
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 6. Desafíos éticos y sociales de la tecnología en el ámbito laboral. | Pagina: 1]
   > _**Bibliografía Nacional:**_ Ley de Teletrabajo (Ley 27.555).
6. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: IV. BIBLIOGRAFÍA GENERAL | Pagina: 3]
   > _**Bibliografía Básica:**_ Nicolás S. Tato, El Derecho Informático - Aspectos Fundamentales. Mariana Nazar, Tecnologías, información y derechos. Gonzalo Ana Dobratinich, derecho y nuevas tecnología
7. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 5. comercio electrónico, manifestación del consentimiento en internet | Pagina: 3]
   > _**Bibliografía Nacional:**_ Ley de Teletrabajo (Ley 27.555) Código Civil y Comercial de la Nación (aspectos relacionados con contratos digitales). Artículos académicos sobre la economía gig y el t
8. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 3]
   > Legislación sobre delitos informáticos en Argentina. Ley Nacional de Protección de Datos Personales (Ley 25.326). Ley Propiedad Intelectual (Ley 11.723) y su modificatoria. **Unidad 5: Trabajo Autó
9. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 4. Derecho a la desconexión digital y equilibrio entre vida personal y laboral. | Pagina: 2]
   > _**Bibliografía Nacional:**_ Ley Nacional de Protección de Datos Personales (Ley 25.326). Código Civil y Comercial de la Nación (aspectos relacionados con contratos digitales y firma electrónica).
10. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Proceso de Inferencia. Tratamiento paralelo de las reglas. Determinación del aporte parcial de cada regla. Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del

**Respuesta:**

Para abordar el impacto de los "Agentes que aprenden" y las "Redes Neuronales" en el ámbito laboral y de selección de personal en Argentina, el estudiante debe integrar los siguientes ejes temáticos y normativos:

### Ejes Temáticos de Inteligencia Artificial y RRHH
El marco teórico debe articular los conceptos técnicos de la IA con las problemáticas de la gestión del talento:
*   **Fundamentos Técnicos:** Utilizar los conceptos de Redes Neuronales Artificiales (generalidades, clasificación y agentes basados en procesos de aprendizaje) junto con los procesos de inferencia (tratamiento de reglas y defuzzificación) para comprender cómo operan los sistemas automatizados.
*   **Gestión del Talento:** Analizar el impacto de la inteligencia artificial en la gestión del talento, la transformación del trabajo y la economía *gig* (trabajo autónomo y plataformas digitales).
*   **Calidad de Vida:** Evaluar los efectos de estas tecnologías en la calidad de vida laboral, el derecho a la desconexión digital y el equilibrio entre la vida personal y laboral.
*   **Ética:** Considerar los desafíos éticos y sociales que plantea la tecnología en el ámbito laboral.

### Marco Normativo Argentino
La investigación debe fundamentarse en la legislación nacional para analizar el impacto normativo de las TIC y la IA en las relaciones laborales:
*   **Teletrabajo:** Es imperativo incluir la Ley de Teletrabajo (Ley 27.555) y el Reglamento de Teletrabajo en Argentina.
*   **Protección de Datos y Privacidad:** Aplicar la Ley Nacional de Protección de Datos Personales (Ley 25.326).
*   **Contratos y Propiedad:** Integrar el Código Civil y Comercial de la Nación (específicamente en lo relativo a contratos digitales y firma electrónica), la Ley de Propiedad Intelectual (Ley 11.723 y su modificatoria Ley 25.036) y la legislación sobre delitos informáticos.
*   **Derecho y Tecnología:** Incorporar los aportes de la bibliografía nacional, tales como *Derecho y nuevas tecnologías* de Gonzalo Ana Dobratinich, *El Derecho Informático - Aspectos Fundamentales* de Nicolás S. Tato, y *Tecnologías, información y derechos* de Mariana Nazar.

El cruce de estos elementos permitirá analizar cómo la implementación técnica de agentes inteligentes y redes neuronales en la selección y gestión de personal se ve condicionada por el marco legal vigente y los principios del derecho informático en Argentina.

**Tokens:** entrada: 1627 | salida: 539 | total: 2166

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
   > Educativa [https://youtu.be/dydibttPBGU](https://youtu.be/dydibttPBGU) **Operadores Booleanos para búsquedas**
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 13]
   > - Yuni, J y Urbano, C (2016) Técnicas para investigar 2: Recursos metodológicos para la preparación de proyectos de investigación. Editorial Brujas: Argentina _Material audiovisual de la unidad_
9. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 12]
   > - Natale, Lucía (Coordinadora) (2013). En carrera: escritura y lectura de textos académicos y profesionales. Argentina. Universidad Nacional de Ǫuilmes. Visto en [https://ediciones.ungs.edu.ar/wp-co

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1398 | salida: 13 | total: 1411

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
   > Inteligencia Artificial Programa de Contenidos **Capítulo I** **Agentes Inteligentes** Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas p
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > **Capítulo III** **Sistemas Basados en Conocimientos**. Conceptos básicos. Representación de Conocimientos. Estructuras basadas en Lógica. Lógica de Primer Orden. Reglas de Inferencia. Representación
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Comportamiento de Agentes Basados en Conocimientos. **Capítulo IV** **Diseño de los Sistemas Expertos**. Definición y descripción de sus módulos componentes. Proceso de Adquisición de Conocimiento.
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > Modificación del algoritmo SOM para evitar una excesiva acumulación de información, por parte de una misma neurona. **Capítulo XII** **Sistemas Multi Agentes** Introducción a los sistemas multiagen
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > **Capítulo IX** **Redes** **Perceptron** **Multicapa**, estructura básica. Proceso de Entrenamiento Backpropagation (BP). Interpretación heurística y matemática del procedimiento BP. Término de Momen
9. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > **Red Perceptron Simple.** Elemento de Procesamiento. Función de Transferencia. Condiciones de Convergencia. Proceso de Entrenamiento. Algoritmo de Modificación de los
10. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Proceso de Inferencia. Tratamiento paralelo de las reglas. Determinación del aporte parcial de cada regla. Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del

**Respuesta:**

El Ing. Jorge L. Schmukler forma parte del equipo docente en las siguientes cátedras:

*   **Bases de Datos Avanzadas:** Se desempeña en el área de Práctica.
*   **Comunicaciones y Redes:** Integra el equipo docente de la cátedra (código 340424) en la sede de Oro Verde de la Facultad de Ciencia y Tecnología de la UADER.

No dispongo de información en mis documentos que vincule al Ing. Jorge L. Schmukler con la cátedra de Inteligencia Artificial.

**Tokens:** entrada: 1701 | salida: 120 | total: 1821

---

### Pregunta 15

> - ¿Cuál es el costo de la certificación oficial de Cisco que se menciona como opcional en la planificación?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > **Obligatoria** - Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] - Cisco Systems: Academia de Networking de Cisco Systems: Guía del primer añ
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > enlace troncal, Configuración de las VLAN y de los enlaces troncales, Administración de las VLAN, Resolución de problemas de las VLAN y de los enlaces troncales. **Unidad X** **-Dirección IPv6-**
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > - Huidobro Moya, José Manuel: Redes de datos y convergencia IP / J. M. Huidobro Moya, Ramón Jesús Millán Tejedor. - México: Alfaomega, 2007. ISBN 9789701512784 [Disponible en Biblioteca FCyT- Oro Verd
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > - USERS-CISCO. [Disponible en Biblioteca FCyT- Oro Verde] - Comer, Douglas E.: Redes de computadoras, Internet e Interredes / D. E. Comer. - México: Prentice Hall, 1997. ISBN 970170021X [Disponible
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > . Explicar el **propósito de IOS como Sistema** **Operativo de red**, Explicar cómo acceder al IOS y cómo explorarlo para configurar los dispositivos de red, Describir la estructura de comandos, Confi
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Sitios web sobre normativas, tecnologías y soluciones, opcional** | Pagina: 5]
   > IETF -> www.ietf.org IEEE -> www.ieee.org ISO -> www.iso.org CISCO -> www.cisco.com IANA -> www.iana.org ISOC -> www.isoc.org ARIN -> www.arin.net LACNIC -> http://lacnic.net/sp/ LAC IPV6 TF -> www.la
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . ARP proxy. **Cableado Estructurado**: Selección de dispositivos intermedios. Interconexiones de dispositivos intermedios y finales (longitud del medio, áreas de trabajo, cuarto de telecomunicaciones
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Proveedores de servicio de internet (ISP), descripción Ipv6. **Unidad IX** **-VLans-** Definiciones de Vlan, Beneficios de una Vlan, Rangos de ID de la Vlan (rango normal y rango extendido), Tipos d
9. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Clase de direccionamiento (clase a, b, c, d y e). Prefijo y Mascara de red. Lógica de and. Calculo de direcciones. División de subredes (por clase y vlsm (mascara de subred de longitud variable)), i
10. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > - Terán Pérez, David Moisés: Redes convergentes: diseño e implementación / D. M. Terán Pérez. - México: Alfaomega, 2010. ISBN 9786077854890 [Disponible en Biblioteca FCyT- Oro Verde] **Opcional y amp

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta. La planificación menciona a Cisco como un sitio web de referencia sobre normativas, tecnologías y soluciones, y lista bibliografía relacionada con Cisco, pero no proporciona detalles ni costos sobre certificaciones oficiales.

**Tokens:** entrada: 2209 | salida: 51 | total: 2260

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
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > **2-** Haber realizado y aprobado los dos trabajos Práctico impartido por la cátedra. **3-** Asistir al 80% de las clases teóricas y prácticas. El alumno tendrá condición de **LIBRE** si no cumple con
5. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **RÉGIMEN DE CURSADA** | Pagina: 2]
   > **Regularidad:** Asistencia: Según norma vigente Todos los trabajos prácticos aprobados 6/7 parciales aprobados con más del 50% **Promoción:** Régimen regular Obtener más del 70% en todos los parci
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > **1 -** Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos. Tener aprobado con 60 puntos los tres parciales.
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > **b.** **Alumno Regular** - 60 % de asistencia. - Aprobación del examen parcial teórico con una calificación igual o superior a 60 (sesenta) puntos. - Entrega de todos los trabajos en tiempo y
9. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos vertidos en la teoría. Más dos trabajos Prácticos que se realizan en el ho
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > El/la estudiante que no se ajuste a los requisitos establecidos en los puntos A y B, se considerará en condición libre. Deberá presentar el trabajo práctico integrador con una antelación mínima de v

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta. Si bien las materias detallan como requisito la aprobación de los trabajos prácticos para acceder a la promoción, no se especifica una calificación numérica mínima individual para cada trabajo práctico en ninguna de las asignaturas mencionadas.

**Tokens:** entrada: 1912 | salida: 56 | total: 1968

---

### Pregunta 17

> - ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > Lineal: proporcionalidad, aditividad, divisibilidad y certidumbre. Formulación de problemas de optimización. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en l
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **PHP Simplex:** Herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el Método Simplex y el Método Gráfico. Es ideal para validaciones rápidas y vis
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > entrada y salida de variables. Interpretación de la tabla óptima. Aplicación del método de la "M Grande" y método de las "Dos Fases". Análisis de dualidad y sensibilidad básica en modelos lineales.
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadístico
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 3]
   > hojas de cálculo.
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad I: -Introducción y Modelos Matemáticos-** Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del problema, construcción del modelo mate
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > estructura del modelo y suposiciones. Métodos para obtener una solución básica inicial: Esquina Noroeste, Costo Mínimo y Aproximación de Vogel. Método MODI (Distribución Modificada) para la optimiza
9. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
10. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > optimalidad de Bellman. Resolución de problemas de diligencia, asignación de recursos y reemplazo de equipos. Diferencias entre Programación Dinámica Determinística y Probabilística.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta. El contenido disponible describe el algoritmo del método Simplex (forma estándar, variables de holgura y artificiales, tabla inicial, criterios de entrada/salida e interpretación) y menciona el uso de hojas de cálculo de forma genérica, pero no detalla el procedimiento técnico para ejecutar dicho método específicamente dentro de Excel.

**Tokens:** entrada: 1707 | salida: 77 | total: 1784

---

### Pregunta 18

> - ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > corridos tras la evaluación. Los exámenes se desarrollarán estrictamente en los bloques horarios asignados a la materia. La ausencia no justificada (sin certificado médico o motivo de fuerza mayor v
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > **Instancias de Recuperación:** La cátedra dispone de **dos oportunidades de** **recuperatorio** totales. Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no s
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > **Condición del Alumno:** - **ALUMNO PROMOCIONADO:** El estudiante logrará la promoción directa si alcanza un promedio general de **80 puntos** - más entre los **1 parcial** previstos, no pudiendo
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > |||||investigación| |17|13 de agosto|Virtual|Tutorías|Tutorías| |18|20 de agosto|**_Presencial (cambio_**<br>**_encuentro)_**|**Teoría**|Parcial teoría| |19|27 de agosto|Virtual|Tutorías|Tutorías| |20
6. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **HORARIOS DE CLASE** | Pagina: 1]
   > Lunes: 13:30 a 15:30 (Teoría) Viernes: 17:00 a 19:00 (Práctica) Nota: Los horarios están en proceso de evaluación y pueden sufrir cambios
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad I: -Introducción y Modelos Matemáticos-** Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del problema, construcción del modelo mate
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > |12|28 de mayo|Virtual|Teoría|Col5| |---|---|---|---|---| |13|04 de junio|**Presencial**|**Teoría**|Marco metodológico I
9. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > : enfoque y<br>tipo de investigación / muestra| |14|11 de junio|Virtual|Práctica|| |15|18 de junio|Virtual|Teoría|Marco metodológico II:<br>recolección de datos y análisis de<br>datos| |||||| |RECESO
10. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > Lineal: proporcionalidad, aditividad, divisibilidad y certidumbre. Formulación de problemas de optimización. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en l

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta. El contexto no especifica una fecha de examen parcial para el 15/06 en la materia Investigación Operativa, ni proporciona horarios exactos para sus instancias de evaluación.

**Tokens:** entrada: 2059 | salida: 49 | total: 2108

---

## Conversacion 3

**Puntaje evaluado: 18 / 18**

**Parametros modificados respecto a la conversacion anterior:**

| Parametro | Valor |
|---|---|
| retrieval_type | mmr |

### Pregunta 1

> - ¿Cuáles son los contenidos de la materia Inteligencia Artificial?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos **Capítulo I** **Agentes Inteligentes** Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas p
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Estructura de Control: Procedimientos de Inferencia; Interfase con el usuario. Memoria de Trabajo, Módulo generador de explicaciones al usuario. **Capítulo V** **Funcionalidad de los Sistemas Exper
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Proceso de Inferencia. Tratamiento paralelo de las reglas. Determinación del aporte parcial de cada regla. Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > **Red Perceptron Simple.** Elemento de Procesamiento. Función de Transferencia. Condiciones de Convergencia. Proceso de Entrenamiento. Algoritmo de Modificación de los
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > Regiones de Decisión. Modo de operación autoasociativo. **Capítulo X** **Generalización en las RNA,** definición, factores que influyen en la capacidad de Generalización. Tamaño del conjunto de pat
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (2
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: pesos. Regiones de Decisión. Problema de separación lineal. Aplicaciones. Limitaciones | Pagina: 2]
   > Problema XOR.
8. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 4. El impacto de la inteligencia artificial en la gestión del talento. | Pagina: 2]
   > _**Bibliografía Nacional:**_ Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales. **Uni
9. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: dentro de la plataforma Moodle. La organización será la siguiente | Pagina: 5]
   > curso. - Desarrollo de contenidos: distribuidos en tres pestañas temáticas: - Introducción - Dimensión epistemológica - Dimensión estratégica - Dimensión técnica - Cada semana se habilitar
10. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > Lineal: proporcionalidad, aditividad, divisibilidad y certidumbre. Formulación de problemas de optimización. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en l

**Respuesta:**

Los contenidos de la materia Inteligencia Artificial se estructuran en los siguientes ejes temáticos:

**Agentes Inteligentes**
*   Introducción, definiciones, objetivos, herramientas y técnicas de la IA.
*   Entornos de trabajo y sus propiedades.
*   Estructura y programas de agentes: reactivos simples, basados en modelos, basados en objetivos y agentes que aprenden.

**Sistemas Expertos**
*   Estructura de control: procedimientos de inferencia, interfaz con el usuario, memoria de trabajo y módulo generador de explicaciones.
*   Funcionalidad: encadenamiento hacia adelante (*Forward Chaining*) y hacia atrás (*Backward Chaining*).
*   Herramientas para el desarrollo de sistemas expertos.

**Lógica Difusa**
*   Procesos de inferencia: tratamiento paralelo de reglas, determinación de aporte parcial e integración de la solución difusa final.
*   Procesos de defuzzificación: definición, método del centroide, método de máxima e influencia de estos métodos en el sistema.
*   Agentes basados en lógica difusa.

**Redes Neuronales Artificiales (RNA)**
*   Generalidades, conceptos básicos, reseña histórica y clasificación.
*   Agentes basados en procesos de aprendizaje.
*   Red Perceptron Simple: elemento de procesamiento, función de transferencia, condiciones de convergencia, proceso de entrenamiento, algoritmo de modificación de pesos, regiones de decisión, problema de separación lineal, aplicaciones, limitaciones y el problema XOR.
*   Modo de operación autoasociativo.
*   Generalización en RNA: definición, factores influyentes, tamaño del conjunto de patrones de entrenamiento, algoritmos de reducción (*Pruning Algorithms*), *Deep Learning* y modelos generativos.
*   Redes Autoorganizadas: características generales y Red SOM (Kohonen), incluyendo proceso de aprendizaje competitivo, realimentación lateral, algoritmo SOFM/SOM, determinación del proceso de adaptación de pesos y función de vecindad.

**Tokens:** entrada: 1727 | salida: 420 | total: 2147

---

### Pregunta 2

> - ¿En qué materia se enseña el concepto de Lógica Difusa?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Herramientas para el desarrollo de Sistemas Expertos. **Capítulo VI** **Lógica Difusa (Fuzzy).** Consideraciones generales, Conjuntos Difusos, definición. Operaciones simples entre conjuntos Difusos
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Proceso de Inferencia. Tratamiento paralelo de las reglas. Determinación del aporte parcial de cada regla. Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: pesos. Regiones de Decisión. Problema de separación lineal. Aplicaciones. Limitaciones | Pagina: 2]
   > Problema XOR.
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (2
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: **Equipo docente:** PROFESORA RESPONSABLE ADJUNTO: ALEJANDRA MARǪUESIN; JEFE DE | Pagina: 1]
   > TRABAJOS PRÁCTICOS: TAMARA SUIVA. JEFE DE TRABAJOS PRÁCTICOS: JIMENA SANTA CRUZ; **Año de la carrera a la que pertenece la cátedra:** 4 **Régimen de la materia:** Anual **Carga horaria semanal:** 3
6. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: PROGRAMA DE CÁTEDRA: INFORMÁTICA Y RELACIONES HUMANAS | Pagina: 1]
   > Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas semanales
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 3]
   > hojas de cálculo.
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 15]
   > ; director Aldo Daniel Sigura ;<br>codirector Pablo Emanuel Goette.|2019| |Deep Learning aplicado al aprendizaje automático de ontologías para la<br>representación del conocimiento a partir de texto n
9. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > ; Algoritmos de control de congestión (Principios generales del control de congestión, Políticas de prevención de congestión, Control de congestión en subredes de circuitos virtuales, Control de conge
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: -> Paula Espeche Trayecto 2 Google académico y operadores booleanos | Pagina: 12]
   > **[https://youtu.be/fiSJ4bDb Nwrc](https://youtu.be/1SJ4bDb Nwrc)**

**Respuesta:**

El concepto de Lógica Difusa se enseña en la materia Inteligencia Artificial.

**Tokens:** entrada: 1668 | salida: 17 | total: 1685

---

### Pregunta 3

> - ¿Cuál es el plan de estudios de Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > integrador se determinará exclusivamente en la mesa de examen, junto con la nota correspondiente a la instancia teórica, estableciéndose en ese momento la calificación final y la condición de aproba
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: dentro de la plataforma Moodle. La organización será la siguiente | Pagina: 5]
   > curso. - Desarrollo de contenidos: distribuidos en tres pestañas temáticas: - Introducción - Dimensión epistemológica - Dimensión estratégica - Dimensión técnica - Cada semana se habilitar
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > objetivos y relación de los objetivos con las preguntas de la investigación. **Unidad 3: La dimensión de la estrategia general de investigación** ¿Cómo se va a estudiar el problema? Tipo de diseños c
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 3]
   > orientar la búsqueda de información relevante. Tipo de fuentes, obras y producciones que pueden consultarse. Escritura de reseñas, resúmenes e informes de lectura. Características y organización de
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: **Equipo docente:** PROFESORA RESPONSABLE ADJUNTO: ALEJANDRA MARǪUESIN; JEFE DE | Pagina: 1]
   > TRABAJOS PRÁCTICOS: TAMARA SUIVA. JEFE DE TRABAJOS PRÁCTICOS: JIMENA SANTA CRUZ; **Año de la carrera a la que pertenece la cátedra:** 4 **Régimen de la materia:** Anual **Carga horaria semanal:** 3
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > estudiantes los materiales y herramientas necesarios para la construcción autónoma del conocimiento. - Cada clase incluirá uno o más de los siguientes recursos: - Un video explicativo. - Materi
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > |METODOLOGÍA DE LA INVESTIGACIÓN- 2026|Col2|Col3|Col4|Col5| |---|---|---|---|---| |**Clase **|**FECHA**|**Tipo de encuentro**|**Tipo encuentro**|**Tema**| |1|12 de marzo|**Presencial**|**Teórico/práct
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > Dado que se trata de una asignatura de cuarto año, la modalidad de cursado será combinada. En este marco, se llevará a cabo un encuentro presencial físico mensual, enfocado en la escritura del antep
9. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 1]
   > **2026 - FCYT-ORO VERDE - Licenciatura en Sistemas de Información - Metodología de la** **Investigación** **Carrera:** Licenciatura en Sistemas de Información **Cátedra:** Metodología de la Investig
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 9]
   > conceptos. Formulación de objetivos e hipótesis. Tp 4: Elaboración de un escrito en donde presenten: Marco metodológico. El tiempo, período o secuencia de estudio. Universo, muestra y unidad de mues

**Respuesta:**

El plan de estudios de la asignatura Metodología de la Investigación, correspondiente a la Licenciatura en Sistemas de Información (año 2026), se estructura en cuatro unidades temáticas:

*   **Unidad 1:** Introducción a la ciencia y conocimiento científico.
*   **Unidad 2:** La dimensión epistemológica.
*   **Unidad 3:** La dimensión de la estrategia general de investigación, que abarca la definición del problema, los tipos de diseños (cuantitativos o cualitativos), las estrategias de indagación, el universo de análisis y la población.
*   **Unidad 4:** La dimensión de las técnicas de obtención y análisis de información empírica, incluyendo el análisis de opciones (entrevistas, observación, análisis documental, etc.) y la comunicación de los resultados.

En la plataforma Moodle, estos contenidos se organizan en las siguientes pestañas temáticas: Introducción, Dimensión epistemológica, Dimensión estratégica y Dimensión técnica.

**Tokens:** entrada: 1992 | salida: 209 | total: 2201

---

### Pregunta 4

> - ¿Qué herramientas de software se recomiendan en la carrera para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **PHP Simplex:** Herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el Método Simplex y el Método Gráfico. Es ideal para validaciones rápidas y vis
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadístico
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > Lineal: proporcionalidad, aditividad, divisibilidad y certidumbre. Formulación de problemas de optimización. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en l
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > optimalidad de Bellman. Resolución de problemas de diligencia, asignación de recursos y reemplazo de equipos. Diferencias entre Programación Dinámica Determinística y Probabilística.
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
8. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **SOFTWARE REQUERIDO** | Pagina: 2]
   > PostgreSQL: versión 9.6 o superior SQL Server: versión 2016 o superior QGIS: versión compatible con PostgreSQL Anaconda (Python): últimas versiones
9. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: pesos. Regiones de Decisión. Problema de separación lineal. Aplicaciones. Limitaciones | Pagina: 2]
   > Problema XOR.
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: -> BÚSǪUEDA AVANZADA GOOGLE - BÚSǪUEDA GOOGLE AVANZADA - 4TA PARTE | Pagina: 12]
   > APRENDER A INVESTIGAR: [https://youtu.be/w-yuPlI_wC8](https://youtu.be/w-yuPlI_wC8) -> [BITÁCORA DE BÚSǪUEDA https://youtu.be/w-7l4rsx3TA](https://youtu.be/w-7l4rsx3TA) **Unidad 3: La dimensión de l

**Respuesta:**

Para la resolución de problemas de optimización lineal y otros modelos de gestión en la cátedra de Investigación Operativa, se utilizan las siguientes herramientas de software, las cuales se vinculan con las unidades teóricas del programa:

*   **PHP Simplex:** Es una herramienta online diseñada para resolver problemas de programación lineal mediante el Método Simplex y el Método Gráfico. Su uso se relaciona directamente con la **Unidad III (Método Simplex)** y los contenidos iniciales sobre la **resolución gráfica de modelos de PL** (región factible y búsqueda de soluciones en los vértices). Es ideal para validaciones rápidas y visualización.
*   **TORA:** Herramienta de carácter educativo que incluye módulos específicos para el Método Simplex, permitiendo una visualización paso a paso, además de abordar modelos de transporte, redes y teoría de juegos.
*   **LINDO:** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Se destaca por su sintaxis sencilla para el ingreso de ecuaciones y restricciones, facilitando la formulación de problemas de optimización.
*   **LINGO (64 bits):** Representa una versión avanzada y potente de LINDO. Está orientado a la resolución de problemas de optimización de gran escala y permite la integración con bases de datos.
*   **WinQSB 2.0:** Una suite integral que abarca múltiples módulos, incluyendo programación lineal (LP), modelos de transporte, asignación, programación dinámica, teoría de colas y gestión de inventarios. Su alcance cubre tanto la optimización lineal como los modelos tratados en la **Unidad IV (Modelos de Transporte y Transbordo)** y temas de programación dinámica.
*   **Storm:** Software enfocado en el análisis cuantitativo y la gestión de operaciones, facilitando el procesamiento de modelos matemáticos y estadísticos mediante una interfaz basada en menús.

Estas herramientas permiten abordar de forma práctica los conceptos de la planificación, tales como la formulación de problemas de optimización, el análisis de casos especiales (soluciones múltiples, no acotadas e infactibles) y la aplicación de los algoritmos de resolución definidos en la teoría.

**Tokens:** entrada: 1788 | salida: 451 | total: 2239

---

### Pregunta 5

> - ¿Qué instancias de recuperación nos provee Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > **Instancias de Recuperación:** La cátedra dispone de **dos oportunidades de** **recuperatorio** totales. Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no s
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadístico
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **PHP Simplex:** Herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el Método Simplex y el Método Gráfico. Es ideal para validaciones rápidas y vis
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad I: -Introducción y Modelos Matemáticos-** Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del problema, construcción del modelo mate
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > entrada y salida de variables. Interpretación de la tabla óptima. Aplicación del método de la "M Grande" y método de las "Dos Fases". Análisis de dualidad y sensibilidad básica en modelos lineales.
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > estructura del modelo y suposiciones. Métodos para obtener una solución básica inicial: Esquina Noroeste, Costo Mínimo y Aproximación de Vogel. Método MODI (Distribución Modificada) para la optimiza
9. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 20]
   > de noviembr e Espacio de recuperación y cierre
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: -> BÚSǪUEDA AVANZADA GOOGLE - BÚSǪUEDA GOOGLE AVANZADA - 4TA PARTE | Pagina: 12]
   > APRENDER A INVESTIGAR: [https://youtu.be/w-yuPlI_wC8](https://youtu.be/w-yuPlI_wC8) -> [BITÁCORA DE BÚSǪUEDA https://youtu.be/w-7l4rsx3TA](https://youtu.be/w-7l4rsx3TA) **Unidad 3: La dimensión de l

**Respuesta:**

La cátedra de Investigación Operativa dispone de dos oportunidades de recuperatorio totales. Estas pueden utilizarse para cualquiera de los dos exámenes parciales, bajo la restricción de que no es posible aplicar ambos recuperatorios a un mismo examen parcial. La calificación obtenida en la instancia de recuperación sustituye automáticamente a la nota del examen original.

**Tokens:** entrada: 1849 | salida: 67 | total: 1916

---

### Pregunta 6

> - ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadístico
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > entrada y salida de variables. Interpretación de la tabla óptima. Aplicación del método de la "M Grande" y método de las "Dos Fases". Análisis de dualidad y sensibilidad básica en modelos lineales.
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 3]
   > hojas de cálculo.
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > estructura del modelo y suposiciones. Métodos para obtener una solución básica inicial: Esquina Noroeste, Costo Mínimo y Aproximación de Vogel. Método MODI (Distribución Modificada) para la optimiza
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 3]
   > : - **Capa de Transporte** Propósito y funciones, Protocolo de Control de Transmisión - **TCP** - (protocolo orientado a la conexión, segmento TCP, establecimiento de sesiones (sesiones orientadas a l
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos vertidos en la teoría. Más dos trabajos Prácticos que se realizan en el ho
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Comportamiento de Agentes Basados en Conocimientos. **Capítulo IV** **Diseño de los Sistemas Expertos**. Definición y descripción de sus módulos componentes. Proceso de Adquisición de Conocimiento.
9. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: dentro de la plataforma Moodle. La organización será la siguiente | Pagina: 5]
   > - Inicio del curso: contendrá información general de la cátedra, incluyendo el programa, el equipo docente, el cronograma, los objetivos, los materiales utilizados, el enlace de videoconferencia, la
10. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > . Red telefónica pública conmutada (circuito local (módem, ADSL e inalámbrico), concepto de ultima milla, troncales y multiplexación FDM, TDM, conmutación de circuitos, conmutación de paquetes). Siste

**Respuesta:**

El software TORA es una herramienta educativa diseñada específicamente para el aprendizaje de la Investigación Operativa.

Dentro de la cátedra, se destaca por incluir los siguientes módulos:
*   **Método Simplex:** permite la resolución con visualización paso a paso.
*   **Modelos de transporte.**
*   **Redes.**
*   **Teoría de juegos.**

**Tokens:** entrada: 1661 | salida: 78 | total: 1739

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
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos vertidos en la teoría. Más dos trabajos Prácticos que se realizan en el ho
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Aspectos de diseño de la capa de red (Conmutación de paquetes de almacenamiento y reenvío, Servicios proporcionados a la capa de transporte, Implementación del servicio no orientado a la conexión, I
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > - Terán Pérez, David Moisés: Redes convergentes: diseño e implementación / D. M. Terán Pérez. - México: Alfaomega, 2010. ISBN 9786077854890 [Disponible en Biblioteca FCyT- Oro Verde] **Opcional y amp
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Proveedores de servicio de internet (ISP), descripción Ipv6. **Unidad IX** **-VLans-** Definiciones de Vlan, Beneficios de una Vlan, Rangos de ID de la Vlan (rango normal y rango extendido), Tipos d
9. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > . Medios de transmisión (medios guiados o alámbricos -par trenzado, cable coaxial, líneas eléctricas, fibra óptica-; medios no guiados o inalámbricos -transmisión inalámbrica, radiotransmisión, transm
10. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . La ethernet actual. La trama de ethernet. Power Over Ethernet. Direcciones MAC. Dispositivo de red (nic). Ethernet unicast, multicast, broadcast. CSMA/CD (Acceso Múltiple por Detección de Portadora

**Respuesta:**

El profesor Jorge L. Schmukler (también identificado como Jorge Schmuckler) forma parte del equipo docente tanto en la cátedra de Comunicaciones y Redes como en la de Bases de Datos Avanzadas, donde se desempeña en el área de práctica.

**Tokens:** entrada: 1993 | salida: 54 | total: 2047

---

### Pregunta 8

> - ¿Qué otra asignatura, además de la propia materia de Inteligencia Artificial, incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas?

**Chunks de contexto:**

1. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 4. El impacto de la inteligencia artificial en la gestión del talento. | Pagina: 2]
   > _**Bibliografía Nacional:**_ Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales. **Uni
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos **Capítulo I** **Agentes Inteligentes** Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas p
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (2
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > Modificación del algoritmo SOM para evitar una excesiva acumulación de información, por parte de una misma neurona. **Capítulo XII** **Sistemas Multi Agentes** Introducción a los sistemas multiagen
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > **Red Perceptron Simple.** Elemento de Procesamiento. Función de Transferencia. Condiciones de Convergencia. Proceso de Entrenamiento. Algoritmo de Modificación de los
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Estructura de Control: Procedimientos de Inferencia; Interfase con el usuario. Memoria de Trabajo, Módulo generador de explicaciones al usuario. **Capítulo V** **Funcionalidad de los Sistemas Exper
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: pesos. Regiones de Decisión. Problema de separación lineal. Aplicaciones. Limitaciones | Pagina: 2]
   > Problema XOR.
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > Regiones de Decisión. Modo de operación autoasociativo. **Capítulo X** **Generalización en las RNA,** definición, factores que influyen en la capacidad de Generalización. Tamaño del conjunto de pat
9. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: **I. FUNDAMENTACIÓN** | Pagina: 1]
   > El avance de las tecnologías de la información y la comunicación (TIC) ha transformado la dinámica del mundo laboral y las relaciones humanas dentro de las organizaciones. Esta asignatura busca analiz
10. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: PROGRAMA DE CÁTEDRA: INFORMÁTICA Y RELACIONES HUMANAS | Pagina: 1]
   > Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas semanales

**Respuesta:**

La asignatura **Informática y Recursos Humanos**, perteneciente a la Licenciatura en Sistemas de Información, incluye explícitamente el impacto de la inteligencia artificial en sus unidades temáticas. Específicamente, en su Unidad 3, denominada "Gestión del Talento en la Era Digital", se aborda el impacto de la inteligencia artificial en la gestión del talento y las relaciones laborales, complementado con el análisis de la transformación del trabajo.

**Tokens:** entrada: 1703 | salida: 90 | total: 1793

---

### Pregunta 9

> - Los requisitos para regularizar en Bases de Datos Avanzadas y en Redes y Comunicaciones, ¿son iguales? ¿Qué diferencias tienen?

**Chunks de contexto:**

1. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **RÉGIMEN DE CURSADA** | Pagina: 2]
   > **Regularidad:** Asistencia: Según norma vigente Todos los trabajos prácticos aprobados 6/7 parciales aprobados con más del 50% **Promoción:** Régimen regular Obtener más del 70% en todos los parci
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > **Evaluación Final:** El alumno con condición de REGULAR, deberá rendir un examen de los temas teóricos y prácticos desarrollados en la materia (prueba escrita). El alumno LIBRE rendirá un examen fina
3. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **CANALES DE COMUNICACIÓN** | Pagina: 2]
   > Correo: Lista de mail (consultas y comunicación de rutina) Aula virtual: Material académico - Clave de matriculación: bda2023 (ÚNICO MEDIO OFICIAL) Telegram: https://t.me/+c7PPIrc9nQM4MzEx (avisos y n
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos vertidos en la teoría. Más dos trabajos Prácticos que se realizan en el ho
5. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **SOFTWARE REQUERIDO** | Pagina: 2]
   > PostgreSQL: versión 9.6 o superior SQL Server: versión 2016 o superior QGIS: versión compatible con PostgreSQL Anaconda (Python): últimas versiones
6. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **HORARIOS DE CLASE** | Pagina: 1]
   > Lunes: 13:30 a 15:30 (Teoría) Viernes: 17:00 a 19:00 (Práctica) Nota: Los horarios están en proceso de evaluación y pueden sufrir cambios
7. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **BIBLIOGRAFÍA BASE** | Pagina: 2]
   > Elmasri, R. / Navathe, S. - Fundamentos de Sistemas de Bases de Datos (Addison Wesley) Silberschatz / Korth / Sudarshan - Fundamentos de Bases de Datos (Mc Graw Hill) Date, C.J. - Introducción a los S
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 1]
   > **Facultad de Ciencia y Tecnología de la UADER** SEDE: Oro Verde CATEDRA: Comunicaciones y Redes (Código 340424) EQUIPO DOCENTE: Lic. Luciano M. Caisso, Ing. Jorge L. Schmukler.
9. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > ; Algoritmos de control de congestión (Principios generales del control de congestión, Políticas de prevención de congestión, Control de congestión en subredes de circuitos virtuales, Control de conge
10. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > retroceso exponencial binario, LAN Inalámbricas IEEE 802.11, Banda Ancha Inalámbrica IEEE 802.16, Comparación entre el estándar IEEE 802.11 y IEEE 802.16, Bluetooh, Conmutación en la capa de enlace (R

**Respuesta:**

Los requisitos para alcanzar la regularidad en ambas materias no son iguales; presentan diferencias significativas en cuanto a la exigencia de parciales y la gestión de trabajos prácticos.

**Bases de Datos Avanzadas:**
*   **Asistencia:** Debe cumplirse según la norma vigente.
*   **Trabajos Prácticos:** Es obligatorio tener todos los trabajos prácticos aprobados.
*   **Parciales:** Se requiere aprobar 6 de los 7 parciales con una calificación superior al 50%.

**Comunicación y Redes:**
*   **Trabajos Prácticos:** Se deben aprobar dos trabajos prácticos específicos, los cuales se desarrollan al finalizar los cuatrimestres en el horario de clase.
*   **Parciales:** La información proporcionada no especifica requisitos de aprobación de parciales para obtener la regularidad en esta materia.

En resumen, mientras que Bases de Datos Avanzadas establece una estructura cuantitativa estricta basada en el rendimiento de parciales (6 de 7) y la totalidad de los trabajos prácticos, Comunicación y Redes centra su requisito de regularidad en la aprobación de dos trabajos prácticos finales, sin mencionar una exigencia de parciales para dicha condición.

**Tokens:** entrada: 1654 | salida: 257 | total: 1911

---

### Pregunta 10

> - ¿Cuál es el porcentaje de asistencia a clases que exigen en común las materias de Investigación Operativa, Comunicaciones y Redes, y Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > **2-** Haber realizado y aprobado los dos trabajos Práctico impartido por la cátedra. **3-** Asistir al 80% de las clases teóricas y prácticas. El alumno tendrá condición de **LIBRE** si no cumple con
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > **Condición del Alumno:** - **ALUMNO PROMOCIONADO:** El estudiante logrará la promoción directa si alcanza un promedio general de **80 puntos** - más entre los **1 parcial** previstos, no pudiendo
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > corridos tras la evaluación. Los exámenes se desarrollarán estrictamente en los bloques horarios asignados a la materia. La ausencia no justificada (sin certificado médico o motivo de fuerza mayor v
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > **b.** **Alumno Regular** - 60 % de asistencia. - Aprobación del examen parcial teórico con una calificación igual o superior a 60 (sesenta) puntos. - Entrega de todos los trabajos en tiempo y
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 3]
   > hojas de cálculo.
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > entrada y salida de variables. Interpretación de la tabla óptima. Aplicación del método de la "M Grande" y método de las "Dos Fases". Análisis de dualidad y sensibilidad básica en modelos lineales.
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > campo disciplinar y desarrollo de ejercicios vinculados con la construcción progresiva del anteproyecto de investigación. Esta metodología busca facilitar el acceso a los contenidos para aquellos es
9. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: Dr Roberto Hernández Sampieri Charla enfoques cuantitativo, cualitativo, mixto | Pagina: 13]
   > **comunicación de los resultados** Bibliografía obligatoria sobre investigación - Arias, F. (2012). El proyecto de investigación: Introducción a la metodología de la investigación (Sexta edición a
10. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadístico

**Respuesta:**

No existe un porcentaje de asistencia común para las tres materias.

Las exigencias de asistencia son las siguientes:

*   **Investigación Operativa:** Requiere un 80% de asistencia a las clases teóricas y prácticas.
*   **Comunicación y Redes:** Requiere un 80% de asistencia a las clases teóricas y prácticas.
*   **Metodología de la Investigación:** Requiere un 60% de asistencia.

**Tokens:** entrada: 1812 | salida: 99 | total: 1911

---

### Pregunta 11

> - Un proyecto integrador requiere utilizar un software para resolver problemas de optimización a gran escala que pueda conectarse de forma fluida con bases de datos espaciales. Según las herramientas enseñadas en las materias, ¿qué combinación de software visto en Bases de Datos Avanzadas e Investigación Operativa sería la más adecuada para este objetivo?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **PHP Simplex:** Herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el Método Simplex y el Método Gráfico. Es ideal para validaciones rápidas y vis
2. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **SOFTWARE REQUERIDO** | Pagina: 2]
   > PostgreSQL: versión 9.6 o superior SQL Server: versión 2016 o superior QGIS: versión compatible con PostgreSQL Anaconda (Python): últimas versiones
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadístico
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
6. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **BIBLIOGRAFÍA BASE** | Pagina: 2]
   > Elmasri, R. / Navathe, S. - Fundamentos de Sistemas de Bases de Datos (Addison Wesley) Silberschatz / Korth / Sudarshan - Fundamentos de Bases de Datos (Mc Graw Hill) Date, C.J. - Introducción a los S
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > entrada y salida de variables. Interpretación de la tabla óptima. Aplicación del método de la "M Grande" y método de las "Dos Fases". Análisis de dualidad y sensibilidad básica en modelos lineales.
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > estructura del modelo y suposiciones. Métodos para obtener una solución básica inicial: Esquina Noroeste, Costo Mínimo y Aproximación de Vogel. Método MODI (Distribución Modificada) para la optimiza
9. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **EQUIPO DOCENTE** | Pagina: 1]
   > Teoría: Trossero, Sebastián (Trossero.sebastian@uader.edu.ar) Práctica: Schmuckler, Jorge (Schmukler.jorge@uader.edu.ar)
10. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **CANALES DE COMUNICACIÓN** | Pagina: 2]
   > Correo: Lista de mail (consultas y comunicación de rutina) Aula virtual: Material académico - Clave de matriculación: bda2023 (ÚNICO MEDIO OFICIAL) Telegram: https://t.me/+c7PPIrc9nQM4MzEx (avisos y n

**Respuesta:**

Para resolver problemas de optimización a gran escala con integración fluida a bases de datos, la combinación más adecuada consiste en utilizar **LINGO (64 bits)** en conjunto con **PostgreSQL** (versión 9.6 o superior) y **QGIS**.

Esta configuración integra las capacidades específicas de cada área de la siguiente manera:

*   **Optimización:** LINGO es la herramienta indicada para el modelado y resolución de problemas de optimización de gran escala, destacándose por su capacidad de integrarse de forma fluida con bases de datos.
*   **Gestión de Datos y Espacialidad:** PostgreSQL, en sus versiones 9.6 o superiores, provee la infraestructura de base de datos, mientras que QGIS actúa como el software compatible con PostgreSQL, permitiendo el manejo y procesamiento de datos espaciales.

Esta combinación permite aprovechar la potencia de cálculo de LINGO para los modelos complejos y la robustez de PostgreSQL y QGIS para la gestión y análisis de la información geográfica requerida.

**Tokens:** entrada: 1678 | salida: 210 | total: 1888

---

### Pregunta 12

> - Si un estudiante desea investigar sobre el impacto de los "Agentes que aprenden" y las "Redes Neuronales" en la selección de personal y el teletrabajo en Argentina, ¿qué normativas legales y temas específicos de los programas de Inteligencia Artificial y RRHH debería cruzar en su marco teórico?

**Chunks de contexto:**

1. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: **I. FUNDAMENTACIÓN** | Pagina: 1]
   > Los estudiantes explorarán los efectos de las nuevas tecnologías en el trabajo, la calidad de vida laboral y la administración del talento humano en la era digital. Además, se abordarán aspectos legal
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 4. El impacto de la inteligencia artificial en la gestión del talento. | Pagina: 2]
   > _**Bibliografía Nacional:**_ Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales. **Uni
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: IV. BIBLIOGRAFÍA GENERAL | Pagina: 3]
   > _**Bibliografía Complementaria:**_ Reglamento de Teletrabajo en Argentina. Legislación sobre delitos informáticos en Argentina. Artículos académicos sobre la transformación del trabajo y el impacto
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 2]
   > Reglamento de Teletrabajo en Argentina. Nicolás S. Tato, El Derecho Informático - Aspectos Fundamentales. Mariana Nazar, Tecnologías, información y derechos. **Unidad 2:** **Relaciones Humanas en e
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 6. Desafíos éticos y sociales de la tecnología en el ámbito laboral. | Pagina: 1]
   > _**Bibliografía Nacional:**_ Ley de Teletrabajo (Ley 27.555).
6. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 3]
   > Legislación sobre delitos informáticos en Argentina. Ley Nacional de Protección de Datos Personales (Ley 25.326). Ley Propiedad Intelectual (Ley 11.723) y su modificatoria. **Unidad 5: Trabajo Autó
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Proceso de Inferencia. Tratamiento paralelo de las reglas. Determinación del aporte parcial de cada regla. Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > Modificación del algoritmo SOM para evitar una excesiva acumulación de información, por parte de una misma neurona. **Capítulo XII** **Sistemas Multi Agentes** Introducción a los sistemas multiagen
9. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > Regiones de Decisión. Modo de operación autoasociativo. **Capítulo X** **Generalización en las RNA,** definición, factores que influyen en la capacidad de Generalización. Tamaño del conjunto de pat
10. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Comportamiento de Agentes Basados en Conocimientos. **Capítulo IV** **Diseño de los Sistemas Expertos**. Definición y descripción de sus módulos componentes. Proceso de Adquisición de Conocimiento.

**Respuesta:**

Para investigar el impacto de los agentes inteligentes y las redes neuronales en la selección de personal y el teletrabajo en Argentina, el marco teórico debe integrar los siguientes componentes técnicos y normativos:

### 1. Componentes técnicos (Inteligencia Artificial)
El estudiante debe abordar los fundamentos de los sistemas basados en agentes y el aprendizaje automático para comprender cómo estos operan en la gestión del talento:
*   **Agentes y Comportamiento:** Es necesario estudiar los "Agentes basados en conocimientos" (Capítulo IV) y los "Sistemas Multiagente" (Capítulo XII), los cuales incluyen modelos formales, metodologías de diseño (Gaia), protocolos de interacción y estándares (FIPA, ACL).
*   **Redes Neuronales (RNA):** Se deben analizar las generalidades y clasificaciones de las RNA (Capítulo VIII), la capacidad de generalización, el *Deep Learning*, los modelos generativos y los algoritmos de reducción (*Pruning*).
*   **Aprendizaje y Autoorganización:** Resulta clave profundizar en el aprendizaje competitivo, las redes autoorganizadas (Red SOM/Kohonen) y los agentes basados en procesos de aprendizaje, que permiten a los sistemas adaptarse y procesar información.

### 2. Marco Normativo Argentino
Para analizar la legalidad y el impacto ético de estas tecnologías en el ámbito laboral local, deben cruzarse los siguientes cuerpos legales:
*   **Teletrabajo:** Es obligatorio contemplar la Ley de Teletrabajo (Ley 27.555) y el Reglamento de Teletrabajo en Argentina.
*   **Protección de Datos y Propiedad Intelectual:** Dada la naturaleza de los datos procesados por agentes y redes neuronales, es fundamental aplicar la Ley Nacional de Protección de Datos Personales (Ley 25.326) y la Ley de Propiedad Intelectual (Ley 11.723).
*   **Delitos Informáticos:** La legislación vigente sobre delitos informáticos en Argentina constituye un eje preventivo necesario frente a la implementación de sistemas automatizados.

### 3. Ejes de integración (RRHH y Ética)
Estos elementos técnicos y legales deben articularse bajo los temas transversales de la materia de Informática y RRHH:
*   **Gestión del talento en la era digital:** Analizar cómo la IA transforma las relaciones laborales y la administración del talento humano.
*   **Desafíos éticos y sociales:** Evaluar el impacto de la tecnología en la calidad de vida laboral y los aspectos normativos de las TIC, apoyándose en la bibliografía nacional sobre Derecho y nuevas tecnologías (Gonzalo Ana Dobratinich, Nicolás S. Tato y Mariana Nazar).

Al cruzar estos datos, el estudiante podrá fundamentar cómo los modelos de aprendizaje (como los agentes y las RNA) se insertan en un entorno regulado por leyes de protección de datos y teletrabajo, permitiendo una gestión del talento que cumpla con el marco normativo argentino vigente.

**Tokens:** entrada: 1662 | salida: 626 | total: 2288

---

### Pregunta 13

> - ¿Dónde puedo descargar la materia de Cálculo de 1er año?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: -> BÚSǪUEDA AVANZADA con GOOGLE - PRIMERA PARTE - APRENDER A INVESTIGAR **:** | Pagina: 12]
   > **[https://youtu.be/9oWM50RDsLǪ](https://youtu.be/9oWM50RDsLQ)**
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 3]
   > hojas de cálculo.
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: AÑO ACADEMICO: 2023 | Pagina: 1]
   > PLAN DE ESTUDIO: 2010 (Resolución No 397/10 UADER)
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 13]
   > - Yuni, J y Urbano, C (2016) Técnicas para investigar 2: Recursos metodológicos para la preparación de proyectos de investigación. Editorial Brujas: Argentina _Material audiovisual de la unidad_
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: dentro de la plataforma Moodle. La organización será la siguiente | Pagina: 5]
   > - Inicio del curso: contendrá información general de la cátedra, incluyendo el programa, el equipo docente, el cronograma, los objetivos, los materiales utilizados, el enlace de videoconferencia, la
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > **Instancias de Recuperación:** La cátedra dispone de **dos oportunidades de** **recuperatorio** totales. Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no s
7. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **CANALES DE COMUNICACIÓN** | Pagina: 2]
   > Correo: Lista de mail (consultas y comunicación de rutina) Aula virtual: Material académico - Clave de matriculación: bda2023 (ÚNICO MEDIO OFICIAL) Telegram: https://t.me/+c7PPIrc9nQM4MzEx (avisos y n
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: UNDERWRITERS LABORATORIES (UL) -> www.ul.com | Pagina: 5]
   > PANDUIT -> www.panduit.com AMP -> www.tycoelectronics.com/components/ ETHEREAL -> www.ethereal.com SIEMENS -> www.sea.siemens.com/step/templates/lesson.mason?electricity:2:3:3
9. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > **Obligatoria** - Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] - Cisco Systems: Academia de Networking de Cisco Systems: Guía del primer añ
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 15]
   > ; director José Luis Mengarelli.|2019| |Estrategia para planear una migración de software propietario a<br>software librepara la Facultad de Ciencia y Tecnología (FCyT) Sede Oro<br>Verde en el año 201

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1645 | salida: 13 | total: 1658

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
   > Comportamiento de Agentes Basados en Conocimientos. **Capítulo IV** **Diseño de los Sistemas Expertos**. Definición y descripción de sus módulos componentes. Proceso de Adquisición de Conocimiento.
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > **Red Perceptron Simple.** Elemento de Procesamiento. Función de Transferencia. Condiciones de Convergencia. Proceso de Entrenamiento. Algoritmo de Modificación de los
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > Regiones de Decisión. Modo de operación autoasociativo. **Capítulo X** **Generalización en las RNA,** definición, factores que influyen en la capacidad de Generalización. Tamaño del conjunto de pat
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: pesos. Regiones de Decisión. Problema de separación lineal. Aplicaciones. Limitaciones | Pagina: 2]
   > Problema XOR.
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Clase de direccionamiento (clase a, b, c, d y e). Prefijo y Mascara de red. Lógica de and. Calculo de direcciones. División de subredes (por clase y vlsm (mascara de subred de longitud variable)), i
9. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (2
10. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **BIBLIOGRAFÍA BASE** | Pagina: 2]
   > Elmasri, R. / Navathe, S. - Fundamentos de Sistemas de Bases de Datos (Addison Wesley) Silberschatz / Korth / Sudarshan - Fundamentos de Bases de Datos (Mc Graw Hill) Date, C.J. - Introducción a los S

**Respuesta:**

La afirmación es parcialmente correcta. El Ing. Jorge L. Schmukler forma parte del equipo docente en las cátedras de Bases de Datos Avanzadas y Comunicaciones y Redes. No existe información en los documentos proporcionados que lo vincule como docente de la materia Inteligencia Artificial.

**Tokens:** entrada: 1523 | salida: 61 | total: 1584

---

### Pregunta 15

> - ¿Cuál es el costo de la certificación oficial de Cisco que se menciona como opcional en la planificación?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > **Obligatoria** - Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] - Cisco Systems: Academia de Networking de Cisco Systems: Guía del primer añ
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > . Explicar el **propósito de IOS como Sistema** **Operativo de red**, Explicar cómo acceder al IOS y cómo explorarlo para configurar los dispositivos de red, Describir la estructura de comandos, Confi
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Sitios web sobre normativas, tecnologías y soluciones, opcional** | Pagina: 5]
   > IETF -> www.ietf.org IEEE -> www.ieee.org ISO -> www.iso.org CISCO -> www.cisco.com IANA -> www.iana.org ISOC -> www.isoc.org ARIN -> www.arin.net LACNIC -> http://lacnic.net/sp/ LAC IPV6 TF -> www.la
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . ARP proxy. **Cableado Estructurado**: Selección de dispositivos intermedios. Interconexiones de dispositivos intermedios y finales (longitud del medio, áreas de trabajo, cuarto de telecomunicaciones
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Proveedores de servicio de internet (ISP), descripción Ipv6. **Unidad IX** **-VLans-** Definiciones de Vlan, Beneficios de una Vlan, Rangos de ID de la Vlan (rango normal y rango extendido), Tipos d
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Clase de direccionamiento (clase a, b, c, d y e). Prefijo y Mascara de red. Lógica de and. Calculo de direcciones. División de subredes (por clase y vlsm (mascara de subred de longitud variable)), i
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: UNDERWRITERS LABORATORIES (UL) -> www.ul.com | Pagina: 5]
   > PANDUIT -> www.panduit.com AMP -> www.tycoelectronics.com/components/ ETHEREAL -> www.ethereal.com SIEMENS -> www.sea.siemens.com/step/templates/lesson.mason?electricity:2:3:3
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos vertidos en la teoría. Más dos trabajos Prácticos que se realizan en el ho
9. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . La ethernet actual. La trama de ethernet. Power Over Ethernet. Direcciones MAC. Dispositivo de red (nic). Ethernet unicast, multicast, broadcast. CSMA/CD (Acceso Múltiple por Detección de Portadora
10. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 3]
   > - privados). Protocolo de Datagrama de Usuario - **UDP** - (datagrama, protocolo no orientado a la conexión, encabezado). **Unidad XII**: - **Capa de Aplicación, Presentación y Sesión** Función capa A

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta. La planificación menciona a Cisco como un sitio web opcional sobre normativas, tecnologías y soluciones, pero no hace referencia a costos de certificaciones oficiales.

**Tokens:** entrada: 2108 | salida: 43 | total: 2151

---

### Pregunta 16

> - Para la Promoción Directa, se exige la aprobación de la totalidad de los trabajos prácticos (TP 1 al TP 5). ¿Cuál es la calificación numérica mínima que debe obtenerse en cada TP individual para que se considere aprobado?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 16]
   > Para acceder a la condición de Promoción Directa, el/la estudiante deberá cumplir con los siguientes requisitos: - 80 % de asistencia a la cursada. - Aprobación del examen parcial teórico con una
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > **Condición del Alumno:** - **ALUMNO PROMOCIONADO:** El estudiante logrará la promoción directa si alcanza un promedio general de **80 puntos** - más entre los **1 parcial** previstos, no pudiendo
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > **2-** Haber realizado y aprobado los dos trabajos Práctico impartido por la cátedra. **3-** Asistir al 80% de las clases teóricas y prácticas. El alumno tendrá condición de **LIBRE** si no cumple con
4. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **RÉGIMEN DE CURSADA** | Pagina: 2]
   > **Regularidad:** Asistencia: Según norma vigente Todos los trabajos prácticos aprobados 6/7 parciales aprobados con más del 50% **Promoción:** Régimen regular Obtener más del 70% en todos los parci
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > **1 -** Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos. Tener aprobado con 60 puntos los tres parciales.
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos vertidos en la teoría. Más dos trabajos Prácticos que se realizan en el ho
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > El/la estudiante que no se ajuste a los requisitos establecidos en los puntos A y B, se considerará en condición libre. Deberá presentar el trabajo práctico integrador con una antelación mínima de v
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 9]
   > **Programa de trabajos prácticos:** Tp 1: Escritura académica. Se solicita a los estudiantes seleccionar un artículo de investigación sobre un tema de interés específico relacionado al campo profesi
9. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 8]
   > - Entrega obligatoria de las actividades prácticas y aprobación del trabajo práctico integrador final, respetando las fechas establecidas en el cronograma académico.
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 9]
   > conceptos. Formulación de objetivos e hipótesis. Tp 4: Elaboración de un escrito en donde presenten: Marco metodológico. El tiempo, período o secuencia de estudio. Universo, muestra y unidad de mues

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta. Si bien se especifica que la aprobación de la totalidad de los trabajos prácticos es un requisito para la Promoción Directa en la materia Metodología de la Investigación, el programa no establece una calificación numérica mínima individual para cada uno de los trabajos prácticos (TP 1 al TP 5).

**Tokens:** entrada: 1780 | salida: 74 | total: 1854

---

### Pregunta 17

> - ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > Lineal: proporcionalidad, aditividad, divisibilidad y certidumbre. Formulación de problemas de optimización. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en l
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **PHP Simplex:** Herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el Método Simplex y el Método Gráfico. Es ideal para validaciones rápidas y vis
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > entrada y salida de variables. Interpretación de la tabla óptima. Aplicación del método de la "M Grande" y método de las "Dos Fases". Análisis de dualidad y sensibilidad básica en modelos lineales.
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadístico
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 3]
   > hojas de cálculo.
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > estructura del modelo y suposiciones. Métodos para obtener una solución básica inicial: Esquina Noroeste, Costo Mínimo y Aproximación de Vogel. Método MODI (Distribución Modificada) para la optimiza
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > **Condición del Alumno:** - **ALUMNO PROMOCIONADO:** El estudiante logrará la promoción directa si alcanza un promedio general de **80 puntos** - más entre los **1 parcial** previstos, no pudiendo
9. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: pesos. Regiones de Decisión. Problema de separación lineal. Aplicaciones. Limitaciones | Pagina: 2]
   > Problema XOR.
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: -> Paula Espeche Trayecto 2 Google académico y operadores booleanos | Pagina: 12]
   > **[https://youtu.be/fiSJ4bDb Nwrc](https://youtu.be/1SJ4bDb Nwrc)**

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta. El contenido disponible describe los fundamentos teóricos del método Simplex (forma estándar, variables de holgura y artificiales, tabla inicial, criterios de entrada/salida e interpretación) y menciona diversas herramientas de software específicas para la resolución de modelos (PHP Simplex, LINGO, Storm, TORA, LINDO y WinQSB), pero no incluye instrucciones ni procedimientos para realizarlo mediante Excel.

**Tokens:** entrada: 1680 | salida: 94 | total: 1774

---

### Pregunta 18

> - ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > corridos tras la evaluación. Los exámenes se desarrollarán estrictamente en los bloques horarios asignados a la materia. La ausencia no justificada (sin certificado médico o motivo de fuerza mayor v
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > **Instancias de Recuperación:** La cátedra dispone de **dos oportunidades de** **recuperatorio** totales. Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no s
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > **Condición del Alumno:** - **ALUMNO PROMOCIONADO:** El estudiante logrará la promoción directa si alcanza un promedio general de **80 puntos** - más entre los **1 parcial** previstos, no pudiendo
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > |||||investigación| |17|13 de agosto|Virtual|Tutorías|Tutorías| |18|20 de agosto|**_Presencial (cambio_**<br>**_encuentro)_**|**Teoría**|Parcial teoría| |19|27 de agosto|Virtual|Tutorías|Tutorías| |20
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > **b.** **Alumno Regular** - 60 % de asistencia. - Aprobación del examen parcial teórico con una calificación igual o superior a 60 (sesenta) puntos. - Entrega de todos los trabajos en tiempo y
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > . La nota obtenida en este reemplaza a la obtenida en el parcial que se recupera La cátedra dará el resultado de cada una de las evaluaciones parciales y recuperatorios una semana después de que estas
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > entrada y salida de variables. Interpretación de la tabla óptima. Aplicación del método de la "M Grande" y método de las "Dos Fases". Análisis de dualidad y sensibilidad básica en modelos lineales.
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: -> Paula Espeche Trayecto 2 Google académico y operadores booleanos | Pagina: 12]
   > **[https://youtu.be/fiSJ4bDb Nwrc](https://youtu.be/1SJ4bDb Nwrc)**
9. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: Unidad VII: Bases de Datos Orientadas a Objetos - Parcial | Pagina: 1]
   > Nota: Los parciales serán agrupados en 2 o 3 instancias durante el cursado
10. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > estructura del modelo y suposiciones. Métodos para obtener una solución básica inicial: Esquina Noroeste, Costo Mínimo y Aproximación de Vogel. Método MODI (Distribución Modificada) para la optimiza

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1872 | salida: 13 | total: 1885

---

## Resumen de tokens

| Conversacion | Entrada | Salida | Total |
|---|---|---|---|
| 1 | 34382 | 3140 | 37522 |
| 2 | 32252 | 3326 | 35578 |
| 3 | 31795 | 2876 | 34671 |
| **Total** | **98429** | **9342** | **107771** |
