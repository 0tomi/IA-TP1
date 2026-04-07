---
modelo: Claude Opus 4.6 medium effort, Orquestador de subagentes utilizando Claude Sonnet 4.6 high effort. 
---

### Goal
Tendras como trabajo desarrollar un script de Python encargado exclusivamente de Chunking, Embedding y Persistencia de datos. El mismo será invocado por otro procedimiento, llamado Limpieza, que se encargara de traerte el documento en formato TOON dentro de un string, para que hagas el proceso de chunking, embedding, y persistencia en la base de datos vectorial de Chroma. 
Al terminar el procesamiento de los datos, se guardará en /data/ un JSON llamado registry.json que contenga un arreglo con los documentos cargados, junto a otra metadata importante como lo es: filename, materia, sha256, fecha procesamiento, cantidad de chunks, parametros usados para procesar el documento (chunk size, chunk overlap, embedding model), y el state (incorporado / error).

### Tareas
El script se llamará Carga.
El script debe permitir configurar chunk_size, chunk_overlap, embedding_model, chunking technique. 
Por default chunk_size viene definido en 512, chunk_overlap en 50, y embedding_model viene como 'gemini-embedding-001', sin embargo, estos 3 parámetros deben ser configurables, permitiendo a quien use este script (ya sea un Usuario u otro procedimiento / script), configurar estos 3 parámetros. 

- La base de datos que usarás para persistir los vectores sera Chroma, la cual deberá estar seteada en /data/, si la carpeta no existe, crearla. Lo mismo para la DB.
- El SHA256 es proveído por el script que llama a este script / usuario. No es necesario calcularlo.
- Mediante prints, se debe avisar al usuario cuando arranca el procesamiento de datos, cuando termina, y en caso de haber errores NO IMPLEMENTAR FALLBACKS SILENCIOSOS, NOTIFICAR AL USUARIO POR CONSOLA, y marcar con state de error en el registry.json junto a un mensaje descriptivo de porque falló.
- Utilizar técnica de chunking como default el "recursive_chunking", permitir configurar fixed_size_overlap. Implementar un paragraph_chunking_custom, el cual chunkea por parrafos, mantiene metadata el titulo al que le pertenece el artículo de dicho párrafo, pero tiene un tamaño fijo dado por el chunk-size. Si el parrafo excede el chunk-size, se corta el párrafo. 
- Los chunks deben contener metadata pertinente, como materia a la que pertenecen, documento, sección del pdf (nos basamos en los títulos para esto), y otros metadatos pertinentes que agilizen la busqueda de LLM encargado del retrieval.
- El contenido llega mediante un string al procedimiento, este llegará en formato TOON para ahorro de tokens, asi que ten cuidado con la semántica.

Cualquier duda sobre la implementación NO tienes permitido improvisar, ni asumir cosas. Se le debe preguntar al usuario cada confusión, contradicción y problema que encuentres.
