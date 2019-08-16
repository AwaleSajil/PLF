# import time
import numpy as np
var = np.array([9,7])

def sub2():
	print("I'm sub2 and var:", var[1])

def sub1():
	# time.sleep(1)
	print("I'm sub 1 and var:", var[0])
	sub2()
