from flask import Flask, abort, render_template
""" starts a flask web application """
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
def c(text):
    """ returns text """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python(text='is cool'):
    """ returns text """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<n>')
def number(n):
    """ returns if number """
    if n.isnumeric():
        return "{} is a number".format(n)
    else:
        abort(404)


@app.route('/number_template/<n>')
def template(n):
    """ returns if number """
    if n.isnumeric():
        return render_template('5-number.html', n=n)
    else:
        abort(404)


@app.route('/number_odd_or_even/<n>')
def oddeven(n):
    """ returns odd or even """
    if n.isnumeric():
        if int(n) % 2 == 0:
            oddeven = "even"
        else:
            oddeven = "odd"
        return render_template('6-number_odd_or_even.html', n=int(n),
                               oddeven=oddeven)
    else:
        abort(404)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
