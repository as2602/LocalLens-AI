# import streamlit as st
# from services.weather_service import get_current_weather
# from utils.theme import load_css, apply_page_theme

# # ------------------------------
# # PAGE CONFIG (ALWAYS FIRST)
# # ------------------------------
# st.set_page_config(
#     page_title="Weather | LocalLens-AI",
#     page_icon="🌦",
#     layout="wide"
# )

# # ------------------------------
# # COMMON THEME & CSS
# # ------------------------------
# load_css()
# apply_page_theme()

# # ------------------------------
# # PAGE CONTENT
# # ------------------------------
# st.title("🌦 Weather Dashboard")
# st.write("Search any city to get live weather updates")

# # ------------------------------
# # SESSION STATE
# # ------------------------------
# if "unit" not in st.session_state:
#     st.session_state.unit = "metric"

# # ------------------------------
# # SEARCH + TOGGLE ROW
# # ------------------------------
# col1, col2, col3 = st.columns([3, 1, 1])

# with col1:
#     city = st.text_input(
#     "Search City (example: Delhi, IN)",
#     placeholder="City name only"
# )


# with col2:
#     toggle = st.toggle("°C / °F", value=(st.session_state.unit == "imperial"))

# with col3:
#     search = st.button("🔍 Search")

# # Toggle logic
# st.session_state.unit = "imperial" if toggle else "metric"
# unit_symbol = "°C" if st.session_state.unit == "metric" else "°F"

# # ------------------------------
# # WEATHER RESULT
# # ------------------------------
# if search and city:
#     with st.spinner("Fetching weather..."):
#         data, error = get_current_weather(city, st.session_state.unit)

#     if error:
#         st.error(error)
#     else:
#         st.subheader(f"📍 {data['city']}, {data['country']}")

#         c1, c2, c3, c4 = st.columns(4)

#         c1.metric("🌡 Temperature", f"{data['temperature']} {unit_symbol}")
#         c2.metric("💧 Humidity", f"{data['humidity']} %")
#         c3.metric("💨 Wind Speed", f"{data['wind']} m/s")
#         c4.metric("☁ Condition", data["condition"])

#         st.caption(data["description"].title())


import streamlit as st
from services.weather_service import get_current_weather
from utils.theme import load_css, apply_page_theme

st.set_page_config(
    page_title="Weather | LocalLens-AI",
    page_icon="🌦",
    layout="wide"
)

load_css()
apply_page_theme()

st.title("🌦 Weather Dashboard")
st.write("Search any city worldwide to get live weather updates")

# ------------------------------
# SESSION STATE
# ------------------------------
if "unit" not in st.session_state:
    st.session_state.unit = "metric"

# ------------------------------
# SEARCH + TOGGLE
# ------------------------------
col1, col2, col3 = st.columns([3, 1, 1])

with col1:
    city = st.text_input(
        "Search City",
        placeholder="e.g. Saharanpur, Delhi, New York"
    )

with col2:
    toggle = st.toggle("°C / °F")

with col3:
    search = st.button("🔍 Search")

# Toggle logic
st.session_state.unit = "imperial" if toggle else "metric"
unit_symbol = "°C" if st.session_state.unit == "metric" else "°F"

# ------------------------------
# WEATHER RESULT
# ------------------------------
if search and city:
    with st.spinner("Fetching weather..."):
        data, error = get_current_weather(city, st.session_state.unit)

    if error:
        st.error(error)
    else:
        st.subheader(f"📍 {data['city']}, {data['country']}")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("🌡 Temperature", f"{data['temperature']} {unit_symbol}")
        c2.metric("💧 Humidity", f"{data['humidity']} %")
        c3.metric("💨 Wind Speed", f"{data['wind']} kph")
        c4.metric("☁ Condition", data["condition"])

        st.image(data["icon"], width=80)
