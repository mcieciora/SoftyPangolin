from requests import get
from flask import Blueprint, render_template, request, flash, redirect

from .lang import lang
from .models import Settings
from . import db, create_app
from .utils import get_latest_weather_data, get_last_data_from_model, get_current_weather


views = Blueprint('views', __name__)


@views.route('/')
def home():
    with create_app().app_context():
        latest_settings = get_last_data_from_model(Settings)
        if latest_settings:
            return render_template("home.html", data=get_latest_weather_data(), lang=lang[latest_settings.lang])
        else:
            return redirect('/setup')


@views.route('/history')
def history():
    with create_app().app_context():
        latest_settings = get_last_data_from_model(Settings)
        if latest_settings:
            return render_template("history.html")
        else:
            return redirect('/setup')


@views.route('/setup', methods=['GET', 'POST'])
def setup():
    if request.method == 'POST':
        appid = request.form.get('appid')
        language = request.form.get('lang')
        plan = request.form.get('plan')

        plans = {
            'free': 120,
            'startup': 60
        }

        if get(f'https://api.openweathermap.org/data/2.5/onecall?appid={appid}&lat=0&lon=0').status_code == 200:
            db.session.add(Settings(appid=appid, lang=language, repeat=plans[plan]))
            db.session.commit()
            flash('Settings saved!', category='success')
            get_current_weather()
            return redirect('/')

    return render_template("setup.html")
