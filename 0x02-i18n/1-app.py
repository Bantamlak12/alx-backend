#!/usr/bin/env python3
"""File: 1-app.py
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config
    """
    LANGUAGES = ["en", "fr"]
    app.config["BEBEL_DEFAULT_LOCALE"] = "en"
    app.config["BABEL_DEFAULT_TIMEZONE"] = "UTC"

    @app.route('/')
    def home():
        return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
