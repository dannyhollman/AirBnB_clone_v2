from flask import Flask
"""  starts a flask web application """
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """ returns Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """ returns HBNB """
    return "HBNB"


@app.route('/c/<text>')
def text(text):
    """ prints text """
    return "C {}".format(text.replace('_', ' '))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
