import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from services.weather_service import get_current_weather, get_5day_forecast
from utils.theme import load_css, apply_page_theme

st.set_page_config(
    page_title="Weather | LocalLens-AI",
    page_icon="🌦",
    layout="wide"
)

load_css()
apply_page_theme()

# -------------------------
# SESSION STATE
# -------------------------
if "unit" not in st.session_state:
    st.session_state.unit = "metric"

if "city" not in st.session_state:
    st.session_state.city = "Delhi"

# -------------------------
# HEADER
# -------------------------
st.title("🌍 Weather Intelligence Dashboard")

col1, col2, col3 = st.columns([3, 1, 1])

with col1:
    city = st.text_input(
        "Search City",
        value=st.session_state.city
    )

with col2:
    toggle = st.toggle("°C / °F")

with col3:
    search = st.button("Search")

st.session_state.unit = "imperial" if toggle else "metric"
unit_symbol = "°C" if st.session_state.unit == "metric" else "°F"

if search:
    st.session_state.city = city

# -------------------------
# FETCH DATA
# -------------------------
if st.session_state.city:

    with st.spinner("Fetching Weather Data..."):
        current, error1 = get_current_weather(
            st.session_state.city,
            st.session_state.unit
        )

        forecast, error2 = get_5day_forecast(
            st.session_state.city,
            st.session_state.unit
        )

    if error1:
        st.error(error1)
    else:

        # =====================
        # CURRENT WEATHER
        # =====================
        st.subheader(f"📍 {current['city']}, {current['country']}")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Temperature", f"{current['temperature']} {unit_symbol}")
        c2.metric("Humidity", f"{current['humidity']} %")
        c3.metric("Wind Speed", f"{current['wind']} kph")
        c4.metric("Condition", current["condition"])

        st.image(current["icon"], width=80)

        st.divider()

        # =====================
        # MAP SECTION
        # =====================
        st.subheader("🗺 Location Map")

        map_data = folium.Map(
            location=[current["lat"], current["lon"]],
            zoom_start=10
        )

        folium.Marker(
            [current["lat"], current["lon"]],
            popup=current["city"]
        ).add_to(map_data)

        st_folium(map_data, width=1000, height=400)

        st.divider()

        # =====================
        # 5 DAY FORECAST
        # =====================
        st.subheader("📅 5-Day Forecast")

        # forecast_cols = st.columns(5)

        # for i in range(5):
        #     with forecast_cols[i]:
        #         st.write(forecast[i]["date"])
        #         st.image(forecast[i]["icon"], width=60)
        #         st.write(f"{forecast[i]['temp']} {unit_symbol}")
        #         st.caption(forecast[i]["condition"])

    if error2:
        st.error(error2)
    elif forecast:
        forecast_cols = st.columns(len(forecast))

        for i in range(len(forecast)):
            with forecast_cols[i]:
                st.write(forecast[i]["date"])
                st.image(forecast[i]["icon"], width=60)
                st.write(f"{forecast[i]['temp']} {unit_symbol}")
                st.caption(forecast[i]["condition"])
    else:
        st.warning("Forecast data not available.")
