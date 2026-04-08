----
Modelo Sonnet 4.6 en modo Plan.
----

 Necesito planear como implementar el modelo sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 para generar los embeddings en @carga.py . Tambien sumar la opcion de usar bge-m3
  pero con parametros mas finos para no reventar las PCS ya que el modelo local puede ser pesado, recomendado fp16. La idea es que si se detecta en la flag del modelo de embedding que se
  usa alguno de estos 2, se alterne el metodo de embedding para usarlo directamente. A la par, necesito unas mejoras en @saneamiento/sanear.py , haciendo que el script SI no encuentra la
  carpeta /data/, la cree. Lo mismo para el archivo de registry.json. Inlcuir tambien el flag --refresh, que borra la carpeta /data/ completamente, y la carpeta /output/.
