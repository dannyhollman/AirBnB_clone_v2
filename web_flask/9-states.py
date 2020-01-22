#!/usr/bin/python3
from flask import Flask, abort, render_template
from models import storage
""" starts a flask web application """
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def states():
    """ display states """
    states = storage.all("State")
    switch = 0
    return render_template('9-states.html', states=states, switch=switch)


@app.route('/states/<id>')
def states_id(id):
    """ display state by id """
    s = storage.all("State")
    switch = 1
    for k, v in s.items():
        if v.id == id:
            return render_template('9-states.html', states=v, switch=switch)

    return render_template('9-states.html', states=None, switch=switch)


@app.teardown_appcontext
def teardown(error):
    """ close after request """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
