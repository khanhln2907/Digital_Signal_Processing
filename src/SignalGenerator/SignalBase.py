import numpy as np
import matplotlib.pyplot as plt

class SignalGeneratorBase :
    _samples = 0
    def __init__(self, samples) -> None:
        self._samples = samples
        pass

    def printValues(self):
        print(self._samples)
        pass

    def getSamples(self):
        return self._samples

    def __add__(self, other):
        return SignalGeneratorBase(self._samples + other._samples)

    def plot(self):
        plt.stem(np.linspace(0, 1, len(self._samples)), self._samples)
        pass

class SinusoidSignal(SignalGeneratorBase):

    def __init__(self, amplitude = 1, freq = 1, nSamples = 256, initPhase = 0) -> None:
        t = np.linspace(0, 1, nSamples)
        samples = amplitude * np.sin(2*np.pi*freq*t + initPhase)
        super().__init__(samples)

class SquareSignal(SignalGeneratorBase):

    def __init__(self, amplitude = 1, freq = 1, duty = 0.5, nSamples = 256) -> None:
        assert 0 <= duty <= 1, "Invalid duty cycle" # duty Cycle must be in [0,1]
        tPeriod =float(1) / float(freq) #nSamples / freq #np.floor(nSamples / freq)
        t = np.linspace(0, 1, nSamples)
        samples = np.zeros(nSamples)
        for i in range(nSamples):
            cyclesPass = np.floor((t[i] - t[0]) // tPeriod)
            timePassCurCycle = (t[i] - t[0]) - cyclesPass * tPeriod
            if(float(timePassCurCycle) / float(tPeriod) <= duty):
                samples[i] = amplitude
            else:
                print(float(timePassCurCycle) / float(tPeriod))
        super().__init__(samples)

if __name__ == "__main__":

    myWave = SinusoidSignal(amplitude = 10, freq = 4)
    myWave.printValues()
    #myWave.plot()

    squareWave = SquareSignal(amplitude = 5, duty = 0.3, freq = 6)
    #squareWave.printValues()
    squareWave.plot()
    plt.show()