from database.db import database
from database.models.weather import Location, CurrentWeather
from integrations.open_weather import OpenWeather
from utils.util import get_weather_obvs_time, kelvin_to_celsius

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
    weather_location = database.session.query(Location).filter(Location.latitude == float(latitude), Location.longitude == float(longitude)).first()
    weather_obsv_time = get_weather_obvs_time()

    try:
        if weather_location:
            weather_location_id = weather_location
            set_location_current_weather = CurrentWeather(location_id=weather_location_id.id, temperature= kelvin_to_celsius(location_weather['main']['temp']),humidity=location_weather['main']['humidity'], wind_speed=location_weather['wind']['speed'], pressure=location_weather['main']['pressure'], observation_time=weather_obsv_time)
            database.session.add(set_location_current_weather)
            database.session.commit()
        else:
            print("Error location id not found")    
    except Exception as e:
        database.session.rollback()
        raise e

    return location_weather