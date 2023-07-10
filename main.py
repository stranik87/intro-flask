from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    fruits = [
        {
            'name': 'apple',
            'price': 10
        },
        {
            'name': 'banana',
            'price': 20
        },
        {
            'name': 'orange',
            'price': 30
        },
        {
            'name': 'lemon',
            'price': 10
        }
    ]
    return render_template('index.html', fruits=fruits)

if __name__ == '__main__':
    app.run(debug=True)
