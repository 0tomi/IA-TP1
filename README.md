# IA-TP1: Sistema RAG (LangChain)

Este es un sistema **RAG (Retrieval-Augmented Generation)** diseñado para responder consultas precisas sobre los **planes de estudio y programas de cátedra** de diversas materias de la carrera para CUARTO Año.

> [!IMPORTANT]
> El sistema utiliza el corpus documental en `./corpus/` para extraer información verídica y evitar alucinaciones, permitiendo consultar objetivos, contenidos, bibliografía y metodologías de evaluación de cada asignatura de forma precisa.

---

## Requisitos Previos e Instalación

Este proyecto utiliza **Poetry** para la gestión de dependencias. Si no lo tenés instalado, podés seguir las instrucciones en la [página oficial de Poetry](https://python-poetry.org/docs/).

Para instalar las dependencias básicas del proyecto, ejecutá:

```bash
poetry install
```

### Soporte opcional para Ollama

Si querés utilizar modelos locales con Ollama (por ejemplo, Llama 3.1), instalá las dependencias opcionales:

```bash
poetry install -E ollama
ollama pull llama3.1
```
*(Nota: Ollama debe estar instalado en tu sistema y en ejecución al momento de usarlo).*

---

## Uso del Sistema RAG (Backend)

Existen dos scripts principales para probar y utilizar el RAG. Ambos se ejecutan a través de Poetry:

1. **Recuperación (Interfaz por consola)**
   Despliega una interfaz interactiva por consola para realizar consultas al sistema RAG.
   ```bash
   poetry run python3 recuperacion.py
   ```

2. **Evaluación (Tests automáticos)**
   Script destinado a ejecutar pruebas automáticas de rendimiento y precisión del sistema RAG.
   ```bash
   poetry run python3 evaluacion.py
   ```

---

## Interfaz Web (Frontend)

Para probar la versión web del sistema RAG, es necesario cambiar de rama e iniciar el entorno de desarrollo de Node:

1. Cambiá a la rama del frontend:
   ```bash
   git checkout FrontendFastAPI
   ```
2. Instalá las dependencias:
   ```bash
   npm install
   ```
3. Ejecutá la página web en local:
   ```bash
   npm run dev
   ```