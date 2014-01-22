"""
   DWF Python Example 3
   Author:  Tobias Badertscher based on work by Digilent, Inc.
   Revision: 12/31/2013

   Requires:                       
       Python 2.7
"""

import sys
sys.path.append('..')
from pydwf import dwf
import numpy as np
import time


def AnalogOut_Custom():
    #Generate Sawtooth
    rgdSamples = np.zeros(4000, dtype=np.double)
    for i in xrange(rgdSamples.shape[0]):
        val  =((i%100)-50)/100.0
        rgdSamples[i] = val
    channel = 0
    
    #print DWF version
    version = dwf.GetVersion()
    print "DWF Version: "+version
    
    #open device
    "Opening first device..."
    hdwf =dwf.DeviceOpen(-1)
    
    if hdwf == dwf.hdwfNone:
        print "failed to open device"
    else:
        print "Generating custom waveform..."
        dwf.AnalogOutNodeEnableSet(hdwf, channel, dwf.AnalogOutNodeCarrier, True)
        dwf.AnalogOutNodeFunctionSet(hdwf, channel, dwf.AnalogOutNodeCarrier, dwf.funcCustom) 
        dwf.AnalogOutNodeDataSet(hdwf, channel, dwf.AnalogOutNodeCarrier, rgdSamples)
        dwf.AnalogOutNodeFrequencySet(hdwf, channel, dwf.AnalogOutNodeCarrier, 10000.0) 
        dwf.AnalogOutNodeAmplitudeSet(hdwf, channel, dwf.AnalogOutNodeCarrier, 2) 
        dwf.AnalogOutConfigure(hdwf, channel, True)
        print "Playing waveform for 10 seconds..."
        time.sleep(10)
        print "done."
        dwf.DeviceCloseAll() 


if __name__ == '__main__':
    AnalogOut_Custom()