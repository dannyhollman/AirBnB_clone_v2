from flask import Flask
""" starts a flask web application """
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """ return hello HBNB! """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
