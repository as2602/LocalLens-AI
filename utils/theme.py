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
        .stApp {
            background-color: #020617;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)

    else:
        st.markdown("""
        <style>
        .stApp {
            background-color: #F8FAFC;
            color: #020617;
        }
        </style>
        """, unsafe_allow_html=True)
