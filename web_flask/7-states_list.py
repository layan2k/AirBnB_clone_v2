#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
"""

from models import storage
from models import *
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def tearDown(self):
    """Closes each SQLAlchemyTask"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def display_html():
    """Displays html page"""
    stateobjs = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template("7-states_list.html", stateobjs=stateobjs)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
