from langchain_community.llms import HuggingFaceHub
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate

# Configurar el LLM
llm = HuggingFaceHub(
    repo_id="google/flan-t5-small",
    model_kwargs={"temperature":0.7, "max_length":256},
    huggingfacehub_api_token="TU_TOKEN_AQUI"  # Reemplaza por tu token
)

# Crear el template de prompt personalizado
template = """La siguiente es una conversación amigable entre un Humano y una IA. 
La IA es útil, creativa, inteligente y muy amigable.

Conversación actual:
{history}
Humano: {input}
IA:"""

prompt = PromptTemplate(
    input_variables=["history", "input"],
    template=template
)

# Configurar la memoria de conversación
memory = ConversationBufferMemory(human_prefix="Humano", ai_prefix="IA")

# Crear la cadena de conversación con memoria
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    prompt=prompt,
    verbose=True
)

# Función para chatear
def chat_with_bot(message):
    """Función para interactuar con el chatbot."""
    response = conversation.predict(input=message)
    return response

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplos de conversación
    print("=== Chatbot con Memoria ===")
    print("Escribe 'salir' para terminar la conversación\n")
    
    # Primera pregunta
    pregunta1 = "Hola, ¿cómo te llamas?"
    print(f"Usuario: {pregunta1}")
    respuesta1 = chat_with_bot(pregunta1)
    print(f"Bot: {respuesta1}\n")
    
    # Segunda pregunta (el bot debería recordar el contexto)
    pregunta2 = "¿Te acuerdas de mi nombre?"
    print(f"Usuario: {pregunta2}")
    respuesta2 = chat_with_bot(pregunta2)
    print(f"Bot: {respuesta2}\n")
    
    # Tercera pregunta
    pregunta3 = "¿Qué te gusta hacer?"
    print(f"Usuario: {pregunta3}")
    respuesta3 = chat_with_bot(pregunta3)
    print(f"Bot: {respuesta3}\n")
    
    # Mostrar el historial completo
    print("=== Historial de la conversación ===")
    print(memory.buffer) 