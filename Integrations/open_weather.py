import requests

class OpenWeather:
    key = 'your_api_key'
    api_url = 'https://api.openweathermap.org/data/3.0/weather'

    def get_location_forecast(self, latitude, longitude, city):
        url = f"{self.api_url}?lat={latitude}&lon={longitude}&city={city}&appid={self.key}&exclude=hourly,daily"
        response = requests.get(url)
        return response.json()

        

        
