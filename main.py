from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/sum', methods=['GET', 'POST'])
def sum():
    if request.method == 'GET':
        params  = request.args

        print(params)

        a = params.get('a', 0)
        b = params.get('b', 0)

    if request.method == 'POST':
        data = request.get_json()
        
        a = data.get('a')
        b = data.get('b')

    return jsonify({"sum": int(a) + int(b)})



if __name__ == '__main__':
    app.run(debug=True)