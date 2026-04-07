# Prompts Utilizados - Modulo de Saneamiento

---

**Prompt 0**

> Tengo que armar un script en Python para sanear PDFs para un TP de RAG. No quiero que sea un bloque de codigo gigante e inmanejable. Como me conviene seccionarlo o modularizarlo? La idea es que despues pueda escalar a muchos archivos y que sea facil de entender separar la extraccion, la limpieza y el registro de que cosas ya procese.

---

**Prompt 1**

> tengo un script que lee pdfs con pypdf y extrae el texto, pero el problema es que el texto sale con saltos de linea al final de cada renglon del pdf y palabras pegadas tipo "HolaMundo". como limpio eso con regex sin romper siglas ni terminos tecnicos?

---

**Prompt 2**

> necesito reemplazar caracteres unicode raros que mete pypdf al leer pdfs, como ligaduras tipograficas (fi, fl) y guiones especiales. dame una tabla de reemplazos y como aplicarla en python

---

**Prompt 3**

> tengo varios pdfs en una carpeta y subcarpetas. quiero procesarlos todos de forma recursiva pero sin reprocesar los que ya procese antes. como implemento un cache usando sha256 para saber si el archivo cambio o no?

---

**Prompt 4**

> en vez de guardar todo el texto saneado en un solo archivo, quiero generar un archivo separado por cada pdf con sus metadatos incorporados (nombre, sha256, paginas, chars). que formato liviano me recomendas para que sea eficiente en tokens cuando se lo mando a un llm?

---

**Prompt 5**

> como guardo rutas de archivos en un json de forma que sean relativas al proyecto y funcionen en cualquier sistema operativo, ya sea windows o linux?

---

**Prompt 6**

> perdon, me tira error el script porque me dice que el texto es NoneType en algunas paginas de ciertos pdfs y se me clava todo el proceso. como puedo hacer para que el script siga de largo si una pagina viene vacia?
