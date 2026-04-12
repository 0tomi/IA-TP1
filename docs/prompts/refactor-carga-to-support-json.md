Tu objetivo va a ser diseñar un refactor completo de carga.py para funcionar de forma distinta. 
saneo.py ahora devuelve en /output/ JSONs estructurados con el contenido de cada documento que debemos de chunkear y hacer el embedding para cargar en la base de datos vectorial.
Debemos adaptar carga.py para funcionar con este nuevo formato y aprovechar las nuevas ventajas que nos da.
Primero, el JSON esta estructurado por paginas, donde cada pagina esta estructurada por secciones. Cada seccion contiene el texto limpio que se mandara a cada la tecnica de chunking elegida por el usuario. 
Al tener paginados los json y ademas seccionados, vamos a aprovechar esto para tomar la pagina y la seccion como metadata.
Esta metadata NO debe inyectarse en el page content, sin embargo, a la hora de hacer el embedding, para aumentar el rendimiento, al principio del chunk vamos a ingresar la materia de la que estamos hablando y la seccion. La pagina no es relevante por ahora.
Al procesar el embedding, se procesara con estos datos. Sin embargo, en la base de datos vectorial de Chroma es importante NO contaminar el page_content con la metadata. Aca tiene que llegar el chunk con el texto limpio sin la metadata.
Al armar el plan, revisa que partes del codigo se pueden simplificar o eliminar porque queden obsoletas.
Revisar la integracion de tecnicas de chunking como el paragraph chunking o el recursive chunking, si es que no se veran afectadas por este cambio. 
Cualquier duda que te surja, NO tenes permitido asumir nada, debes preguntar priemro. Las sugerencias de mejora tambien son bienvenidas. Utiliza la tool para hacer preguntas si lo ves indicado.
