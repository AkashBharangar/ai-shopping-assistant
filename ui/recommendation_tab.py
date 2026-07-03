import streamlit as st

from services.recommendation import recommend_product


def render_recommendation_tab(products):

    st.subheader(
        "🤖 AI Recommendation"
    )

    profile = st.text_area(

        "Describe yourself",

        placeholder="""
College Student

Budget ₹80,000

Programming

Gaming
"""
    )

    if st.button(

        "Generate Recommendation",

        use_container_width=True

    ):

        with st.spinner("Thinking..."):

            result = recommend_product(
                profile,
                products
            )

        st.success(

            result["recommended_product"]

        )

        st.metric(

            "Confidence",

            f"{result['confidence']}%"

        )

        st.markdown("### Why?")

        st.write(result["reason"])

        st.markdown("### Best For")

        st.write(result["best_for"])

        st.markdown("### Runner Up")

        st.write(result["runner_up"])