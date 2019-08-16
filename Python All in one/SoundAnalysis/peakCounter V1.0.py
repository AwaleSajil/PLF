import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import time

CHUNK = 1024*2
RATE = 44100

freqRange = [1200, 1600]
avgThreshold = [600, 1100]    #[lower, upper]
promThreshold = [6000, 22000]    #[lower, upper]
peckCount = 0
peckStatus  = 0
#static variable for discrete counting of pecking // 0 if not pecking and 1 if peaking

def updatePeckStatus():
    global peckStatus

    if(peckStatus == 0):
        peckStatus = 1
    else:
        peckStatus = 0
    return

def incORnot():
    global peckStatus

    if(peckStatus == 0):
        updatePeckStatus()
        #increment the count
        return 1
    #donot increment the count
    return 0

def Chopfft(fftVal):
    global freqRange, RATE
    startIndex = int((2*(fftVal[0].shape[0])/RATE)*(freqRange[0]))
    endIndex = int((2*(fftVal[0].shape[0])/RATE)*(freqRange[1]))
    return fftVal[0][startIndex:endIndex], fftVal[1][startIndex:endIndex]


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



def looop():
    global CHUNK, avgThreshold, RATE, peckStatus, peckCount, promThreshold, freqRange

    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    peak=np.average(np.abs(data))*2
    #if peak is high calculate fft 
    # print(peak)
    if(peak > avgThreshold[1]):
        #calculate fft
        #fftx, ffty in fftval
        fftVal = getFFT(data,RATE)
        #chop unnecessary frequency information
        fftVal = Chopfft(fftVal)
        #find the index of the peaks in the fftsignal
        # peakIndex = signal.find_peaks_cwt(fftVal[1], np.arange(0.1,1))
        peakIndex, _ = signal.find_peaks(fftVal[1])


        #find the highest peak
        highestPeakIndex = np.argmax(fftVal[1])
        highestPeak = [fftVal[0][highestPeakIndex], fftVal[1][highestPeakIndex]]	#[frequency, yvalue or amplitude]
        # print("Higest Peak at frequency:", highestPeak[0])		#print the frequency whrere there is the hiest peak


        #finding the highest prominent peak///optional ??? //is more flexiable
        peakProminance = signal.peak_prominences(fftVal[1], peakIndex)[0]	#returns prominance of each peak givenn hence shape of 'peakIndex' and 'peakProminance' is same
        PeakPIndex = np.argmax(peakProminance)			#returns the index of maximum element in the list
        indexOfHigestProminance = peakIndex[PeakPIndex]
        higestProminancePeak = [fftVal[0][indexOfHigestProminance], fftVal[1][indexOfHigestProminance]]
        # print("Higest PeakProminance at frequency:", higestProminancePeak[0])

        # print("Higest prominance Value of peak:", higestProminancePeak[1])

        #check if the prominance of the higest peak of greater than the threhold
        if (higestProminancePeak[1] > promThreshold[1]):
            #if yes try to increment the peckCount
            if incORnot() == 1:
                peckCount += 1
                print("Peck Count: ", peckCount)

        elif (higestProminancePeak[1] < promThreshold[0]):
            updatePeckStatus()

    elif (peak < avgThreshold[0]) :
        updatePeckStatus()

 	

		
        # plt.plot(fftVal[0], fftVal[1])
        # plt.plot(fftVal[0][peakIndex], fftVal[1][peakIndex], 'r.')
        # plt.show()



print("Stream Started")
for i in range(int(10*44100/1024)): #go for a few seconds
	looop()



stream.stop_stream()
stream.close()
p.terminate()