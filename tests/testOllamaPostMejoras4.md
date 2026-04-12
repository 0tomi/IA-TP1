# Evaluacion — testOllamaPostMejoras4

_Iniciada: 2026-04-12 19:46:41_
_Ultima actualizacion: 2026-04-12 19:55:57_

**Estado:** completado
**Archivo de evaluacion:** `tests/evaluaciones/testOllamaPostMejoras.md`
**Preguntas:** 18 | **Conversaciones planificadas:** 3 | **Conversaciones iniciadas:** 3 | **Preguntas procesadas:** 54

## Conversacion 1

**Puntaje evaluado: 15.5 / 18**

**Parametros:**

| Parametro | Valor |
|---|---|
| top_k | 10 |
| retrieval_type | similarity_search |
| threshold | 0.5 |
| max_context_chunks | 10 |
| temperatura | 1.0 |
| debug | False |
| llm_provider | ollama |
| llm_model | llama3.1 |
| chunk_size | 600 |
| chunk_overlap | 100 |
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
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > ión del aporte parcial de cada regla. Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación de los disti
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > *Capítulo III** **Sistemas Basados en Conocimientos**. Conceptos básicos. Representación de Conocimientos. Estructuras basadas en Lógica. Lógica de Primer Orden. Reglas de Inferencia. Representación
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (2
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > cidad de Generalización. Tamaño del conjunto de patrones para el entrenamiento. Algoritmos de reducción (Pruning Algorithms). Deep Learning. Modelos Generativos **Capítulo XI** Redes Autoorganizadas
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > amiento de Agentes Basados en Conocimientos. **Capítulo IV** **Diseño de los Sistemas Expertos**. Definición y descripción de sus módulos componentes. Proceso de Adquisición de Conocimiento. Base d
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > en objetivos. Agentes que aprenden. **Capítulo II** **Procesos de Búsqueda.** Representación en un espacio de estados. Búsqueda Ciega, definición; búsqueda primero en amplitud, búsqueda de costo un
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Estructura de Control: Procedimientos de Inferencia; Interfase con el usuario. Memoria de Trabajo, Módulo generador de explicaciones al usuario. **Capítulo V** **Funcionalidad de los Sistemas Exper
9. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > a acumulación de información, por parte de una misma neurona. **Capítulo XII** **Sistemas Multi Agentes** Introducción a los sistemas multiagente, modelos formales. Metodologías de diseño basadas e
10. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > o de Procesamiento. Función de Transferencia. Condiciones de Convergencia. Proceso de Entrenamiento. Algoritmo de Modificación de los

**Respuesta:**

Los contenidos de la materia Inteligencia Artificial abarcan varios capítulos. El primer capítulo aborda los Agentes Inteligentes, incluyendo la introducción a la Inteligencia Artificial, definiciones y objetivos, herramientas y técnicas, descripción de los temas específicos a desarrollarse, introducción a los agentes inteligentes, entornos de trabajo, propiedades de los entornos, estructura de los agentes, programas de agentes, agentes reactivos simples, agentes reactivos basados en modelos, agentes basados en objetivos, y agentes que aprenden.

Además, se encuentran otros capítulos que cubren temas específicos como Procesos de Búsqueda, Representación del conocimiento mediante reglas y estructuras basadas en lógica, Sistemas Basados en Conocimientos, Diseño de los Sistemas Expertos, Redes Neuronales Artificiales, Agentes Basados en Lógica Difusa, Redes Autoorganizadas, y Sistemas Multi Agentes.

Es importante mencionar que también se proporcionan bibliografías recomendadas para profundizar en algunos de estos temas.

**Tokens:** entrada: 2145 | salida: 254 | total: 2399

---

### Pregunta 2

> - ¿En qué materia se enseña el concepto de Lógica Difusa?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > simples entre conjuntos Difusos: Inclusión, Igualdad, Complementación, Intersección, Unión. Estructuras FAM (Fuzzy Associative Memories). Composición MAX-MIN. **Capítulo VII** **Sistemas** **Difusos
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > ión del aporte parcial de cada regla. Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación de los disti
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Estructura de Control: Procedimientos de Inferencia; Interfase con el usuario. Memoria de Trabajo, Módulo generador de explicaciones al usuario. **Capítulo V** **Funcionalidad de los Sistemas Exper
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > *Capítulo III** **Sistemas Basados en Conocimientos**. Conceptos básicos. Representación de Conocimientos. Estructuras basadas en Lógica. Lógica de Primer Orden. Reglas de Inferencia. Representación
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > el modelo de aula invertida, en el que los estudiantes adquieren los conocimientos teóricos de manera previa a la clase, a través de videos elaborados por la cátedra, lecturas y otros materiales int
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > cidad de Generalización. Tamaño del conjunto de patrones para el entrenamiento. Algoritmos de reducción (Pruning Algorithms). Deep Learning. Modelos Generativos **Capítulo XI** Redes Autoorganizadas
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > en objetivos. Agentes que aprenden. **Capítulo II** **Procesos de Búsqueda.** Representación en un espacio de estados. Búsqueda Ciega, definición; búsqueda primero en amplitud, búsqueda de costo un
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > e de direccionamiento (clase a, b, c, d y e). Prefijo y Mascara de red. Lógica de and. Calculo de direcciones. División de subredes (por clase y vlsm (mascara de subred de longitud variable)), icmpv4
9. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 12]
   > - Natale, Lucía (Coordinadora) (2013). En carrera: escritura y lectura de textos académicos y profesionales. Argentina. Universidad Nacional de Ǫuilmes. Visto en [https://ediciones.ungs.edu.ar/wp-co
10. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > **Capítulo IX** **Redes** **Perceptron** **Multicapa**, estructura básica. Proceso de Entrenamiento Backpropagation (BP). Interpretación heurística y matemática del procedimiento BP. Término de Momen

**Respuesta:**

La materia en la que se enseña el concepto de Lógica Difusa es la Inteligencia Artificial.

**Tokens:** entrada: 2468 | salida: 26 | total: 2494

---

### Pregunta 3

> - ¿Cuál es el plan de estudios de Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: **Equipo docente:** PROFESORA RESPONSABLE ADJUNTO: ALEJANDRA MARǪUESIN; JEFE DE | Pagina: 1]
   > TRABAJOS PRÁCTICOS: TAMARA SUIVA. JEFE DE TRABAJOS PRÁCTICOS: JIMENA SANTA CRUZ; **Año de la carrera a la que pertenece la cátedra:** 4 **Régimen de la materia:** Anual **Carga horaria semanal:** 3
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > btención y análisis de información empírica. La comunicación de los resultados **Cronograma de trabajo** |METODOLOGÍA DE LA INVESTIGACIÓN- 2026|Col2|Col3|Col4|Col5| |---|---|---|---|---| |**Clase **
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > ificación del trabajo integrador se determinará exclusivamente en la mesa de examen, junto con la nota correspondiente a la instancia teórica, estableciéndose en ese momento la calificación final y
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: dentro de la plataforma Moodle. La organización será la siguiente | Pagina: 5]
   > - Desarrollo de contenidos: distribuidos en tres pestañas temáticas: - Introducción - Dimensión epistemológica - Dimensión estratégica - Dimensión técnica - Cada semana se habilitarán los co
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: dentro de la plataforma Moodle. La organización será la siguiente | Pagina: 5]
   > - Inicio del curso: contendrá información general de la cátedra, incluyendo el programa, el equipo docente, el cronograma, los objetivos, los materiales utilizados, el enlace de videoconferencia, la
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > |12|28 de mayo|Virtual|Teoría|Col5| |---|---|---|---|---| |13|04 de junio|**Presencial**|**Teoría**|Marco metodológico I: enfoque y<br>tipo de investigación / muestra| |14|11 de junio|Virtual|Práctica
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > clase)|(sin clase)|(sin clase)| |5|09 de abril|**Presencial**|**Teoría**|Tema/ problema| |6|16 de abril|Virtual|Práctica|| |7|23 de abril|Virtual|Teoría|Pregunta de investigación<br>(variables, unidad
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: **Equipo docente:** PROFESORA RESPONSABLE ADJUNTO: ALEJANDRA MARǪUESIN; JEFE DE | Pagina: 1]
   > a la Metodología de la Investigación como el conjunto de estrategias, reflexiones y decisiones que configuran los procesos de investigación científica. Por lo general, estos espacios en la formación
9. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 3]
   > **Objetivos generales:** - Acercar al campo de la investigación científica desde espacios de reflexión sistemáticos enmarcados en trabajos propios de la disciplina y el campo profesional. **Objeti
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > mientras que el resto de las clases se desarrollarán de manera presencial mediadas por tecnología a través de Google Meet. En estos encuentros virtuales, se trabajarán tanto los fundamentos teóricos

**Respuesta:**

El plan de estudios de Metodología de la Investigación está resumido en cinco unidades:

- Unidad 1: Introducción a la ciencia y conocimiento científico
- Unidad 2: La dimensión epistemológica
- Unidad 3: La dimensión de la estrategia general de investigación
- Unidad 4: La Dimensión de las técnicas de obtención y análisis de información empírica. La comunicación de los resultados
- Unidad 5: Se menciona una unidad 5 pero no se especifica el tema.

**Tokens:** entrada: 2557 | salida: 130 | total: 2687

---

### Pregunta 4

> - ¿Qué herramientas de software se recomiendan en la carrera para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > :** Herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el Método Simplex y el Método Gráfico. Es ideal para validaciones rápidas y visualización de r
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadísticos mediante una i
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > eal: proporcionalidad, aditividad, divisibilidad y certidumbre. Formulación de problemas de optimización. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en los
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > estructura del modelo y suposiciones. Métodos para obtener una solución básica inicial: Esquina Noroeste, Costo Mínimo y Aproximación de Vogel. Método MODI (Distribución Modificada) para la optimiza
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: pesos. Regiones de Decisión. Problema de separación lineal. Aplicaciones. Limitaciones | Pagina: 2]
   > Problema XOR.
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad I: -Introducción y Modelos Matemáticos-** Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del problema, construcción del modelo mate
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
9. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > n de problemas de diligencia, asignación de recursos y reemplazo de equipos. Diferencias entre Programación Dinámica Determinística y Probabilística.
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 15]
   > rategia para planear una migración de software propietario a<br>software librepara la Facultad de Ciencia y Tecnología (FCyT) Sede Oro<br>Verde en el año 2018 /Emanuel Antonio Wasinger ; director Aldo

**Respuesta:**

La respuesta está relacionada con el contenido del documento "PROGRAMA - Investigación Operativa.pdf". Se recomiendan herramientas de software como LINDO, WinQSB 2.0 y PHP Simplex para resolver problemas de optimización lineal. LINDO se destaca por su sintaxis sencilla para ingresar ecuaciones y restricciones directamente. Por otro lado, WinQSB 2.0 es una suite que abarca múltiples módulos de Investigación Operativa y permite resolver problemas de programación lineal entre otros. Por último, PHP Simplex es una herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el Método Simplex y el Método Gráfico. Estas herramientas se relacionan con las unidades teóricas, como la Unidad II - Programación Lineal (PL), donde se estudian propiedades de los modelos de Programación Lineal.

**Tokens:** entrada: 2059 | salida: 200 | total: 2259

---

### Pregunta 5

> - ¿Qué instancias de recuperación nos provee Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > ncias de Recuperación:** La cátedra dispone de **dos oportunidades de** **recuperatorio** totales. Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se puede
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad I: -Introducción y Modelos Matemáticos-** Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del problema, construcción del modelo mate
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadísticos mediante una i
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > **Condición del Alumno:** - **ALUMNO PROMOCIONADO:** El estudiante logrará la promoción directa si alcanza un promedio general de **80 puntos** - más entre los **1 parcial** previstos, no pudiendo
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > eal: proporcionalidad, aditividad, divisibilidad y certidumbre. Formulación de problemas de optimización. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en los
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > :** Herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el Método Simplex y el Método Gráfico. Es ideal para validaciones rápidas y visualización de r
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > lida de variables. Interpretación de la tabla óptima. Aplicación del método de la "M Grande" y método de las "Dos Fases". Análisis de dualidad y sensibilidad básica en modelos lineales.
9. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
10. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 3]
   > hojas de cálculo.

**Respuesta:**

La cátedra de Investigación Operativa dispone de dos oportunidades de recuperatorio totales. Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mismo examen parcial. La calificación obtenida en la instancia de recuperación sustituirá automáticamente a la nota del examen original.

**Tokens:** entrada: 2098 | salida: 85 | total: 2183

---

### Pregunta 6

> - ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadísticos mediante una i
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > a<br>cátedra-Grupos Tamara| |22|17<br>de<br>septiembr<br>e|Teoría|Coloquio|Avances proyectos a la<br>cátedra-Grupos Jimena| |23|24<br>de<br>septiembr<br>e|Virtual|Tutorías|Tutorías| |24|01 de octubre|
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos vertidos en la teoría. Más dos trabajos Prácticos que se realizan en el ho
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > :** Herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el Método Simplex y el Método Gráfico. Es ideal para validaciones rápidas y visualización de r
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > **Capítulo IX** **Redes** **Perceptron** **Multicapa**, estructura básica. Proceso de Entrenamiento Backpropagation (BP). Interpretación heurística y matemática del procedimiento BP. Término de Momen
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: pesos. Regiones de Decisión. Problema de separación lineal. Aplicaciones. Limitaciones | Pagina: 2]
   > Problema XOR.
9. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > cidad de Generalización. Tamaño del conjunto de patrones para el entrenamiento. Algoritmos de reducción (Pruning Algorithms). Deep Learning. Modelos Generativos **Capítulo XI** Redes Autoorganizadas
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > estudiantes los materiales y herramientas necesarios para la construcción autónoma del conocimiento. - Cada clase incluirá uno o más de los siguientes recursos: - Un video explicativo. - Materi

**Respuesta:**

El software TORA es una herramienta educativa diseñada específicamente para el aprendizaje de la Investigación Operativa. Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos.

**Tokens:** entrada: 2114 | salida: 57 | total: 2171

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
   > onible en Biblioteca FCyT- Oro Verde] - Arena, Héctor Facundo: Linux: la guía definitiva / H. F. Arena. - Buenos Aires: Gradi, 2010. ISBN 9789872601386 [Disponible en Biblioteca FCyT- Oro Verde] -
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > **Obligatoria** - Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] - Cisco Systems: Academia de Networking de Cisco Systems: Guía del primer añ
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 15]
   > laro ;<br>directora Patricia Lucila Vivas.|2018| |Implementación de Bases de Datos NOSǪL / Rubén Orlando Almada ; director<br>Alejandro Javier Hadad.|2018| |Herramientas ágiles utilizadas en el desarr
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > rid: Pearson Educación, 2006. ISBN 9788478290833 [Disponible en Biblioteca FCyT- Oro Verde] - Huidobro Moya, José Manuel: Redes de datos y convergencia IP / J. M. Huidobro Moya, Ramón Jesús Millán T
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > n con el cable). **Unidad IV**: - **Capa de enlace de dato** - **sub capa** **LLC (control de enlace lógico)** Cuestiones en el diseño de la capa de enlace de dato, servicios proporcionados por la cap
9. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **PRESENTACIÓN DE LA MATERIA** | Pagina: 1]
   > Facultad de Ciencia y Tecnología Universidad Autónoma de Entre Ríos (UADER)
10. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **HORARIOS DE CLASE** | Pagina: 1]
   > Lunes: 13:30 a 15:30 (Teoría) Viernes: 17:00 a 19:00 (Práctica) Nota: Los horarios están en proceso de evaluación y pueden sufrir cambios

**Respuesta:**

El profesor que forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes es Ing. Jorge L. Schmukler.

**Tokens:** entrada: 2069 | salida: 44 | total: 2113

---

### Pregunta 8

> - ¿Qué otra asignatura, además de la propia materia de Inteligencia Artificial, incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos **Capítulo I** **Agentes Inteligentes** Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas p
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 4. El impacto de la inteligencia artificial en la gestión del talento. | Pagina: 2]
   > _**Bibliografía Nacional:**_ Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales. **Uni
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (2
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > a acumulación de información, por parte de una misma neurona. **Capítulo XII** **Sistemas Multi Agentes** Introducción a los sistemas multiagente, modelos formales. Metodologías de diseño basadas e
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Estructura de Control: Procedimientos de Inferencia; Interfase con el usuario. Memoria de Trabajo, Módulo generador de explicaciones al usuario. **Capítulo V** **Funcionalidad de los Sistemas Exper
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > ión del aporte parcial de cada regla. Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del centroide. Método de máxima. Influencia de la aplicación de los disti
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > o de Procesamiento. Función de Transferencia. Condiciones de Convergencia. Proceso de Entrenamiento. Algoritmo de Modificación de los
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > *Capítulo III** **Sistemas Basados en Conocimientos**. Conceptos básicos. Representación de Conocimientos. Estructuras basadas en Lógica. Lógica de Primer Orden. Reglas de Inferencia. Representación
9. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > en objetivos. Agentes que aprenden. **Capítulo II** **Procesos de Búsqueda.** Representación en un espacio de estados. Búsqueda Ciega, definición; búsqueda primero en amplitud, búsqueda de costo un
10. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > **Capítulo IX** **Redes** **Perceptron** **Multicapa**, estructura básica. Proceso de Entrenamiento Backpropagation (BP). Interpretación heurística y matemática del procedimiento BP. Término de Momen

**Respuesta:**

Además de la materia de Inteligencia Artificial, la asignatura de Informática y Recursos Humanos incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas.

**Tokens:** entrada: 2200 | salida: 52 | total: 2252

---

### Pregunta 9

> - Los requisitos para regularizar en Bases de Datos Avanzadas y en Redes y Comunicaciones, ¿son iguales? ¿Qué diferencias tienen?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > ma salvo que se presente justificativo medico o que sea entendida justificada la ausencia. **Evaluación Final:** El alumno con condición de REGULAR, deberá rendir un examen de los temas teóricos y pr
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > PROMOCIONADO REGULAR LIBRE El alumno accederá a la condición de **PROMOCIÓN** si cumple con las siguientes condiciones de cátedra: **1 -** Obtener en los 3 parciales, una calificación promedio sup
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > ediza). Protocolo enlace de datos ( **HDLC** -Control de enlace de datos de alto nivel-, Capa de enlace de datos en Internet -Protocolo **PPP** (Protocolo Punto a Punto)-). **Unidad V**: - **Capa de e
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > hernet de 10 gigabits (10gbe)). Utilización de hubs como dispositivo intermedio (problemas con el crecimiento de la red: escalabilidad, fallas en la red, colisiones). Switches (ancho de banda dedicado
5. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **SOFTWARE REQUERIDO** | Pagina: 2]
   > PostgreSQL: versión 9.6 o superior SQL Server: versión 2016 o superior QGIS: versión compatible con PostgreSQL Anaconda (Python): últimas versiones
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > e de direccionamiento (clase a, b, c, d y e). Prefijo y Mascara de red. Lógica de and. Calculo de direcciones. División de subredes (por clase y vlsm (mascara de subred de longitud variable)), icmpv4
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > sión, Enrutamiento para hosts móviles, Enrutamiento en redes ad hoc, Búsqueda de nodos en redes de igual a igual), RIP protocolo de enrutamiento por clase vector de distancia, configuración, VLSM y CI
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > iguientes condiciones de cátedra: **1 -** Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos. Tener aprobado con 60 puntos los tres parciales. **2-** Haber realiz
9. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **CANALES DE COMUNICACIÓN** | Pagina: 2]
   > Correo: Lista de mail (consultas y comunicación de rutina) Aula virtual: Material académico - Clave de matriculación: bda2023 (ÚNICO MEDIO OFICIAL) Telegram: https://t.me/+c7PPIrc9nQM4MzEx (avisos y n
10. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > vos intermedios y finales (longitud del medio, áreas de trabajo, cuarto de telecomunicaciones, cableado horizontal, cableado backbone, cableado vertical, tipos de medios). Conexiones según norma t568a

**Respuesta:**

Los requisitos para obtener la condición de regular en Bases de Datos Avanzadas no están disponibles en el contexto proporcionado. Sin embargo, sí tenemos información sobre los requisitos para regularizar en Redes y Comunicación.

En Redes y Comunicación, un alumno debe tener una calificación promedio superior o igual a los 80 puntos en los 3 parciales, con ninguna nota inferior a 60 puntos en cada parcial. También deben haber realizado y aprobado los dos trabajos prácticos impartidos por la cátedra y asistir al 80% de las clases teóricas y prácticas.

Por otro lado, en Bases de Datos Avanzadas, el requisito para regularizar (en lugar de promoción o libre) está descrito en el fragmento del documento BDA_Planificación.pdf. No obstante, el requisito mencionado para alcanzar la condición de Regular es obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos, y haber aprobado con 60 puntos los tres parciales. 

Se requiere la aprobación de los dos trabajos prácticos impartidos por la cátedra y la asistencia al 80% de las clases teóricas y prácticas. El alumno con la condición de Regular tendrá dos recuperatorios para cualquiera de los parciales.

**Tokens:** entrada: 2275 | salida: 307 | total: 2582

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
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 16]
   > Para acceder a la condición de Promoción Directa, el/la estudiante deberá cumplir con los siguientes requisitos: - 80 % de asistencia a la cursada. - Aprobación del examen parcial teórico con una
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > btención y análisis de información empírica. La comunicación de los resultados **Cronograma de trabajo** |METODOLOGÍA DE LA INVESTIGACIÓN- 2026|Col2|Col3|Col4|Col5| |---|---|---|---|---| |**Clase **
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > iguientes condiciones de cátedra: **1 -** Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos. Tener aprobado con 60 puntos los tres parciales. **2-** Haber realiz
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: Dr Roberto Hernández Sampieri Charla enfoques cuantitativo, cualitativo, mixto | Pagina: 13]
   > [https://youtu.be/CfjSC_pp8o0](https://youtu.be/CfjSC_pp8o0) _Bibliografía obligatoria sobre escritura académica_ - Natale, Lucía (Coordinadora) (2013). En carrera: escritura y lectura de textos ac
9. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > ncias de Recuperación:** La cátedra dispone de **dos oportunidades de** **recuperatorio** totales. Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se puede
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > clase)|(sin clase)|(sin clase)| |5|09 de abril|**Presencial**|**Teoría**|Tema/ problema| |6|16 de abril|Virtual|Práctica|| |7|23 de abril|Virtual|Teoría|Pregunta de investigación<br>(variables, unidad

**Respuesta:**

El porcentaje de asistencia a clases que exigen en común las materias de Investigación Operativa y Metodología de la Investigación es **80%**. Esta condición se encuentra en ambos programas, específicamente en la página 16 del programa de Metodología de la Investigación y en la página 2 del programa de Investigación Operativa.

No encuentro una referencia directa a la materia de Comunicaciones y Redes en los fragmentos proporcionados, por lo que no puedo determinar con certeza si esta materia también exige un porcentaje de asistencia de 80%.

**Tokens:** entrada: 2619 | salida: 127 | total: 2746

---

### Pregunta 11

> - Un proyecto integrador requiere utilizar un software para resolver problemas de optimización a gran escala que pueda conectarse de forma fluida con bases de datos espaciales. Según las herramientas enseñadas en las materias, ¿qué combinación de software visto en Bases de Datos Avanzadas e Investigación Operativa sería la más adecuada para este objetivo?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > :** Herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el Método Simplex y el Método Gráfico. Es ideal para validaciones rápidas y visualización de r
3. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **SOFTWARE REQUERIDO** | Pagina: 2]
   > PostgreSQL: versión 9.6 o superior SQL Server: versión 2016 o superior QGIS: versión compatible con PostgreSQL Anaconda (Python): últimas versiones
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadísticos mediante una i
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > eal: proporcionalidad, aditividad, divisibilidad y certidumbre. Formulación de problemas de optimización. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en los
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > lida de variables. Interpretación de la tabla óptima. Aplicación del método de la "M Grande" y método de las "Dos Fases". Análisis de dualidad y sensibilidad básica en modelos lineales.
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > ificación del trabajo integrador se determinará exclusivamente en la mesa de examen, junto con la nota correspondiente a la instancia teórica, estableciéndose en ese momento la calificación final y
9. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad I: -Introducción y Modelos Matemáticos-** Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del problema, construcción del modelo mate
10. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > estructura del modelo y suposiciones. Métodos para obtener una solución básica inicial: Esquina Noroeste, Costo Mínimo y Aproximación de Vogel. Método MODI (Distribución Modificada) para la optimiza

**Respuesta:**

LINDO (en su versión 64 bits) sería adecuada para modelar y resolver problemas de optimización de gran escala y puede conectarse de forma fluida con bases de datos gracias a su integración avanzada con bases de datos. Sin embargo, para poder conectarse con bases de datos espaciales, sería necesario que la versión de LINGO 64 bits estuviera compatible con un software de base de datos espacial como PostgreSQL versión 9.6 o superior, ya que QGIS podría funcionar como intermediario.

**Tokens:** entrada: 2124 | salida: 115 | total: 2239

---

### Pregunta 12

> - Si un estudiante desea investigar sobre el impacto de los "Agentes que aprenden" y las "Redes Neuronales" en la selección de personal y el teletrabajo en Argentina, ¿qué normativas legales y temas específicos de los programas de Inteligencia Artificial y RRHH debería cruzar en su marco teórico?

**Chunks de contexto:**

1. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: IV. BIBLIOGRAFÍA GENERAL | Pagina: 3]
   > entaria:**_ Reglamento de Teletrabajo en Argentina. Legislación sobre delitos informáticos en Argentina. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relac
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: **I. FUNDAMENTACIÓN** | Pagina: 1]
   > igital. Además, se abordarán aspectos legales fundamentales para comprender el impacto normativo de las TIC en el ámbito laboral, tomando como base la legislación argentina y los aportes de autores na
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 3]
   > Legislación sobre delitos informáticos en Argentina. Ley Nacional de Protección de Datos Personales (Ley 25.326). Ley Propiedad Intelectual (Ley 11.723) y su modificatoria. **Unidad 5: Trabajo Autó
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: General | Pagina: 2]
   > Reglamento de Teletrabajo en Argentina. Nicolás S. Tato, El Derecho Informático - Aspectos Fundamentales. Mariana Nazar, Tecnologías, información y derechos. **Unidad 2:** **Relaciones Humanas en e
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 4. El impacto de la inteligencia artificial en la gestión del talento. | Pagina: 2]
   > _**Bibliografía Nacional:**_ Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales. **Uni
6. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: IV. BIBLIOGRAFÍA GENERAL | Pagina: 3]
   > _**Bibliografía Básica:**_ Nicolás S. Tato, El Derecho Informático - Aspectos Fundamentales. Mariana Nazar, Tecnologías, información y derechos. Gonzalo Ana Dobratinich, derecho y nuevas tecnología
7. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: **I. FUNDAMENTACIÓN** | Pagina: 1]
   > El avance de las tecnologías de la información y la comunicación (TIC) ha transformado la dinámica del mundo laboral y las relaciones humanas dentro de las organizaciones. Esta asignatura busca analiz
8. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 6. Desafíos éticos y sociales de la tecnología en el ámbito laboral. | Pagina: 1]
   > _**Bibliografía Nacional:**_ Ley de Teletrabajo (Ley 27.555).
9. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 5. comercio electrónico, manifestación del consentimiento en internet | Pagina: 3]
   > _**Bibliografía Nacional:**_ Ley de Teletrabajo (Ley 27.555) Código Civil y Comercial de la Nación (aspectos relacionados con contratos digitales). Artículos académicos sobre la economía gig y el t
10. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > a acumulación de información, por parte de una misma neurona. **Capítulo XII** **Sistemas Multi Agentes** Introducción a los sistemas multiagente, modelos formales. Metodologías de diseño basadas e

**Respuesta:**

Para investigar sobre el impacto de los "Agentes que aprenden" y las "Redes Neuronales" en la selección de personal y el teletrabajo en Argentina, el estudiante debería considerar las siguientes normativas legales y temas específicos de los programas de Inteligencia Artificial y RRHH:

- La Ley de Teletrabajo (Ley 27.555) es fundamental para comprender el entorno legal del teletrabajo en Argentina y cómo se relaciona con la incorporación de tecnologías como la Inteligencia Artificial en la gestión laboral.
- El Código Civil y Comercial de la Nación, específicamente los aspectos relacionados con contratos digitales y firma electrónica, es crucial para entender las implicaciones legales de utilizar agentes que aprenden y redes neuronales en procesos de selección de personal y gestión remota.
- Los artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales son fundamentales para contextualizar el uso de la IA en el ámbito laboral y su influencia en el trabajo remoto y la selección de personal.
- El programa de Inteligencia Artificial podría ofrecer información específica sobre el desarrollo y aplicación de sistemas multiagentes y su posible impacto en la selección de personal y el teletrabajo.
- Los artículos académicos sobre la economía gig y el trabajo autónomo podrían ser útiles para comprender las implicaciones del uso de la IA en la gestión de trabajos y la relación entre empresas y trabajadores en el contexto de la era digital.

Es importante que el estudiante combine estos conocimientos con las normativas y conceptos específicos de los programas de Inteligencia Artificial y RRHH para tener una visión integral del impacto de la IA en la selección de personal y el teletrabajo en Argentina.

**Tokens:** entrada: 1795 | salida: 402 | total: 2197

---

### Pregunta 13

