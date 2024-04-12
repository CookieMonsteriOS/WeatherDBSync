from database.db import database
from database.models.weather import Location

def weather_location_request(latitude, longitude, city):

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
    
    
