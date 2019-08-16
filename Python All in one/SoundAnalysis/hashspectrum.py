import pyaudio
import numpy as np

import matplotlib.pyplot as plt

CHUNK = 2048
RATE = 44100


def getFFT(data,rate):
    """Given some data and rate, returns FFTfreq and FFT (half)."""
    data=data*np.hamming(len(data))
    fft=np.fft.fft(data)
    fft=np.abs(fft)
    #fft=10*np.log10(fft)
    freq=np.fft.fftfreq(len(fft),1.0/rate)
    return freq[:int(len(freq)/2)],fft[:int(len(fft)/2)]

p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK)

# for i in range(int(10*44100/1024)): #go for a few seconds
data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
# peak=np.average(np.abs(data))*2
# bars="#"*int(50*peak/2**16)
# print("%04d %05d %s"%(i,peak,bars))


fftx, ffty = getFFT(data,RATE)

print(fftx, ffty)
plt.plot(fftx, ffty)
plt.show


stream.stop_stream()
stream.close()
p.terminate()