> - ¿Dónde puedo descargar la materia de Cálculo de 1er año?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 12]
   > - Natale, Lucía (Coordinadora) (2013). En carrera: escritura y lectura de textos académicos y profesionales. Argentina. Universidad Nacional de Ǫuilmes. Visto en [https://ediciones.ungs.edu.ar/wp-co
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: UNDERWRITERS LABORATORIES (UL) -> www.ul.com | Pagina: 5]
   > PANDUIT -> www.panduit.com AMP -> www.tycoelectronics.com/components/ ETHEREAL -> www.ethereal.com SIEMENS -> www.sea.siemens.com/step/templates/lesson.mason?electricity:2:3:3
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: PROGRAMA DE CÁTEDRA: INFORMÁTICA Y RELACIONES HUMANAS | Pagina: 1]
   > Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas semanales
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > **Obligatoria** - Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] - Cisco Systems: Academia de Networking de Cisco Systems: Guía del primer añ
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio | Pagina: 1]
   > Docente: Abog. Rodriguez Zanin, Fabio
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: AÑO ACADEMICO: 2023 | Pagina: 1]
   > PLAN DE ESTUDIO: 2010 (Resolución No 397/10 UADER)
7. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: **II. CONTENIDOS** | Pagina: 1]
   > **Unidad 1:** **El Trabajo en la Sociedad de la Información**
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > n con el cable). **Unidad IV**: - **Capa de enlace de dato** - **sub capa** **LLC (control de enlace lógico)** Cuestiones en el diseño de la capa de enlace de dato, servicios proporcionados por la cap
9. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > P, critica al modelo OSI y los protocolos; Organismos de estandarización de comunicación y redes. **Unidad II**: - **Capa física concepto y medios** Capa física (objetivo, funciones y funcionamiento,
10. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > en objetivos. Agentes que aprenden. **Capítulo II** **Procesos de Búsqueda.** Representación en un espacio de estados. Búsqueda Ciega, definición; búsqueda primero en amplitud, búsqueda de costo un

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1980 | salida: 14 | total: 1994

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
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > *Capítulo III** **Sistemas Basados en Conocimientos**. Conceptos básicos. Representación de Conocimientos. Estructuras basadas en Lógica. Lógica de Primer Orden. Reglas de Inferencia. Representación
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Estructura de Control: Procedimientos de Inferencia; Interfase con el usuario. Memoria de Trabajo, Módulo generador de explicaciones al usuario. **Capítulo V** **Funcionalidad de los Sistemas Exper
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > cidad de Generalización. Tamaño del conjunto de patrones para el entrenamiento. Algoritmos de reducción (Pruning Algorithms). Deep Learning. Modelos Generativos **Capítulo XI** Redes Autoorganizadas
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (2
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > amiento de Agentes Basados en Conocimientos. **Capítulo IV** **Diseño de los Sistemas Expertos**. Definición y descripción de sus módulos componentes. Proceso de Adquisición de Conocimiento. Base d
9. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos **Capítulo I** **Agentes Inteligentes** Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas p
10. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > a acumulación de información, por parte de una misma neurona. **Capítulo XII** **Sistemas Multi Agentes** Introducción a los sistemas multiagente, modelos formales. Metodologías de diseño basadas e

**Respuesta:**

Ing. Jorge L. Schmukler da clases en Inteligencia Artificial y en Redes y Comunicaciones, pero no en Bases de Datos Avanzadas, donde es el Profesor Teoría Sebastián Trossero.

**Tokens:** entrada: 1979 | salida: 52 | total: 2031

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
   > so de la redes de computadora, aplicaciones de negocios, domésticas, distintos usuarios. Hardware de redes, Sistema Cliente/Servidor, tipos de redes LAN, MAN, WAN, redes inalámbricas, redes domesticas
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > n con el cable). **Unidad IV**: - **Capa de enlace de dato** - **sub capa** **LLC (control de enlace lógico)** Cuestiones en el diseño de la capa de enlace de dato, servicios proporcionados por la cap
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > nstalación y configuración de hardware y software. - USERS-CISCO. [Disponible en Biblioteca FCyT- Oro Verde] - Comer, Douglas E.: Redes de computadoras, Internet e Interredes / D. E. Comer. - Méxi
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > P, critica al modelo OSI y los protocolos; Organismos de estandarización de comunicación y redes. **Unidad II**: - **Capa física concepto y medios** Capa física (objetivo, funciones y funcionamiento,
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > PROMOCIONADO REGULAR LIBRE El alumno accederá a la condición de **PROMOCIÓN** si cumple con las siguientes condiciones de cátedra: **1 -** Obtener en los 3 parciales, una calificación promedio sup
9. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: PROGRAMA DE CÁTEDRA: INFORMÁTICA Y RELACIONES HUMANAS | Pagina: 1]
   > Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas semanales
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 15]
   > rategia para planear una migración de software propietario a<br>software librepara la Facultad de Ciencia y Tecnología (FCyT) Sede Oro<br>Verde en el año 2018 /Emanuel Antonio Wasinger ; director Aldo

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 2416 | salida: 14 | total: 2430

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
   > **Programa de trabajos prácticos:** Tp 1: Escritura académica. Se solicita a los estudiantes seleccionar un artículo de investigación sobre un tema de interés específico relacionado al campo profesi
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > en condición libre. Deberá presentar el trabajo práctico integrador con una antelación mínima de veinte (20) días hábiles respecto de la fecha de la mesa de examen. En caso contrario, su evaluación
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > **b.** **Alumno Regular** - 60 % de asistencia. - Aprobación del examen parcial teórico con una calificación igual o superior a 60 (sesenta) puntos. - Entrega de todos los trabajos en tiempo y
9. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 9]
   > lación entre los conceptos. Formulación de objetivos e hipótesis. Tp 4: Elaboración de un escrito en donde presenten: Marco metodológico. El tiempo, período o secuencia de estudio. Universo, muestr
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 8]
   > . - Entrega obligatoria de las actividades prácticas y aprobación del trabajo práctico integrador final, respetando las fechas establecidas en el cronograma académico.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 2153 | salida: 14 | total: 2167

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
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad I: -Introducción y Modelos Matemáticos-** Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del problema, construcción del modelo mate
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > estructura del modelo y suposiciones. Métodos para obtener una solución básica inicial: Esquina Noroeste, Costo Mínimo y Aproximación de Vogel. Método MODI (Distribución Modificada) para la optimiza
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > preguntas le hago al problema? ¿Cómo construir el marco teórico? ¿Con qué categorías? Definición temporal y de contexto. Relación con los antecedentes relevados. Formulación de las preguntas que se
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > _remitirá un informe con las observaciones correspondientes y se establecerá un encuentro sincrónico_ _para su devolución y orientación. Cumplida esta instancia de revisión, el/la estudiante quedará_
9. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: pesos. Regiones de Decisión. Problema de separación lineal. Aplicaciones. Limitaciones | Pagina: 2]
   > Problema XOR.
10. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > lida de variables. Interpretación de la tabla óptima. Aplicación del método de la "M Grande" y método de las "Dos Fases". Análisis de dualidad y sensibilidad básica en modelos lineales.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 2163 | salida: 14 | total: 2177

---

### Pregunta 18

> - ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > ncias de Recuperación:** La cátedra dispone de **dos oportunidades de** **recuperatorio** totales. Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se puede
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > s se desarrollarán estrictamente en los bloques horarios asignados a la materia. La ausencia no justificada (sin certificado médico o motivo de fuerza mayor validado) se considerará como examen repr
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > ESO DE INVIERNO/ MESAS DE EXAMENES FINALES| |16|06 de agosto|Virtual|Teoría|Repaso del proceso de| |||||investigación| |17|13 de agosto|Virtual|Tutorías|Tutorías| |18|20 de agosto|**_Presencial (cambi
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > |12|28 de mayo|Virtual|Teoría|Col5| |---|---|---|---|---| |13|04 de junio|**Presencial**|**Teoría**|Marco metodológico I: enfoque y<br>tipo de investigación / muestra| |14|11 de junio|Virtual|Práctica
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > **b.** **Alumno Regular** - 60 % de asistencia. - Aprobación del examen parcial teórico con una calificación igual o superior a 60 (sesenta) puntos. - Entrega de todos los trabajos en tiempo y
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > **Condición del Alumno:** - **ALUMNO PROMOCIONADO:** El estudiante logrará la promoción directa si alcanza un promedio general de **80 puntos** - más entre los **1 parcial** previstos, no pudiendo
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > clase)|(sin clase)|(sin clase)| |5|09 de abril|**Presencial**|**Teoría**|Tema/ problema| |6|16 de abril|Virtual|Práctica|| |7|23 de abril|Virtual|Teoría|Pregunta de investigación<br>(variables, unidad
9. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > en condición libre. Deberá presentar el trabajo práctico integrador con una antelación mínima de veinte (20) días hábiles respecto de la fecha de la mesa de examen. En caso contrario, su evaluación
10. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **HORARIOS DE CLASE** | Pagina: 1]
   > Lunes: 13:30 a 15:30 (Teoría) Viernes: 17:00 a 19:00 (Práctica) Nota: Los horarios están en proceso de evaluación y pueden sufrir cambios

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 2267 | salida: 14 | total: 2281

---

## Conversacion 2

**Puntaje evaluado: 15.5 / 18**

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
   > **Capítulo III** **Sistemas Basados en Conocimientos**. Conceptos básicos. Representación de Conocimientos. Estructuras basadas en Lógica. Lógica de Primer Orden. Reglas de Inferencia. Representación
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Proceso de Inferencia. Tratamiento paralelo de las reglas. Determinación del aporte parcial de cada regla. Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (2
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Comportamiento de Agentes Basados en Conocimientos. **Capítulo IV** **Diseño de los Sistemas Expertos**. Definición y descripción de sus módulos componentes. Proceso de Adquisición de Conocimiento.
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > Regiones de Decisión. Modo de operación autoasociativo. **Capítulo X** **Generalización en las RNA,** definición, factores que influyen en la capacidad de Generalización. Tamaño del conjunto de pat
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > Modificación del algoritmo SOM para evitar una excesiva acumulación de información, por parte de una misma neurona. **Capítulo XII** **Sistemas Multi Agentes** Introducción a los sistemas multiagen
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Estructura de Control: Procedimientos de Inferencia; Interfase con el usuario. Memoria de Trabajo, Módulo generador de explicaciones al usuario. **Capítulo V** **Funcionalidad de los Sistemas Exper
9. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > **Capítulo IX** **Redes** **Perceptron** **Multicapa**, estructura básica. Proceso de Entrenamiento Backpropagation (BP). Interpretación heurística y matemática del procedimiento BP. Término de Momen
10. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > **Capítulo II** **Procesos de Búsqueda.** Representación en un espacio de estados. Búsqueda Ciega, definición; búsqueda primero en amplitud, búsqueda de costo uniforme; búsqueda primero en profundid

**Respuesta:**

Los contenidos de la materia Inteligencia Artificial se dividen en varios capítulos y temas. Algunos de los tópicos incluidos son Agentes Inteligentes, Sistemas Basados en Conocimientos, Proceso de Inferencia, Redes Neuronales Artificiales, Agentes Basados en Conocimientos, Diseño de los Sistemas Expertos, Base de Conocimientos, Regiones de Decisión, Modo de operación autoasociativo, Generalización en las Redes Neuronales, Redes Autoorganizadas, Redes SOM, Sistemas Multi Agentes, Funcionalidad de los Sistemas Expertos, Procesos de inferencia, y Redes Perceptron Multicapa.

**Tokens:** entrada: 2092 | salida: 159 | total: 2251

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
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > La cátedra implementará el modelo de aula invertida, en el que los estudiantes adquieren los conocimientos teóricos de manera previa a la clase, a través de videos elaborados por la cátedra, lectura
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Clase de direccionamiento (clase a, b, c, d y e). Prefijo y Mascara de red. Lógica de and. Calculo de direcciones. División de subredes (por clase y vlsm (mascara de subred de longitud variable)), i
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 3]
   > conocimiento vulgar, conocimiento científico. Clasificación de las ciencias. Diferencias entre ciencia, técnica, tecnología, ingeniería e intervención profesional. La ciencia y los sistemas de infor
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > **Capítulo II** **Procesos de Búsqueda.** Representación en un espacio de estados. Búsqueda Ciega, definición; búsqueda primero en amplitud, búsqueda de costo uniforme; búsqueda primero en profundid
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 15]
   > ; director Aldo Daniel Sigura ;<br>codirector Pablo Emanuel Goette.|2019| |Deep Learning aplicado al aprendizaje automático de ontologías para la<br>representación del conocimiento a partir de texto n
9. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > **Capítulo IX** **Redes** **Perceptron** **Multicapa**, estructura básica. Proceso de Entrenamiento Backpropagation (BP). Interpretación heurística y matemática del procedimiento BP. Término de Momen
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 12]
   > - Natale, Lucía (Coordinadora) (2013). En carrera: escritura y lectura de textos académicos y profesionales. Argentina. Universidad Nacional de Ǫuilmes. Visto en [https://ediciones.ungs.edu.ar/wp-co

**Respuesta:**

La materia en la que se enseña el concepto de Lógica Difusa es la Inteligencia Artificial.

**Tokens:** entrada: 2187 | salida: 26 | total: 2213

---

### Pregunta 3

> - ¿Cuál es el plan de estudios de Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > |METODOLOGÍA DE LA INVESTIGACIÓN- 2026|Col2|Col3|Col4|Col5| |---|---|---|---|---| |**Clase **|**FECHA**|**Tipo de encuentro**|**Tipo encuentro**|**Tema**| |1|12 de marzo|**Presencial**|**Teórico/práct
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: **Equipo docente:** PROFESORA RESPONSABLE ADJUNTO: ALEJANDRA MARǪUESIN; JEFE DE | Pagina: 1]
   > TRABAJOS PRÁCTICOS: TAMARA SUIVA. JEFE DE TRABAJOS PRÁCTICOS: JIMENA SANTA CRUZ; **Año de la carrera a la que pertenece la cátedra:** 4 **Régimen de la materia:** Anual **Carga horaria semanal:** 3
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > integrador se determinará exclusivamente en la mesa de examen, junto con la nota correspondiente a la instancia teórica, estableciéndose en ese momento la calificación final y la condición de aproba
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: dentro de la plataforma Moodle. La organización será la siguiente | Pagina: 5]
   > curso. - Desarrollo de contenidos: distribuidos en tres pestañas temáticas: - Introducción - Dimensión epistemológica - Dimensión estratégica - Dimensión técnica - Cada semana se habilitar
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: dentro de la plataforma Moodle. La organización será la siguiente | Pagina: 5]
   > - Inicio del curso: contendrá información general de la cátedra, incluyendo el programa, el equipo docente, el cronograma, los objetivos, los materiales utilizados, el enlace de videoconferencia, la
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > objetivos y relación de los objetivos con las preguntas de la investigación. **Unidad 3: La dimensión de la estrategia general de investigación** ¿Cómo se va a estudiar el problema? Tipo de diseños c
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > |5|09 de abril|**Presencial**|**Teoría**|Tema/ problema| |6|16 de abril|Virtual|Práctica|| |7|23 de abril|Virtual|Teoría|Pregunta de investigación<br>(variables, unidad de análisis,<br>contexto)/ Ante
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: **Equipo docente:** PROFESORA RESPONSABLE ADJUNTO: ALEJANDRA MARǪUESIN; JEFE DE | Pagina: 1]
   > A los fines de su desarrollo, se entenderá a la Metodología de la Investigación como el conjunto de estrategias, reflexiones y decisiones que configuran los procesos de investigación científica. Por
9. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > : enfoque y<br>tipo de investigación / muestra| |14|11 de junio|Virtual|Práctica|| |15|18 de junio|Virtual|Teoría|Marco metodológico II:<br>recolección de datos y análisis de<br>datos| |||||| |RECESO
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > |||||investigación| |17|13 de agosto|Virtual|Tutorías|Tutorías| |18|20 de agosto|**_Presencial (cambio_**<br>**_encuentro)_**|**Teoría**|Parcial teoría| |19|27 de agosto|Virtual|Tutorías|Tutorías| |20

**Respuesta:**

El plan de estudios resumido de Metodología de la Investigación está compuesto por cuatro unidades: 

1. Unidad 1: Introducción a la ciencia y conocimiento científico.
2. Unidad 2: La dimensión epistemológica.
3. Unidad 3: La dimensión de la estrategia general de investigación.
4. Unidad 4: La dimensión de las técnicas de obtención y análisis de información empírica. La comunicación de los resultados.

**Tokens:** entrada: 2549 | salida: 116 | total: 2665

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
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > Lineal: proporcionalidad, aditividad, divisibilidad y certidumbre. Formulación de problemas de optimización. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en l
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > optimalidad de Bellman. Resolución de problemas de diligencia, asignación de recursos y reemplazo de equipos. Diferencias entre Programación Dinámica Determinística y Probabilística.
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: pesos. Regiones de Decisión. Problema de separación lineal. Aplicaciones. Limitaciones | Pagina: 2]
   > Problema XOR.
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > estructura del modelo y suposiciones. Métodos para obtener una solución básica inicial: Esquina Noroeste, Costo Mínimo y Aproximación de Vogel. Método MODI (Distribución Modificada) para la optimiza
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
9. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad I: -Introducción y Modelos Matemáticos-** Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del problema, construcción del modelo mate
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 15]
   > ; director José Luis Mengarelli.|2019| |Estrategia para planear una migración de software propietario a<br>software librepara la Facultad de Ciencia y Tecnología (FCyT) Sede Oro<br>Verde en el año 201

**Respuesta:**

Se recomiendan herramientas como LINDO, WinQSB 2.0, PHP Simplex y LINGO (64 bits) para resolver problemas de optimización lineal. Estas herramientas se relacionan con las unidades teóricas en la carrera de Investigación Operativa, específicamente con la **Unidad II: -Programación Lineal (PL)**, donde se estudian propiedades de los modelos de Programación Lineal y se forma a los estudiantes en la formulación de modelos de optimización lineal.

**Tokens:** entrada: 1968 | salida: 114 | total: 2082

---

### Pregunta 5

> - ¿Qué instancias de recuperación nos provee Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > **Instancias de Recuperación:** La cátedra dispone de **dos oportunidades de** **recuperatorio** totales. Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no s
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad I: -Introducción y Modelos Matemáticos-** Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del problema, construcción del modelo mate
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadístico
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > entrada y salida de variables. Interpretación de la tabla óptima. Aplicación del método de la "M Grande" y método de las "Dos Fases". Análisis de dualidad y sensibilidad básica en modelos lineales.
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > Lineal: proporcionalidad, aditividad, divisibilidad y certidumbre. Formulación de problemas de optimización. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en l
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > **Condición del Alumno:** - **ALUMNO PROMOCIONADO:** El estudiante logrará la promoción directa si alcanza un promedio general de **80 puntos** - más entre los **1 parcial** previstos, no pudiendo
9. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **PHP Simplex:** Herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el Método Simplex y el Método Gráfico. Es ideal para validaciones rápidas y vis
10. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 3]
   > hojas de cálculo.

**Respuesta:**

La cátedra de Investigación Operativa dispone de dos oportunidades de recuperatorio totales. Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mismo examen parcial. La calificación obtenida en la instancia de recuperación sustituirá automáticamente a la nota del examen original.

**Tokens:** entrada: 2044 | salida: 85 | total: 2129

---

### Pregunta 6

> - ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadístico
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: **I. FUNDAMENTACIÓN** | Pagina: 1]
   > Los estudiantes explorarán los efectos de las nuevas tecnologías en el trabajo, la calidad de vida laboral y la administración del talento humano en la era digital. Además, se abordarán aspectos legal
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > |23|24<br>de<br>septiembr<br>e|Virtual|Tutorías|Tutorías| |24|01 de octubre|Presencial|Tutorías|Presentación tesina- ver<br>posibilidad| |25|08 de octubre|Virtual|Tutorías|Presentación tesina- ver<br>
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos vertidos en la teoría. Más dos trabajos Prácticos que se realizan en el ho
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > **Capítulo IX** **Redes** **Perceptron** **Multicapa**, estructura básica. Proceso de Entrenamiento Backpropagation (BP). Interpretación heurística y matemática del procedimiento BP. Término de Momen
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **PHP Simplex:** Herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el Método Simplex y el Método Gráfico. Es ideal para validaciones rápidas y vis
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: pesos. Regiones de Decisión. Problema de separación lineal. Aplicaciones. Limitaciones | Pagina: 2]
   > Problema XOR.
9. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > |||||investigación| |17|13 de agosto|Virtual|Tutorías|Tutorías| |18|20 de agosto|**_Presencial (cambio_**<br>**_encuentro)_**|**Teoría**|Parcial teoría| |19|27 de agosto|Virtual|Tutorías|Tutorías| |20
10. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par

**Respuesta:**

El software TORA sirve para el aprendizaje de la Investigación Operativa. Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos.

**Tokens:** entrada: 2024 | salida: 49 | total: 2073

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
   > - Huidobro Moya, José Manuel: Redes de datos y convergencia IP / J. M. Huidobro Moya, Ramón Jesús Millán Tejedor. - México: Alfaomega, 2007. ISBN 9789701512784 [Disponible en Biblioteca FCyT- Oro Verd
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > - Arena, Héctor Facundo: Linux: la guía definitiva / H. F. Arena. - Buenos Aires: Gradi, 2010. ISBN 9789872601386 [Disponible en Biblioteca FCyT- Oro Verde] - Graziani, Rick: Conceptos y protocolos
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Clase de direccionamiento (clase a, b, c, d y e). Prefijo y Mascara de red. Lógica de and. Calculo de direcciones. División de subredes (por clase y vlsm (mascara de subred de longitud variable)), i
8. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **PRESENTACIÓN DE LA MATERIA** | Pagina: 1]
   > Facultad de Ciencia y Tecnología Universidad Autónoma de Entre Ríos (UADER)
9. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **HORARIOS DE CLASE** | Pagina: 1]
   > Lunes: 13:30 a 15:30 (Teoría) Viernes: 17:00 a 19:00 (Práctica) Nota: Los horarios están en proceso de evaluación y pueden sufrir cambios
10. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > . Modelo de referencia OSI, Modelo de protocolo TCP/IP, comparación modelo OSI y TCP/IP, critica al modelo OSI y los protocolos; Organismos de estandarización de comunicación y redes. **Unidad II**: -

**Respuesta:**

Ing. Jorge L. Schmukler.

**Tokens:** entrada: 1863 | salida: 11 | total: 1874

---

### Pregunta 8

> - ¿Qué otra asignatura, además de la propia materia de Inteligencia Artificial, incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos **Capítulo I** **Agentes Inteligentes** Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas p
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 4. El impacto de la inteligencia artificial en la gestión del talento. | Pagina: 2]
   > _**Bibliografía Nacional:**_ Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales. **Uni
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Proceso de Inferencia. Tratamiento paralelo de las reglas. Determinación del aporte parcial de cada regla. Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (2
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > Modificación del algoritmo SOM para evitar una excesiva acumulación de información, por parte de una misma neurona. **Capítulo XII** **Sistemas Multi Agentes** Introducción a los sistemas multiagen
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > Regiones de Decisión. Modo de operación autoasociativo. **Capítulo X** **Generalización en las RNA,** definición, factores que influyen en la capacidad de Generalización. Tamaño del conjunto de pat
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Estructura de Control: Procedimientos de Inferencia; Interfase con el usuario. Memoria de Trabajo, Módulo generador de explicaciones al usuario. **Capítulo V** **Funcionalidad de los Sistemas Exper
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > **Capítulo IX** **Redes** **Perceptron** **Multicapa**, estructura básica. Proceso de Entrenamiento Backpropagation (BP). Interpretación heurística y matemática del procedimiento BP. Término de Momen
9. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > **Capítulo III** **Sistemas Basados en Conocimientos**. Conceptos básicos. Representación de Conocimientos. Estructuras basadas en Lógica. Lógica de Primer Orden. Reglas de Inferencia. Representación
10. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Comportamiento de Agentes Basados en Conocimientos. **Capítulo IV** **Diseño de los Sistemas Expertos**. Definición y descripción de sus módulos componentes. Proceso de Adquisición de Conocimiento.

**Respuesta:**

La asignatura de Informática y Recursos Humanos incluye explícitamente el impacto o uso de la "Inteligencia artificial" (IA) dentro de sus unidades temáticas.

**Tokens:** entrada: 2080 | salida: 41 | total: 2121

---

### Pregunta 9

> - Los requisitos para regularizar en Bases de Datos Avanzadas y en Redes y Comunicaciones, ¿son iguales? ¿Qué diferencias tienen?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > **Evaluación Final:** El alumno con condición de REGULAR, deberá rendir un examen de los temas teóricos y prácticos desarrollados en la materia (prueba escrita). El alumno LIBRE rendirá un examen fina
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > ; Algoritmos de enrutamiento (Principio de optimización, Enrutamiento por la ruta más corta, Inundación, Enrutamiento por vector de distancia, Enrutamiento por estado del enlace, Enrutamiento jerárqui
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > PROMOCIONADO REGULAR LIBRE El alumno accederá a la condición de **PROMOCIÓN** si cumple con las siguientes condiciones de cátedra: **1 -** Obtener en los 3 parciales, una calificación promedio sup
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Utilización de hubs como dispositivo intermedio (problemas con el crecimiento de la red: escalabilidad, fallas en la red, colisiones). Switches (ancho de banda dedicado a cada puerto, entorno libre
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > . Protocolo enlace de datos ( **HDLC** -Control de enlace de datos de alto nivel-, Capa de enlace de datos en Internet -Protocolo **PPP** (Protocolo Punto a Punto)-). **Unidad V**: - **Capa de enlace
6. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **SOFTWARE REQUERIDO** | Pagina: 2]
   > PostgreSQL: versión 9.6 o superior SQL Server: versión 2016 o superior QGIS: versión compatible con PostgreSQL Anaconda (Python): últimas versiones
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > **1 -** Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos. Tener aprobado con 60 puntos los tres parciales.
8. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **CANALES DE COMUNICACIÓN** | Pagina: 2]
   > Correo: Lista de mail (consultas y comunicación de rutina) Aula virtual: Material académico - Clave de matriculación: bda2023 (ÚNICO MEDIO OFICIAL) Telegram: https://t.me/+c7PPIrc9nQM4MzEx (avisos y n
9. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > : - **Capa de enlace de dato** - **sub capa** **LLC (control de enlace lógico)** Cuestiones en el diseño de la capa de enlace de dato, servicios proporcionados por la capa de red, entramado, control d
10. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Proveedores de servicio de internet (ISP), descripción Ipv6. **Unidad IX** **-VLans-** Definiciones de Vlan, Beneficios de una Vlan, Rangos de ID de la Vlan (rango normal y rango extendido), Tipos d

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 2033 | salida: 14 | total: 2047

---

### Pregunta 10

> - ¿Cuál es el porcentaje de asistencia a clases que exigen en común las materias de Investigación Operativa, Comunicaciones y Redes, y Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > **b.** **Alumno Regular** - 60 % de asistencia. - Aprobación del examen parcial teórico con una calificación igual o superior a 60 (sesenta) puntos. - Entrega de todos los trabajos en tiempo y
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > **Condición del Alumno:** - **ALUMNO PROMOCIONADO:** El estudiante logrará la promoción directa si alcanza un promedio general de **80 puntos** - más entre los **1 parcial** previstos, no pudiendo
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: **Equipo docente:** PROFESORA RESPONSABLE ADJUNTO: ALEJANDRA MARǪUESIN; JEFE DE | Pagina: 1]
   > TRABAJOS PRÁCTICOS: TAMARA SUIVA. JEFE DE TRABAJOS PRÁCTICOS: JIMENA SANTA CRUZ; **Año de la carrera a la que pertenece la cátedra:** 4 **Régimen de la materia:** Anual **Carga horaria semanal:** 3
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 16]
   > Para acceder a la condición de Promoción Directa, el/la estudiante deberá cumplir con los siguientes requisitos: - 80 % de asistencia a la cursada. - Aprobación del examen parcial teórico con una
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: Dr Roberto Hernández Sampieri Charla enfoques cuantitativo, cualitativo, mixto | Pagina: 13]
   > [https://youtu.be/CfjSC_pp8o0](https://youtu.be/CfjSC_pp8o0) _Bibliografía obligatoria sobre escritura académica_ - Natale, Lucía (Coordinadora) (2013). En carrera: escritura y lectura de textos ac
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > campo disciplinar y desarrollo de ejercicios vinculados con la construcción progresiva del anteproyecto de investigación. Esta metodología busca facilitar el acceso a los contenidos para aquellos es
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > |METODOLOGÍA DE LA INVESTIGACIÓN- 2026|Col2|Col3|Col4|Col5| |---|---|---|---|---| |**Clase **|**FECHA**|**Tipo de encuentro**|**Tipo encuentro**|**Tema**| |1|12 de marzo|**Presencial**|**Teórico/práct
9. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 16]
   > durante el proceso. - 80 % de los cuestionarios de autoevaluación respondidos. - Presentación y defensa oral del trabajo práctico integrador, previamente aprobado, en instancia de coloquio. Es r
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > |5|09 de abril|**Presencial**|**Teoría**|Tema/ problema| |6|16 de abril|Virtual|Práctica|| |7|23 de abril|Virtual|Teoría|Pregunta de investigación<br>(variables, unidad de análisis,<br>contexto)/ Ante

**Respuesta:**

80% de asistencia a clases es el porcentaje que exigen comúnmente las materias de Investigación Operativa y Metodología de la Investigación. No dispongo de información en mis documentos para comparar el porcentaje de asistencia de la materia de Comunicaciones y Redes.

