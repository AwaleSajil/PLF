import time


def printPeak(soundAnalysis):
    for i in range(10000):
        print(i , ": Peack count", soundAnalysis[0])
        print(i , ": Weight Feed", soundAnalysis[1])
        time.sleep(0.1)
