import time
import cv2 as cv
import numpy as np
import os

def rskIndex(rsk_image_analysis):

    data = np.genfromtxt('data.csv', delimiter=',')
    # print(data)

    while(True):

        vid = cv.VideoCapture('chicken.mp4')
        i=0
        state=0
        
        while(vid.isOpened() and i<200):
            ret, frame = vid.read()

            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            cv.imshow('object_tracking',frame)

            rsk_image_analysis[0] = data[i,0]
            rsk_image_analysis[1] = data[i,1]

            i += 1
            time.sleep(0.17)

            ch = cv.waitKey(1)
            if ch == 27:
                state=1
                break

            cv.waitKey(1)

        vid.release()
        
        if(state==1):
            state=0
            break
    
    cv.destroyAllWindows()