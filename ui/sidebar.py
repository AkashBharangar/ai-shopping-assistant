import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.title("🛒 AI Shopping")

        st.markdown(
            """
AI Powered Shopping Assistant

Built using

- LangChain
- Groq
- Streamlit
            """
        )

        st.divider()

        mode = st.radio(

            "Select Mode",

            [

                "Developer Mode",

                "Assistant Mode"

            ]

        )

        st.divider()

        st.caption(
            "Made with ❤️ using Groq + LangChain"
        )

    return mode