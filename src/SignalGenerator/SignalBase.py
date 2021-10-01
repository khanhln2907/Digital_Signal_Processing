import numpy as np
import matplotlib.pyplot as plt

class SignalGeneratorBase :
    _samples = 0
    _timeArr = 0
    _parameter = 0

    def __init__(self, samples, timeArr = 0) -> None:
        self._samples = samples
        if(len(timeArr) == 1):
            self._timeArr = np.range(len(samples))
        else:
            assert len(timeArr) == len(samples), "Dimension mismatched" 
            self._timeArr = timeArr
        #self._parameter = param
        pass

    def printValues(self):
        print(self._samples)
        pass

    def getSamples(self):
        return self._samples

    def plot(self):
        plt.stem(self._timeArr, self._samples)
        pass

class SinusoidSignal(SignalGeneratorBase):

    def __init__(self, amplitude = 1, freq = 1, nSamples = 64, tInterval = [0, 10], initPhase = 0) -> None:
        t = np.linspace(tInterval[0], tInterval[1], num = nSamples)
        samples = amplitude * np.sin(2*np.pi*freq*t + initPhase)
        super().__init__(samples)

class SquareSignal(SignalGeneratorBase):

    def __init__(self, amplitude = 1, tPeriod = 1, duty = 0.5, nSamples = 64, tInterval = [0, 10], initState = 0) -> None:
        assert 0 <= duty <= 1, "Invalid duty cycle" # duty Cycle must be in [0,1]
        timeArr = np.linspace(tInterval[0], tInterval[1], num = nSamples)
        samples = np.zeros(len(timeArr))
        for i in range(len(timeArr)):
            timePass = timeArr[i] - timeArr[0]
            cyclesPass = np.floor(timePass // tPeriod)
            timePassCurCycle = timePass - cyclesPass * tPeriod
            if(float(timePassCurCycle) / float(tPeriod) < duty):
                samples[i] = amplitude
        super().__init__(samples, timeArr)

if __name__ == "__main__":

    # myWave = SinusoidSignal(amplitude = 10, tInterval = [0, 5], nSamples = 100)
    # myWave.printValues()
    # myWave.plot()

    squareWave = SquareSignal()
    squareWave.printValues()
    squareWave.plot()
    plt.show()