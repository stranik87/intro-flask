from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello!</p>"

@app.route("/about")
def about():
    return "<p>about page!</p>"

@app.route("/contact")
def contact():
    return "<p>contact page!</p>"

@app.route("/say-hi/<name>")
def hi(name):
    return f"<p>hi {name}!</p>"

@app.route("/number/<int:a>")
def number(a):
    return f"<p>hi {a}!</p>"


if __name__ == '__main__':
    app.run(debug=True)