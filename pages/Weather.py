import streamlit as st 
from utils.theme import load_css,apply_page_theme

load_css()

st.set_page_config(
    page_title="Weather | LocalLens-AI",
    layout="wide"
)


apply_page_theme()

st.title("☀️ Weather Updates")
st.write("Weather info will appear here.")


