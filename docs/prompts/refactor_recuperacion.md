-----
Modelo planeador: Opus 4.6; Orquestador Sonnet 4.6.
-----
Actualmente recuperacion.py engloba tanto el chat por consola con el LLM, como la llamada al proceso de saneamiento, conexion con la DB de Chroma, busqueda y demas.
Este enfoque hace que si queremos implementar un frontend mas adelante para crear una interfaz amigable al usuario, sea imposible reutilizando este script.
Necesito que refactorices por lo tanto el script de recuperacion.py, para crear un servicio que actue como un Singleton.
Este servicio es quien instancia a la DB, quien recibe las consultas, y responde. El mismo debe mantener su naturaleza configurable, y debe instanciar a los programas que le anteceden tal cual hace actualmente recuperacion.py
La idea despues, es que recuperacion.py quede como una interfaz por consola, la cual interactua con este objeto, para mandar consultas del usuario mediante la consola al servicio, y que este se encargue de lo demas.
Ya que recuperacion.py va a quedar como visor de la consola, vamos a aprovechar el momento para que antes de invocar a RAGService (o el nombre que le pongas al servicio para hablar con el LLM usando el RAG), aprovecharemos y haremos:
- Al instanciarse, se le pregunta al usuario que configuraciones quiere para el rag. Tendra 2 opciones al principio, Default (mostrar las default), y Custom. 
Custom permite modificar CADA parámetro que ofrece actualmente recuperacion.py (que sera transferido a la clase de RAGService), y CADA parámetro de carga.py. Asi como invocar al método --refresh de sanear.py.
- Luego, se abre el programa por consola, el cual le debe permitir al usuario intercambiar consultas con el bot hasta que escriba ¨salir¨. 

Nuevamente, el GOAL es separar en 2 modulos distintos la interfaz por consola, y el servicio encargado de proveer la interacción con el LLM. 
El plan debe estar dirigido a ORQUESTAR agentes para realizar la tarea. NO TENES PERMITIDO TOCAR CóDIGO en la implementacion, tu rol es PURAMENTE de orquestador.
