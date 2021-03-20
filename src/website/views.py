from flask import Blueprint, render_template
from .utils import get_latest_weather_data

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html", data=get_latest_weather_data())


@views.route('/history')
def history():
    return render_template("history.html", data='')


@views.route('/settings')
def settings():
    return render_template("settings.html")
