"""
   DWF Python Example 5
   Author:  Tobias Badertscher based on work by Digilent, Inc.
   Revision: 12/31/2013

   Requires:                       
       Python 2.7, numpy, matplotlib
       python-dateutil, pyparsing
"""
import sys
sys.path.append('..')
from pydwf import dwf
import numpy as np
import math
import time
import matplotlib.pyplot as plt


def AnalogIn_Trigger(hdwf):

    rgdSamples =np.zeros(4000, dtype=np.double)
    
    #set up acquisition
    dwf.AnalogInFrequencySet(hdwf, 20000000.0)
    dwf.AnalogInBufferSizeSet(hdwf, 8192) 
    dwf.AnalogInChannelEnableSet(hdwf, 0, True)
    dwf.AnalogInChannelRangeSet(hdwf, 0, 5)
    
    #set up trigger
    dwf.AnalogInTriggerAutoTimeoutSet(hdwf, 0) #disable auto trigger
    dwf.AnalogInTriggerSourceSet(hdwf, dwf.trigsrcDetectorAnalogIn) #one of the analog in channels
    dwf.AnalogInTriggerTypeSet(hdwf, dwf.trigtypeEdge)
    dwf.AnalogInTriggerChannelSet(hdwf, 0) # first channel
    dwf.AnalogInTriggerLevelSet(hdwf, 1.5) # 1.5V
    dwf.AnalogInTriggerConditionSet(hdwf, dwf.trigcondRisingPositive) 
    
    #wait at least 2 seconds for the offset to stabilize
    time.sleep(2)
    
    print "   starting repeated acquisitons"
    for iTrigger in range(1,100):
        #begin acquisition
        dwf.AnalogInConfigure(hdwf, False, True)   
        while True:
            sts = dwf.AnalogInStatus(hdwf, 1)
            if sts == dwf.DwfStateDone :
                break
            time.sleep(0.001)
    
        dwf.AnalogInStatusData(hdwf, 0, rgdSamples)
        
        dc = np.mean(rgdSamples)
        print "Acquisition #%3d average: %g V" %  (iTrigger, dc)
        
    dwf.DeviceCloseAll()


def GenerateStimuli(hdwf,chNr= 0, fSignal = 1.0, ampl = 1.0, offset  = 1.5):   
    dwf.AnalogOutEnableSet(hdwf, chNr, True)
    dwf.AnalogOutFunctionSet(hdwf, chNr, dwf.funcSine)
    dwf.AnalogOutFrequencySet(hdwf, chNr, fSignal)
    dwf.AnalogOutAmplitudeSet(hdwf, chNr, ampl)
    dwf.AnalogOutOffsetSet(hdwf, chNr, offset)
    dwf.AnalogOutConfigure(hdwf, chNr, True)
    
def openDevice():
    
    #print DWF version
    version = dwf.GetVersion()
    print "DWF Version: %s" % version
    
    #open device
    print "Opening first device"
    hdwf =dwf.DeviceOpen(-1)
    
    if hdwf == dwf.hdwfNone:
        print "failed to open device"
    else:
        print "Preparing to read sample..."
    
    return hdwf
    
    
if __name__ == '__main__':
    '''
    For this script to run please connect the Outut Channel 0
    with the input channel 0.
    '''
    hdwf = openDevice()
    GenerateStimuli(hdwf)
    AnalogIn_Trigger(hdwf)