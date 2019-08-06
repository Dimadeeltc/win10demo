from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    print("Hello world")


@app.route('/<string:name>')
def dima(name):
    name = name.capitalize()
    return f"<h1>Hello, {name}!</h1>"
