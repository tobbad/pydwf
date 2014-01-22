"""
   DWF Python Example translated to swig bindings
   Author:  Tobias Badertscher based on work by Digilent, Inc.
   Revision: 12/31/2013

   Requires:                       
       Python 2.7, numpy, matplotlib
       python-dateutil, pyparsing
"""
import sys
sys.path.append('..')
from pydwf import dwf
import math
import time
import numpy as np
import matplotlib.pyplot as plt



def AnalogIn_Acquisition():
    #print DWF version
    version = dwf.GetVersion()
    print "DWF Version: %s" % (version)
    
    #open device
    print "Opening first device"
    hdwf = dwf.DeviceOpen(-1)
    
    if hdwf ==  dwf.hdwfNone:
        print "failed to open device"
    else:
        print "Preparing to read sample..."
    
    #set up acquisition
    dwf.AnalogInFrequencySet(hdwf, 20000000.0)
    dwf.AnalogInBufferSizeSet(hdwf, 4000) 
    dwf.AnalogInChannelEnableSet(hdwf, 0, True)
    dwf.AnalogInChannelRangeSet(hdwf, 0, 5)
    
    #wait at least 2 seconds for the offset to stabilize
    time.sleep(2)
    
    #begin acquisition
    dwf.AnalogInConfigure(hdwf, False, True)
    print "   waiting to finish"
    
    while True:
        sts = dwf.AnalogInStatus(hdwf, 1)
        print "STS VAL: %s STS DONE: %s" %( sts, dwf.DwfStateDone)
        if sts == dwf.DwfStateDone :
            break
        time.sleep(0.1)
    print "Acquisition finished"
    rgdSamples = np.zeros(4000, dtype=np.double)
    dwf.AnalogInStatusData(hdwf, 0, rgdSamples)
    dwf.DeviceCloseAll()
    
    #plot window
    dc = np.mean(rgdSamples)
    print "DC: %f V" % (dc)
   
    plt.plot(rgdSamples)
    plt.show()
    
    
if __name__ == '__main__':
    AnalogIn_Acquisition()