import streamlit as st

from ui.sidebar import render_sidebar
from ui.product_card import render_product_cards

from services.product_search import search_products
from services.shopping_pipeline import shopping_pipeline

st.set_page_config(
    page_title="AI Shopping Assistant",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

mode = render_sidebar()

st.title("🛒 AI Shopping Assistant")
st.caption(
    "Compare products, analyze reviews and get AI-powered recommendations."
)

# Initialize products safely
products = st.session_state.get("products", [])

# =====================================================
# Developer Mode
# =====================================================

if mode == "Developer Mode":

    query = st.text_input(
        "🔍 Search Products",
        placeholder="Example: phone, laptop, perfume..."
    )

    if st.button("Search", use_container_width=True):

        if query.strip():

            products = search_products(query)

            if products:
                st.session_state["products"] = products
            else:
                st.warning("No products found.")
                st.session_state.pop("products", None)

        else:
            st.warning("Please enter a search query.")

    products = st.session_state.get("products", [])

    if products:

        st.divider()

        render_product_cards(products)

        st.divider()

        comparison_tab, review_tab, recommendation_tab = st.tabs(
            [
                "⚖ Comparison",
                "📝 Reviews",
                "🤖 Recommendation"
            ]
        )

        with comparison_tab:
            from ui.comparison_tab import render_comparison_tab
            render_comparison_tab(products)

        with review_tab:
            from ui.review_tab import render_review_tab
            render_review_tab(products)

        with recommendation_tab:
            from ui.recommendation_tab import render_recommendation_tab
            render_recommendation_tab(products)

# =====================================================
# Assistant Mode
# =====================================================

else:

    st.subheader("🤖 AI Shopping Assistant")

    query = st.text_input(
        "Product",
        placeholder="Gaming Laptop"
    )

    profile = st.text_area(
        "Tell AI about yourself",
        placeholder="College student, budget ₹80k..."
    )

    if st.button("Ask Assistant", use_container_width=True):

        with st.spinner("Thinking..."):

            result = shopping_pipeline(
                query,
                profile
            )

        if result is None:

            st.warning("No matching products found.")

        else:

            recommendation = result["recommendation"]
            comparison = result["comparison"]

            st.success(
                recommendation["recommended_product"]
            )

            st.write(
                recommendation["reason"]
            )

            st.progress(
                recommendation["confidence"] / 100
            )

            st.caption(
                f"Confidence: {recommendation['confidence']}%"
            )

            st.divider()

            st.subheader("Comparison Summary")

            st.write(
                comparison["summary"]
            )