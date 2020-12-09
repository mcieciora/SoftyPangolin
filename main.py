#!/usr/bin/env python3
from flask import Flask, render_template
from threading import Timer
from logging import info, error
from Parser import Parser
from Request import Request
from Weather import Weather


config_ini = Parser('config/config.ini')
weather_init = Parser('data/weather.ini')


def setup():
    get_current_location()


def awake():
    read_ini = config_ini.read_ini()
    request = Request(config_ini.read_setting_value('weather_url'), read_ini)
    if request.verify_url() is True:
        get_current_weather(request)


def get_current_weather(request):
    Timer(900, get_current_weather).start()
    return_request = request.send().json()['current']
    weather = Weather(return_request)
    weather.parse_weather_data()


def get_current_location():
    location = Request('https://ipinfo.io/loc', {})
    if location.verify_url() is True:
        lat, lon = location.send().text.replace('\n', '').split(',')
        read_ini = config_ini.read_ini()
        read_ini['lat'], read_ini['lon'] = lat, lon
        config_ini.save_data(read_ini)
    else:
        error('[ERR] Cannot get current location!')


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', data=weather_init.read_ini())


if __name__ == '__main__':
    setup()
    awake()
    app.run(host='127.0.0.1', port=5000)
