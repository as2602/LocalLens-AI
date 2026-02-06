import streamlit as st
from utils.theme import load_css

load_css()
st.set_page_config(
    page_title="News | LocalLens-AI",
    layout="wide"
)

st.title("📰 Latest News")
st.write("All news headlines will appear here.")