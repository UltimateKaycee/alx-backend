#!/usr/bin/env python3
"""
Module for Flask app
"""
from flask import (
    Flask,
    render_template,
    request,
    g
)
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """
    Class for configuration for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """
    Function to return user dictionary or None if ID isn't found
    or if 'login_as' URL parameter isn't found
    """
    id = request.args.get('login_as', None)
    if id is not None and int(id) in users.keys():
        return users.get(int(id))
    return None


@app.before_request
def before_request():
    """
    Function to add user to flask.g if user is found
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """
    Function to return best supported  language match
    """
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Function to handle / route
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
