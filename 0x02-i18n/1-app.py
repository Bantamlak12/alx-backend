#!/usr/bin/env python3
"""File: 1-app.py
"""
from flask import Flask, render_template
from flask_babel import Babel
from typing import List


class Config:
    """Config
    """
    LANGUAGES: List[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def home() -> str:
    """Home"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
