
from flask import Flask, request, jsonify


app = Flask(__name__)



@app.route("/hello" , methods=['GET','POST'])
def hello_world():
    if request.method=="GET":
        return ["Hello World"]
    elif request.method=="POST":
        return ["Hello World"]
    


@app.route("/add" , methods=['GET','POST'])
def add():
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



@app.route("/sub" , methods=['GET','POST'])
def sub():
    if request.method=="GET":
        paramis=request.args
        a=paramis.get("a")
        b=paramis.get("b")
    elif request.method=="POST":
        data=request.get_json()
        a=data.get("a")
        b=data.get("b")
    s=int(a)-int(b)    
    return jsonify({"cub":abs(s)})

        
    
@app.route("/mul" , methods=['GET','POST'])
def mul():
    if request.method=="GET":
        paramis=request.args
        a=paramis.get("a")
        b=paramis.get("b")
    elif request.method=="POST":
        data=request.get_json()
        a=data.get("a")
        b=data.get("b")
    s=int(a)*int(b)    
    return jsonify({"mul":s})


 
@app.route("/div" , methods=['GET','POST'])
def div():
    if request.method=="GET":
        paramis=request.args
        a=paramis.get("a")
        b=paramis.get("b")
    elif request.method=="POST":
        data=request.get_json()
        a=data.get("a")
        b=data.get("b")
    s=int(a)/int(b)    
    return jsonify({"div":s}) 
        

     



if __name__ == '__main__':
    app.run(debug=True)