import pytest
import Weather_Api

@pytest.mark.parametrize("city", ["Hyderabad", "Mumbai", "Delhi", "Tokyo", "Berlin", "Moscow", "Yakutsk"])
def test_weather_api(city):
    """Tests the OpenWeather API response for various cities."""
    result = Weather_Api.get_weather(city)
    assert "Temperature" in result or "API request error" in result, f"Unexpected response for {city}: {result}"
    # Extract temperature from result (e.g., "🌡 Temperature: 32.23°C / 90.01°F")
    temp_line = [line for line in result.split("\n") if "Temperature" in line][0]
    temp_c = temp_line.split("Temperature: ")[1].split("°C")[0].strip()
    print(f"✅ Test passed for {city}: {temp_c}°C")
    print("This is Code related to weather api using pytest")