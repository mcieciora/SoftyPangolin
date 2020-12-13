#!/usr/bin/env python3
from flask import Flask, render_template
from threading import Timer
from logging import error
from Parser import Parser
from Request import Request
from Weather import Weather


config_ini = Parser('config/config.ini')
weather_init = Parser('data/weather.ini')


def setup():
    get_current_location()


def create_request():
    read_ini = config_ini.read_ini()
    url = config_ini.read_setting_value('weather_url')
    return Request(url, read_ini)


def get_current_weather():
    Timer(300, get_current_weather).start()
    if (return_request := create_request().send()).status_code == 200:
        weather = Weather(return_request.json()['current'])
        weather.parse_weather_data()
    else:
        error('Error {}: {} at {}. Url or data is not valid.'.format(return_request.status_code, return_request.reason,
                                                                     return_request.url))


def get_current_location():
    location = Request('https://ipinfo.io/loc', {})
    lat, lon = location.send().text.replace('\n', '').split(',')
    read_ini = config_ini.read_ini()
    read_ini['lat'], read_ini['lon'] = lat, lon
    config_ini.save_data(read_ini)


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', data=weather_init.read_ini())


if __name__ == '__main__':
    setup()
    get_current_weather()
    app.run(host='127.0.0.1', port=5000)
