import datetime as dt
import os
import click
import requests
import logging
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

# Configure logging
logging.basicConfig(filename='.\logs\weather.log', level=logging.INFO)

# Tool name, slogan, and description
TOOL_NAME = os.getenv('TOOL_NAME')
VERSION = os.getenv('VERSION')
SLOGAN = os.getenv('SLOGAN')


# Display tool information
#click.echo(click.style(f"\n{TOOL_NAME}!  v.{VERSION} :{SLOGAN}", fg='green', bold=True, reverse=True))
#click.echo(click.style(" - Created by Using Python and OpenWeatherMap API Using Github Copilot", fg='green', bold=True, reverse=True))
click.echo(click.style(f"\n - {click.style(TOOL_NAME, underline=True, bold=True, fg='green')}{click.style(VERSION, underline=True, bold=True, fg='green')}", bold=True))
click.echo(click.style(f" - {click.style(SLOGAN, underline=True, bold=True, fg='yellow')}", bold=True))


def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return celsius, fahrenheit

@click.group()
def cli():
    pass

@cli.command()
@click.option('--city', help="Get Weather Data for a City [cityname]", metavar='<city>' ,required=True, type=str, nargs=1)
@click.argument('city')
def city(city):
    city = city.title()
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    url = f"{BASE_URL}?appid={API_KEY}&q={city}"

    try:
        response = requests.get(url).json()
        logging.info(f"API request successful for city: {city}")
    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed for city: {city}. Error: {e}")
        click.echo(f"Error: Failed to fetch weather data for {city}. Please try again later.")
        click.echo(f"Error: Failed to fetch weather data for {city}. Please try again later.")
        return

    if 'message' in response:
        error_message = response['message']
        click.echo(f"Error: {error_message}")
        logging.warning(f"API response error for city: {city}. Error: {error_message}")
    else:
        print("*****************************************************************************************")
        click.echo(click.style("[ Weather Report 📝]", bold=True))
        #city named followed by the state name and country name by comma like " - city, state, country"
        #{result['location']['region']},{result['location']['country']}
        #click.echo(click.style(f" - {city},{['location']['region']},{['location']['country']}",fg="blue"))
        lan = response["coord"]["lon"]
        lat = response["coord"]["lat"]
                # Get city, region, and country names from reverse geocoding
        geocode_url = f"https://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lan}&limit=1&appid={API_KEY}"
        try:
            geocode_response = requests.get(geocode_url).json()
            region_name = geocode_response[0]['state']
            country_name = geocode_response[0]['country']
        except (requests.exceptions.RequestException, IndexError, KeyError) as e:
            logging.error(f"Reverse geocoding failed for city: {city}. Error: {e}")
            click.echo(f"Error: Failed to retrieve location information. Please try again later.")
            return
        
        click.echo(click.style("\n[ Location Information 🌍]", bold=True, fg="blue"))
        click.echo(click.style(f" - City name: {click.style(city, underline=True, bold=True, fg='red')}", bold=True))
        click.echo(click.style(f" - State/Region: {region_name}"))
        click.echo(click.style(f" - Country: {country_name}"))
        

        #click.echo(click.style(f" - {click.style(city, underline=True, bold=True, fg='blue')}", bold=True))
        #country = response["sys"]["country"]
    
        display_weather_data(response)

