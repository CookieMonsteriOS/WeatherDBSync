import requests

import requests

class OpenWeather:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = 'https://api.openweathermap.org/data/2.5/weather'

    def get_location_forecast(self, latitude, longitude, city):
        """Retrieve current weather data based on latitude, longitude, and city."""
        url = f"{self.api_url}?lat={latitude}&lon={longitude}&city={city}&appid={self.api_key}&exclude=hourly,daily"
        response = requests.get(url)
        return response.json()


    