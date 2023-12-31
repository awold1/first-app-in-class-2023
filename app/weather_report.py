from pgeocode import Nominatim
import requests
import json
from IPython.display import Image, display


def display_forecast(zip_code, country_code="US"):
    """
    Displays a seven day weather forecast for the provided zip code.

    Params :

        country_code (str) a valid country code (see supported country codes list). Default is "US".

        zip_code (str) a valid US zip code, like "20057" or "06510".

    """
    
    DEGREE_SIGN = u"\N{DEGREE SIGN}"
    nomi = Nominatim(country_code)
    geo = nomi.query_postal_code(zip_code)
    latitude = geo["latitude"]
    longitude = geo["longitude"]

    request_url = f"https://api.weather.gov/points/{latitude},{longitude}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)

    forecast_url = parsed_response["properties"]["forecast"]
    forecast_response = requests.get(forecast_url)
    #print(forecast_response.status_code)
    parsed_forecast_response = json.loads(forecast_response.text)

    periods = parsed_forecast_response["properties"]["periods"]
    daytime_periods = [period for period in periods if period["isDaytime"] == True]

    for period in daytime_periods:
        #print(period.keys())
        print("-------------")
        print(period["name"], period["startTime"][0:7])
        print(period["shortForecast"], f"{period['temperature']} {DEGREE_SIGN}{period['temperatureUnit']}")
        #print(period["detailedForecast"])
        display(Image(url=period["icon"]))

    return(response.status_code)

if __name__ == "__main__":
    my_zip = input("Please input a zip code (e.g. '06510'): ")
    display_forecast(my_zip)