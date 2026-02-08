import requests
import os

GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")

BASE_URL = "https://gnews.io/api/v4/top-headlines"

# 🌍 Countries supported (GNews)
COUNTRIES = {
    "India 🇮🇳": "in",
    "United States 🇺🇸": "us",
    "United Kingdom 🇬🇧": "gb",
    "Canada 🇨🇦": "ca",
    "Australia 🇦🇺": "au",
    "France 🇫🇷": "fr",
    "Germany 🇩🇪": "de",
    "Japan 🇯🇵": "jp"
}

# 🗂 Categories supported by GNews
CATEGORIES = [
    "general",
    "world",
    "nation",
    "business",
    "technology",
    "entertainment",
    "sports",
    "science",
    "health"
]

# 🌐 Languages
LANGUAGES = {
    "English": "en",
    "Hindi": "hi"
}


def get_news(country="in", category="general", language="en"):
    params = {
        "token": GNEWS_API_KEY,
        "country": country,
        "topic": category,
        "lang": language,
        "max": 10
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        data = response.json()
        return data.get("articles", [])

    except Exception as e:
        print("GNews API Error:", e)
        return []
