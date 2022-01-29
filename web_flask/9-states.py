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


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def display_html(state_id=None):
    """Displays html page"""
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