**Tokens:** entrada: 2453 | salida: 63 | total: 2516

---

### Pregunta 11

> - Un proyecto integrador requiere utilizar un software para resolver problemas de optimización a gran escala que pueda conectarse de forma fluida con bases de datos espaciales. Según las herramientas enseñadas en las materias, ¿qué combinación de software visto en Bases de Datos Avanzadas e Investigación Operativa sería la más adecuada para este objetivo?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **PHP Simplex:** Herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el Método Simplex y el Método Gráfico. Es ideal para validaciones rápidas y vis
3. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **SOFTWARE REQUERIDO** | Pagina: 2]
   > PostgreSQL: versión 9.6 o superior SQL Server: versión 2016 o superior QGIS: versión compatible con PostgreSQL Anaconda (Python): últimas versiones
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadístico
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > Lineal: proporcionalidad, aditividad, divisibilidad y certidumbre. Formulación de problemas de optimización. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en l
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > entrada y salida de variables. Interpretación de la tabla óptima. Aplicación del método de la "M Grande" y método de las "Dos Fases". Análisis de dualidad y sensibilidad básica en modelos lineales.
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > optimalidad de Bellman. Resolución de problemas de diligencia, asignación de recursos y reemplazo de equipos. Diferencias entre Programación Dinámica Determinística y Probabilística.
9. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: **Equipo docente:** PROFESORA RESPONSABLE ADJUNTO: ALEJANDRA MARǪUESIN; JEFE DE | Pagina: 1]
   > A los fines de su desarrollo, se entenderá a la Metodología de la Investigación como el conjunto de estrategias, reflexiones y decisiones que configuran los procesos de investigación científica. Por
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > integrador se determinará exclusivamente en la mesa de examen, junto con la nota correspondiente a la instancia teórica, estableciéndose en ese momento la calificación final y la condición de aproba

**Respuesta:**

LINGO (64 bits) es la herramienta más adecuada para modelar y resolver problemas de optimización de gran escala. Además, según el Plan de estudios, se menciona que el estudiante debe contar con herramientas prácticas para encarar los desafíos que suponen el ejercicio de la profesión y la investigación.

Si bien en Bases de Datos Avanzadas se menciona la posibilidad de integración con bases de datos, no hay una mención específica a bases de datos espaciales. El requisito de que el software pueda conectarse con bases de datos espaciales no está respaldado en el Contexto proporcionado.

**Tokens:** entrada: 1973 | salida: 142 | total: 2115

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
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: IV. BIBLIOGRAFÍA GENERAL | Pagina: 3]
   > _**Bibliografía Básica:**_ Nicolás S. Tato, El Derecho Informático - Aspectos Fundamentales. Mariana Nazar, Tecnologías, información y derechos. Gonzalo Ana Dobratinich, derecho y nuevas tecnología
6. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 4. El impacto de la inteligencia artificial en la gestión del talento. | Pagina: 2]
   > _**Bibliografía Nacional:**_ Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales. **Uni
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Proceso de Inferencia. Tratamiento paralelo de las reglas. Determinación del aporte parcial de cada regla. Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del
8. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 6. Desafíos éticos y sociales de la tecnología en el ámbito laboral. | Pagina: 1]
   > _**Bibliografía Nacional:**_ Ley de Teletrabajo (Ley 27.555).
9. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 5. comercio electrónico, manifestación del consentimiento en internet | Pagina: 3]
   > _**Bibliografía Nacional:**_ Ley de Teletrabajo (Ley 27.555) Código Civil y Comercial de la Nación (aspectos relacionados con contratos digitales). Artículos académicos sobre la economía gig y el t
10. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > Modificación del algoritmo SOM para evitar una excesiva acumulación de información, por parte de una misma neurona. **Capítulo XII** **Sistemas Multi Agentes** Introducción a los sistemas multiagen

**Respuesta:**

Para investigar sobre el impacto de los "Agentes que aprenden" y las "Redes Neuronales" en la selección de personal y el teletrabajo en Argentina, el estudiante debería cruzar en su marco teórico las siguientes normativas legales y temas específicos:

*   La Ley de Teletrabajo (Ley 27.555), ya que regula el trabajo a distancia y sus condiciones laborales.
*   El Código Civil y Comercial de la Nación, específicamente los aspectos relacionados con contratos digitales y firma electrónica, ya que abordan cuestiones relevantes para la implementación de tecnologías como las Redes Neuronales en el ámbito laboral.
*   El concepto de Agentes que aprenden (o inteligencia artificial) en sistemas multiagentes, ya que estos pueden estar involucrados en la selección de personal o procesos de gestión laboral automatizados.

**Tokens:** entrada: 1837 | salida: 207 | total: 2044

---

### Pregunta 13

> - ¿Dónde puedo descargar la materia de Cálculo de 1er año?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 12]
   > - Natale, Lucía (Coordinadora) (2013). En carrera: escritura y lectura de textos académicos y profesionales. Argentina. Universidad Nacional de Ǫuilmes. Visto en [https://ediciones.ungs.edu.ar/wp-co
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: UNDERWRITERS LABORATORIES (UL) -> www.ul.com | Pagina: 5]
   > PANDUIT -> www.panduit.com AMP -> www.tycoelectronics.com/components/ ETHEREAL -> www.ethereal.com SIEMENS -> www.sea.siemens.com/step/templates/lesson.mason?electricity:2:3:3
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: PROGRAMA DE CÁTEDRA: INFORMÁTICA Y RELACIONES HUMANAS | Pagina: 1]
   > Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas semanales
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > **Obligatoria** - Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] - Cisco Systems: Academia de Networking de Cisco Systems: Guía del primer añ
5. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio | Pagina: 1]
   > Docente: Abog. Rodriguez Zanin, Fabio
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: AÑO ACADEMICO: 2023 | Pagina: 1]
   > PLAN DE ESTUDIO: 2010 (Resolución No 397/10 UADER)
7. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: **II. CONTENIDOS** | Pagina: 1]
   > **Unidad 1:** **El Trabajo en la Sociedad de la Información**
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > : - **Capa de enlace de dato** - **sub capa** **LLC (control de enlace lógico)** Cuestiones en el diseño de la capa de enlace de dato, servicios proporcionados por la capa de red, entramado, control d
9. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > . Televisión por cable (televisión por antena comunal, Internet a través de cable, asignación de espectro, modem de cable, ADSL en comparación con el cable). **Unidad IV**
10. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > . Modelo de referencia OSI, Modelo de protocolo TCP/IP, comparación modelo OSI y TCP/IP, critica al modelo OSI y los protocolos; Organismos de estandarización de comunicación y redes. **Unidad II**: -

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1778 | salida: 14 | total: 1792

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
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > **Capítulo III** **Sistemas Basados en Conocimientos**. Conceptos básicos. Representación de Conocimientos. Estructuras basadas en Lógica. Lógica de Primer Orden. Reglas de Inferencia. Representación
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Estructura de Control: Procedimientos de Inferencia; Interfase con el usuario. Memoria de Trabajo, Módulo generador de explicaciones al usuario. **Capítulo V** **Funcionalidad de los Sistemas Exper
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Proceso de Inferencia. Tratamiento paralelo de las reglas. Determinación del aporte parcial de cada regla. Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > Modificación del algoritmo SOM para evitar una excesiva acumulación de información, por parte de una misma neurona. **Capítulo XII** **Sistemas Multi Agentes** Introducción a los sistemas multiagen
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Comportamiento de Agentes Basados en Conocimientos. **Capítulo IV** **Diseño de los Sistemas Expertos**. Definición y descripción de sus módulos componentes. Proceso de Adquisición de Conocimiento.
9. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (2
10. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Clase de direccionamiento (clase a, b, c, d y e). Prefijo y Mascara de red. Lógica de and. Calculo de direcciones. División de subredes (por clase y vlsm (mascara de subred de longitud variable)), i

**Respuesta:**

Sí, Ing. Jorge L. Schmukler es parte del equipo docente de la materia "Bases de Datos Avanzadas", como se menciona en el primer fragmento. También se menciona que es el profesor de la materia "Comunicación y Redes" en el segundo fragmento del Planificación 2025. En cuanto a la materia "Inteligencia Artificial", no se menciona explícitamente al Ing. Schmukler como profesor en los fragmentos disponibles.

**Tokens:** entrada: 1832 | salida: 108 | total: 1940

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
6. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: PROGRAMA DE CÁTEDRA: INFORMÁTICA Y RELACIONES HUMANAS | Pagina: 1]
   > Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas semanales
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > PROMOCIONADO REGULAR LIBRE El alumno accederá a la condición de **PROMOCIÓN** si cumple con las siguientes condiciones de cátedra: **1 -** Obtener en los 3 parciales, una calificación promedio sup
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > . Explicar el **propósito de IOS como Sistema** **Operativo de red**, Explicar cómo acceder al IOS y cómo explorarlo para configurar los dispositivos de red, Describir la estructura de comandos, Confi
9. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . La ethernet actual. La trama de ethernet. Power Over Ethernet. Direcciones MAC. Dispositivo de red (nic). Ethernet unicast, multicast, broadcast. CSMA/CD (Acceso Múltiple por Detección de Portadora
10. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > - Arena, Héctor Facundo: Linux: la guía definitiva / H. F. Arena. - Buenos Aires: Gradi, 2010. ISBN 9789872601386 [Disponible en Biblioteca FCyT- Oro Verde] - Graziani, Rick: Conceptos y protocolos

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 2233 | salida: 14 | total: 2247

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
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 9]
   > **Programa de trabajos prácticos:** Tp 1: Escritura académica. Se solicita a los estudiantes seleccionar un artículo de investigación sobre un tema de interés específico relacionado al campo profesi
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > **b.** **Alumno Regular** - 60 % de asistencia. - Aprobación del examen parcial teórico con una calificación igual o superior a 60 (sesenta) puntos. - Entrega de todos los trabajos en tiempo y
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > **1 -** Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos. Tener aprobado con 60 puntos los tres parciales.
9. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 9]
   > conceptos. Formulación de objetivos e hipótesis. Tp 4: Elaboración de un escrito en donde presenten: Marco metodológico. El tiempo, período o secuencia de estudio. Universo, muestra y unidad de mues
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 8]
   > - Entrega obligatoria de las actividades prácticas y aprobación del trabajo práctico integrador final, respetando las fechas establecidas en el cronograma académico.

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 2015 | salida: 14 | total: 2029

---

### Pregunta 17

> - ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **PHP Simplex:** Herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el Método Simplex y el Método Gráfico. Es ideal para validaciones rápidas y vis
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > Lineal: proporcionalidad, aditividad, divisibilidad y certidumbre. Formulación de problemas de optimización. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en l
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadístico
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad I: -Introducción y Modelos Matemáticos-** Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del problema, construcción del modelo mate
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > estructura del modelo y suposiciones. Métodos para obtener una solución básica inicial: Esquina Noroeste, Costo Mínimo y Aproximación de Vogel. Método MODI (Distribución Modificada) para la optimiza
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > _establecerá un encuentro sincrónico para su devolución y orientación. Cumplida esta instancia_ _de revisión, el/la estudiante quedará habilitado/a para presentarse a la mesa de examen final._ _No s
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: pesos. Regiones de Decisión. Problema de separación lineal. Aplicaciones. Limitaciones | Pagina: 2]
   > Problema XOR.
9. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > entrada y salida de variables. Interpretación de la tabla óptima. Aplicación del método de la "M Grande" y método de las "Dos Fases". Análisis de dualidad y sensibilidad básica en modelos lineales.
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > _remitirá un informe con las observaciones correspondientes y se establecerá un encuentro sincrónico_ _para su devolución y orientación. Cumplida esta instancia de revisión, el/la estudiante quedará_

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 2094 | salida: 14 | total: 2108

---

### Pregunta 18

> - ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > corridos tras la evaluación. Los exámenes se desarrollarán estrictamente en los bloques horarios asignados a la materia. La ausencia no justificada (sin certificado médico o motivo de fuerza mayor v
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > **Instancias de Recuperación:** La cátedra dispone de **dos oportunidades de** **recuperatorio** totales. Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no s
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > : enfoque y<br>tipo de investigación / muestra| |14|11 de junio|Virtual|Práctica|| |15|18 de junio|Virtual|Teoría|Marco metodológico II:<br>recolección de datos y análisis de<br>datos| |||||| |RECESO
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > |5|09 de abril|**Presencial**|**Teoría**|Tema/ problema| |6|16 de abril|Virtual|Práctica|| |7|23 de abril|Virtual|Teoría|Pregunta de investigación<br>(variables, unidad de análisis,<br>contexto)/ Ante
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > |23|24<br>de<br>septiembr<br>e|Virtual|Tutorías|Tutorías| |24|01 de octubre|Presencial|Tutorías|Presentación tesina- ver<br>posibilidad| |25|08 de octubre|Virtual|Tutorías|Presentación tesina- ver<br>
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > **Condición del Alumno:** - **ALUMNO PROMOCIONADO:** El estudiante logrará la promoción directa si alcanza un promedio general de **80 puntos** - más entre los **1 parcial** previstos, no pudiendo
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > **b.** **Alumno Regular** - 60 % de asistencia. - Aprobación del examen parcial teórico con una calificación igual o superior a 60 (sesenta) puntos. - Entrega de todos los trabajos en tiempo y
9. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > |||||investigación| |17|13 de agosto|Virtual|Tutorías|Tutorías| |18|20 de agosto|**_Presencial (cambio_**<br>**_encuentro)_**|**Teoría**|Parcial teoría| |19|27 de agosto|Virtual|Tutorías|Tutorías| |20
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > |METODOLOGÍA DE LA INVESTIGACIÓN- 2026|Col2|Col3|Col4|Col5| |---|---|---|---|---| |**Clase **|**FECHA**|**Tipo de encuentro**|**Tipo encuentro**|**Tema**| |1|12 de marzo|**Presencial**|**Teórico/práct

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 2420 | salida: 14 | total: 2434

---

## Conversacion 3

**Puntaje evaluado: 16 / 18**

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
   > Proceso de Inferencia. Tratamiento paralelo de las reglas. Determinación del aporte parcial de cada regla. Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (2
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > Regiones de Decisión. Modo de operación autoasociativo. **Capítulo X** **Generalización en las RNA,** definición, factores que influyen en la capacidad de Generalización. Tamaño del conjunto de pat
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > **Capítulo IX** **Redes** **Perceptron** **Multicapa**, estructura básica. Proceso de Entrenamiento Backpropagation (BP). Interpretación heurística y matemática del procedimiento BP. Término de Momen
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Herramientas para el desarrollo de Sistemas Expertos. **Capítulo VI** **Lógica Difusa (Fuzzy).** Consideraciones generales, Conjuntos Difusos, definición. Operaciones simples entre conjuntos Difusos
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: pesos. Regiones de Decisión. Problema de separación lineal. Aplicaciones. Limitaciones | Pagina: 2]
   > Problema XOR.
8. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: **I. FUNDAMENTACIÓN** | Pagina: 1]
   > Los estudiantes explorarán los efectos de las nuevas tecnologías en el trabajo, la calidad de vida laboral y la administración del talento humano en la era digital. Además, se abordarán aspectos legal
9. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Clase de direccionamiento (clase a, b, c, d y e). Prefijo y Mascara de red. Lógica de and. Calculo de direcciones. División de subredes (por clase y vlsm (mascara de subred de longitud variable)), i
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 3]
   > conocimiento vulgar, conocimiento científico. Clasificación de las ciencias. Diferencias entre ciencia, técnica, tecnología, ingeniería e intervención profesional. La ciencia y los sistemas de infor

**Respuesta:**

El programa de Contenidos de la materia Inteligencia Artificial incluye:

Agentes Inteligentes: Introducción a la Inteligencia Artificial (IA), descripción de los temas específicos a desarrollarse en la asignatura, introducción a los agentes inteligentes, entorno de Trabajo, propiedades de los entornos, estructura de los Agentes, programas de Agentes, Agente Reactivo Simple, Agentes Reactivos basados en Modelos, Agente basado en objetivos y Agentes que aprenden.

Proceso de Inferencia, tratamiento paralelo de las reglas, determinación del aporte parcial de cada regla e integración de la solución difusa final. Proceso de Defuzzificación, definición, método del centroide y método de máxima.

Agentes Basados en Lógica Difusa.

Redes Neuronales Artificiales (RNA): Generalidades, conceptos básicos, resumen histórico, clasificación de las RNA y agentes basados en proceso de Aprendizaje.

Bibliografía: "Inteligencia Artificial - Un Enfoque Moderno" y "Aprendizaje automático y aprendizaje profundo con Python, scikit-learn y Tensor Flow".

Regiones de Decisión. Modo de operación autoasociativo.

Redes Perceptron Multicapa: Estructura básica, proceso de Entrenamiento Backpropagation (BP), interpretación heurística y matemática del procedimiento BP.

Lógica Difusa (Fuzzy): Consideraciones generales, conjuntos difusos, operaciones simples entre conjuntos difusos, estructuras FAM (Fuzzy Associative Memories) y composición MAX-MIN.

Sistemas Difusos: Consideraciones generales, representación de conocimiento estructurado mediante reglas lingüísticas, proceso de Fuzzificación e influencia de la forma y distribución de los conjuntos difusos en el comportamiento del sistema.

Redes Autoorganizadas: Características generales y el Red SOM (Kohonen).

Generalización en las RNA: Definición, factores que influyen en la capacidad de generalización y algoritmos de reducción (Pruning Algorithms).

**Tokens:** entrada: 2014 | salida: 484 | total: 2498

---

### Pregunta 2

> - ¿En qué materia se enseña el concepto de Lógica Difusa?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Herramientas para el desarrollo de Sistemas Expertos. **Capítulo VI** **Lógica Difusa (Fuzzy).** Consideraciones generales, Conjuntos Difusos, definición. Operaciones simples entre conjuntos Difusos
2. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > **Capítulo III** **Sistemas Basados en Conocimientos**. Conceptos básicos. Representación de Conocimientos. Estructuras basadas en Lógica. Lógica de Primer Orden. Reglas de Inferencia. Representación
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > La cátedra implementará el modelo de aula invertida, en el que los estudiantes adquieren los conocimientos teóricos de manera previa a la clase, a través de videos elaborados por la cátedra, lectura
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Clase de direccionamiento (clase a, b, c, d y e). Prefijo y Mascara de red. Lógica de and. Calculo de direcciones. División de subredes (por clase y vlsm (mascara de subred de longitud variable)), i
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 15]
   > ; director Aldo Daniel Sigura ;<br>codirector Pablo Emanuel Goette.|2019| |Deep Learning aplicado al aprendizaje automático de ontologías para la<br>representación del conocimiento a partir de texto n
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos vertidos en la teoría. Más dos trabajos Prácticos que se realizan en el ho
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 3]
   > - Fomentar espacios de trabajo compartido favoreciendo la comprensión de la naturaleza del objeto de conocimiento desde una posición reflexiva y crítica estableciendo puentes entre la investigación
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (2
9. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
10. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: **I. FUNDAMENTACIÓN** | Pagina: 1]
   > Los estudiantes explorarán los efectos de las nuevas tecnologías en el trabajo, la calidad de vida laboral y la administración del talento humano en la era digital. Además, se abordarán aspectos legal

**Respuesta:**

La materia en la que se enseña el concepto de Lógica Difusa es la de Inteligencia Artificial.

**Tokens:** entrada: 2107 | salida: 27 | total: 2134

---

### Pregunta 3

> - ¿Cuál es el plan de estudios de Metodología de la Investigación?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > |METODOLOGÍA DE LA INVESTIGACIÓN- 2026|Col2|Col3|Col4|Col5| |---|---|---|---|---| |**Clase **|**FECHA**|**Tipo de encuentro**|**Tipo encuentro**|**Tema**| |1|12 de marzo|**Presencial**|**Teórico/práct
2. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: **Equipo docente:** PROFESORA RESPONSABLE ADJUNTO: ALEJANDRA MARǪUESIN; JEFE DE | Pagina: 1]
   > TRABAJOS PRÁCTICOS: TAMARA SUIVA. JEFE DE TRABAJOS PRÁCTICOS: JIMENA SANTA CRUZ; **Año de la carrera a la que pertenece la cátedra:** 4 **Régimen de la materia:** Anual **Carga horaria semanal:** 3
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 18]
   > integrador se determinará exclusivamente en la mesa de examen, junto con la nota correspondiente a la instancia teórica, estableciéndose en ese momento la calificación final y la condición de aproba
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: dentro de la plataforma Moodle. La organización será la siguiente | Pagina: 5]
   > curso. - Desarrollo de contenidos: distribuidos en tres pestañas temáticas: - Introducción - Dimensión epistemológica - Dimensión estratégica - Dimensión técnica - Cada semana se habilitar
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > objetivos y relación de los objetivos con las preguntas de la investigación. **Unidad 3: La dimensión de la estrategia general de investigación** ¿Cómo se va a estudiar el problema? Tipo de diseños c
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: **Equipo docente:** PROFESORA RESPONSABLE ADJUNTO: ALEJANDRA MARǪUESIN; JEFE DE | Pagina: 1]
   > A los fines de su desarrollo, se entenderá a la Metodología de la Investigación como el conjunto de estrategias, reflexiones y decisiones que configuran los procesos de investigación científica. Por
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 8]
   > especializada. - Encuentro entre pares: se organizarán espacios de intercambio con estudiantes que ya han cursado la carrera, con el fin de compartir experiencias. **Sistema de evaluación:** - U
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 8]
   > - Articulación con la cátedra Tesina de Grado: se organizarán encuentros conjuntos en los que los estudiantes presentarán los avances de sus proyectos, promoviendo un trabajo coordinado entre Metodo
9. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > Dado que se trata de una asignatura de cuarto año, la modalidad de cursado será combinada. En este marco, se llevará a cabo un encuentro presencial físico mensual, enfocado en la escritura del antep
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 1]
   > **2026 - FCYT-ORO VERDE - Licenciatura en Sistemas de Información - Metodología de la** **Investigación** **Carrera:** Licenciatura en Sistemas de Información **Cátedra:** Metodología de la Investig

**Respuesta:**

El plan de estudios de Metodología de la Investigación se encuentra resumido en las siguientes unidades:

 - Unidad 1: Introducción a la ciencia y conocimiento científico
 - Unidad 2: La dimensión epistemológica
 - Unidad 3: La dimensión de la estrategia general de investigación
 - Unidad 4: La dimensión de las técnicas de obtención y análisis de información empírica. La comunicación de los resultados

**Tokens:** entrada: 2281 | salida: 110 | total: 2391

---

### Pregunta 4

> - ¿Qué herramientas de software se recomiendan en la carrera para resolver problemas de optimización lineal y cómo se relacionan con las unidades teóricas?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadístico
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > optimalidad de Bellman. Resolución de problemas de diligencia, asignación de recursos y reemplazo de equipos. Diferencias entre Programación Dinámica Determinística y Probabilística.
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: pesos. Regiones de Decisión. Problema de separación lineal. Aplicaciones. Limitaciones | Pagina: 2]
   > Problema XOR.
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
6. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: PROGRAMA DE CÁTEDRA: INFORMÁTICA Y RELACIONES HUMANAS | Pagina: 1]
   > Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas semanales
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 7]
   > Durante los encuentros sincrónicos orientados a la práctica, se trabajará bajo modalidad de taller, con instancias de escritura guiada, revisión de avances y discusión de decisiones metodológicas, f
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: UNDERWRITERS LABORATORIES (UL) -> www.ul.com | Pagina: 5]
   > PANDUIT -> www.panduit.com AMP -> www.tycoelectronics.com/components/ ETHEREAL -> www.ethereal.com SIEMENS -> www.sea.siemens.com/step/templates/lesson.mason?electricity:2:3:3
9. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: **I. FUNDAMENTACIÓN** | Pagina: 1]
   > Los estudiantes explorarán los efectos de las nuevas tecnologías en el trabajo, la calidad de vida laboral y la administración del talento humano en la era digital. Además, se abordarán aspectos legal
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 15]
   > ; director Aldo Daniel Sigura ;<br>codirector Pablo Emanuel Goette.|2019| |Deep Learning aplicado al aprendizaje automático de ontologías para la<br>representación del conocimiento a partir de texto n

**Respuesta:**

Para resolver problemas de optimización lineal, se recomiendan las herramientas de software LINDO (Linear, Interactive, and Discrete Optimizer), que es reconocido por su sintaxis sencilla para ingresar ecuaciones y restricciones de manera directa, y WinQSB 2.0, que abarca múltiples módulos de Investigación Operativa y permite resolver problemas de programación lineal (LP).

Estas herramientas están relacionadas con las unidades teóricas de la materia, como la Unidad IV: "Modelos de Transporte y Transbordo", que abarca el problema del transporte y la optimidad de Bellman.

**Tokens:** entrada: 1750 | salida: 146 | total: 1896

---

### Pregunta 5

> - ¿Qué instancias de recuperación nos provee Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > **Instancias de Recuperación:** La cátedra dispone de **dos oportunidades de** **recuperatorio** totales. Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no s
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadístico
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > entrada y salida de variables. Interpretación de la tabla óptima. Aplicación del método de la "M Grande" y método de las "Dos Fases". Análisis de dualidad y sensibilidad básica en modelos lineales.
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
7. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > estructura del modelo y suposiciones. Métodos para obtener una solución básica inicial: Esquina Noroeste, Costo Mínimo y Aproximación de Vogel. Método MODI (Distribución Modificada) para la optimiza
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > corridos tras la evaluación. Los exámenes se desarrollarán estrictamente en los bloques horarios asignados a la materia. La ausencia no justificada (sin certificado médico o motivo de fuerza mayor v
9. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 15]
   > ; director Aldo Daniel Sigura ;<br>codirector Pablo Emanuel Goette.|2019| |Deep Learning aplicado al aprendizaje automático de ontologías para la<br>representación del conocimiento a partir de texto n
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: **Equipo docente:** PROFESORA RESPONSABLE ADJUNTO: ALEJANDRA MARǪUESIN; JEFE DE | Pagina: 1]
   > A los fines de su desarrollo, se entenderá a la Metodología de la Investigación como el conjunto de estrategias, reflexiones y decisiones que configuran los procesos de investigación científica. Por

**Respuesta:**

La cátedra de Investigación Operativa dispone de dos oportunidades de recuperatorio totales. Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no se pueden aplicar ambos recuperatorios al mismo examen parcial.

**Tokens:** entrada: 2008 | salida: 61 | total: 2069

---

### Pregunta 6

> - ¿Para qué sirve el software TORA y qué módulos incluye según la cátedra?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadístico
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: **I. FUNDAMENTACIÓN** | Pagina: 1]
   > Los estudiantes explorarán los efectos de las nuevas tecnologías en el trabajo, la calidad de vida laboral y la administración del talento humano en la era digital. Además, se abordarán aspectos legal
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > |23|24<br>de<br>septiembr<br>e|Virtual|Tutorías|Tutorías| |24|01 de octubre|Presencial|Tutorías|Presentación tesina- ver<br>posibilidad| |25|08 de octubre|Virtual|Tutorías|Presentación tesina- ver<br>
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos vertidos en la teoría. Más dos trabajos Prácticos que se realizan en el ho
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > **Capítulo IX** **Redes** **Perceptron** **Multicapa**, estructura básica. Proceso de Entrenamiento Backpropagation (BP). Interpretación heurística y matemática del procedimiento BP. Término de Momen
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: pesos. Regiones de Decisión. Problema de separación lineal. Aplicaciones. Limitaciones | Pagina: 2]
   > Problema XOR.
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
9. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: IV. BIBLIOGRAFÍA GENERAL | Pagina: 3]
   > _**Bibliografía Básica:**_ Nicolás S. Tato, El Derecho Informático - Aspectos Fundamentales. Mariana Nazar, Tecnologías, información y derechos. Gonzalo Ana Dobratinich, derecho y nuevas tecnología
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > La cátedra implementará el modelo de aula invertida, en el que los estudiantes adquieren los conocimientos teóricos de manera previa a la clase, a través de videos elaborados por la cátedra, lectura

**Respuesta:**

TORA es una herramienta educativa diseñada específicamente para el aprendizaje de la Investigación Operativa. Incluye módulos para el Método Simplex (con visualización paso a paso), modelos de transporte, redes y teoría de juegos.

**Tokens:** entrada: 1992 | salida: 55 | total: 2047

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
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Clase de direccionamiento (clase a, b, c, d y e). Prefijo y Mascara de red. Lógica de and. Calculo de direcciones. División de subredes (por clase y vlsm (mascara de subred de longitud variable)), i
6. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **HORARIOS DE CLASE** | Pagina: 1]
   > Lunes: 13:30 a 15:30 (Teoría) Viernes: 17:00 a 19:00 (Práctica) Nota: Los horarios están en proceso de evaluación y pueden sufrir cambios
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > . Modelo de referencia OSI, Modelo de protocolo TCP/IP, comparación modelo OSI y TCP/IP, critica al modelo OSI y los protocolos; Organismos de estandarización de comunicación y redes. **Unidad II**: -
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 4]
   > La cátedra consta de trabajos prácticos de laboratorio que se realizan en clase, los cuales sirven para asentar los conceptos vertidos en la teoría. Más dos trabajos Prácticos que se realizan en el ho
9. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **BIBLIOGRAFÍA BASE** | Pagina: 2]
   > Elmasri, R. / Navathe, S. - Fundamentos de Sistemas de Bases de Datos (Addison Wesley) Silberschatz / Korth / Sudarshan - Fundamentos de Bases de Datos (Mc Graw Hill) Date, C.J. - Introducción a los S
10. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > retroceso exponencial binario, LAN Inalámbricas IEEE 802.11, Banda Ancha Inalámbrica IEEE 802.16, Comparación entre el estándar IEEE 802.11 y IEEE 802.16, Bluetooh, Conmutación en la capa de enlace (R

**Respuesta:**

Jorge L. Schmukler es el profesor que forma parte del equipo docente tanto en la materia de Bases de Datos Avanzadas como en la de Comunicaciones y Redes.

**Tokens:** entrada: 1897 | salida: 43 | total: 1940

---

### Pregunta 8

> - ¿Qué otra asignatura, además de la propia materia de Inteligencia Artificial, incluye explícitamente el impacto o uso de la 'Inteligencia artificial' (IA) dentro de sus unidades temáticas?

**Chunks de contexto:**

1. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > Inteligencia Artificial Programa de Contenidos **Capítulo I** **Agentes Inteligentes** Introducción a la Inteligencia Artificial (IA). Definiciones y objetivos. Herramientas y técnicas provistas p
2. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 4. El impacto de la inteligencia artificial en la gestión del talento. | Pagina: 2]
   > _**Bibliografía Nacional:**_ Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales. **Uni
3. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (2
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > Regiones de Decisión. Modo de operación autoasociativo. **Capítulo X** **Generalización en las RNA,** definición, factores que influyen en la capacidad de Generalización. Tamaño del conjunto de pat
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > **Capítulo IX** **Redes** **Perceptron** **Multicapa**, estructura básica. Proceso de Entrenamiento Backpropagation (BP). Interpretación heurística y matemática del procedimiento BP. Término de Momen
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: pesos. Regiones de Decisión. Problema de separación lineal. Aplicaciones. Limitaciones | Pagina: 2]
   > Problema XOR.
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Herramientas para el desarrollo de Sistemas Expertos. **Capítulo VI** **Lógica Difusa (Fuzzy).** Consideraciones generales, Conjuntos Difusos, definición. Operaciones simples entre conjuntos Difusos
8. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: **I. FUNDAMENTACIÓN** | Pagina: 1]
   > Los estudiantes explorarán los efectos de las nuevas tecnologías en el trabajo, la calidad de vida laboral y la administración del talento humano en la era digital. Además, se abordarán aspectos legal
9. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > La cátedra implementará el modelo de aula invertida, en el que los estudiantes adquieren los conocimientos teóricos de manera previa a la clase, a través de videos elaborados por la cátedra, lectura
10. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra

**Respuesta:**

La materia "Informática y Recursos Humanos" menciona en su sección 4 el "impacto de la inteligencia artificial en la gestión del talento".

**Tokens:** entrada: 1928 | salida: 37 | total: 1965

---

### Pregunta 9

> - Los requisitos para regularizar en Bases de Datos Avanzadas y en Redes y Comunicaciones, ¿son iguales? ¿Qué diferencias tienen?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > **Evaluación Final:** El alumno con condición de REGULAR, deberá rendir un examen de los temas teóricos y prácticos desarrollados en la materia (prueba escrita). El alumno LIBRE rendirá un examen fina
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > ; Algoritmos de enrutamiento (Principio de optimización, Enrutamiento por la ruta más corta, Inundación, Enrutamiento por vector de distancia, Enrutamiento por estado del enlace, Enrutamiento jerárqui
3. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Utilización de hubs como dispositivo intermedio (problemas con el crecimiento de la red: escalabilidad, fallas en la red, colisiones). Switches (ancho de banda dedicado a cada puerto, entorno libre
4. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **SOFTWARE REQUERIDO** | Pagina: 2]
   > PostgreSQL: versión 9.6 o superior SQL Server: versión 2016 o superior QGIS: versión compatible con PostgreSQL Anaconda (Python): últimas versiones
5. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **CANALES DE COMUNICACIÓN** | Pagina: 2]
   > Correo: Lista de mail (consultas y comunicación de rutina) Aula virtual: Material académico - Clave de matriculación: bda2023 (ÚNICO MEDIO OFICIAL) Telegram: https://t.me/+c7PPIrc9nQM4MzEx (avisos y n
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > : - **Capa de enlace de dato** - **sub capa** **LLC (control de enlace lógico)** Cuestiones en el diseño de la capa de enlace de dato, servicios proporcionados por la capa de red, entramado, control d
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Proveedores de servicio de internet (ISP), descripción Ipv6. **Unidad IX** **-VLans-** Definiciones de Vlan, Beneficios de una Vlan, Rangos de ID de la Vlan (rango normal y rango extendido), Tipos d
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > retroceso exponencial binario, LAN Inalámbricas IEEE 802.11, Banda Ancha Inalámbrica IEEE 802.16, Comparación entre el estándar IEEE 802.11 y IEEE 802.16, Bluetooh, Conmutación en la capa de enlace (R
9. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Sitios web sobre normativas, tecnologías y soluciones, opcional** | Pagina: 5]
   > IETF -> www.ietf.org IEEE -> www.ieee.org ISO -> www.iso.org CISCO -> www.cisco.com IANA -> www.iana.org ISOC -> www.isoc.org ARIN -> www.arin.net LACNIC -> http://lacnic.net/sp/ LAC IPV6 TF -> www.la
10. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **RÉGIMEN DE CURSADA** | Pagina: 2]
   > **Regularidad:** Asistencia: Según norma vigente Todos los trabajos prácticos aprobados 6/7 parciales aprobados con más del 50% **Promoción:** Régimen regular Obtener más del 70% en todos los parci

**Respuesta:**

En Redes y Comunicaciones, los requisitos para regularizar mencionados en el Contexto son:

* El alumno con condición de REGULAR deberá rendir un examen de los temas teóricos y prácticos desarrollados en la materia (prueba escrita).
* Los temas a evaluar en la prueba escrita no se especifican explícitamente en el Contexto proporcionado.

En Bases de Datos Avanzadas, los requisitos para regularizar mencionados en el Contexto son:

* Asistencia según norma vigente.
* Todos los trabajos prácticos deben estar aprobados.
* Se debe obtener 6/7 parciales aprobados con más del 50%.
* No se mencionan específicamente los requisitos de examen o prueba escrita para regularizar.

Por lo tanto, los requisitos para regularizar no son exactamente iguales. En Redes y Comunicaciones, el requisito principal mencionado es rendir un examen de los temas teóricos y prácticos, mientras que en Bases de Datos Avanzadas, los requisitos incluyen asistencia, aprobación de trabajos prácticos, y un promedio de parciales aprobados.

**Tokens:** entrada: 2037 | salida: 268 | total: 2305

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
4. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 16]
   > Para acceder a la condición de Promoción Directa, el/la estudiante deberá cumplir con los siguientes requisitos: - 80 % de asistencia a la cursada. - Aprobación del examen parcial teórico con una
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: Dr Roberto Hernández Sampieri Charla enfoques cuantitativo, cualitativo, mixto | Pagina: 13]
   > [https://youtu.be/CfjSC_pp8o0](https://youtu.be/CfjSC_pp8o0) _Bibliografía obligatoria sobre escritura académica_ - Natale, Lucía (Coordinadora) (2013). En carrera: escritura y lectura de textos ac
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 16]
   > durante el proceso. - 80 % de los cuestionarios de autoevaluación respondidos. - Presentación y defensa oral del trabajo práctico integrador, previamente aprobado, en instancia de coloquio. Es r
7. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > . Modelo de referencia OSI, Modelo de protocolo TCP/IP, comparación modelo OSI y TCP/IP, critica al modelo OSI y los protocolos; Organismos de estandarización de comunicación y redes. **Unidad II**: -
8. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 8]
   > - Articulación con la cátedra Tesina de Grado: se organizarán encuentros conjuntos en los que los estudiantes presentarán los avances de sus proyectos, promoviendo un trabajo coordinado entre Metodo
9. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 6]
   > estudiantes los materiales y herramientas necesarios para la construcción autónoma del conocimiento. - Cada clase incluirá uno o más de los siguientes recursos: - Un video explicativo. - Materi
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > |||||investigación| |17|13 de agosto|Virtual|Tutorías|Tutorías| |18|20 de agosto|**_Presencial (cambio_**<br>**_encuentro)_**|**Teoría**|Parcial teoría| |19|27 de agosto|Virtual|Tutorías|Tutorías| |20

**Respuesta:**

80%. Esta es la condición compartida por estas materias. En Investigación Operativa, en la condición de "Alumno Regular", se exige un 80 % de asistencia. En Metodología de la Investigación, el "Alumno Regular" también requiere asistir a un 80 % de las clases. En el Planificación 2025 - Comunicacion y Redes, en la unidad I, se menciona una "Capa física concepto y medios", y la información disponible en el programa indica que la asistencia al 80% es un requisito para poder acceder a la condición de "Promoción Directa".

**Tokens:** entrada: 2458 | salida: 142 | total: 2600

---

### Pregunta 11

> - Un proyecto integrador requiere utilizar un software para resolver problemas de optimización a gran escala que pueda conectarse de forma fluida con bases de datos espaciales. Según las herramientas enseñadas en las materias, ¿qué combinación de software visto en Bases de Datos Avanzadas e Investigación Operativa sería la más adecuada para este objetivo?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **PHP Simplex:** Herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el Método Simplex y el Método Gráfico. Es ideal para validaciones rápidas y vis
3. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **SOFTWARE REQUERIDO** | Pagina: 2]
   > PostgreSQL: versión 9.6 o superior SQL Server: versión 2016 o superior QGIS: versión compatible con PostgreSQL Anaconda (Python): últimas versiones
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > dinámica, teoría de colas y gestión de inventarios. - **Storm:** Software orientado al análisis cuantitativo y gestión de operaciones. Facilita el procesamiento de modelos matemáticos y estadístico
5. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Software de Aplicación - Investigación Operativa** | Pagina: 2]
   > A continuación, se describen las herramientas informáticas utilizadas en la cátedra
6. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > optimalidad de Bellman. Resolución de problemas de diligencia, asignación de recursos y reemplazo de equipos. Diferencias entre Programación Dinámica Determinística y Probabilística.
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: **Equipo docente:** PROFESORA RESPONSABLE ADJUNTO: ALEJANDRA MARǪUESIN; JEFE DE | Pagina: 1]
   > A los fines de su desarrollo, se entenderá a la Metodología de la Investigación como el conjunto de estrategias, reflexiones y decisiones que configuran los procesos de investigación científica. Por
8. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **EQUIPO DOCENTE** | Pagina: 1]
   > Teoría: Trossero, Sebastián (Trossero.sebastian@uader.edu.ar) Práctica: Schmuckler, Jorge (Schmukler.jorge@uader.edu.ar)
9. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: **I. FUNDAMENTACIÓN** | Pagina: 1]
   > El avance de las tecnologías de la información y la comunicación (TIC) ha transformado la dinámica del mundo laboral y las relaciones humanas dentro de las organizaciones. Esta asignatura busca analiz
10. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > previa instancia de revisión y devolución con el equipo docente. El trabajo deberá entregarse con una antelación mínima de diez (10) días hábiles respecto de la fecha de la mesa; en caso contrario,

**Respuesta:**

La herramienta más adecuada para resolver problemas de optimización a gran escala y conectarse de forma fluida con bases de datos espaciales es **LINGO (64 bits)**. Este software se menciona en el contexto de la materia de Investigación Operativa como una versión avanzada y potente del motor LINDO, diseñada para modelar y resolver problemas de optimización de gran escala.

En cuanto a la integración con bases de datos espaciales, la combinación que mejor se ajusta a este objetivo es la de **QGIS** (versión compatible con PostgreSQL) y **PostgreSQL** (versión 9.6 o superior). QGIS es una herramienta de análisis espacial que permite la integración con bases de datos espaciales, mientras que PostgreSQL es una base de datos que se menciona como compatible con QGIS en el contexto de la materia de Bases de Datos Avanzadas. 

Además, LINGO es compatible con bases de datos, por lo que sería posible utilizar esta herramienta para modelar y resolver problemas de optimización y conectarla con bases de datos espaciales, como PostgreSQL, mediante QGIS.

**Tokens:** entrada: 1857 | salida: 247 | total: 2104

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
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 4. El impacto de la inteligencia artificial en la gestión del talento. | Pagina: 2]
   > _**Bibliografía Nacional:**_ Gonzalo Ana Dobratinich, Derecho y nuevas tecnologías. Artículos académicos sobre la transformación del trabajo y el impacto de la IA en las relaciones laborales. **Uni
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Proceso de Inferencia. Tratamiento paralelo de las reglas. Determinación del aporte parcial de cada regla. Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del
6. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 5. comercio electrónico, manifestación del consentimiento en internet | Pagina: 3]
   > _**Bibliografía Nacional:**_ Ley de Teletrabajo (Ley 27.555) Código Civil y Comercial de la Nación (aspectos relacionados con contratos digitales). Artículos académicos sobre la economía gig y el t
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > Modificación del algoritmo SOM para evitar una excesiva acumulación de información, por parte de una misma neurona. **Capítulo XII** **Sistemas Multi Agentes** Introducción a los sistemas multiagen
8. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 4. Derecho a la desconexión digital y equilibrio entre vida personal y laboral. | Pagina: 2]
   > _**Bibliografía Nacional:**_ Ley Nacional de Protección de Datos Personales (Ley 25.326). Código Civil y Comercial de la Nación (aspectos relacionados con contratos digitales y firma electrónica).
9. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 14]
   > ; director Fernando Sato ;<br>codirector Sebastián Jorge Trossero.|2022| |Modelos vectoriales y redes neuronales artifciales, para la aplicación de<br>procesamiento de lenguaje natural en normativas j
10. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > . **Conceptos** **usados en Comunicaciones y Redes:** Uso de la redes de computadora, aplicaciones de negocios, domésticas, distintos usuarios. Hardware de redes, Sistema Cliente/Servidor, tipos de re

**Respuesta:**

Para investigar sobre el impacto de los "Agentes que aprenden" y las "Redes Neuronales" en la selección de personal y el teletrabajo en Argentina, el estudiante debería considerar las siguientes normativas legales y temas específicos:

- Ley de Teletrabajo (Ley 27.555): Como se menciona en la sección "5. Comercio electrónico, manifestación del consentimiento en internet" del programa de Informática y RRHH, esta ley es relevante para comprender el marco legal del teletrabajo en Argentina.
- Código Civil y Comercial de la Nación (aspectos relacionados con contratos digitales): Este texto jurídico es mencionado en la misma sección del programa como base para comprender las implicaciones legales del teletrabajo y la firma electrónica.
- Ley Nacional de Protección de Datos Personales (Ley 25.326): Esta ley es mencionada en la sección "4. Derecho a la desconexión digital y equilibrio entre vida personal y laboral" del programa, y es importante considerar sus aspectos relacionados con la privacidad y la seguridad de los datos personales en el contexto del teletrabajo.
- Ley Propiedad Intelectual (Ley 11.723) y su modificatoria: Si bien la relación con el tema en específico es menor, es importante recordar que cualquier implementación o aplicación de Redes Neuronales o Agentes que Aprenden, tendrán un impacto en la propiedad intelectual.
- Ley de Protección de Datos Personales y su conexión con los temas de la IA y RRHH.

