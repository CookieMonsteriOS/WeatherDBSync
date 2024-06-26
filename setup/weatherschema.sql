CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    latitude FLOAT(10, 6),
    longitude FLOAT(10, 6)
);

CREATE TABLE current_weather (
    id SERIAL PRIMARY KEY,
    location_id INT REFERENCES locations(id),
    temperature NUMERIC,
    humidity NUMERIC,
    wind_speed NUMERIC,
    pressure NUMERIC,
    observation_time TIMESTAMP
);

CREATE TABLE forecast_weather (
    id SERIAL PRIMARY KEY,
    location_id INT REFERENCES locations(id),
    forecast_date DATE,
    min_temperature NUMERIC,
    max_temperature NUMERIC,
    humidity NUMERIC,
    wind_speed NUMERIC,
    pressure NUMERIC
);

CREATE TABLE historical_weather (
    id SERIAL PRIMARY KEY,
    location_id INT REFERENCES locations(id),
    observation_date DATE,
    temperature NUMERIC,
    humidity NUMERIC,
    wind_speed NUMERIC,
    pressure NUMERIC
);