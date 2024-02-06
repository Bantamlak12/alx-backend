#!/usr/bin/env python3
"""
File: 1-app.py

Basic Babel setup
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import List


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    Configures available languages
    """
    LANGUAGES: List[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"


app: Flask = Flask(__name__)
app.config.from_object(Config)
babel: Babel = Babel(app)


@app.route('/')
def home() -> str:
    """
    Returns:
    - The html file
    """
    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    """
    Returns:
    - Best language match
    """
    # Locale from URL parameters
    locale = request.args['locale']
    if locale in app.config['LANGUAGES']:
        return locale

    # Locale from user settings
    if g.user:
        locale = g.user['locale']
        if locale in app.config['LANGUAGES']:
            return locale

    # Locale from request header
    locale = request.headers['locale']
    if locale in app.config['LANGUAGES']:
        return locale

    # Default locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """
    Returns:
    - User dictionary or None if the ID cannot be found.
    """
    try:
        id = int(request.args.get('login_as'))
        if id in users.keys():
            return users[id]
        else:
            return None
    except TypeError:
        return None


@app.before_request
def before_request():
    """
    Sets a user global on flask.g.user
    """
    g.user = get_user()


if __name__ == "__main__":
    app.run(debug=True)
