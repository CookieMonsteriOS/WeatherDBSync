import datetime import datetime 

class Utils:

    def kelvin_to_celsius(self,temperature_kelvin):
        """Convert temperature from Kelvin to Celsius."""
        return temperature_kelvin - 273.15

    def epoch_to_human_readable(self,epoch_time):
        """Convert epoch time to human-readable format."""
        timestamp = datetime.datetime.fromtimestamp(epoch_time)
        return timestamp.strftime('%Y-%m-%d %H:%M:%S')
    
    def get_todays_date_uk_format():
        """Return today's date in UK format (DD-MM-YYYY) as a string."""
        return datetime.today().strftime('%d-%m-%Y')

