#!/usr/bin/python3
from flask import Flask, abort, render_template
from models import storage
""" starts a flask web application """
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states():
    """ display HTML page """
    s = storage.all("State")
    return render_template('8-cities_by_states.html', storage=s)


@app.teardown_appcontext
def teardown(error):
    """ close after request """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
