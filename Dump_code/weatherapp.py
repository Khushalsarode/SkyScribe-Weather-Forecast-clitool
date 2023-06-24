import datetime as dt
import json
import os
#import click
import requests
from dotenv import load_dotenv
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
#API_KEY = "9a58d34a1b1d62990685e9d100b52737"
CITY = "Jalgaon"
#how to load dot env file
load_dotenv()
API_KEY = os.getenv('API_KEY')


url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return celsius, fahrenheit

#Coordinates
Geolan = response["coord"]["lon"]
Geolat = response["coord"]["lat"]

#Weather
weathertype= response["weather"][0]["main"]
weathertypedesc = response["weather"][0]["description"]

#Base:(source of data)
datasource = response["base"]

#Main weather information:
    #Temperature
temp_kelvin = response["main"]["temp"]
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)

feels_like_kelvin = response["main"]["feels_like"]
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)

tempmin = response["main"]["temp_min"]
tempmin_celsius, tempmin_fahrenheit = kelvin_to_celsius_fahrenheit(tempmin)

tempmax = response["main"]["temp_max"]
tempmax_celsius, tempmax_fahrenheit = kelvin_to_celsius_fahrenheit(tempmax)


    #Pressure
pressure = response["main"]["pressure"]

    #Humidity
humidity = response["main"]["humidity"]

#Wind
wind_speed = response["wind"]["speed"]
winddegree= response["wind"]["deg"]

#Time-related information:
sunrise = dt.datetime.utcfromtimestamp(response["sys"]["sunrise"] + response["timezone"] )
sunset = dt.datetime.utcfromtimestamp(response["sys"]["sunset"] + response["timezone"] )



#print(response)
#print(f"Temperature in {CITY} is {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F")
print(f"Weather Report for {CITY}")
print(f"Source of Data: {datasource}")
print("\n[General Information]")
print(f"- Temperature: {temp_celsius:.2f}°C ({temp_fahrenheit:.2f}°F)")
print(f"- Feels Like: {feels_like_celsius:.2f}°C ({feels_like_fahrenheit:.2f}°F)")
print(f"- Minimum Temperature: {tempmin_celsius:.2f}°C ({tempmin_fahrenheit:.2f}°F)")
print(f"- Maximum Temperature: {tempmax_celsius:.2f}°C ({tempmax_fahrenheit:.2f}°F)")
print(f"- Humidity: {humidity}%")

print("\n[Weather Details]")
print(f"- Weather Type: {weathertype}")
print(f"- Description: {weathertypedesc}")

print("\n[Wind Information]")
print(f"- Wind Speed: {wind_speed} m/s")
print(f"- Wind Direction: {winddegree}°")

print("\n[Sunrise and Sunset]")
print(f"- Sunrise: {sunrise} (local time)")
print(f"- Sunset: {sunset} (local time)")

#click.echo("\033[1mWeather Report for\033[0m")  # Bold style
#click.echo(f"\033[4m - {CITY}\033[0m")  # Underline style

