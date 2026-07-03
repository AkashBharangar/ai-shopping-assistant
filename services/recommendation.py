import json

from chains import create_json_chain

from prompts import (
    SYSTEM_PROMPT,
    RECOMMENDATION_PROMPT
)

chain = create_json_chain(
    RECOMMENDATION_PROMPT
)


def recommend_product(
    user_profile: str,
    products: list
):
    """
    Recommend the best product for a user.
    """

    return chain.invoke(
        {
            "system_prompt": SYSTEM_PROMPT,
            "user_profile": user_profile,
            "products": json.dumps(
                products,
                indent=2
            )
        }
    )