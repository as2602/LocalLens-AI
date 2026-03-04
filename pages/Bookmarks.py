import streamlit as st
from utils.helpers import load_bookmarks, remove_bookmark
from utils.theme import load_css, apply_page_theme

st.set_page_config(
    page_title="Bookmarks | LocalLens-AI",
    layout="wide"
)

load_css()
apply_page_theme()

st.title("📌 Saved Bookmarks")

bookmarks = load_bookmarks()

if not bookmarks:
    st.info("No bookmarks yet.")
else:
    for item in bookmarks:
        st.subheader(item["title"])
        st.write(f"Source: {item['source']}")
        st.markdown(f"[🔗 Read Full Article]({item['url']})")

        if st.button("❌ Remove", key=item["url"]):
            remove_bookmark(item["url"])
            st.rerun()

        st.divider()