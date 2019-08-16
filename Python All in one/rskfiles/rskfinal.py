import time
import cv2 as cv
import numpy as np
import os

def rskIndex(rsk_image_analysis):

    vid = cv.VideoCapture('chicken.mp4')

    data = np.genfromtxt('data.csv', delimiter=',')
    print(data)
    i=0

    while(vid.isOpened()):
        ret, frame = vid.read()

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        cv.imshow('frame',frame)

        rsk_image_analysis[0] = data[i,0]
        rsk_image_analysis[1] = data[i,1]

        i += 1;
        time.sleep(0.2)

        ch = cv.waitKey(1)
        if ch == 27:
            break

        cv.waitKey(1)

    i=0

    vid.release()
    cv.destroyAllWindows()