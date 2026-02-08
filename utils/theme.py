
import streamlit as st

def load_css():
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def apply_page_theme():
    if "theme" not in st.session_state:
        st.session_state.theme = "dark"

    if st.session_state.theme == "dark":
        st.markdown("""
        <style>
        /* PAGE BACKGROUND */
        .stApp {
            background-color: #020617;
            color: white;
        }

        /* INPUTS / SELECTBOX — ALWAYS BLACK TEXT */
        .stApp input,
        .stApp textarea,
        .stApp select,
        .stApp [data-baseweb="select"] * {
            color: black !important;
        }
        </style>
        """, unsafe_allow_html=True)

    else:
        st.markdown("""
        <style>
        /* PAGE BACKGROUND */
        .stApp {
            background-color: #F8FAFC;
            color: #020617;
        }

        /* INPUTS / SELECTBOX — BLACK TEXT */
        .stApp input,
        .stApp textarea,
        .stApp select,
        .stApp [data-baseweb="select"] * {
            color: black !important;
        }
        </style>
        """, unsafe_allow_html=True)
