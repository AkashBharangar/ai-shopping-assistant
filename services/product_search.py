import requests

BASE_URL = "https://dummyjson.com/products"


def search_products(query: str, limit: int = 5):
    """
    Search products using DummyJSON API.
    Returns a list of normalized product dictionaries.
    """

    try:
        response = requests.get(
            f"{BASE_URL}/search",
            params={
                "q": query
            },
            timeout=10
        )

        response.raise_for_status()

        products = response.json()["products"]

        normalized_products = []

        for product in products[:limit]:

            normalized_products.append(
                {
                    "title": product["title"],
                    "brand": product["brand"],
                    "price": product["price"],
                    "rating": product["rating"],
                    "category": product["category"],
                    "description": product["description"],
                    "thumbnail": product["thumbnail"],
                }
            )

        return normalized_products

    except Exception as e:

        print(e)

        return []