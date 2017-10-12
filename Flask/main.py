from flask import Flask, render_template, jsonify, request
import huff
import knapsack as kp
import json
import numpy as np
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/huffman')
def huffman():
    return render_template("huffman.html")

@app.route('/knapsack')
def knapsack_page():
    return render_template("knapsack.html")

@app.route('/_textmanipulator')
def text_manipulator():
    print("calling")
    txt = request.args.get('txt')
    newt = huff.huffman(txt)
    return jsonify(result=newt)

@app.route('/_knapsack')
def knap_func():
    par1 = int(request.args.get('par1'))
    #print(par1)

    par2 = int(request.args.get('par2'))
    #print(par2)
    res = kp.knapsack(par1,par2)
    res2 = np.array(res)

    
    print(res)
    return json.dumps(res2.tolist())
# @app.route('/Huffman/<username>')
# def profile(username):
#     return "Welcome %s" % request.method

if __name__ == "__main__":
    app.run(threaded=True, debug=True)
