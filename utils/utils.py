import datetime

class Utils:

    def kelvin_to_celsius(self,temperature_kelvin):
        """Convert temperature from Kelvin to Celsius."""
        return temperature_kelvin - 273.15

    def epoch_to_human_readable(self,epoch_time):
        """Convert epoch time to human-readable format."""
        timestamp = datetime.datetime.fromtimestamp(epoch_time)
        return timestamp.strftime('%Y-%m-%d %H:%M:%S')


