from sys import exit
from logging import error
from threading import Timer
from sqlalchemy import desc
from datetime import datetime
from requests import get, ConnectionError
from . import db
from .models import WeatherData
from website import create_app


def get_current_location():
    location = get('https://ipinfo.io/loc')
    try:
        return location.text.replace('\n', '').split(',')
    except ConnectionError:
        error('Error: Please check your internet connection!')
        exit()


def get_current_weather():
    Timer(60, get_current_weather).start()
    if (return_request := send_weather_request()).status_code == 200:
        request = return_request.json()['current']
        if request:
            request['date'] = datetime.now()
            request['sunrise'] = datetime.fromtimestamp(request['sunrise']).strftime('%H:%M')
            request['sunset'] = datetime.fromtimestamp(request['sunset']).strftime('%H:%M')
            request['icon'] = f"icons/{request['weather'][0]['icon'][:2]}.png"
            request['weather'] = request['weather'][0]['description'].capitalize()

            with create_app().app_context():
                db.session.add(WeatherData(request))
                db.session.commit()
    else:
        error('Error {}: {} at {}. Url or data is not valid.'.format(return_request.status_code, return_request.reason,
                                                                     return_request.url))


def get_latest_weather_data():
    units = {
        'temp': '°C',
        'feels_like': '°C',
        'pressure': 'hpa',
        'wind_speed': 'm/s',
        'humidity': '%',
        'clouds': '%',
    }
    weather_data_query = WeatherData.query
    weather_data_ordered_descending = weather_data_query.order_by(desc(WeatherData.id))
    latest_weather_data = weather_data_ordered_descending.first().get_dict()
    for key in list(units):
        latest_weather_data[key] = str(latest_weather_data[key]) + units[key]
    return latest_weather_data


def send_weather_request():
    data_list = []
    call_data = {
        'units': 'metric',
        'exclude': 'minutely,hourly,daily',
        'lang': 'pl',
        'appid': '',
        'lat': '',
        'lon': ''
    }
    weather_url = 'https://api.openweathermap.org/data/2.5/onecall?'
    for key, value in call_data.items():
        data_list.append('{}={}'.format(key, value))
    weather_url += '&'.join(data_list)
    return get(weather_url)
