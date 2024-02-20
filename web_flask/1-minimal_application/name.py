#!/usr/bin/python3

from flask import Flask

app =  Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return 'Index Page'

@app.route('/hello/<name>')
def hello(name):
    print(name)
    return f'Hello, {name}!'

if __name__=="__main__":
    app.run(debug=True)