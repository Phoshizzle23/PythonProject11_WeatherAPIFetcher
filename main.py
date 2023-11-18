# Python Automation Project 2 - Weather API Fetcher
# pip install requests -> to get module

import requests

API_KEY = "43e5027af31d8b96c682a6ff9ad7155b"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_conditions = data["weather"][0]["description"]

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature} K")
        print(f"Humidity: {humidity}%")
        print(f"Weather Conditions: {weather_conditions}")
    else:
        print("An error occurred while fetching weather data.")

def convert_temperature(temperature, unit):
    if unit == "C":
        return temperature - 273.15
    elif unit == "F":
        return (temperature - 273.15) * 9/5 + 32
    else:
        return temperature

def main():
    city = input("Enter a city name: ")
    get_weather(city)

    convert_unit = input("Convert temperature to Celsius (C) or Fahrenheit (F)? Press any other key to skip: ")
    if convert_unit in ["C", "F"]:
        temperature_in_kelvin = float(input("Enter the current temperature in Kelvin: "))
        converted_temperature = convert_temperature(temperature_in_kelvin, convert_unit)
        print(f"Converted Temperature: {converted_temperature} {convert_unit}")

if __name__ == "__main__":
    main()

