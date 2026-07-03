from services.product_search import search_products
from services.review_summarizer import enrich_products_with_reviews
from services.product_compare import compare_products
from services.recommendation import recommend_product


def shopping_pipeline(query: str, user_profile: str):
    """
    End-to-end shopping workflow.

    Search
        ↓
    Review Analysis
        ↓
    Product Comparison
        ↓
    Recommendation
    """

    products = search_products(query)

    if not products:
        return None

    enriched_products = enrich_products_with_reviews(
        products
    )

    comparison = compare_products(
        enriched_products
    )

    recommendation = recommend_product(
        user_profile,
        enriched_products
    )

    return {
        "products": enriched_products,
        "comparison": comparison,
        "recommendation": recommendation
    }