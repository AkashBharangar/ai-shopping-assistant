from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

from llm import llm


def create_json_chain(prompt_template: str):
    """
    Creates a LangChain pipeline:

    Prompt
        ↓
    Groq LLM
        ↓
    JSON Parser
    """

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "{system_prompt}"),
            ("human", prompt_template)
        ]
    )

    parser = JsonOutputParser()

    chain = prompt | llm | parser

    return chain