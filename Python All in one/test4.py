import time

def changesendData(sendData):
    
    while True:
        sendData[0] += 1
        sendData[1] += 1
        sendData[2] += 1
        sendData[3] += 1
        time.sleep(1)


