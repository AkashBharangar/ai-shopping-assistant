import json
from pathlib import Path

from chains import create_json_chain

from prompts import (
    SYSTEM_PROMPT,
    REVIEW_SUMMARY_PROMPT
)

REVIEWS_FILE = Path("data/reviews.json")

chain = create_json_chain(REVIEW_SUMMARY_PROMPT)


def load_reviews(product_name: str):
    """
    Load reviews for a product from the local dataset.
    """

    try:

        with open(
            REVIEWS_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        return data.get(product_name, [])

    except FileNotFoundError:

        print("reviews.json not found.")

        return []

    except json.JSONDecodeError:

        print("Invalid reviews.json.")

        return []


def summarize_reviews(product_name: str):
    """
    Generate an AI summary for customer reviews.
    """

    reviews = load_reviews(product_name)

    if not reviews:
        return None

    try:

        return chain.invoke(
            {
                "system_prompt": SYSTEM_PROMPT,
                "reviews": json.dumps(
                    reviews,
                    indent=2
                )
            }
        )

    except Exception as e:

        print(e)

        return None


def enrich_products_with_reviews(products: list):
    """
    Adds review analysis to every product.
    """

    enriched_products = []

    for product in products:

        enriched_product = product.copy()

        enriched_product["review_analysis"] = summarize_reviews(
            product["title"]
        )

        enriched_products.append(
            enriched_product
        )

    return enriched_products