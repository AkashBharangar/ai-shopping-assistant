from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

from config import GROQ_API_KEY, MODEL_NAME


llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name=MODEL_NAME,
    temperature=0.2
)


def invoke_llm(system_prompt: str, user_prompt: str):
    """
    Sends a prompt to the LLM and returns the response text.
    """

    try:
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ]

        response = llm.invoke(messages)

        return response.content

    except Exception as e:
        return f"Error: {e}"