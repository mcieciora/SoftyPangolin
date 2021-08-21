from . import db


class WeatherData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime())
    sunrise = db.Column(db.String(50))
    sunset = db.Column(db.String(50))
    temp = db.Column(db.Float())
    feels_like = db.Column(db.Float())
    icon = db.Column(db.String(75))
    weather = db.Column(db.String(100))
    pressure = db.Column(db.Integer())
    wind_speed = db.Column(db.Float())
    clouds = db.Column(db.Integer())
    humidity = db.Column(db.Integer())

    def __init__(self, request_dict):
        for key in request_dict:
            if hasattr(self, key):
                if type(request_dict[key]) is float:
                    request_dict[key] = round(request_dict[key], 1)
                setattr(self, key, request_dict[key])

    def get_dict(self):
        return vars(self)


class Settings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    appid = db.Column(db.String(50))
    lang = db.Column(db.String(2))
    lat = db.Column(db.Integer())
    lon = db.Column(db.Integer())
    repeat = db.Column(db.Integer())

    def get_dict(self):
        return vars(self)
