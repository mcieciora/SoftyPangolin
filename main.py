#!/usr/bin/env python3
from flask import Flask, render_template
from threading import Timer
from datetime import datetime
from Config import Config
from Request import Request

baseconf = Config('config/config.ini', 'config/example.ini')
url = 'https://api.openweathermap.org/data/2.5/onecall?'


def get_current_weather():
    Timer(900, get_current_weather).start()
    r = Request(url, baseconf.read_config()).send()
    r['date'] = datetime.now().strftime('%d-%m-%Y %H:%M')
    baseconf.save_data(r)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', data=baseconf.read_data())


if __name__ == '__main__':
    get_current_weather()
    app.run(host='0.0.0.0', port=5000)
