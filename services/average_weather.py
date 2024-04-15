from database.db import database
from database.models.weather import Location, CurrentWeather
from sqlalchemy import and_
from utils.util import parse_date

def get_average_weather_data(location_id, start_date, end_date):

    try:
        weather_location = database.session.query(Location).filter(Location.id == location_id).first()
        
        #Check if the location exists in the database
        if not weather_location:
            print('Location not found in database')
        else:

            #Get Weather conditions from database
            current_weather_details = database.session.query(CurrentWeather).filter(and_(CurrentWeather.observation_time.between(parse_date(start_date), parse_date(end_date)),
                CurrentWeather.location_id == location_id)).all()            
            
            print(current_weather_details[0].humidity)

            response = {
                "location_id": weather_location.id,
                "name": weather_location.name,
                "average_weather": {
                    "start_date": "2024-04-01",
                    "end_date": "2024-04-10",
                    "average_temperature": 287.35,
                    "average_humidity": 85.2
                }
            }
        return response
    except Exception as e:
        database.session.rollback()
        print(f"An error occurred: {e}")
        return None

    
    
