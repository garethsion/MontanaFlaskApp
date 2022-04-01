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

@app.route('/toptica_controller')
def toptica_controller():
    # call_lq = laser_quantum.call_lq()
    return render_template('toptica_controller.html')

@app.route('/montana_vnc')
def montana_vnc():
    # call_lq = laser_quantum.call_lq()
    return render_template('montana_vnc.html')

@app.route('/aom_enable')
def aom_enable():
    # call_lq = laser_quantum.call_lq()
    return render_template('aom_enable.html')

@app.route('/p_scan_labview')
def pl_scan_labview():
    # call_lq = laser_quantum.call_lq()
    return render_template('pl_scan_labview.html')

@app.route('/ple_labview')
def ple_labview():
    # call_lq = laser_quantum.call_lq()
    return render_template('ple_labview.html')

@app.route('/wavemeter')
def wavemeter():
    # call_lq = laser_quantum.call_lq()
    return render_template('wavemeter.html')

@app.route('/camera')
def camera():
    # call_lq = laser_quantum.call_lq()
    return render_template('camera.html')

# @app.route("/")
# def hello_world():
#     return "<p>Hello World! </p>"