@cli.command()
@click.option('--cities', help="Cities Names [cityname] [cityname]...", metavar='<city1> <city2> ...', required=True, multiple=True, type=str)
@click.argument('cities', nargs=-1)
def cities(cities):
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    results = []

    Title_cities = [city.title() for city in cities]
    for city in Title_cities:
        url = f"{BASE_URL}?appid={API_KEY}&q={city}"

        try:
            response = requests.get(url).json()
            logging.info(f"API request successful for city: {city}")
        except requests.exceptions.RequestException as e:
            logging.error(f"API request failed for city: {city}. Error: {e}")
            results.append({'city': city, 'error': f"Failed to fetch weather data. Error: {e}"})
            continue

        if 'message' in response:
            error_message = response['message']
            results.append({'city': city, 'error': error_message})
            logging.warning(f"API response error for city: {city}. Error: {error_message}")
        else:
            results.append({'city': city, 'data': response})

    for result in results:
        print("\n*****************************************************************************************")
        click.echo(click.style("[ Weather Report 📝]", bold=True))
        #click.echo(click.style(f" - {result['city']}", fg="blue"))

        if 'error' in result:
            click.echo(f"Error: {result['error']}")
        else:
            Geolan = result['data']["coord"]["lon"]
            Geolat = result['data']["coord"]["lat"]

            # Get city, region, and country names from reverse geocoding
            geocode_url = f"https://api.openweathermap.org/geo/1.0/reverse?lat={Geolat}&lon={Geolan}&limit=1&appid={API_KEY}"
            try:
                geocode_response = requests.get(geocode_url).json()
                city_name = geocode_response[0]['name']
                region_name = geocode_response[0]['state']
                country_name = geocode_response[0]['country']
            except (requests.exceptions.RequestException, IndexError, KeyError) as e:
                logging.error(f"Reverse geocoding failed for city: {result['city']}. Error: {e}")
                click.echo(f"Error: Failed to retrieve location information for {result['city']}. Please try again later.")
                continue

            click.echo(click.style("\n[ Location Information 🌍]", bold=True, fg="blue"))
            click.echo(click.style(f" - City name: {click.style(city_name, underline=True, bold=True, fg='red')}", bold=True))
            click.echo(click.style(f" - State/Region: {region_name}"))
            click.echo(click.style(f" - Country: {country_name}"))

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

    click.echo(click.style("\n[ Source of Data ]", bold=True,fg="blue"))
    click.echo(f" - {click.style(datasource, bold=True)}")

    click.echo(click.style("\n[ GeoLocation Information 🌐]", bold=True, fg="blue"))
    click.echo(f" - Longitude: {Geolan}")
    click.echo(f" - Latitude: {Geolat}")

    click.echo(click.style("\n[ General Information 🌡 ]", bold=True, fg="blue"))
    click.echo(f" - Temperature: {temp_celsius:.2f}°C ({temp_fahrenheit:.2f}°F)")
    click.echo(f" - Feels Like: {feels_like_celsius:.2f}°C ({feels_like_fahrenheit:.2f}°F)")
    click.echo(f" - Minimum Temperature: {tempmin_celsius:.2f}°C ({tempmin_fahrenheit:.2f}°F)")
    click.echo(f" - Maximum Temperature: {tempmax_celsius:.2f}°C ({tempmax_fahrenheit:.2f}°F)")
    click.echo(f" - Humidity: {humidity}%")
    click.echo(f" - Pressure: {pressure} hPa")

    click.echo(click.style("\n[ Weather Details 🌦 ]", bold=True, fg="blue"))
    click.echo(f" - Weather Type: {weathertype}")
    click.echo(f" - Description: {weathertypedesc}")
   
    click.echo(click.style("\n[ Visibility and Cloudiness 🥽 ]", bold=True, fg="blue"))
    click.echo(f" - Visibility: {visibility} m")
    click.echo(f" - Cloudiness: {cloudiness}%")
    click.echo(f" - Precipitation: {precipitation} mm")

    click.echo(click.style("\n[ Wind Information 🍃 ]", bold=True, fg="blue"))
    click.echo(f" - Wind Speed: {wind_speed} m/s")
    click.echo(f" - Wind Direction: {winddegree}°")

    click.echo(click.style("\n[ Sunrise and Sunset 🌞 ]", bold=True, fg="blue"))
    click.echo(f" - Sunrise: {sunrise} (local time)")
    click.echo(f" - Sunset: {sunset} (local time)")
    click.echo('\n - 🙏 Thank you for using WeatherApp!')


if __name__ == '__main__':
    cli()
