import json

from chains import create_json_chain

from prompts import (
    SYSTEM_PROMPT,
    COMPARISON_PROMPT
)

chain = create_json_chain(COMPARISON_PROMPT)


def compare_products(products: list):
    """
    Compare multiple products using the LLM.
    """

    return chain.invoke(
        {
            "system_prompt": SYSTEM_PROMPT,
            "products": json.dumps(products, indent=2)
        }
    )