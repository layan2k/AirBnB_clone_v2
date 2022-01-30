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


@app.route('/hbnb_filters', strict_slashes=False)
def filters_html(state_id=None):
    """Displays html hbnh filters"""
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
