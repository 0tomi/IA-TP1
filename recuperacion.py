import argparse
import sys
import os
from dotenv import load_dotenv

# Importar de nuestros modulos propios
from carga import CargaConfig, construir_embeddings, COLLECTION_NAME, DATA_DIR
from saneamiento.sanear import main as sanear_main

# LangChain
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI

def parsear_y_ejecutar_saneamiento(args, original_argv):
    """
    Simula los argumentos como si se llamase a sanear.py directamente desde la linea de comandos 
    para poder re-utilizar su parseador interno sin colisiones.
    """
    sanear_argv = [sys.argv[0]]
    sanear_argv.extend(["--chunk-size", str(args.chunk_size)])
    sanear_argv.extend(["--chunk-overlap", str(args.chunk_overlap)])
    sanear_argv.extend(["--embedding-model", str(args.embedding_model)])
    sanear_argv.extend(["--embedding-batch-size", str(args.embedding_batch_size)])
    sanear_argv.extend(["--max-retries", str(args.max_retries)])
    sanear_argv.extend(["--retry-wait-seconds", str(args.retry_wait_seconds)])
    sanear_argv.extend(["--chunking-technique", str(args.chunking_technique)])
    
    if args.refresh:
        sanear_argv.append("--refresh")
        
    # Reemplazamos temporalmente sys.argv
    sys.argv = sanear_argv
    try:
        print("\n=== INICIANDO PROCESO DE SANEAMIENTO Y CARGA ===")
        sanear_main()
        print("=== FIN DEL PROCESO DE SANEAMIENTO Y CARGA ===\n")
    except Exception as e:
        print(f"[ERROR] Falló el proceso de saneamiento previo: {e}")
    finally:
        sys.argv = original_argv

