from datetime import datetime
from logging import error
from Parser import Parser


class Weather:
    def __init__(self, request):
        self.request = request

    @property
    def request(self):
        return self.__request

    @request.setter
    def request(self, data):
        if type(data) is dict:
            self.__request = data
        else:
            self.__request = {}

    def parse_weather_data(self):
        if self.request:
            self.request['weather'] = self.request['weather'][0]['description'].capitalize()
            self.request['sunrise'] = datetime.fromtimestamp(self.request['sunrise']).strftime('%H:%M')
            self.request['sunset'] = datetime.fromtimestamp(self.request['sunset']).strftime('%H:%M')
            self.request['date'] = datetime.now().strftime('%d-%m-%Y %H:%M')

            units = {
                'temp': '°C',
                'feels_like': '°C',
                'pressure': 'hpa',
                'wind_speed': 'm/s',
                'humidity': '%%',
                'clouds': '%%',
                'weather': '',
                'sunrise': '',
                'sunset': '',
                'date': ''
            }

            for key in list(self.request):
                if key in units.keys():
                    if type(self.request[key]) is float:
                        self.request[key] = round(self.request[key], 1)
                    self.request[key] = str(self.request[key]) + units[key]
                else:
                    self.request.pop(key)
            Parser.save_data(self.request, 'data/weather.ini')
        else:
            error("ERROR: Nothing to parse. Request return is empty!")
