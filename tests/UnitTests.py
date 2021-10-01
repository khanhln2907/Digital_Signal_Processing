import unittest
import numpy as np

import sys
import logging
sys.path.append('C:\\Users\\khanh\\Desktop\\Workspace\\DSP\\')

"""@UnitTests
    Hello
"""

class Test_Parser(unittest.TestCase):
    
    def test_WAV_Parser(self):
        """
        Hello
        """
        filepath = ".\\dataset\\IRMAS-Sample\\Training\\sax\\118__[sax][nod][jaz_blu]1702__3.wav"
        from src.Parser import Parser
        myParser = Parser(filepath)
        myParser.visualize()
        myParser.saveChannels()

class Test_Fourier_Analysis(unittest.TestCase):
    def test_dft(self):
        """
        Hello
        """
        from src.FourierAnalysis.Algorithms import dft

        fSig_1 = 1000
        fSig_2 = 2000
        fs = 8000
        ts = 1/fs

        #n = np.linspace(0, 1, fs, endpoint=False)
        n = np.array(range(0,128)) # Amount of samples (DFT- Points)
        sinWave_1 = np.sin(2*np.pi*fSig_1*n*ts)
        sinWave_2 = 0.5*np.sin(2*np.pi*fSig_2*n*ts + 3*np.pi/4)

        wave = sinWave_1 + sinWave_2
        _calcSpektrum, _calcFreq = dft(wave, fs)
        pass

    def Test_DoxyGen(self):
        """
        Does nothing more than demonstrate syntax.

        This is an example of how a Pythonic human-readable docstring can get parsed by doxypypy and marked up with Doxygen commands as a regular input filter to Doxygen.

        Args:
            arg1:   A positional argument.
            arg2:   Another positional argument.

        Kwargs:
            kwarg:  A keyword argument.

        Returns:
            A string holding the result.

        Raises:
            ZeroDivisionError, AssertionError, & ValueError.

        Examples:
            >>> myfunction(2, 3)
            '5 - 0, whatever.'
            >>> myfunction(5, 0, 'oops.')
            Traceback (most recent call last):
                ...
        """

if __name__ == '__main__':
    unittest.main()