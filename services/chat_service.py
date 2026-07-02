from llm import invoke_llm
from prompts import SYSTEM_PROMPT


def chat(question: str):
    return invoke_llm(
        SYSTEM_PROMPT,
        question
    )