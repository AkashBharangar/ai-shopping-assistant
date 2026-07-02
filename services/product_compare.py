import json

from llm import invoke_llm
from prompts import COMPARISON_PROMPT


def compare_products(products):

    prompt = COMPARISON_PROMPT.format(
        products=json.dumps(products, indent=2)
    )

    return invoke_llm(
        system_prompt="You are an expert shopping assistant.",
        user_prompt=prompt
    )