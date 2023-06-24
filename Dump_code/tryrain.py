import datetime as dt
import os
import click
import requests
from dotenv import load_dotenv
from tabulate import tabulate

load_dotenv()
API_KEY = os.getenv('API_KEY')

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return celsius, fahrenheit

@click.group()
def cli():
    pass

@cli.command(name='city', help="Get Weather Data for a City.")
@click.argument('city', metavar='<city>')
def City(city):
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    
    try:
        response = requests.get(url).json()
        
        if 'message' in response:
            error_message = response['message']
            click.echo(f"Error: {error_message}")
        else:
            click.echo(f"Weather Report for {city}")
            display_weather_data(response)
    
    except requests.exceptions.RequestException as e:
        click.echo(f"Error: {str(e)}")

@cli.command(name='cities', help="Get Weather Data for Multiple Cities.")
@click.argument('cities', nargs=-1, metavar='<city1> <city2> ...')
def Cities(cities):
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    results = []

    for city in cities:
        url = f"{BASE_URL}?appid={API_KEY}&q={city}"
        
        try:
            response = requests.get(url).json()

            if 'message' in response:
                error_message = response['message']
                results.append({'city': city, 'error': error_message})
            else:
                results.append({'city': city, 'data': response})
        
        except requests.exceptions.RequestException as e:
            results.append({'city': city, 'error': str(e)})
    
    for result in results:
        click.echo(f"Weather Report for {result['city']}")
        
        if 'error' in result:
            click.echo(f"Error: {result['error']}")
        else:
            display_weather_data(result['data'])
    
def display_weather_data(response):
    table = []

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

    table.append(["Source of Data", datasource])
    table.append(["GeoLocation Information"])
    table.append(["- Longitude", Geolan])
    table.append(["- Latitude", Geolat])
    table.append(["General Information", ""])
    table.append(["- Temperature", f"{temp_celsius:.2f}°C ({temp_fahrenheit:.2f}°F)"])
    table.append(["- Feels Like", f"{feels_like_celsius:.2f}°C ({feels_like_fahrenheit:.2f}°F)"])
    table.append(["- Minimum Temperature", f"{tempmin_celsius:.2f}°C ({tempmin_fahrenheit:.2f}°F)"])
    table.append(["- Maximum Temperature", f"{tempmax_celsius:.2f}°C ({tempmax_fahrenheit:.2f}°F)"])
    table.append(["- Humidity", f"{humidity}%"])
    table.append(["- Pressure", f"{pressure} hPa"])
    table.append(["Weather Details", ""])
    table.append(["- Weather Type", weathertype])
    table.append(["- Description", weathertypedesc])
    table.append(["- Visibility", f"{visibility} meters" if visibility else "N/A"])
    table.append(["- Cloudiness", f"{cloudiness}%"])
    table.append(["- Precipitation (1h)", f"{precipitation} mm"])
    table.append(["Wind Information", ""])
    table.append(["- Wind Speed", f"{wind_speed} m/s"])
    table.append(["- Wind Direction", f"{winddegree}°"])
    table.append(["Sunrise and Sunset", ""])
    table.append(["- Sunrise", str(sunrise) + " (local time)"])
    table.append(["- Sunset", str(sunset) + " (local time)"])

    click.echo(tabulate(table, headers=["Information", "Value"], tablefmt="fancy_grid"))
   
if __name__ == '__main__':
    cli()
