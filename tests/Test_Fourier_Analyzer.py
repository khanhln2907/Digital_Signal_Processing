import sys
import logging
sys.path.append('C:\\Users\\khanh\\Desktop\\Workspace\\DSP\\')
from src.FourierAnalysis.Fourier_Analyzer import Fourier_Analyzer
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from src.FourierAnalysis.Algorithms import fft

fSig_1 = 1000
fSig_2 = 2000
fs = 8000
ts = 1/fs

#n = np.linspace(0, 1, fs, endpoint=False)
n = np.array(range(0,8))
sinWave_1 = np.sin(2*np.pi*fSig_1*n*ts)
sinWave_2 =  0.5*np.sin(2*np.pi*fSig_2*n*ts + 3*np.pi/4)

wave = sinWave_1 + sinWave_2


analyzer = Fourier_Analyzer(fs, wave)

print("DFT")
print(analyzer._calcSpektrum)
print("FFT")
print(fft(wave))

#fig, (axSignal, axMag, axPhase) = plt.subplots(3)
#analyzer.plotSignal(axSignal)
#analyzer.plotSpectrum(axMag, axPhase)
#plt.show()