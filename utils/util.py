import datetime 


def kelvin_to_celsius(temperature_kelvin):
    """Convert temperature from Kelvin to Celsius."""
    celsius = temperature_kelvin - 273.15
    return celsius

def epoch_to_human_readable(epoch_time):
    """Convert epoch time to human-readable format."""
    timestamp = datetime.datetime.fromtimestamp(epoch_time)
    return timestamp.strftime('%Y-%m-%d %H:%M:%S')
    
def get_weather_obvs_time():
    """Return observation time in the format 'YYYY-MM-DD HH:MM:SS'."""
    return datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')

