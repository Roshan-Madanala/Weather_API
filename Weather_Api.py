import requests

def get_weather(city):
    # OpenWeather API Key (Replace with your own API key)
    weather_api_key = "203b232dc4cc7e522a39f092a05e07d2"
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"

    response = requests.get(weather_url)
    if response.status_code == 200:
        data = response.json()

        # Extracting required details
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        pressure = data['main']['pressure']
        temp_fahrenheit = (temp * 9 / 5) + 32  # Convert to Fahrenheit

        # Formatting output
        weather_info = (
            f"Weather in {city}:\n"
            f"🌡 Temperature: {temp}°C / {temp_fahrenheit:.2f}°F\n"
            f"☁ Description: {desc}\n"
            f"💧 Humidity: {humidity}%\n"
            f"🌬 Wind Speed: {wind_speed} m/s\n"
            f"🔵 Pressure: {pressure} hPa"
        )
        return weather_info
    else:
        return "Invalid city name or API error"


# Get user input
city = input("Enter city name: ")
weather_info = get_weather(city)
print(weather_info)
print("This is the weather API!!")
