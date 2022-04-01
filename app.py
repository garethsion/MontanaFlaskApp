#!usr/bin/env python
import spd3303x
import laser_quantum
from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/power_supply')
def power_supply():
    ps = spd3303x.PowerSupply()
    ps.connect(USB=True) # for the time being, just connect when the webpage is opened
    return render_template('power_supply.html')

@app.route('/laser_controller')
def laser_controller():
    call_lq = laser_quantum.call_lq()
    return render_template('laser_controller.html')


# @app.route("/")
# def hello_world():
#     return "<p>Hello World! </p>"