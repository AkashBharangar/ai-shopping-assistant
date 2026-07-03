import streamlit as st

from services.product_compare import compare_products


def render_comparison_tab(products):

    st.subheader("⚖ Product Comparison")

    selected = []

    for index, product in enumerate(products):

        if st.checkbox(
            product["title"],
            key=f"comparison_{index}"
        ):
            selected.append(product)

    if len(selected) < 2:

        st.info(
            "Select at least two products."
        )

        return

    if st.button(
        "Compare Products",
        use_container_width=True
    ):

        with st.spinner("Comparing..."):

            result = compare_products(selected)

        st.success(result["summary"])

        st.markdown(
            f"## 🏆 {result['winner']}"
        )

        cols = st.columns(len(result["comparison"]))

        for col, item in zip(cols, result["comparison"]):

            with col:

                st.markdown(
                    f"### {item['product']}"
                )

                st.write("#### ✅ Strengths")

                for strength in item["strengths"]:

                    st.write(
                        "•",
                        strength
                    )

                st.write("#### ❌ Weaknesses")

                for weakness in item["weaknesses"]:

                    st.write(
                        "•",
                        weakness
                    )