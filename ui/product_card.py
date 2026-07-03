import streamlit as st


def render_product_cards(products):

    st.subheader("Search Results")

    cols = st.columns(2)

    for index, product in enumerate(products):

        col = cols[index % 2]

        with col:

            with st.container(border=True):

                st.image(
                    product["thumbnail"],
                    use_container_width=True
                )

                st.subheader(
                    product["title"]
                )

                st.caption(
                    product["brand"]
                )

                metric1, metric2 = st.columns(2)

                with metric1:

                    st.metric(
                        "Price",
                        f"${product['price']}"
                    )

                with metric2:

                    st.metric(
                        "Rating",
                        product["rating"]
                    )

                st.write(
                    product["description"]
                )

                st.checkbox(

                    "Compare",

                    key=f"compare_{index}"

                )