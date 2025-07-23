from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langchain_community.llms import HuggingFaceHub
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
import operator

# Definir el estado del grafo
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    next: str

# Configurar el LLM
llm = HuggingFaceHub(
    repo_id="google/flan-t5-small",
    model_kwargs={"temperature":0.5, "max_length":128},
    huggingfacehub_api_token="TU_TOKEN_AQUI"  
)

# Definir herramientas
search = DuckDuckGoSearchRun()

@tool
def search_web(query: str) -> str:
    """Busca información en la web usando DuckDuckGo."""
    return search.run(query)

tools = [search_web]

# Crear nodos del grafo
def should_continue(state: AgentState) -> str:
    """Determina si el agente debe continuar o terminar."""
    messages = state["messages"]
    last_message = messages[-1]
    
    # Si es un mensaje del usuario, continuar
    if isinstance(last_message, HumanMessage):
        return "agent"
    
    # Si es un mensaje de la IA, terminar
    return END

def call_model(state: AgentState) -> AgentState:
    """Llama al modelo de lenguaje."""
    messages = state["messages"]
    response = llm.invoke(messages)
    return {"messages": [response]}

# Crear el grafo
workflow = StateGraph(AgentState)

# Agregar nodos
workflow.add_node("agent", call_model)

# Agregar edges
workflow.set_entry_point("agent")
workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "agent": "agent",
        END: END
    }
)

# Compilar el grafo
app = workflow.compile()

# Ejemplo de uso
if __name__ == "__main__":
    # Ejecutar el grafo
    result = app.invoke({
        "messages": [HumanMessage(content="¿Quién escribió el paper Attention is All You Need?")]
    })
    
    print("Respuesta:", result["messages"][-1].content) 