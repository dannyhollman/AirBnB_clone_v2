from flask import Flask, abort, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello():
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    return "HBNB"

@app.route('/c/<text>')
def c(text):
    return "C {}".format(text.replace('_', ' '))

@app.route('/python')
@app.route('/python/<text>')
def python(text='is cool'):
    return "Python {}".format(text.replace('_', ' '))

@app.route('/number/<n>')
def number(n):
    if n.isnumeric():
        return "{} is a number".format(n)
    else:
        abort(404)

@app.route('/number_template/<n>')
def template(n):
    if n.isnumeric():
        return render_template('5-number.html', n=n)
    else:
        abort(404)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
