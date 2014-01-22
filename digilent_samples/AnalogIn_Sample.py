"""
   DWF Python Example 4
   Author:  Tobias Badertscher based on work by Digilent, Inc.
   Revision: 12/31/2013

   Requires:                       
       Python 2.7
"""

import sys
sys.path.append('..')
from pydwf import dwf
import time

def AnalogIn_Sample():
    #print DWF version
    version = dwf.GetVersion()
    print "DWF Version: %s" % (version)
    
    #open device
    "Opening first device..."
    hdwf = dwf.DeviceOpen(-1)
    
    if hdwf == dwf.hdwfNone:
        print "failed to open device"
    else:
        print "Preparing to read sample..."
        dwf.AnalogInChannelEnableSet(hdwf, 0, True) 
        dwf.AnalogInChannelOffsetSet(hdwf, 0, 0) 
        dwf.AnalogInChannelRangeSet(hdwf, 0, 5) 
        dwf.AnalogInConfigure(hdwf, False, False) 
        time.sleep(2)
        sts = dwf.AnalogInStatus(hdwf, False) 
        voltage = dwf.AnalogInStatusSample(hdwf, 0)
        print "Voltage:  %f V" % ( voltage)
    
        dwf.DeviceCloseAll()
    
if __name__ == '__main__':
    AnalogIn_Sample()