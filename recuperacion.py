import os
import argparse
from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv

from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
COLLECTION_NAME = "rag_tp1"

@dataclass
class RecuperacionConfig:
    top_k: int = 5
    retrieval_type: str = "similarity_search" # "similarity_search" | "mmr" | "threshold"
    threshold: float = 0.5
    max_context_chunks: int = 10
    temperatura: float = 0.7
    dominio: str = "la documentación provista"
    modelo_llm: str = "gemini-flash-latest"


def format_docs(docs) -> str:
    # Formatea los documentos para el contexto del LLM y transparencia
    contexto = []
    for i, doc in enumerate(docs):
        materia = doc.metadata.get('materia', 'Sin clasificar')
        titulo = doc.metadata.get('seccion', 'Sin título')
        documento = doc.metadata.get('documento', 'Documento desconocido')
        
        chunk_text = (
            f"--- FUENTE [{i+1}] ---\n"
            f"Documento: {documento}\n"
            f"Sección: {materia} - {titulo}\n"
            f"Contenido:\n{doc.page_content}\n"
        )
        contexto.append(chunk_text)
    return "\n".join(contexto)


def main():
    parser = argparse.ArgumentParser(description="Chat de Recuperación RAG")
    parser.add_argument("--top_k", type=int, default=5, help="Cantidad de chunks a recuperar")
    parser.add_argument("--retrieval_type", type=str, choices=["similarity_search", "mmr", "threshold"], default="similarity_search")
    parser.add_argument("--threshold", type=float, default=0.5, help="Similitud mínima requerida (0.0-1.0)")
    parser.add_argument("--max_context_chunks", type=int, default=10, help="Máximo de chunks en contexto")
    parser.add_argument("--temperatura", type=float, default=0.7, help="Creatividad del modelo (0.0-2.0)")
    parser.add_argument("--dominio", type=str, default="la documentación académica e indexada", help="Dominio para el prompt")
    parser.add_argument("--modelo", type=str, default="gemini-flash-latest", help="Modelo de LLM a usar")

    args = parser.parse_args()
    config = RecuperacionConfig(
        top_k=args.top_k,
        retrieval_type=args.retrieval_type,
        threshold=args.threshold,
        max_context_chunks=args.max_context_chunks,
        temperatura=args.temperatura,
        dominio=args.dominio,
        modelo_llm=args.modelo
    )

    if not os.environ.get("GOOGLE_API_KEY"):
        print("Error: No se encontró GOOGLE_API_KEY en el entorno.")
        return

    print("Inicializando Base de Datos Vectorial...")
    embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
    vectorstore = Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=str(DATA_DIR),
        embedding_function=embeddings,
    )

    print("Inicializando LLM...")
    llm = ChatGoogleGenerativeAI(
        model=config.modelo_llm,
        temperature=config.temperatura
    )

    system_prompt = (
        "Eres un asistente especializado en {dominio}. Tu objetivo es responder preguntas "
        "basándote únicamente en la información proporcionada en el contexto.\n\n"
        "REGLAS OBLIGATORIAS:\n"
        "1. Si el contexto no contiene información suficiente para responder, debes indicar claramente: "
        "'No encuentro evidencia suficiente en el contexto para responder esta pregunta'.\n"
        "2. Evita especular o usar conocimiento general del modelo. Si encuentras información parcial, "
        "especifica qué datos están disponibles y qué información está faltando.\n"
        "3. Transparencia: Debes indicar siempre de dónde sacaste la información usando el formato: "
        "'Esta información proviene de [documento], sección [sección]'. Y si aplica, usar la fecha contenida.\n"
        "4. Acknowledging uncertainty: Si la respuesta no es exhaustiva o exacta, emplea frases como: "
        "'Según los documentos disponibles, [respuesta], pero no tengo información sobre [aspecto no cubierto]'.\n\n"
        "CONTEXTO DISPONIBLE:\n"
        "{context}"
    )
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{question}")
    ])

    chain = prompt_template | llm

    print("\n" + "="*50)
    print("🤖 CHAT RAG INICIADO")
    print("="*50)
    print(f"Parámetros: retrieval={config.retrieval_type}, top_k={config.top_k}, temp={config.temperatura}")
    print("Escribe 'salir' o 'exit' para terminar.\n")

    while True:
        try:
            query = input("\n👤 Tú: ")
            if not query.strip():
                continue
            if query.lower() in ["salir", "exit", "quit"]:
                break
                
            # Recuperación (Retrieval)
            retrieved_docs = []
            if config.retrieval_type == "similarity_search":
                retrieved_docs = vectorstore.similarity_search(query, k=config.top_k)
            elif config.retrieval_type == "mmr":
                retrieved_docs = vectorstore.max_marginal_relevance_search(query, k=config.top_k)
            elif config.retrieval_type == "threshold":
                # similarity_search_with_relevance_scores da una tupla (doc, score)
                doc_scores = vectorstore.similarity_search_with_relevance_scores(query, k=config.top_k)
                retrieved_docs = [doc for doc, score in doc_scores if score >= config.threshold]

            # Recorte por max_context_chunks (Punto 5 del flujo)
            retrieved_docs = retrieved_docs[:config.max_context_chunks]

            # Formateamos el contexto (Punto 6 del flujo)
            context = format_docs(retrieved_docs)

            print("\n🤖 Sistema:")
            # Invocación LLM (Punto 7 del flujo)
            response = chain.invoke({
                "dominio": config.dominio,
                "context": context,
                "question": query
            })
            
            # Generación de respuesta (Punto 8)
            respuesta = response.content
            if isinstance(respuesta, list):
                # Extraemos el texto si LangChain nos devuelve el dict en crudo
                text_blocks = [blk.get("text", "") if isinstance(blk, dict) else str(blk) for blk in respuesta]
                respuesta = "".join(text_blocks)
                
            print(f"{respuesta}\n")
            
            # Imprimimos información de recuperación para debugging/trazabilidad técnica
            print("-" * 50)
            print(f"Fuentes consultadas ({len(retrieved_docs)} chunks):")
            for i, doc in enumerate(retrieved_docs):
                doc_name = doc.metadata.get('documento', 'N/A')
                print(f" - [{i+1}] {doc_name} (Sección: {doc.metadata.get('seccion', 'N/A')})")
            print("-" * 50)

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error procesando la consulta: {e}")

    print("\n¡Adiós!")

if __name__ == "__main__":
    main()
