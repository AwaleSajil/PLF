from scipy import signal
import numpy as np
import matplotlib.pyplot as plt


xs = np.arange(0, 20, 0.1)

data = np.sin(xs) + 0.6 * np.sin(2.6 * xs) + 2*np.cos(3.4*xs)

peaks, _ = signal.find_peaks(data)

# peakind = signal.find_peaks_cwt(data, np.arange(1,10,1))

peakProminance = signal.peak_prominences(data, peaks)[0]

contour_heights = data[peaks] - peakProminance

print(peakProminance)
print(np.max(data))


plt.vlines(x=xs[peaks], ymin=contour_heights, ymax=data[peaks])

plt.plot(xs,data)
plt.plot(xs[peaks], data[peaks], 'rx')
plt.show()
# print(peakind, xs[peakind], data[peakind])

