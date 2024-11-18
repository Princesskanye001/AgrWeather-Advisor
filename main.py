import datetime as dt
import requests
from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "baab4fef1af1a796ef7429d969971b73"