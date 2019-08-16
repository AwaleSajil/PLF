import time 

#this test changes the temp, humidity, ldr and ammnia data in run time

def changeReadData(readData, soundAnalysis):
    while True:
        time.sleep(1)
        readData[0] += 1
        readData[1] += 1
        readData[2] += 1
        readData[3] += 1

        soundAnalysis[0] += 1
        soundAnalysis[1] += 1

def displaysendData(sendData):
    while True:
        time.sleep(1)
        print("Heater: ", sendData[0])
        print("Fans: ", sendData[1])
        print("Lights: ", sendData[2])
        print("Servo: ", sendData[3])
        print("------------------------")

