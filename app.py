import streamlit as st

from services.product_search import search_products
from services.product_compare import compare_products

st.set_page_config(
    page_title="AI Shopping Assistant",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 AI Shopping Assistant")

query = st.text_input("Search for products")

if st.button("Search"):

    products = search_products(query)

    if not products:
        st.warning("No products found.")

    else:

        st.session_state["products"] = products

if "products" in st.session_state:

    st.subheader("Search Results")

    products = st.session_state["products"]

    selected = []

    for index, product in enumerate(products):

        if st.checkbox(product["title"], key=index):

            selected.append(product)

    if len(selected) >= 2:

        if st.button("Compare Selected Products"):

            with st.spinner("Comparing..."):

                result = compare_products(selected)

            st.markdown(result)

    elif len(selected) == 1:

        st.info("Select one more product.")

    else:

        st.info("Select at least two products.")