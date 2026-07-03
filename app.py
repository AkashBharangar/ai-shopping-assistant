import streamlit as st

from ui.sidebar import render_sidebar
from ui.product_card import render_product_cards
from ui.assistant_mode import render_assistant_mode

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

    render_assistant_mode()