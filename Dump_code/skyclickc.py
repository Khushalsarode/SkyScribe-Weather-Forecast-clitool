import datetime as dt
import os
import click
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return celsius, fahrenheit

@click.group()
def cli():
    pass

@cli.command(name='city',help=" - Get Weather Data for a City.", short_help="- Weather Report for a City [city]")
@click.argument('city', metavar='<city>')
def City(city):
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    response = requests.get(url).json()

    if 'message' in response:
        error_message = response['message']
        click.echo(f"Error: {error_message}")
    else:
        print("*****************************************************************************************")
        click.echo(f"Weather Report for")
        click.echo(f" - {city}")

        display_weather_data(response)

@cli.command(name='cities',help=" - Get Weather Data for Multiple Cities.", short_help="- Weather Report Multiple Cities [city1] [city2] ...]")
@click.argument('cities', nargs=-1, metavar='<city1> <city2> ...')
def Cities(cities):
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    results = []

    for city in cities:
        url = f"{BASE_URL}?appid={API_KEY}&q={city}"
        response = requests.get(url).json()

        if 'message' in response:
            error_message = response['message']
            results.append({'city': city, 'error': error_message})
        else:
            results.append({'city': city, 'data': response})

    for result in results:

        print("*****************************************************************************************")
        click.echo(f"Weather Report for")
        click.echo(f" - {result['city']}")
        if 'error' in result:
            click.echo(f"Error: {result['error']}")
        else:
            display_weather_data(result['data'])

def display_weather_data(response):
    Geolan = response["coord"]["lon"]
    Geolat = response["coord"]["lat"]
    weathertype = response["weather"][0]["main"]
    weathertypedesc = response["weather"][0]["description"]
    datasource = response["base"]

    temp_kelvin = response["main"]["temp"]
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)

    feels_like_kelvin = response["main"]["feels_like"]
    feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)

    tempmin = response["main"]["temp_min"]
    tempmin_celsius, tempmin_fahrenheit = kelvin_to_celsius_fahrenheit(tempmin)

    tempmax = response["main"]["temp_max"]
    tempmax_celsius, tempmax_fahrenheit = kelvin_to_celsius_fahrenheit(tempmax)

    pressure = response["main"]["pressure"]
    humidity = response["main"]["humidity"]

    wind_speed = response["wind"]["speed"]
    winddegree = response["wind"]["deg"]

    sunrise = dt.datetime.utcfromtimestamp(response["sys"]["sunrise"] + response["timezone"])
    sunset = dt.datetime.utcfromtimestamp(response["sys"]["sunset"] + response["timezone"])

    visibility = response.get("visibility")
    cloudiness = response["clouds"]["all"]
    precipitation = response.get("rain", {}).get("1h", 0.0)

    
    click.echo(f"\nSource of Data: {datasource}")

    click.echo("\n[GeoLocation Information]")
    click.echo(f"- Longitude: {Geolan}")
    click.echo(f"- Latitude: {Geolat}")

    click.echo("\n[General Information]")
    click.echo(f"- Temperature: {temp_celsius:.2f}°C ({temp_fahrenheit:.2f}°F)")
    click.echo(f"- Feels Like: {feels_like_celsius:.2f}°C ({feels_like_fahrenheit:.2f}°F)")
    click.echo(f"- Minimum Temperature: {tempmin_celsius:.2f}°C ({tempmin_fahrenheit:.2f}°F)")
    click.echo(f"- Maximum Temperature: {tempmax_celsius:.2f}°C ({tempmax_fahrenheit:.2f}°F)")
    click.echo(f"- Humidity: {humidity}%")
    click.echo(f"- Pressure: {pressure} hPa")

    click.echo("\n[Weather Details]")
    click.echo(f"- Weather Type: {weathertype}")
    click.echo(f"- Description: {weathertypedesc}")
   
    click.echo("\n[Visibility and Cloudiness]")
    click.echo(f"- Visibility: {visibility} m")
    click.echo(f"- Cloudiness: {cloudiness}%")
    click.echo(f"- Precipitation: {precipitation} mm")

    click.echo("\n[Wind Information]")
    click.echo(f"- Wind Speed: {wind_speed} m/s")
    click.echo(f"- Wind Direction: {winddegree}°")

    click.echo("\n[Sunrise and Sunset]")
    click.echo(f"- Sunrise: {sunrise} (local time)")
    click.echo(f"- Sunset: {sunset} (local time)")
    click.echo('---')


if __name__ == '__main__':
    cli()
