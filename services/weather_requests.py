from database.db import database
from database.models.weather import Location, CurrentWeather
from integrations.open_weather import OpenWeather
from utils.util import get_weather_obvs_time, kelvin_to_celsius

def weather_location_request(latitude, longitude, city):

    weather_client = OpenWeather()
    
    try:
        # Check if the location already exists in the database
        weather_location = database.session.query(Location).filter(Location.latitude == float(latitude), Location.longitude == float(longitude)).first()
        
        # If the location does not exist, add it to the database
        if not weather_location:
            weather_location = Location(name=city, longitude=longitude, latitude=latitude)
            database.session.add(weather_location)
            database.session.commit()
        else:
            print("Location already exists in the database.")

        # Fetch the weather forecast for the location
        location_weather = weather_client.get_location_forecast(latitude, longitude, city)
        weather_obsv_time = get_weather_obvs_time()

        # Add the current weather data to the CurrentWeather table
        set_location_current_weather = CurrentWeather(location_id=weather_location.id,
                                                      temperature=kelvin_to_celsius(location_weather['main']['temp']),
                                                      humidity=location_weather['main']['humidity'],
                                                      wind_speed=location_weather['wind']['speed'],
                                                      pressure=location_weather['main']['pressure'],
                                                      observation_time=weather_obsv_time)
        database.session.add(set_location_current_weather)
        database.session.commit()

        return weather_location
    except Exception as e:
        database.session.rollback()
        print(f"An error occurred: {e}")
        return None