from flask import Flask, render_template
from flask import request
import random
from ardtopycomm import *



# flask code
app = Flask(__name__)
# codes from python-arduino side
# ports = serial_ports()
# print(ports)
# usb_port = serial.Serial(ports[0], baudrate=9600, timeout=0.5)
# read_from_Arduino_instance = ReadFromArduino(usb_port, verbose=6)


heater=str()
fan=str()
light=str()
servo=str()

@app.route('/index', methods=['GET', 'POST'])
def index():
    # read_from_Arduino_instance.read_one_value()
    # values = np.array(read_from_Arduino_instance.latest_values)
    x=random.randint(20,100)
    y=random.randint(20,85)
    z=random.randint(70,100)
    # x= values[0]
    # y= values[1]
    # z= values[2]
    texts=str(x)+" "+str(y)+" "+str(z)
    return """{}""".format(texts)


@app.route('/heater', methods=['GET','POST'])
def heater():
    
    global heater
    if request.method=='POST':
        heater = request.get_data(as_text=True)

    return """At {} °C""".format(heater)
    

@app.route('/fan', methods=['GET','POST'])
def fan():
    
    global fan
    if request.method=='POST':
        fan = request.get_data(as_text=True)

    return """Fan is {}""".format(fan)


@app.route('/light', methods=['GET','POST'])
def light():
    
    global light
    if request.method=='POST':
        light = request.get_data(as_text=True)

    return """Light is {}""".format(light)

@app.route('/servo', methods=['GET','POST'])
def servo():
    global servo
    if request.method=='POST':
        servo = request.get_data(as_text=True)

    return """Servo is {}""".format(servo)


@app.route('/auto', methods=['GET','POST'])
def auto():
    if request.methods=='POST':
        autoState = request.get_data(as_text=True)

    return"""automatic mode {}""".format(autoState)

#app.run(port=5555)
app.run(host='192.168.1.69', port=8070)
#app.run(host='192.168.1.7', port=8070)


