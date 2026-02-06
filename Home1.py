import streamlit as st
from utils.theme import load_css

load_css()  # 🔥 CSS sabse pehle

st.set_page_config(
    page_title="LocalLens-AI",
    layout="wide"
)

st.title("🏠Home")
st.write("Welcome to LocalLens-AI")


