import requests
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline


# Extraer texto del PDF
reader = PdfReader(pdf_path)
full_text = ""
for page in reader.pages:
    full_text += page.extract_text() + "\n"

# Dividir el texto en fragmentos (chunks)
def chunk_text(text, max_length=500):
    words = text.split()
    chunks = []
    for i in range(0, len(words), max_length):
        chunk = " ".join(words[i:i+max_length])
        chunks.append(chunk)
    return chunks

chunks = chunk_text(full_text, max_length=200)

# Crear embeddings y el índice FAISS
embedder = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = embedder.encode(chunks, show_progress_bar=True)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

# Función de recuperación de contexto
def retrieve_context(query, k=3):
    query_emb = embedder.encode([query])
    D, I = index.search(np.array(query_emb), k)
    return [chunks[i] for i in I[0]]

# Cargar Llama 3 desde HuggingFace
llama_model = "meta-llama/Meta-Llama-3-8B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(llama_model)
model = AutoModelForCausalLM.from_pretrained(llama_model, torch_dtype="auto", device_map="auto")
llama_pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=256)

# Función RAG: Recupera contexto y genera respuesta
def rag_ask(question):
    context = retrieve_context(question, k=3)
    prompt = (
        "Contexto relevante extraído del paper:\n"
        + "\n\n".join(context)
        + f"\n\nPregunta: {question}\nRespuesta:"
    )
    result = llama_pipe(prompt)
    return result[0]['generated_text'][len(prompt):]

# Prueba
if __name__ == "__main__":
    pregunta = "¿Qué es el mecanismo de atención en transformers?"
    respuesta = rag_ask(pregunta)
    print("Pregunta:", pregunta)
    print("Respuesta:", respuesta) 