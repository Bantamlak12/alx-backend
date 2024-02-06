#!/usr/bin/env python3
"""
File: 1-app.py

Basic Babel setup
"""
from flask import Flask, render_template, request
from flask_babel import Babel
from typing import List


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
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """
    Returns:
    - Best language match
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(debug=True)
