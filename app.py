#!usr/bin/env python

from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

# @app.route("/")
# def hello_world():
#     return "<p>Hello World! </p>"