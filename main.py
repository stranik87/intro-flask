
from flask import Flask, request, jsonify


app = Flask(__name__)



@app.route("/sum" , methods=['GET','POST'])
def hello_world():
    return "<p>Hello! WORLD</p>"



@app.route("/sum" , methods=['GET','POST'])
def sum():
    if request.method=="GET":
        paramis=request.args

        a=paramis.get("a")
        b=paramis.get("b")

    elif request.method=="POST":
        data=request.get_json()

        a=data.get("a")
        b=data.get("b")
    s=int(a)+int(b)    
    return jsonify({"sum":s}) 



if __name__ == '__main__':
    app.run(debug=True)