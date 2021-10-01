import numpy as np

def dft(samples_1d, fs = 0, tol = 1e-13):
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
        if(abs(Xm.real) < tol):
            Xm.real = 0
        if(abs(Xm.imag) < tol):
            Xm.imag = 0
        X_complex[m] = Xm
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