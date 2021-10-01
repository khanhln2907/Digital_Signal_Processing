import os
import logging
import array
import numpy as np

import wave
import matplotlib.pyplot as plt

class Parser:
    path = 0
    nSamples = 0
    nChannels = 0
    sampleWidth = 0
    sampleRate = 0
    nframes = 0
    wavParams = 0

    channelsData = []
    
    def __init__(self, filePath) -> None:
        self.path = filePath
        wavPtr = wave.open(filePath, mode='rb') # Read only 
        self.nChannels, self.sampleWidth, self.sampleRate, self.nframes, comptype, compname = wavPtr.getparams()
        self.wavParams = wavPtr.getparams()
        logging.info("Init WAV Parser for file %s", filePath)
        logging.info("Channels: %d Sample Width: %d Frame Rate: %d nFrames: %d", self.nChannels, self.sampleWidth, self.sampleRate, self.nframes) #comptype, compname

        # Getting the format
        type_dict = {1: 'B', 2: 'h', 4: 'i'}
        if(self.sampleWidth not in [1,2,4]):
            raise ValueError("Sample width not supported")
        sampleType = type_dict[self.sampleWidth]

        # Reading the data and parse them into channels
        wavPtr.setpos(0)
        rawData = wavPtr.readframes(wavPtr.getnframes())
        dataArr = np.frombuffer(rawData, dtype=sampleType)
        
        for ith_Channel in range(self.nChannels):
            ch_data = dataArr[ith_Channel::self.nChannels]
            self.channelsData.append(ch_data)

        wavPtr.close()
        
    def visualize(self):
        for ith_Channel in range(self.nChannels):
            plt.plot(self.channelsData[ith_Channel])
        

    def saveChannels(self):
        for ith_Channel in range(self.nChannels):
            outname = "%s_Channel_%d.wav" % (self.path.removesuffix('.wav'), ith_Channel)
            outwav = wave.open(outname, 'w')
            outwav.setparams(self.wavParams)
            outwav.setnchannels(1)
            outwav.writeframes(self.channelsData[ith_Channel].tobytes())
            outwav.close()


    def getInfo(self, wavPtr):
        nchannels, sampwidth, framerate, nframes, comptype, compname = wavPtr.getparams()
        print(nframes)
        pass