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


@app.route('/hbnb', strict_slashes=False)
def html_all_filters():
    """display html  """
    state_objs = [s for s in storage.all("State").values()]
    amenity_objs = [a for a in storage.all("Amenity").values()]
    place_objs = [p for p in storage.all("Place").values()]
    user_objs = [u for u in storage.all("User").values()]
    place_owner_objs = []
    for place in place_objs:
        for user in user_objs:
            if place.user_id == user.id:
                place_owner_objs.append(["{} {}".format(
                    user.first_name, user.last_name), place])
    place_owner_objs.sort(key=lambda p: p[1].name)
    return render_template('100-hbnb.html',
                           state_objs=state_objs,
                           amenity_objs=amenity_objs,
                           place_owner_objs=place_owner_objs)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
