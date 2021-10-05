import numpy as np

def roundComplex(x_comp, tol = 1e-15):
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
    n_fft = n_points
    
    # Bit reversion
    input_time_decimation = samples_1d
    # Start
    while(n_fft != 2):
        
        pass

    pass

def butterfly_dft2(x_up, x_down):

    pass


def __generateFFTCoeff(N_points):
    __assert_Power_2(N_points)
    # Generate the weight one time
    _N = N_points
    ret = dict()
    while(_N != 1):
        coeef = np.zeros(_N, dtype=complex)
        for m in range(_N):
            phase = 2 * np.pi * m / _N
            raw_result = (np.cos(phase) - np.sin(phase) * 1j)
            coeef[m] = roundComplex(raw_result)
        # Update look-up table
        ret[_N] = coeef
        # Update counter variables
        _N = _N //2
    return ret

def __bitScrambling(N):
    __assert_Power_2(N)
    originIndex = range(0,N)
    shuffledIndex = np.zeros(N, dtype=int)
    for index, i in zip(originIndex, range(N)):
        shuffledIndex[i] = __reverseBit(index)
    return originIndex, shuffledIndex

def __reverseBit(x, nBit): # https://stackoverflow.com/a/50596723
    result = 0
    for i in range(nBit):
        result <<= 1
        result |= x & 1
        x >>= 1
    return result

def __assert_Power_2(N):
    #Bit flip manipulation to ensure N_points is an exponential of 2 
    assert (N & (N - 1) == 0) and N != 0, "N points for FFT Radix 2 is not a power of 2"



if __name__ == "__main__":

    table = __generateFFTCoeff(8)
    #ori, shuffle = __bitScrambling(8)
    #print(table)
    #print([ori, shuffle])

    tmp = 4
    print(tmp, __reverseBit(tmp,3))