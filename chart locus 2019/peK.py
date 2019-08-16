import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy import signal
import time
import datetime


RATE = None
data = None


RATE, data = read("Feedday.wav")

data = (data + (2**16)/2)/300

sumofPecks = np.sum(data)
totalFeedPerDay = (sumofPecks*0.025)/1000
print(totalFeedPerDay)


xx = np.linspace(0, 0.24*1000, 0.24*RATE)/10

# print(xx)

plt.figure("1", figsize=(10,6.5))
plt.plot(xx, data)

locs, labels = plt.xticks()           # Get locations and labels
plt.xticks([0, 4, 8, 12, 16, 20, 24], ["0:00", "4:00", "8:00", "12:00", "16:00", "20:00", "24:00"])  # Set locations and labels

# plt.plot(fftVal[0][peakIndex], fftVal[1][peakIndex])
plt.title('# of Peckcount vs Time Graph', fontsize=16)
plt.xlabel('Time of the Day', fontsize=11)
plt.ylabel('Number of Peck Count', fontsize=11)


data = data*0.025


plt.figure("1 weight", figsize=(10,6.5))
plt.plot(xx, data)

locs, labels = plt.xticks()           # Get locations and labels
plt.xticks([0, 4, 8, 12, 16, 20, 24], ["0:00", "4:00", "8:00", "12:00", "16:00", "20:00", "24:00"])  # Set locations and labels

# plt.plot(fftVal[0][peakIndex], fftVal[1][peakIndex])
plt.title('Weight Feed vs Time Graph (#pecks to gram)', fontsize=16)
plt.xlabel('Time of the Day', fontsize=11)
plt.ylabel('Feed Weight (gm)', fontsize=11)



peakIndex, _ = signal.find_peaks(data)

plt.figure("2", figsize=(10,6.5))
plt.plot(xx, data)
plt.plot(xx[peakIndex], data[peakIndex], "r.")
locs, labels = plt.xticks()           # Get locations and labels
plt.xticks([0, 4, 8, 12, 16, 20, 24], ["0:00", "4:00", "8:00", "12:00", "16:00", "20:00", "24:00"])  # Set locations and labels

# plt.plot(fftVal[0][peakIndex], fftVal[1][peakIndex])
plt.title('Find Peaks in the Graph', fontsize=16)
plt.xlabel('Time of the Day', fontsize=11)
plt.ylabel('Feed Weight (gm)', fontsize=11)





plt.figure("3", figsize=(10,6.5))

peakProminance = signal.peak_prominences(data, peakIndex)[0]

contour_heights = data[peakIndex] - peakProminance
plt.plot(xx, data)
plt.plot(xx[peakIndex], data[peakIndex], "r.")
plt.vlines(x=xx[peakIndex], ymin=contour_heights, ymax=data[peakIndex])
locs, labels = plt.xticks()           # Get locations and labels
plt.xticks([0, 4, 8, 12, 16, 20, 24], ["0:00", "4:00", "8:00", "12:00", "16:00", "20:00", "24:00"])  # Set locations and labels


plt.title('Calculate Peak Prominances', fontsize=16)
plt.xlabel('Time of the Day', fontsize=11)
plt.ylabel('Feed Weight (gm)', fontsize=11)





plt.figure("4", figsize=(10,6.5))

mask = peakProminance > 1
peakIndex = peakIndex[mask]
peakProminance = peakProminance[mask]

contour_heights = data[peakIndex] - peakProminance
plt.plot(xx, data)
plt.plot(xx[peakIndex], data[peakIndex], "gX")
plt.vlines(x=xx[peakIndex], ymin=contour_heights, ymax=data[peakIndex])


locs, labels = plt.xticks()           # Get locations and labels
plt.xticks([0, 4, 8, 12, 16, 20, 24], ["0:00", "4:00", "8:00", "12:00", "16:00", "20:00", "24:00"])  # Set locations and labels

plt.title('Show Peaks if peakProminance > Threshold', fontsize=16)
plt.xlabel('Time of the Day', fontsize=11)
plt.ylabel('Feed Weight (gm)', fontsize=11)


plt.show()




