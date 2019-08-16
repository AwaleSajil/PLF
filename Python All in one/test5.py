import time

def displayreadData(readData):
    while True:
        time.sleep(1)
        print("T:", readData[0])
        print("H:", readData[1])
        print("L:", readData[2])
        print("A:", readData[3])
        print("-----------------")
