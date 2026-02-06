import streamlit as st 
from utils.theme import load_css

load_css()

st.set_page_config(
    page_title="Weather | LocalLens-AI",
    layout="wide"
)

st.title("☀️ Weather Updates")
st.write("Weather info will appear here.")


