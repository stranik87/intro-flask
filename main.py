from flask import Flask, request

app = Flask(__name__)


@app.route('/sum')
def sum():
    if request.method == 'GET':
        params  = request.args

        print(params)

        a = params.get('a', 0)
        b = params.get('b', 0)

        return f"result: {int(a) + int(b)}"



if __name__ == '__main__':
    app.run(debug=True)