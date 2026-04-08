### Goal
Crear un script llamado evaluacion.py; este script debe leer de un archivo ubicado en la raiz llamado evaluacion.md. El script de evaluacion basicamente iniciara varias conversaciones con el agente de forma iterativa, y le ira pasando las preguntas que esten en el archivo, una a una, esperando cada respuesta, para luego dejarla en una carpeta llamada /tests/ en un formato markdown claro legible para que el usuario pueda saber como fueron las pruebas. En cada iteración se iran alterando parámetros ya sea del proceso de carga, como del RAGService, con el propósito de obtener detalles de investigación.

## Modificaciones necesarias al sistema actual para llevar a cabo los test más eficientemente
Incorporar cache de Embeddings al RAGService a la hora de hacer embedding el prompt del usuario. Actualmente el RAGService no fue diseñado con esto por lo que no deberia estar, pero para hacer estos test más eficientes
y consumir lo menos posible de las APIs limitadas que tenemos, la idea es incoporar el cache de embedding. Te dejo aca la documentación del mismo para que se haga de forma inteligente, aunque en carga.py podes encontrar
ejemplos de uso: https://reference.langchain.com/python/langchain-classic/embeddings/cache

El sistema de cache debe ser inteligente, y estar preparado para mutar / renovarse cuando el embedding model cambia. Crucial para no recibir errores o comprometer las respuestas del LLM que estarán sujetas a evaluar.

Podemos llegar a tener problemas de RESOURCE EXHAUSTED, por lo que es necesario incorporar mecanismos al RAGService para notificar en caso de que no se pueda utilizar más la API.

## Estructura de evaluacion.md
El formato de los txt sera asi:
[Preguntas]
Pregunta 1
Pregunta 2
Pregunta ...
Pregunta n
[Parámetros 1]
chunk_size= 512
retrieval_type=simmilarity_search
refresh= true
...
[Parámetros 2]
retrieval_type=mmr
...
[Parámetros n]
retrieval_type=simmilarity_search
top-k= 2
...

Los parámetros configurables y sus configuraciones por default puedes obtenerlos de recuperacion.py o indagando en los archivos de RAGService, saneo.py, y carga.py.
Si algun parametro no aparece, se asume el que se venia usando (ejemplo si chunk_size no esta, se usa el tamaño de chunk de la consulta anterior).
refresh de Saneo se toma como false si no esta, osea, no se hace. Pero si esta con = true, se toma.

## Estructura del script
El script debe al ejecutarse de ser sencillo para el usuario, avisar que conversacion inicio, y cuando termino la conversación. En caso de ocurrir errores durante una conversación, avisar por consola.
El sistema debe preever los errores, por lo tanto implementaremos un retry de 3 intentos (configurable con el parametro --retry n mediante args al invocar al script).

# Acciones del script
El script debe primero cargar en RAGService las configuraciones deseadas.
Luego debe de ir pasando una a una las preguntas (prompts) planteadas en el archivo el cual termino.
Por cada conversacion, avisar cuando arranco, avisar cuando termino, y en caso de errores, avisar que hubo un error con la pregunta N, y que se hara un retry 1/m (m por default es 3).

# Resultado del Script
Cada conversación nueva iniciada con el LLM, se debe registrar en una carpeta (crearla si no existe) llamada /tests/.
Dentro del mismo, se debe listar la respuesta a cada pregunta que se le hizo. Previo a la respuesta, poner los chunks que se le dieron de contexto al agente.
Al final del a respuesta, poner cuantos tokens consumio la entrada, la salida, y el total consumido.
Si un error sucede al mandarse determinado mensaje, este error debe marcarse en el output de los test.
AL final del archivo markdown, poner tokens totales de entrada / salida / totales usados.
Cada archivo debera tener el nombre de test-n.md 
La n no viene dado por los parametros, ya que muchas personas van a contribuir creando test variados, simplemente se deben ir acumulando, a partir del numero mas alto. 

## Contexto para realizar el planeo
La arquitectura del sistema te provee todas las herramientas necesarias para hacer esto, el resumen de tu tarea es basicamente crear una nueva interfaz para interactuar con el LLM de forma automatica. 
Deberas principalmente depender de RAGService, que es el "backend" encargado de proveer las respuestas del LLM, asi como su conexion.
Cualquier duda que te surja, consultarmela y NO tienes permitido asumir cosas.
