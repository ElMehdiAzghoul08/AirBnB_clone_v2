#!/usr/bin/python3
"""script that starts a Flask web application -Python is cool"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_():
    "function"
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    "function"
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def txt_c_(text):
    "function"
    return "C " + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pytxt_(text="is cool"):
    "function"
    return "Python " + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
