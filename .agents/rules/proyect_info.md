---
trigger: always_on
---

Propósito General
Implementar un sistema RAG (Retrieval-Augmented Generation) con LangChain que responda preguntas basadas en un conjunto documental específico y acotado. El objetivo no es solo hacer que "funcione", sino demostrar criterio técnico, trazabilidad de fuentes y reconocimiento honesto de límites.

Dominio del Trabajo
El sistema está dividido en 3 módulos interdependientes:

Limpieza: Saneamiento de documentos, conversión a formato TOON, cálculo SHA256 para evitar duplicados
Carga: Chunking, generación de embeddings, persistencia en Chroma, actualización de metadata
Recuperación: Interfaz con el usuario final, retrieval configurable, invocación del LLM