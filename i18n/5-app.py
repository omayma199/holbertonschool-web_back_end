#!/usr/bin/env python3
""" Basic Flask app, Basic Babel setup """
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)
""" instantiate the Babel object """


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
"""Mock user database"""
class Config:
    """
    config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
""" Use that class as config for Flask app """


@babel.localeselector
def get_locale():
    """
    Check if the 'locale' parameter is present in the request's query string
    """
    requested_locale = request.args.get('locale')

    """
    If the requested locale is a supported language, return it
    """
    if requested_locale in app.config['LANGUAGES']:
        return requested_locale
    """ to determine the best match with our supported languages """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """ returns a user dictionary or None
    if the ID cannot be found or if login_as was not passed """
    try:
        userId = request.args.get('login_as')
        return users[int(userId)]
    except Exception:
        return None


@app.route('/')
def root():
    """ basic Flask app """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
