import numpy as np
#from src.FourierAnalysis.Algorithms import dft
from scipy.fft import fft, fftshift
import matplotlib.pyplot as plt

class Fourier_Analyzer:
    _fs = 0
    _samples = []
    _timeAxis = []

    _calcSpektrum = []
    _calcFreq = []

    def __init__(self, fs, dataSamples) -> None:
        self._fs = fs
        self._samples = dataSamples

        # Compute the spectrum
        self._timeAxis = np.arange(0, len(dataSamples)) /fs
        self._calcSpektrum = fft(self._samples)

        N_points = len(dataSamples)
        self._calcFreq = []
        for m in range(N_points):
            self._calcFreq.append(m * fs / N_points)
        pass

        

    # Visualization
    def plotSignal(self, axSignal):
        # Plot Time Domain
        axSignal.set_title('Time Domain')
        axSignal.plot(self._timeAxis, self._samples)
        axSignal.set(xlabel="Time", ylabel="Amplitude")
        # TODO: beautify the figure
        #
        #
        return axSignal

    def plotSpectrum(self, axMag, axPhase):
        axMag.set_title("Spectrum")
        axMag.stem(self._calcFreq, fftshift(np.abs(self._calcSpektrum)))
        axMag.set(xlabel="Frequency [Hz]", ylabel="Magtitude")

        axPhase.set_title("Phase")
        axPhase.stem(self._calcFreq, np.angle(self._calcSpektrum, deg=True))
        axPhase.set(xlabel="Frequency [Hz]", ylabel="Phase")
        return axMag, axPhase

    def filter():

        
        pass

    @staticmethod
    def reconstruct():
        
        pass
