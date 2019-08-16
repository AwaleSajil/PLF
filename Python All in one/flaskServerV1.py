from flask import Flask, render_template
from flask import request
import random

# from test6 import *

#global reference variables from shared memory
soundData = None 
setData = None
getData = None
imageData = None



#code to communication between the shared memory and the server
#interface

def getPeckCount():
    global soundData
    return int(soundData[0])

def getPeckFeed():
    global soundData
    return soundData[1]

def getTemperature():
    global getData
    return getData[0]

def getHumidity():
    global getData
    return getData[1]

def getLDR():
    global getData
    return getData[2]

def getAmmonia():
    global getData
    return getData[3]

def setHeater(hValue):
    global setData
    setData[0] = hValue

def setFan(fValue):
    global setData
    setData[1] = fValue

def setLight(lValue):
    global setData
    setData[2] = lValue

def setServo(sValue):
    global setData
    setData[3] = sValue

def setAutoControl(aValue):
    global setData
    setData[4] = aValue

def getDistributionIndex():
    global imageData
    return imageData[0]

def getMobilityIndex():
    global imageData
    return imageData[1]


heater=str()
fan=str()
light=str()
servo=str()
autostate=str()


# flask code
app = Flask(__name__)

def openORclose(x):
    if x=="0":
        x="OFF"
        return x
    else:
        x="ON"
        return x


@app.route('/index', methods=['GET', 'POST'])
def index():
    x = getTemperature()
    y = getHumidity()
    z = int((getLDR())/(1023)*100)
    w = int((getAmmonia())/(1023)*100)
    u = getPeckCount()
    v = getPeckFeed()
    s = getDistributionIndex()
    t = getMobilityIndex()
    # x=random.randint(50,100)
    # y=random.randint(20,45)
    # z=random.randint(40,60)
    # w =random.randint(20,30)
    texts=str(x)+" "+str(y)+" "+str(z) + " " + str(w)+ " " + str(u)+ " " + str(v)+ " " + str(s)+ " " + str(t)
    return """{}""".format(texts)


@app.route('/heater', methods=['GET','POST'])
def heaters():
    global heater
    if request.method=='POST':
        heater = request.get_data(as_text=True)
        setHeater(int(heater))
        
    return """{} %""".format(heater)
    

@app.route('/fan', methods=['GET','POST'])
def fans():
    global fan
    if request.method=='POST':
        fan = request.get_data(as_text=True)
        setFan(int(fan))
        fan=openORclose(fan)

    return """Fan is {}""".format(fan)


@app.route('/light', methods=['GET','POST'])
def lights():
    global light
    if request.method=='POST':
        light = request.get_data(as_text=True)
        setLight(int(light))
        light=openORclose(light)

    return """Light is {}""".format(light)

@app.route('/servo', methods=['GET','POST'])
def servos():
    global servo
    if request.method=='POST':
        servo = request.get_data(as_text=True)
        setServo(int(servo))
        servo=openORclose(servo)


    return """Ventilation is {}""".format(servo)


@app.route('/auto', methods=['GET','POST'])
def autos():
    global autostate
    if request.method=='POST':
        autostate = request.get_data(as_text=True)
        setAutoControl(int(autostate))

    return"""automatic mode {}""".format(autostate)


def flaskServer(soundAnalysis, sendData, readData, imageAnalysis):
    global soundData, setData, getData, imageData
    soundData = soundAnalysis
    setData = sendData
    getData = readData
    imageData = imageAnalysis



    #tests here from test 6
    # displayreadData(getData,soundData)

    # changesendData(setData)

    
    ##create a server
    #app.run(host='0.0.0.0')
    #app.run(port=5555)
    #app.run(host='192.168.1.69', port=9000)
    app.run(host='192.168.43.224', port=9000)
    #app.run(host='10.100.0.152', port=9000)










#testing this module only
if __name__=="__main__":
    #app.run(host='0.0.0.0')
    #app.run(port=5555)
    #app.run(host='192.168.1.69', port=9000)
    app.run(host='192.168.43.7', port=9000)








