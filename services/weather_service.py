# import os
# import requests
# from dotenv import load_dotenv

# load_dotenv()

# API_KEY = os.getenv("WEATHER_API_KEY")
# BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# def get_current_weather(city, unit="metric"):
#     """
#     unit = metric (Celsius)
#     unit = imperial (Fahrenheit)
#     """
#     if not API_KEY:
#         return None, "API key not found"

#     params = {
#         "q": city,
#         "appid": API_KEY,
#         "units": unit
#     }

#     try:
#         response = requests.get(BASE_URL, params=params, timeout=10)

#         if response.status_code != 200:
#             return None, "City not found"

#         data = response.json()

#         weather_data = {
#             "city": data["name"],
#             "country": data["sys"]["country"],
#             "temperature": data["main"]["temp"],
#             "humidity": data["main"]["humidity"],
#             "wind": data["wind"]["speed"],
#             "condition": data["weather"][0]["main"],
#             "description": data["weather"][0]["description"],
#             "icon": data["weather"][0]["icon"]
#         }

#         return weather_data, None

#     except Exception as e:
#         return None, str(e)



import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

def get_current_weather(city, unit="metric"):
    """
    Fetch current weather using WeatherAPI.com
    unit: metric (Celsius) or imperial (Fahrenheit)
    """

    if not API_KEY:
        return None, "Weather API key not found"

    url = "https://api.weatherapi.com/v1/current.json"

    params = {
        "key": API_KEY,
        "q": city,
        "aqi": "no"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None, "City not found or API error"

    data = response.json()

    # Unit handling
    temperature = (
        data["current"]["temp_c"]
        if unit == "metric"
        else data["current"]["temp_f"]
    )

    weather_data = {
        "city": data["location"]["name"],
        "country": data["location"]["country"],
        "temperature": temperature,
        "humidity": data["current"]["humidity"],
        "wind": data["current"]["wind_kph"],
        "condition": data["current"]["condition"]["text"],
        "icon": "https:" + data["current"]["condition"]["icon"]
    }

    return weather_data, None
