from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_view():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"<h1>Answer: {add(a, b)}</h1>"

@app.route('/sub')
def sub_view():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"<h1>Answer: {sub(a, b)}</h1>"

@app.route('/mult')
def mult_view():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"<h1>Answer: {mult(a, b)}</h1>"

@app.route('/div')
def div_view():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"<h1>Answer: {div(a, b)}</h1>"

ops = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<operation>')
def all_in_one(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"<h1>Answer: {ops[operation](a,b)}</h1>"