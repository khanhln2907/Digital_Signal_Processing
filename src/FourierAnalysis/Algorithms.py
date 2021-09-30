import numpy as np

def dft(samples_1d, fs = 0, tol = 1e-13):
    N = len(samples_1d)
    X_2d = np.zeros(N, dtype=complex)
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
        X_2d[m] = Xm
        f_analysys[m] = m * fs / N
    return [X_2d, f_analysys]