from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'latitude': self.latitude,
            'longitude': self.longitude
        }

class CurrentWeather(Base):
    __tablename__ = 'current_weather'

    id = Column(Integer, primary_key=True)
    location_id = Column(Integer, ForeignKey('locations.id'), nullable=False)
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    wind_speed = Column(Float, nullable=False)
    pressure = Column(Float, nullable=False)
    observation_time = Column(DateTime, nullable=False)

    location = relationship('Location', backref='current_weather')

    def to_dict(self):
        return {
            'id': self.id,
            'location_id': self.location_id,
            'temperature': self.temperature,
            'humidity': self.humidity,
            'wind_speed': self.wind_speed,
            'precipitation': self.precipitation,
            'observation_time': self.observation_time
        }

class ForecastWeather(Base):
    __tablename__ = 'forecast_weather'

    id = Column(Integer, primary_key=True)
    location_id = Column(Integer, ForeignKey('locations.id'), nullable=False)
    forecast_date = Column(DateTime, nullable=False)
    min_temperature = Column(Float, nullable=False)
    max_temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    wind_speed = Column(Float, nullable=False)
    pressure = Column(Float, nullable=False)

    location = relationship('Location', backref='forecast_weather')

    def to_dict(self):
        return {
            'id': self.id,
            'location_id': self.location_id,
            'forecast_date': self.forecast_date,
            'min_temperature': self.min_temperature,
            'max_temperature': self.max_temperature,
            'humidity': self.humidity,
            'wind_speed': self.wind_speed,
            'precipitation': self.precipitation
        }

class HistoricalWeather(Base):
    __tablename__ = 'historical_weather'

    id = Column(Integer, primary_key=True)
    location_id = Column(Integer, ForeignKey('locations.id'), nullable=False)
    observation_date = Column(DateTime, nullable=False)
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    wind_speed = Column(Float, nullable=False)
    pressure = Column(Float, nullable=False)

    location = relationship('Location', backref='historical_weather')

    def to_dict(self):
        return {
            'id': self.id,
            'location_id': self.location_id,
            'observation_date': self.observation_date,
            'temperature': self.temperature,
            'humidity': self.humidity,
            'wind_speed': self.wind_speed,
            'precipitation': self.precipitation
        }
