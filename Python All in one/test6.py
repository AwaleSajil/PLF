from flaskServerV1 import *
import time

#accesses the read data and display it 
def displayreadData(getData, soundData):
    while True:
        time.sleep(1)
        print("T: ", getData[0])
        print("H: ", getData[1])
        print("L: ", getData[2])
        print("A: ", getData[3])
        print("#Pecks:", soundData[0])
        print("Feed: ", soundData[1], "gm")
        print("------------------------")


def changesendData(setData):
    while True:
        time.sleep(1)
        setData[0] += 1
        setData[1] += 1
        setData[2] += 1
        setData[3] += 1
    
