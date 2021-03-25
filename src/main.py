#!/usr/bin/env python3
from website import create_app
from website.utils import get_last_data_from_model, get_current_weather
from website.models import Settings

app = create_app()


if __name__ == '__main__':
    with create_app().app_context():
        latest_settings = get_last_data_from_model(Settings)
        if latest_settings:
            get_current_weather()
    app.run(use_reloader=False, host='0.0.0.0')
