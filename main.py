import datetime as dt
import requests
from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "baab4fef1af1a796ef7429d969971b73"

def temperature_to_celsius_fahrenheit(temperature):
    celsius = temperature - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

@app.route("/", methods=["GET", "POST"])
def index():
    error_message = None
    weather_image = None
    if request.method == "POST":
        city = request.form["city"]
        url = BASE_URL + "appid=" + API_KEY + "&q=" + city
        while True:
            response = requests.get(url)
            if response.status_code ==200:
                data = response.json()
                temp = data['main']['temp']
                temp_celsius, temp_fahrenheit = temperature_to_celsius_fahrenheit(temp)
                feels_like_temp = data['main']['feels_like']
                feels_like_celsius, feels_like_fahrenheit = temperature_to_celsius_fahrenheit(feels_like_temp)
                wind_speed = data['wind']['speed']
                humidity = data['main']['humidity']
                description = data['weather'][0]['description']
                sunrise_time = dt.datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone'])
                sunset_time = dt.datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone'])