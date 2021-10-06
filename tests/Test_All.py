import sys
import logging
sys.path.append('C:\\Users\\khanh\\Desktop\\Workspace\\DSP\\')
from src.FourierAnalysis.Fourier_Analyzer import Fourier_Analyzer
from src.SignalGenerator.SignalBase import *
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


fs = 8000

sin1 = SinusoidSignal(amplitude = 10, freq = 1000, nSamples = fs)
sin2 = SinusoidSignal(amplitude = 20, freq = 2000, nSamples = fs)

testwave = sin1 + sin2
samplePoints = testwave.getSamples()

analyzer = Fourier_Analyzer(fs, samplePoints[1:9])

fig, (axTime, axMag, axPhase) =  plt.subplots(3)
analyzer.plotSignal(axTime)
analyzer.plotSpectrum(axMag, axPhase)
plt.show()