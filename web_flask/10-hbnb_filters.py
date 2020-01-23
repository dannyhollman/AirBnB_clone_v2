#!/usr/bin/python3
from flask import Flask, abort, render_template
from models import storage
""" starts a flask web application """
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def nav_bar():
    """ display states """
    states = storage.all('State')
    amenities = storage.all('Amenity')
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(error):
    """ close after request """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
