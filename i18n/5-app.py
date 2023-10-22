#!/usr/bin/env python3
""" Basic Flask app, Basic Babel setup """
from flask import Flask, render_template, request, g
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


@babel.localeselector
def get_locale():
    """ to determine the best match with our supported languages """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """ returns a user dictionary or None
    if the ID cannot be found or if login_as was not passed """
    user_id = request.args.get('login_as')
    if user_id and user_id.isnumeric():
        user_id = int(user_id)
        user = users.get(user_id)
        return user
    return None
    

@app.before_request
def before_request():
    g.user = get_user()


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)


@app.route('/')
def root():
    """ basic Flask app """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
