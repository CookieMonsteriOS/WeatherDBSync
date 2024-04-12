import requests

class OpenWeather:
    key = ''
    api_url = 'https://api.openweathermap.org/data/2.5/weather'

    def get_location_forecast(self, latitude, longitude, city):
        """Current  location weather data based on lat, long and city """
        url = f"{self.api_url}?lat={latitude}&lon={longitude}&city={city}&appid={self.key}&exclude=hourly,daily"
        response = requests.get(url)
        return response.json()

        

    