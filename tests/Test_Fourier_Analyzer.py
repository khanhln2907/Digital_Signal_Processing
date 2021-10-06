import sys
import logging
sys.path.append('C:\\Users\\khanh\\Desktop\\Workspace\\DSP\\')
from src.FourierAnalysis.Fourier_Analyzer import Fourier_Analyzer
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from src.FourierAnalysis.Algorithms import fft
import time

fSig_1 = 1000
fSig_2 = 2000
fs = 8000
ts = 1/fs

def millis():
    return round(time.time() * 1000)

#n = np.linspace(0, 1, fs, endpoint=False)
n = np.array(range(0,8))
sinWave_1 = np.sin(2*np.pi*fSig_1*n*ts)
sinWave_2 =  0.5*np.sin(2*np.pi*fSig_2*n*ts + 3*np.pi/4)

wave = sinWave_1 + sinWave_2


ticDFT = millis()
analyzer = Fourier_Analyzer(fs, wave)
tocDFF = millis() - ticDFT
retDFT = analyzer._calcSpektrum

ticFFT = millis()
retFFT = fft(wave)
tocFFT = millis() - ticFFT

print("Execution Time evaluation")
print("FFT. Time Exc: %d" % (tocFFT))
print("DFT. Time Exc: %d" % (tocDFF))

print("Result Evaluation. Matched?")
#print(retDFT)
#print(retFFT)
print(np.allclose(retDFT, retFFT))
#np.array_equal ()


#fig, (axSignal, axMag, axPhase) = plt.subplots(3)
#analyzer.plotSignal(axSignal)
#analyzer.plotSpectrum(axMag, axPhase)
#plt.show()