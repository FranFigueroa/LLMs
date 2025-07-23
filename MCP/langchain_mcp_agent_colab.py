from langchain.agents import initialize_agent, Tool
from langchain.llms import HuggingFaceHub
from langchain.tools import SerpAPIWrapper
from langchain.schema import AgentType

# Configurar el LLM (puedes usar tu propio modelo o uno de HuggingFace)
llm = HuggingFaceHub(
    repo_id="google/flan-t5-small",
    model_kwargs={"temperature":0.5, "max_length":128},
    huggingfacehub_api_token="TU_TOKEN_AQUI"  # Reemplaza por tu token
)

# Definir una herramienta MCP (SerpAPI)
search = SerpAPIWrapper(serpapi_api_key="TU_SERPAPI_KEY_AQUI")
tools = [
    Tool(
        name="SerpAPI Search",
        func=search.run,
        description="Busca información en la web usando SerpAPI"
    )
]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

if __name__ == "__main__":
    pregunta = "¿Quién ganó el premio Turing en 2017?"
    respuesta = agent.run(pregunta)
    print("Pregunta:", pregunta)
    print("Respuesta:", respuesta) 