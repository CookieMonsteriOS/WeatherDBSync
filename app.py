from flask import Flask, request,jsonify
from database.db import database
from services.weather_requests import weather_location_request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@127.0.0.1/weather' #Replace with your details
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

if __name__ == '__main__':
    app.run(debug=True)