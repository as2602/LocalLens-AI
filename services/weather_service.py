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
        return None, f"API Error: {response.json().get('error', {}).get('message', 'Unknown error')}"

    data = response.json()

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
    "icon": "https:" + data["current"]["condition"]["icon"],
    "is_day": data["current"]["is_day"] ,
    "lat": data["location"]["lat"],
    "lon": data["location"]["lon"]
 
}
    return weather_data, None


def get_5day_forecast(city, unit="metric"):
   

    days = 5

    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days={days}"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            return None, data.get("error", {}).get("message", "Error fetching forecast")

        forecast_data = []

        for day in data["forecast"]["forecastday"]:
            forecast_data.append({
                "date": day["date"],
                "temp": day["day"]["avgtemp_c"] if unit == "metric" else day["day"]["avgtemp_f"],
                "condition": day["day"]["condition"]["text"],
                "icon": "https:" + day["day"]["condition"]["icon"]
            })

        return forecast_data, None

    except Exception as e:
        return None, str(e)

