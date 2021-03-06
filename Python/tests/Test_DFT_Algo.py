import sys
import logging
sys.path.append('C:\\Users\\khanh\\Desktop\\Workspace\\DSP\\')
from src.FourierAnalysis.Algorithms import *
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


fSig_1 = 1000
fSig_2 = 2000
fs = 8000
ts = 1/fs

#n = np.linspace(0, 1, fs, endpoint=False)
n = np.array(range(0,8))
sinWave_1 = np.sin(2*np.pi*fSig_1*n*ts)
sinWave_2 = 0.5*np.sin(2*np.pi*fSig_2*n*ts + 3*np.pi/4)

wave = sinWave_1 + sinWave_2
#plt.plot(wave)
#plt.show()

print(wave)
X, freq = dft(wave)
for i in range(len(X)):
    print(X[i])

calc_x = idft(X)
for i in range(len(calc_x)):
    print(calc_x[i])
