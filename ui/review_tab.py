import streamlit as st

from services.review_summarizer import summarize_reviews


def render_review_tab(products):

    st.subheader("📝 Review Analysis")

    selected_product = st.selectbox(

        "Select Product",

        [

            product["title"]

            for product in products

        ]

    )

    if st.button(

        "Analyze Reviews",

        use_container_width=True

    ):

        with st.spinner("Reading reviews..."):

            result = summarize_reviews(
                selected_product
            )

        if result is None:

            st.warning(
                "No reviews found."
            )

            return

        st.success(result["summary"])

        col1, col2 = st.columns(2)

        with col1:

            st.markdown("### ✅ Pros")

            for pro in result["pros"]:

                st.write(
                    "•",
                    pro
                )

        with col2:

            st.markdown("### ❌ Cons")

            for con in result["cons"]:

                st.write(
                    "•",
                    con
                )

        st.info(

            f"Overall Sentiment: {result['sentiment']}"

        )