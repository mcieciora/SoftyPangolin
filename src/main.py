#!/usr/bin/env python3
from website import create_app
from website.utils import get_current_weather

app = create_app()


if __name__ == '__main__':
    get_current_weather()
    app.run(debug=True, use_reloader=False)
