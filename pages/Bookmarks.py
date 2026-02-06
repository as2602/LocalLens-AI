import streamlit as st
from utils.theme import load_css

load_css()
st.set_page_config(
    page_title="News | LocalLens-AI",
    layout="wide"
)
st.title("🔖 BookMark Page")
st.write("Saved bookmarks will appear here.")

