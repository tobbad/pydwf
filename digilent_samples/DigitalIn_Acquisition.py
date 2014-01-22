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
import time
import matplotlib.pyplot as plt
import numpy as np 

def DigitalIn_Acquisition():
    #print DWF version
    version = dwf.GetVersion()
    print "DWF Version: "+version
    
    #open device
    print "Opening first device"
    hdwf = dwf.DeviceOpen(-1)
    
    if hdwf == dwf.hdwfNone:
        print "failed to open device"
    else:
        print "Preparing to read sample..."
    
    # generate on DIO-0 1Mhz pulse (100MHz/25/(3+1)), 25% duty (3low 1high)
    #dwf.DigitalOutEnableSet(hdwf, c_int(i), 1)
    #dwf.DigitalOutDividerSet(hdwf, c_int(i), 25)
    #dwf.DigitalOutCounterSet(hdwf, c_int(i), 3, 1)
        
    # generate counter
    for i in range(0, 15):
        dwf.DigitalOutEnableSet(hdwf, i, 1)
        dwf.DigitalOutDividerSet(hdwf, i, (1<<i))
        dwf.DigitalOutCounterSet(hdwf, i, 1, 1)
    
    dwf.DigitalOutConfigure(hdwf, 1)
    
    
    #sample rate = system frequency / divider, 100MHz/1
    dwf.DigitalInDividerSet(hdwf, 1)
    # 16bit per sample format
    dwf.DigitalInSampleFormatSet(hdwf, 16)
    # set number of sample to acquire
    cSamples = 1000
    rgwSamples = np.zeros(cSamples, dtype=np.uint16)
    dwf.DigitalInBufferSizeSet(hdwf, cSamples)
    
    # begin acquisition
    dwf.DigitalInConfigure(hdwf, False, True)
    print "   waiting to finish"
    
    while True:
        sts = dwf.DigitalInStatus(hdwf, 1)
        print "STS VAL: " + str(sts)
        if sts == dwf.stsDone :
            break
        time.sleep(1)
    print "Acquisition finished"
    
    # get samples, byte size
    dwf.DigitalInStatusData(hdwf, rgwSamples)
    dwf.DeviceCloseAll()
    
    plt.plot(rgwSamples)
    plt.show()
    
    
if __name__ == '__main__':
    DigitalIn_Acquisition()
