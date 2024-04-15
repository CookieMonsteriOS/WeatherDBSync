from flask import Flask, request,jsonify
from database.db import database
from services.current_weather_requests import weather_location_request
from services.average_weather import get_average_weather_data

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = '' #Replace with your details
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database.init_app(app)

@app.route("/")
def index():
    return "Index"

@app.route('/weather', methods=['POST'])
def get_weather():
    data = request.get_json()
    lat = data.get('latitude')
    long = data.get('longitude')
    city = data.get('city')
    weather_data = weather_location_request(latitude=lat,longitude=long,city=city)
    return jsonify(weather_data),200

@app.route('/weather/average/<int:location_id>', methods=['GET'])
def get_average_weather(location_id):
    start_date = request.args.get('start_date')
    end_date = request.args.get('start_date')
    avg_weather_data = get_average_weather_data(location_id,start_date,end_date)
    return jsonify(avg_weather_data),200

if __name__ == '__main__':
    app.run(debug=True)