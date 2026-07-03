import streamlit as st

from services.shopping_pipeline import shopping_pipeline


def render_assistant_mode():
    """
    End-to-end AI Shopping Assistant.
    """

    st.header("🤖 AI Shopping Assistant")

    query = st.text_input(
        "🔍 What product are you looking for?",
        placeholder="Example: Gaming Laptop"
    )

    profile = st.text_area(
        "Tell AI about yourself",
        placeholder="""
Example:

• College Student
• Budget ₹80,000
• Programming
• Gaming
• Good Battery
"""
    )

    if st.button(
        "Ask AI Assistant",
        use_container_width=True
    ):

        if not query.strip():

            st.warning("Please enter a product.")

            return

        with st.spinner("AI is analyzing products..."):

            result = shopping_pipeline(
                query=query,
                user_profile=profile
            )

        if result is None:

            st.error("No products found.")

            return

        recommendation = result["recommendation"]
        comparison = result["comparison"]
        products = result["products"]

        st.success(
            f"🏆 Recommended Product: {recommendation['recommended_product']}"
        )

        st.metric(
            "Confidence",
            f"{recommendation['confidence']}%"
        )

        st.markdown("### 💡 Why this product?")

        st.write(recommendation["reason"])

        st.divider()

        st.markdown("### 📊 Comparison Summary")

        st.info(comparison["summary"])

        st.write(f"**Winner:** {comparison['winner']}")

        st.divider()

        st.markdown("### 🛍 Products Considered")

        cols = st.columns(len(products))

        for col, product in zip(cols, products):

            with col:

                st.image(
                    product["thumbnail"],
                    use_container_width=True
                )

                st.markdown(
                    f"**{product['title']}**"
                )

                st.caption(product["brand"])

                st.metric(
                    "Price",
                    f"${product['price']}"
                )

                st.metric(
                    "Rating",
                    product["rating"]
                )

                review = product.get("review_analysis")

                if review:

                    with st.expander("Review Analysis"):

                        st.write(review["summary"])

                        st.markdown("**Pros**")

                        for pro in review["pros"]:
                            st.write("✅", pro)

                        st.markdown("**Cons**")

                        for con in review["cons"]:
                            st.write("❌", con)

                        st.info(
                            review["sentiment"]
                        )