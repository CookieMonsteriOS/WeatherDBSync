from flask import Flask, request
from database.db import database

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = '' #Replace with your details
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database.init_app(app)

@app.route("/")
def index():
    return "Hello, World!"

@app.route('/weather', methods=['POST'])
def get_weather():
    data = request.get_json()
    lat = data.get('latitude')
    long = data.get('longitude')
    city = data.get('city')
    print(lat,long,city)
    return {"response":"Some inputs recieved"},200

if __name__ == '__main__':
    app.run(debug=True)