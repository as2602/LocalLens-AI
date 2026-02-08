import streamlit as st
from dotenv import load_dotenv
from utils.theme import load_css, apply_page_theme

load_dotenv()

st.set_page_config(
    page_title="LocalLens-AI",
    layout="wide"
)

load_css()
apply_page_theme()

# ---------- HERO SECTION ----------
st.markdown("## 🌍 LocalLens-AI")
st.markdown(
    "##### Your global news & weather intelligence platform"
)

st.markdown("---")

# ---------- STATS CARDS ----------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">📰 News Categories</div>
        <div class="metric-value">9+</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">🌍 Supported Countries</div>
        <div class="metric-value">8+</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">🗣 Languages</div>
        <div class="metric-value">English / Hindi</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ---------- PREVIEW SECTION ----------
st.subheader("🔥 What can you do here?")

col4, col5 = st.columns(2)

with col4:
    st.markdown("""
    📰 **Read global news**  
    - Country & category based  
    - Entertainment, sports, tech & more  
    - Hindi + English support
    """)

    if st.button("Go to News 📰"):
        st.switch_page("pages/News.py")

with col5:
    st.markdown("""
    ☀️ **Check weather updates**  
    - Location based  
    - 5-day forecast  
    - Maps & charts
    """)

    if st.button("Go to Weather ☀️"):
        st.switch_page("pages/Weather.py")

st.markdown("---")

