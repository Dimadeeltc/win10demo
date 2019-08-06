from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    names = ['Bob', 'Charlie', 'Alice']
    return render_template('index_list.html', names=names)
