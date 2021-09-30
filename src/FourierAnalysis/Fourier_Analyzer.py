#import numpy as np
from src.FourierAnalysis.Algorithms import dft

import matplotlib.pyplot as plt

class Fourier_Analyzer:
    _fs = 0
    _samples = []

    _calcSpektrum = []
    _calcFreq = []

    def __init__(self, fs, dataSamples) -> None:
        self._fs = fs
        self._samples = dataSamples

        # Compute the spectrum
        self._calcSpektrum, self._calcFreq = dft(self._samples, self._fs)
        pass

    def plot(self):
        fig, (axTime, axSpectrum) = plt.subplots(2)

        # Plot Time Domain
        axTime.set_title('Time Domain')
        axTime.plot(self._samples)
        axTime.set(xlabel="Time", ylabel="Amplitude")
        
        # Plot Spectrum
        self.plotSpectrum(axSpectrum, False)

        # Show the figures
        plt.show()

        # TODO: beautify the figure
        #
        #
        return fig, axTime, axSpectrum

    def plotSpectrum(self, ax, showFlag = True):
        ax.set_title('Frequency Spectrum')
        ax.stem(self._calcFreq, abs(self._calcSpektrum))
        ax.set(xlabel="Frequency [Hz]", ylabel="Magtitude")
        plt.show(block = showFlag)
        return ax



