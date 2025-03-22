import requests
import os
from dotenv import load_dotenv

# Load API Key from Environment Variables
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY", "203b232dc4cc7e522a39f092a05e07d2")

# Define the base API URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetches and returns weather details for a given city."""
    weather_url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(weather_url)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx, 5xx)

        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        pressure = data['main']['pressure']
        temp_fahrenheit = (temp * 9 / 5) + 32

        weather_info = (
            f"Weather in {city}:\n"
            f"🌡 Temperature: {temp}°C / {temp_fahrenheit:.2f}°F\n"
            f"☁ Description: {desc}\n"
            f"💧 Humidity: {humidity}%\n"
            f"🌬 Wind Speed: {wind_speed} m/s\n"
            f"🔵 Pressure: {pressure} hPa"
        )
        return weather_info

    except requests.exceptions.RequestException as e:
        return f"API request error: {e}"

if __name__ == "__main__":
    city = input("Enter city name: ")
    print(get_weather(city))