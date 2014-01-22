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
import math
import time
import matplotlib.pyplot as plt

def DigitalOut_BinarayCounter():
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
    
        hzSys = dwf.DigitalOutInternalClockInfo(hdwf)
        print " internal frequency is  %.3f Hz" % (hzSys)
        # generate counter
        for i in range(0, 15):
            dwf.DigitalOutEnableSet(hdwf, i, 1)
            # increase by 2 the period of successive bits
            dwf.DigitalOutDividerSet(hdwf,i , 1<<i)
            # 100kHz counter rate, SystemFrequency/100kHz
            cntFreq = hzSys/1e5
            cntFreqres = int(math.floor(cntFreq))
            print " counter frequency is %.3f Hz " % (cntFreqres)
            dwf.DigitalOutCounterSet(hdwf, i, cntFreqres, cntFreqres)
        
        dwf.DigitalOutConfigure(hdwf, 1)
        
        time.sleep(10)
    dwf.DeviceCloseAll()


if __name__ == '__main__':
    DigitalOut_BinarayCounter()
