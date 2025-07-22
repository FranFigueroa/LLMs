from langchain.agents import initialize_agent, Tool, AgentType
from langchain.llms import HuggingFaceHub
from langchain.tools import DuckDuckGoSearchRun

# Configurar el LLM
llm = HuggingFaceHub(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    model_kwargs={"temperature": 0.5, "max_length": 256}
)

# Definir herramienta de búsqueda web
search = DuckDuckGoSearchRun()
tools = [
    Tool(
        name="DuckDuckGo Search",
        func=search.run,
        description="Busca información en la web usando DuckDuckGo"
    )
]

# Inicializar el agente con la herramienta y el LLM
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

    # Prueba
    if __name__ == "__main__":
        pregunta = "¿Quién escribió el paper Attention is All You Need?"
        respuesta = agent.run(pregunta)
        print("Pregunta:", pregunta)
        print("Respuesta:", respuesta) 