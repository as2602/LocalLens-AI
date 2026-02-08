import streamlit as st

def news_card(article):
    col1, col2 = st.columns([1, 3])

    # ✅ GNews image field
    image_url = article.get("image")

    with col1:
        if image_url:
            st.image(image_url, use_container_width=True)
        else:
            st.image(
                "https://via.placeholder.com/300x200?text=No+Image",
                use_container_width=True
            )

    with col2:
        st.subheader(article.get("title", "No Title"))

        st.write(
            article.get("description", "No description available.")
        )

        # ✅ GNews source link
        if article.get("url"):
            st.markdown(
                f"[🔗 Read full news]({article['url']})",
                unsafe_allow_html=True
            )

    st.divider()
