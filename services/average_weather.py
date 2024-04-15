from database.db import database
from database.models.weather import Location, CurrentWeather
from sqlalchemy import and_
from utils.util import parse_date

def get_average_weather_data(location_id, start_date, end_date):

    try:
        weather_location = database.session.query(
            Location).filter(Location.id == location_id).first()

        # Check if the location exists in the database
        if not weather_location:
            print('Location not found in database')
        else:

            # Get Weather conditions from database
            current_weather_details = database.session.query(CurrentWeather).filter(and_(CurrentWeather.observation_time.between(parse_date(start_date), parse_date(end_date)),
                                                                                         CurrentWeather.location_id == location_id)).all()
            avg_temp = 0
            avg_humidity = 0 
            total_records = len(current_weather_details)

            #Sum details and divide by total number of records
            for weather_detail in current_weather_details:
                avg_temp += weather_detail.temperature
                avg_humidity += weather_detail.humidity 
            
            avg_temp /= total_records
            avg_humidity /= total_records

            avg_weather_res = {
                "location_id": weather_location.id,
                "name": weather_location.name,
                "average_weather": {
                    "start_date": start_date,
                    "end_date": end_date,
                    "average_temperature": avg_temp,
                    "average_humidity": avg_humidity
                }
            }
        return avg_weather_res
    except Exception as e:
        database.session.rollback()
        print(f"An error occurred: {e}")
        return None
