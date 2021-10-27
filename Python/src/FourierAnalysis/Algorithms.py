import numpy as np
from src.Tools.ElapsedTimer.ElapsedTimer import *
 
def roundComplex(x_comp, tol = 1e-12):
    # TODO: numply does now allow changing these values. How to set them properly?
    # Workaround...
    ret = np.zeros(1, dtype=complex)
    ret.imag = x_comp.imag
    ret.real = x_comp.real
    if(abs(x_comp.real) < tol):
        ret.real = 0
    if(abs(x_comp.imag) < tol):
        ret.imag = 0
    return ret

def dft(samples_1d, fs = 0):
    """
    Discrete Fourier Transform
    """
    N = len(samples_1d)
    print(N)
    X_complex = np.zeros(N, dtype=complex)
    f_analysys = np.zeros(N, dtype=int)
    for m in range(N):
        Xm = np.zeros(1, dtype=complex)
        for n in range(N):
            phasor = float(2*np.pi*n*m)/float(N)
            Xm = Xm + samples_1d[n] * (np.cos(phasor) - np.sin(phasor)*1j)
        X_complex[m] = roundComplex(Xm)
        f_analysys[m] = m * fs / N
    return [X_complex, f_analysys]

def idft(X_complex, tol = 1e-13):
    """
    Inverse Discrete Fourier Transform
    """
    N = len(X_complex)
    o_x_complex = np.zeros(N, dtype=complex)
    for n in range(N):
        xn = np.zeros(1, dtype=complex)
        for m in range(N):
            phasor = float(2*np.pi*n*m) / float(N)
            xn += X_complex[m] * (np.cos(phasor) + np.sin(phasor)*1j)

        if(abs(xn.real) < tol):
            xn.real = 0
        if(abs(xn.imag) < tol):
            xn.imag = 0
        o_x_complex[n] = (xn/N).round(10)
    
    return o_x_complex

def fft(samples_1d):
    """
    Fast Fourier Transform
    """

    n_points = len(samples_1d)
    coeff_dict = __generateFFTCoeff(n_points)

    # Determine the type of FFT
    nFFT = 2
    # Create the fft layers
    fftNet = []
    while(nFFT <= n_points):
        fftNet.append(fftLayer(coeff_dict[nFFT], n_points))
        nFFT = nFFT * 2

    # Input bit scrambling
    mappedIndex = bitScrambling(n_points)
    rev_Sam = [samples_1d[i] for i in mappedIndex] 
    
    # Compute the output for each layer iteratively
    out = rev_Sam
    for layer in fftNet:
        out = layer.execute(out)
    return out

def __generateFFTCoeff(N_points):
    assert_Power_2(N_points)
    # Generate the weight one time
    _N = N_points
    ret = dict()
    while(_N != 1):
        coeef = np.zeros(_N, dtype=complex)
        for m in range(_N):
            phase = 2 * np.pi * m / _N
            coeef[m] = (np.cos(phase) - np.sin(phase) * 1j)
            #coeef[m] = raw_result #roundComplex(raw_result)
        # Update look-up table
        ret[_N] = coeef
        # Update counter variables
        _N = _N //2
    return ret

def bitScrambling(N):
    assert_Power_2(N)
    originIndex = range(N)
    mappedIndex = np.zeros(N, dtype=int)
    # Find the amount of necessary bit to represents the N
    bitCounts = 1
    tmpN = N-1
    while(tmpN != 0):
        tmpN >>= 1
        if(tmpN != 0):
            bitCounts += 1
        else:
            break
    for index, i in zip(originIndex, range(N)):
        mappedIndex[i] = __reverseBit(index, bitCounts)
    return mappedIndex

def __reverseBit(x, nBits): # get from https://stackoverflow.com/a/50596723
    result = 0
    for i in range(nBits):
        result <<= 1
        result |= x & 1
        x >>= 1
    return result

def assert_Power_2(N):
    #Bit flip manipulation to ensure N_points is an exponential of 2 
    assert ((N & (N - 1) == 0) and (N != 0)), "N points = for FFT Radix 2 is not a power of 2" 

class fftBlock:
    coeff = []
    nFFT = 2
    def __init__(self, coeff) -> None:
        self.coeff = coeff
        self.nFFT = len(coeff)
        assert_Power_2(self.nFFT)
        pass

    def print(self):
        print("FFT Block perform %d-points FFT" % self.nFFT)
        print("Coefficient: " ,self.coeff)

    def compute(self, input):
        # Get the total amount of the input samples
        nInput = len(input)
        assert (nInput == self.nFFT), "FFTBlock input dimension mismatch"
        outputLayer = np.zeros(nInput, dtype = complex) 

        for k in np.arange(self.nFFT//2):
            i_xk = input[k]
            i_yk = input[k + self.nFFT//2]
            Wk_yk = i_yk * self.coeff[k % self.nFFT]
            outputLayer[k] = i_xk + Wk_yk
            outputLayer[k + self.nFFT//2] = i_xk - Wk_yk
        return outputLayer

class fftLayer:
    coeff = []
    fftBlockArr =[]
    nFFT = 2
    mappedIndex = []
    def __init__(self, coeff, Npoints) -> None:
        self.coeff = coeff
        self.nFFT = len(coeff)
        assert_Power_2(self.nFFT)
        assert_Power_2(Npoints)
        nBlocks = Npoints // self.nFFT

        self.mappedIndex = bitScrambling(self.nFFT)

        # Create the n-point fft blocks
        self.fftBlockArr = []
        for i in range(Npoints // self.nFFT):
            self.fftBlockArr.append(fftBlock(coeff))
        
    def print(self):
        print("FFT Layer perform multiple of %d-points FFT" % self.nFFT)
        print("Coefficient: " , self.coeff)
        print("Amount of %d-points Blocks: %d" % (self.nFFT, len(self.fftBlockArr)))


    def execute(self, input):
        #print(input)
        # Get the total amount of the input samples
        nInput = len(input)
        assert_Power_2(nInput)
        o_Layer = np.zeros(nInput, dtype=complex)
        for block, i in zip(self.fftBlockArr, range(len(self.fftBlockArr))):
            batchPtr = self.nFFT*i
            # Get the input for each block
            #i_batch = [input[i] for i in range(batchPtr, batchPtr+self.nFFT)]
            # Shuffle the input for this layer
            o_Layer[batchPtr:batchPtr+self.nFFT] = block.compute(input[batchPtr:batchPtr+self.nFFT])
            #o_Layer[batchPtr:batchPtr+self.nFFT] = o_Block #[roundComplex(ret) for ret in o_Block]
        return o_Layer


if __name__ == "__main__":
    coeffTable = __generateFFTCoeff(8)

    samples = range(0,8)
    block2 = fftBlock(coeffTable[2])
    block4 = fftBlock(coeffTable[4])
    block8 = fftBlock(coeffTable[8])

    block2.print()
    block4.print()
    block8.print()

    out = block2.compute([1,4])
    out1 = block4.compute(range(0,4))

    mappedIndex = bitScrambling(8)
    rev_Sam = [samples[i] for i in mappedIndex] 
    out2 = block8.compute(rev_Sam)

    layer2 = fftLayer(coeffTable[2], 8)
    layer4 = fftLayer(coeffTable[4], 8)
    layer8 = fftLayer(coeffTable[8], 8)


    out2 = layer2.execute(rev_Sam)
    out4 = layer4.execute(out2)
    out8 = layer8.execute(out4)
    print(out8)

    print(fft(samples))
    # print(out)
    # print(out1)
    # print(out2)