import streamlit as st
from services.news_service import get_news, COUNTRIES, CATEGORIES, LANGUAGES
from components.news_card import news_card
from utils.theme import load_css, apply_page_theme

# ----- COMMON UI -----
st.set_page_config(
    page_title="News | LocalLens-AI",
    layout="wide"
)

load_css()
apply_page_theme()

st.title("📰 Global News")

# 🌍 Country select
country_name = st.selectbox(
    "Select Country",
    list(COUNTRIES.keys())
)
country_code = COUNTRIES[country_name]

# 🗂 Category select
category = st.selectbox(
    "Select Category",
    CATEGORIES
)

# 🌐 Language select
language_name = st.selectbox(
    "Select Language",
    list(LANGUAGES.keys())
)
language_code = LANGUAGES[language_name]

# 🔍 Fetch news
news_list = get_news(
    country=country_code,
    category=category,
    language=language_code
)

# 📰 Display
if not news_list:
    st.warning("No news found for this selection.")
else:
    for article in news_list:
        news_card(article)
