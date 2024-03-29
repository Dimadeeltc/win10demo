import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()
    new_year = now.month == 8 and now.day == 2
    return render_template('index_ny.html', new_year=new_year)
