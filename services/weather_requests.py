from database.db import database
from database.models.weather import Location
from integrations.open_weather import OpenWeather

def weather_location_request(latitude, longitude, city):

    weather_client = OpenWeather()

    if latitude is None and longitude is None and city is None:
        return
    else:
        try:
            new_location = Location(name=city,longitude=longitude,latitude=latitude)
            database.session.add(new_location)
            database.session.commit()
        except Exception as e:
            database.session.rollback()
            raise e
    
    location_weather = weather_client.get_location_forecast(latitude,longitude,city)
    print(location_weather['current'])