def main():
    load_dotenv()
    
    parser = argparse.ArgumentParser(description="Chatbot de Recuperación y Consulta con RAG usando Chroma y Gemini.")
    
    # -- Argumentos propios del Chatbot RAG --
    parser.add_argument("--top-k", type=int, default=5, help="Cantidad de chunks devengados de la búsqueda vectorial (default 5)")
    parser.add_argument("--retrieval-type", type=str, choices=["similarity_search", "mmr", "threshold"], default="similarity_search", help="Tipo de búsqueda a usar para recuperar documentos")
    parser.add_argument("--threshold", type=float, default=0.5, help="Similitud mínima requerida (0.0-1.0). Solo aplica si retrieval-type es 'threshold'. Default 0.5")
    parser.add_argument("--max-context-chunks", type=int, default=5, help="Máxima cantidad de chunks efectivamente inyectados al contexto del LLM (default 5)")
    parser.add_argument("--temperatura", type=float, default=0.7, help="Temperatura del modelo generativo (0.0 a 2.0) default 0.7")
    parser.add_argument("--debug", action="store_true", help="Muestra los chunks recuperados en consola antes de la respuesta.")
    
    # -- Argumentos trasladados para Saneamiento y Carga --
    parser.add_argument("--chunk-size", type=int, default=512)
    parser.add_argument("--chunk-overlap", type=int, default=50)
    parser.add_argument("--embedding-model", type=str, default="gemini-embedding-001", help="Modelo de embedding para generar e instanciar en Chroma (default: gemini-embedding-001)")
    parser.add_argument("--embedding-batch-size", type=int, default=20)
    parser.add_argument("--max-retries", type=int, default=3)
    parser.add_argument("--retry-wait-seconds", type=int, default=60)
    parser.add_argument("--chunking-technique", type=str, choices=["recursive", "fixed_size_overlap", "paragraph_custom"], default="recursive")
    parser.add_argument("--refresh", action="store_true", help="Fuerza un re-procesamiento de todo el corpus en sanear.py")
    
    original_argv = sys.argv.copy()
    args = parser.parse_args()
    
    if not os.environ.get("GOOGLE_API_KEY"):
        print("[ERROR] GOOGLE_API_KEY no se encontró en el entorno. Por favor verifica tu .env")
        sys.exit(1)
        
    # Paso 1: Llamar al pipeline de saneamiento (orquestación)
    parsear_y_ejecutar_saneamiento(args, original_argv)
    
    # Paso 2: Configurar DB Local Local
    print("[RAG] Inicializando Base de Datos Vectorial Chroma...")
    carga_config = CargaConfig(embedding_model=args.embedding_model)
    embeddings = construir_embeddings(carga_config)
    
    vectorstore = Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=str(DATA_DIR),
        embedding_function=embeddings
    )
    
    # Paso 3: Configurar Retriever
    search_kwargs = {"k": args.top_k}
    search_type = "similarity"
    
    if args.retrieval_type == "mmr":
        search_type = "mmr"
    elif args.retrieval_type == "threshold":
        search_type = "similarity_score_threshold"
        search_kwargs["score_threshold"] = args.threshold
        
    retriever = vectorstore.as_retriever(
        search_type=search_type,
        search_kwargs=search_kwargs
    )
    
    # Paso 4: Configurar LLM Principal
    print("[RAG] Inicializando Modelo LLM (gemini-3.1-flash-lite-preview)...")
    llm = ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite-preview",
        temperature=args.temperatura,
        max_retries=2
    )
    
    print("\n" + "="*55)
    print(" 🤖 Asistente RAG Listo (Escribe 'salir', 'exit' o 'quit' para terminar)")
    print("="*55 + "\n")
    
    # Paso 5: Chat Loop
    while True:
        try:
            query = input("\nUsuario> ").strip()
            if not query:
                continue
            if query.lower() in ['salir', 'exit', 'quit']:
                print("Agente> ¡Hasta luego!")
                break
                
            # Recuperar documentos
            docs = retriever.invoke(query)
            
            # Restringir a max_context_chunks
            docs_contexto = docs[:args.max_context_chunks]
            
            if args.debug:
                print(f"\n[DEBUG] --- Chunks Obtenidos ({len(docs_contexto)} permitidos de {len(docs)} encontrados) ---")
                for i, doc in enumerate(docs_contexto):
                    meta = doc.metadata
                    src = meta.get('documento', 'Oculto')
                    sec = meta.get('seccion', 'Sin seccion')
                    print(f"  [{i+1}] {src} | Seccion: {sec}")
                    print(f"      Texto: {doc.page_content[:150]}...\n")
                print("[DEBUG] -------------------------------------")

            if not docs_contexto:
                print("Agente> No he podido encontrar información relevante en mis documentos para responder a esa consulta.")
                continue
                
            # Construir bloque de contexto
            bloques_texto = []
            for d in docs_contexto:
                meta = d.metadata
                bloques_texto.append(
                    f"Documento: {meta.get('documento', '?')}\n"
                    f"Sección: {meta.get('seccion', '?')}\n"
                    f"Contenido:\n{d.page_content}"
                )
            contexto_str = "\n\n---\n\n".join(bloques_texto)
            
            # Prompt Estricto
            prompt = f"""Eres un asistente diseñado estrictamente para responder a preguntas basándote ÚNICAMENTE en la información proporcionada en el Contexto a continuación.
Si no puedes responder la pregunta del usuario utilizando exclusivamente la información del Contexto, debes indicar claramente "No dispongo de información en mis documentos para responder esta consulta." NO inventes respuestas, ni uses conocimientos externos bajo ninguna circunstancia.

### CONTEXTO ###
{contexto_str}

### PREGUNTA DEL USUARIO ###
{query}
"""
            # Ejecutar LLM
            response = llm.invoke(prompt)
            print(f"\nAgente> {response.content}")
            
            # Extraer e imprimir Tokens
            if hasattr(response, "usage_metadata") and response.usage_metadata is not None:
                usage = response.usage_metadata
                prompt_tokens = usage.get('prompt_token_count', 0)
                completion_tokens = usage.get('candidates_token_count', 0)
                total_tokens = usage.get('total_token_count', 0)
                print(f"\n[Metadatos de Consumo] Tokens de entrada: {prompt_tokens} | Tokens de salida: {completion_tokens} | Total usados: {total_tokens}")
            else:
                print("\n[Metadatos de Consumo] No se detectaron estadísticas de consumo (tokens).")
                
        except KeyboardInterrupt:
            print("\nAgente> ¡Hasta luego!")
            break
        except Exception as e:
            print(f"\n[ERROR EN CADENA] -> {e}")

if __name__ == "__main__":
    main()
