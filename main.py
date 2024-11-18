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

                if temp_celsius < 5:
                    message = """With the temperature of your city, here are the plants you can sow: 
                                    1)Garlic: Garlic cloves can be planted in cool soil in late fall for
                                    overwintering or early spring for spring harvest.
                                    2)Onions: Onions can tolerate cool soil temperatures and are often planted early in the spring.
                                    3)winter wheat"""
                    weather_image = "static/cloud(2).jpg"

                elif 5 <= temp_celsius < 10:
                    message = """With the temperature of your city, here are plants you can sow:
                                1)Carrots: Carrots can be sown in cool soil and will germinate at temperatures as low as 5°C.
                                2)Peas: Peas can be planted as soon as the soil reaches 5-10°C for an early spring crop.
                                3)Lettuce: Lettuce seeds can be sown directly into cool soil for early spring harvests.
                                4)spinach
                                5)beets
                                6)radishes
                                7)turnips"""
                    weather_image = "static/cloud(1).jpg"
                elif 10 <= temp_celsius < 17:
                    message="""With the temperature of your city, here are plants you can sow:
                                1)Beans: Beans prefer warmer soil temperatures and should be planted when the soil has warmed to at least 10°C.
                                2)Corn: Corn seeds should be planted in soil that has warmed to at least 10°C for optimal germination.
                                3)Tomatoes: Tomato plants thrive in warm soil and should be planted after the soil has reached 10-18°C.
                                4)Herbs (e.g. parsley, cilantro)
                                5)spring wheat"""
                    weather_image = "static/download.jpg"
                elif 17 <= temp_celsius < 21:
                    message ="""With the temperature of your city, here are plants you can sow:
                                1)Herbs: e.g Some herbs like basil prefer warmer temperatures, around 18°C (64°F) or higher.
                                2)Cucumbers: Cucumber seeds should be planted in warm soil, typically when temperatures are consistently above 18°C.
                                3)Squash: Squash plants prefer warm soil and should be planted after the soil has warmed to at least 18°C.
                                4)Melons: Melon seeds should be planted in warm soil, typically when temperatures are consistently above 18°C
                                """
                    weather_image = "static/download.jpg"
                elif temp_celsius >= 21 and temp_celsius < 32:
                    message= """With the temperature of your city, here are plants you can sow:
                                1)Peppers
                                2)Watermelons
                                3)Okra"""
                    weather_image = "static/Fairy World.jpg"            