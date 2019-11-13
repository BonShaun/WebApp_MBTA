"""
Simple "Hello, World" application using Flask
"""

from flask import Flask
from mbta_helper import find_stop_near

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/<place_name>')
def get_stop(place_name):
    stop, is_accessible =  find_stop_near(place_name)
    if stop:
        if is_accessible == 1:
            return f'{stop} is wheelchair accessible'
        else:
            return f'{stop} is not wheelchair accessible'
