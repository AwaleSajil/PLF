import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
# import time

CHUNK = 1024*4
RATE = 44100

freqRange = [700, 5000]
avgThreshold = [600, 1100]    #[lower, upper]
avgThreshold = [10000, 0]       #for test
promThreshold = [6000, 22000]    #[lower, upper]
peckCount = 0
peckStatus  = 0
#static variable for discrete counting of pecking // 0 if not pecking and 1 if peaking

weightPerFeed = 0.025  #gram

weightFeedCount = 0  #GRAMS


def resetPeckStatus():
    global peckStatus
    peckStatus = 0
    return
def setPeckStatus():
    global peckStatus
    peckStatus = 1
    return

def incORnot():
    global peckStatus

    if(peckStatus == 0):
        setPeckStatus()
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





def looop(stream):
    global CHUNK, avgThreshold, RATE, peckStatus, promThreshold, freqRange, peckCount, weightPerFeed, weightFeedCount

    data = np.fromstring(stream.read(CHUNK, exception_on_overflow = False),dtype=np.int16)

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



        #finding the highest prominent peak///optional ??? //is more flexiable
        peakProminance = signal.peak_prominences(fftVal[1], peakIndex)[0]	#returns prominance of each peak givenn hence shape of 'peakIndex' and 'peakProminance' is same
        PeakPIndex = np.argmax(peakProminance)			#returns the index of maximum element in the list
        indexOfHigestProminance = peakIndex[PeakPIndex]
        higestProminancePeak = [fftVal[0][indexOfHigestProminance], fftVal[1][indexOfHigestProminance]]
        # print("Higest PeakProminance at frequency:", higestProminancePeak[0])

        # print("Higest prominance Value of peak:", higestProminancePeak[1])


        # xx = np.linspace(0, CHUNK/RATE*1000, CHUNK)
        # print(xx)
        # print(xx.shape , " ",data.shape)
        plt.plot(fftVal[0], fftVal[1])
        # plt.plot(fftVal[0][peakIndex], fftVal[1][peakIndex])
        plt.title('Calculate Peak Prominance of each', fontsize=16)
        plt.xlabel('Frequency(Hz)', fontsize=11)
        plt.ylabel('Amplitude', fontsize=11)

        contour_heights = fftVal[1][peakIndex] - peakProminance
        plt.plot(fftVal[0][peakIndex], fftVal[1][peakIndex], "r.")
        plt.vlines(x=fftVal[0][peakIndex], ymin=contour_heights, ymax=fftVal[1][peakIndex])
        plt.show()


        #check if the prominance of the higest peak of greater than the threhold
        if (higestProminancePeak[1] > promThreshold[1]):
            #if yes try to increment the peckCount
            if incORnot() == 1:
                peckCount += 1
                weightFeedCount = peckCount*weightPerFeed
                print("Peck Count: ", peckCount)

        elif (higestProminancePeak[1] < promThreshold[0]):
            resetPeckStatus()

    elif (peak < avgThreshold[0]) :
        resetPeckStatus()


 	

		
        # plt.plot(fftVal[0], fftVal[1])
        # plt.plot(fftVal[0][peakIndex], fftVal[1][peakIndex], 'r.')
        # plt.show()



# print("Stream Started")
# for i in range(int(10*44100/1024)): #go for a few seconds
# 	looop()

def peakCounter(soundAnalysis):
    p=pyaudio.PyAudio()
    stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
                  frames_per_buffer=CHUNK, input_device_index = 2)

    print("Sound Analysis Stream Started")
    while True:
        looop(stream, soundAnalysis)

    stream.stop_stream()
    stream.close()
    p.terminate()



if __name__ == "__main__":
    #testing this module only
    p=pyaudio.PyAudio()
    stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
                  frames_per_buffer=CHUNK)
    
    looop(stream)