**Tokens:** entrada: 1935 | salida: 356 | total: 2291

---

### Pregunta 13

> - ¿Dónde puedo descargar la materia de Cálculo de 1er año?

**Chunks de contexto:**

1. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 12]
   > - Natale, Lucía (Coordinadora) (2013). En carrera: escritura y lectura de textos académicos y profesionales. Argentina. Universidad Nacional de Ǫuilmes. Visto en [https://ediciones.ungs.edu.ar/wp-co
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: UNDERWRITERS LABORATORIES (UL) -> www.ul.com | Pagina: 5]
   > PANDUIT -> www.panduit.com AMP -> www.tycoelectronics.com/components/ ETHEREAL -> www.ethereal.com SIEMENS -> www.sea.siemens.com/step/templates/lesson.mason?electricity:2:3:3
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: PROGRAMA DE CÁTEDRA: INFORMÁTICA Y RELACIONES HUMANAS | Pagina: 1]
   > Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas semanales
4. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: Plan de Estudio | Pagina: 1]
   > Docente: Abog. Rodriguez Zanin, Fabio
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > . Televisión por cable (televisión por antena comunal, Internet a través de cable, asignación de espectro, modem de cable, ADSL en comparación con el cable). **Unidad IV**
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > : enfoque y<br>tipo de investigación / muestra| |14|11 de junio|Virtual|Práctica|| |15|18 de junio|Virtual|Teoría|Marco metodológico II:<br>recolección de datos y análisis de<br>datos| |||||| |RECESO
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: pesos. Regiones de Decisión. Problema de separación lineal. Aplicaciones. Limitaciones | Pagina: 2]
   > Problema XOR.
8. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **PRESENTACIÓN DE LA MATERIA** | Pagina: 1]
   > Facultad de Ciencia y Tecnología Universidad Autónoma de Entre Ríos (UADER)
9. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > **Unidad I: -Introducción y Modelos Matemáticos-** Definición y origen de la Investigación Operativa. Metodología de la construcción de modelos: definición del problema, construcción del modelo mate
10. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 6. Desafíos éticos y sociales de la tecnología en el ámbito laboral. | Pagina: 1]
   > _**Bibliografía Nacional:**_ Ley de Teletrabajo (Ley 27.555).

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1683 | salida: 14 | total: 1697

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
4. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 1]
   > **Capítulo III** **Sistemas Basados en Conocimientos**. Conceptos básicos. Representación de Conocimientos. Estructuras basadas en Lógica. Lógica de Primer Orden. Reglas de Inferencia. Representación
5. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 4]
   > Bibliografía Principal (Disponibles en biblioteca) Título: "Inteligencia Artificial - Un Enfoque Moderno"- Segunda Edition. Autores: Stuart J. Rusell, Peter Norvig. Editorial: Pearson Educación (2
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 3]
   > **Capítulo IX** **Redes** **Perceptron** **Multicapa**, estructura básica. Proceso de Entrenamiento Backpropagation (BP). Interpretación heurística y matemática del procedimiento BP. Término de Momen
7. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Herramientas para el desarrollo de Sistemas Expertos. **Capítulo VI** **Lógica Difusa (Fuzzy).** Consideraciones generales, Conjuntos Difusos, definición. Operaciones simples entre conjuntos Difusos
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > **Unidad VIII**: - **Direccionamiento IP, Segmentación de Red** Estructura de una dirección IP. Conversión de decimales a binario y binario a decimal. Tipos de direcciones IP (dirección de host e iden
9. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > : - **Capa de enlace de dato** - **sub capa** **LLC (control de enlace lógico)** Cuestiones en el diseño de la capa de enlace de dato, servicios proporcionados por la capa de red, entramado, control d
10. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > - Spinella, Emiliano Francisco: Redes GNU/LINUX: manual del administrador / E. F. Spinella. - Buenos Aires: Gradi, 2007. ISBN 9789871347551 [Disponible en Biblioteca FCyT- Oro Verde] - Stallings, Wi

**Respuesta:**

No. El profesor Ing. Jorge L. Schmukler da clases en Inteligencia Artificial y en Redes y Comunicaciones, pero no aparece mencionado en el documento BDA_Planificación.pdf como el profesor de Bases de Datos Avanzadas. Aparece otro profesor, Trossero, Sebastián.

**Tokens:** entrada: 2004 | salida: 75 | total: 2079

---

### Pregunta 15

> - ¿Cuál es el costo de la certificación oficial de Cisco que se menciona como opcional en la planificación?

**Chunks de contexto:**

1. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: 4- BIBLIOGRAFIA | Pagina: 4]
   > **Obligatoria** - Apuntes teóricos de la Cátedra en distintos formatos. [Disponibles en fotocopiadora FCyT - Oro Verde] - Cisco Systems: Academia de Networking de Cisco Systems: Guía del primer añ
2. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Sitios web sobre normativas, tecnologías y soluciones, opcional** | Pagina: 5]
   > IETF -> www.ietf.org IEEE -> www.ieee.org ISO -> www.iso.org CISCO -> www.cisco.com IANA -> www.iana.org ISOC -> www.isoc.org ARIN -> www.arin.net LACNIC -> http://lacnic.net/sp/ LAC IPV6 TF -> www.la
3. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: PROGRAMA DE CÁTEDRA: INFORMÁTICA Y RELACIONES HUMANAS | Pagina: 1]
   > Carrera: Licenciatura en sistemas de Información Sede: Oro Verde Ciclo Lectivo: 2025 Año: 4° Desarrollo: Cuatrimestral Carga Horaria: Tres (3) horas semanales
4. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > . Explicar el **propósito de IOS como Sistema** **Operativo de red**, Explicar cómo acceder al IOS y cómo explorarlo para configurar los dispositivos de red, Describir la estructura de comandos, Confi
5. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . La ethernet actual. La trama de ethernet. Power Over Ethernet. Direcciones MAC. Dispositivo de red (nic). Ethernet unicast, multicast, broadcast. CSMA/CD (Acceso Múltiple por Detección de Portadora
6. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > **1 -** Obtener en los 3 parciales, una calificación promedio superior o igual a los 60 puntos. Tener aprobado con 60 puntos los tres parciales.
7. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **SOFTWARE REQUERIDO** | Pagina: 2]
   > PostgreSQL: versión 9.6 o superior SQL Server: versión 2016 o superior QGIS: versión compatible con PostgreSQL Anaconda (Python): últimas versiones
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > - **ALUMNO REGULAR:** Obtendrá la regularidad aquel estudiante que logre una calificación mínima de **60 puntos en ambos parciales**. Es requisito indispensable la entrega y aprobación de los dos tr
9. [Documento: PROGRAMA INFORMATICA Y RRHH.pdf | Materia: Informática y Recursos Humanos | Seccion: 5. comercio electrónico, manifestación del consentimiento en internet | Pagina: 3]
   > _**Bibliografía Nacional:**_ Ley de Teletrabajo (Ley 27.555) Código Civil y Comercial de la Nación (aspectos relacionados con contratos digitales). Artículos académicos sobre la economía gig y el t
10. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: General | Pagina: 2]
   > . Utilización de medios según dispositivo a conectar. Conexiones WAN. **Unidad VII**: - **Capa de Red** Capa de Internet - Protocolo IPv4 (Protocolo de Internet versión 4), protocolos de la capa de re

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 1979 | salida: 14 | total: 1993

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
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 9]
   > **Programa de trabajos prácticos:** Tp 1: Escritura académica. Se solicita a los estudiantes seleccionar un artículo de investigación sobre un tema de interés específico relacionado al campo profesi
6. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > previa instancia de revisión y devolución con el equipo docente. El trabajo deberá entregarse con una antelación mínima de diez (10) días hábiles respecto de la fecha de la mesa; en caso contrario,
7. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **RÉGIMEN DE CURSADA** | Pagina: 2]
   > **Regularidad:** Asistencia: Según norma vigente Todos los trabajos prácticos aprobados 6/7 parciales aprobados con más del 50% **Promoción:** Régimen regular Obtener más del 70% en todos los parci
8. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: Condición del Alumno | Pagina: 3]
   > **Evaluación Final:** El alumno con condición de REGULAR, deberá rendir un examen de los temas teóricos y prácticos desarrollados en la materia (prueba escrita). El alumno LIBRE rendirá un examen fina
9. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 16]
   > durante el proceso. - 80 % de los cuestionarios de autoevaluación respondidos. - Presentación y defensa oral del trabajo práctico integrador, previamente aprobado, en instancia de coloquio. Es r
10. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > **Instancias de Recuperación:** La cátedra dispone de **dos oportunidades de** **recuperatorio** totales. Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no s

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 2033 | salida: 14 | total: 2047

---

### Pregunta 17

> - ¿Cómo se resuelve un modelo de Programación Lineal usando el método de Simplex en Excel?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **PHP Simplex:** Herramienta online accesible vía URL que permite resolver problemas de programación lineal mediante el Método Simplex y el Método Gráfico. Es ideal para validaciones rápidas y vis
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > Lineal: proporcionalidad, aditividad, divisibilidad y certidumbre. Formulación de problemas de optimización. Resolución gráfica de modelos de PL: región factible, búsqueda de la solución óptima en l
3. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **Unidad IV: -Modelos de Transporte y Transbordo-** El problema del transporte | Pagina: 1]
   > estructura del modelo y suposiciones. Métodos para obtener una solución básica inicial: Esquina Noroeste, Costo Mínimo y Aproximación de Vogel. Método MODI (Distribución Modificada) para la optimiza
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > _establecerá un encuentro sincrónico para su devolución y orientación. Cumplida esta instancia_ _de revisión, el/la estudiante quedará habilitado/a para presentarse a la mesa de examen final._ _No s
6. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: pesos. Regiones de Decisión. Problema de separación lineal. Aplicaciones. Limitaciones | Pagina: 2]
   > Problema XOR.
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 14]
   > ; director Fernando Sato ; codirector<br>Carlos Fernando<br>Sosa.|2020| |Big Data como modelo de solución para la Administración Tributaria de Entre Ríos<br>/ Agustín Alorda, César Aníbal Sarchioni ;
8. [Documento: IA - Programa de Cátedra (campus).pdf | Materia: Inteligencia Artificial | Seccion: General | Pagina: 2]
   > Proceso de Inferencia. Tratamiento paralelo de las reglas. Determinación del aporte parcial de cada regla. Integración de la solución difusa final. Proceso de Defuzzificación, definición. Método del
9. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 4]
   > preguntas le hago al problema? ¿Cómo construir el marco teórico? ¿Con qué categorías? Definición temporal y de contexto. Relación con los antecedentes relevados. Formulación de las preguntas que se
10. [Documento: Planificación 2025 - Comunicacion y Redes.pdf | Materia: Comunicacion y Redes | Seccion: **Unidad I**: **Introducción -Importancia e Influencia de las Redes en Nuestras Vidas** | Pagina: 1]
   > : - **Capa de enlace de dato** - **sub capa** **LLC (control de enlace lógico)** Cuestiones en el diseño de la capa de enlace de dato, servicios proporcionados por la capa de red, entramado, control d

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 2082 | salida: 14 | total: 2096

---

### Pregunta 18

> - ¿A qué hora exacta empieza el parcial presencial del 15/06 de Investigación Operativa?

**Chunks de contexto:**

1. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > corridos tras la evaluación. Los exámenes se desarrollarán estrictamente en los bloques horarios asignados a la materia. La ausencia no justificada (sin certificado médico o motivo de fuerza mayor v
2. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: General | Pagina: 2]
   > **Instancias de Recuperación:** La cátedra dispone de **dos oportunidades de** **recuperatorio** totales. Estas pueden utilizarse para cualquiera de los dos parciales, con la restricción de que no s
3. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 19]
   > : enfoque y<br>tipo de investigación / muestra| |14|11 de junio|Virtual|Práctica|| |15|18 de junio|Virtual|Teoría|Marco metodológico II:<br>recolección de datos y análisis de<br>datos| |||||| |RECESO
4. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **SISTEMA DE EVALUACIÓN (Investigación Operativa)** | Pagina: 1]
   > **Condición del Alumno:** - **ALUMNO PROMOCIONADO:** El estudiante logrará la promoción directa si alcanza un promedio general de **80 puntos** - más entre los **1 parcial** previstos, no pudiendo
5. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > **b.** **Alumno Regular** - 60 % de asistencia. - Aprobación del examen parcial teórico con una calificación igual o superior a 60 (sesenta) puntos. - Entrega de todos los trabajos en tiempo y
6. [Documento: BDA_Planificacion.pdf | Materia: Bases de Datos Avanzadas | Seccion: **HORARIOS DE CLASE** | Pagina: 1]
   > Lunes: 13:30 a 15:30 (Teoría) Viernes: 17:00 a 19:00 (Práctica) Nota: Los horarios están en proceso de evaluación y pueden sufrir cambios
7. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 17]
   > El/la estudiante que no se ajuste a los requisitos establecidos en los puntos A y B, se considerará en condición libre. Deberá presentar el trabajo práctico integrador con una antelación mínima de v
8. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: **PLANIFICACIÓN INVESTIGACIÓN OPERATIVA** | Pagina: 1]
   > entrada y salida de variables. Interpretación de la tabla óptima. Aplicación del método de la "M Grande" y método de las "Dos Fases". Análisis de dualidad y sensibilidad básica en modelos lineales.
9. [Documento: PROGRAMA- Metodología de la Investigación.pdf | Materia: Metodología de la Investigación | Seccion: General | Pagina: 5]
   > prácticas se desarrollarán en grupos diferenciados bajo la coordinación de las docentes responsables. Además, se dispondrá de un espacio en la plataforma Moodle de la FCyT, que servirá como complem
10. [Documento: PROGRAMA - Investigación Operativa.pdf | Materia: Investigación Operativa | Seccion: para la resolución de modelos de optimización y problemas de gestión | Pagina: 2]
   > - **LINDO (Linear, Interactive, and Discrete Optimizer):** Software especializado en la resolución de problemas de programación lineal, entera y no lineal. Es reconocido por su sintaxis sencilla par

**Respuesta:**

No dispongo de información en mis documentos para responder esta consulta.

**Tokens:** entrada: 2023 | salida: 14 | total: 2037

---

## Resumen de tokens

| Conversacion | Entrada | Salida | Total |
|---|---|---|---|
| 1 | 39481 | 1921 | 41402 |
| 2 | 37475 | 1205 | 38680 |
| 3 | 36068 | 2121 | 38189 |
| **Total** | **113024** | **5247** | **118271** |
