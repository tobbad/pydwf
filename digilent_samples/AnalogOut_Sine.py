"""
   DWF Python Example 2
   Author:  Tobias Badertscher based on work by Digilent, Inc.
   Revision: 12/31/2013

   Requires:                       
       Python 2.7
"""

import sys
sys.path.append('..')
from pydwf import dwf
import time

def AnalogOut_Sine():
    channel = 0
    
    #print DWF version
    version = dwf.GetVersion()
    print "DWF Version: "+version
    
    #open device
    print "Opening first device..."
    hdwf = dwf.DeviceOpen(-1)
    
    if hdwf == dwf.hdwfNone:
        print "failed to open device"
    else:
        print "Generating sine wave..."
        dwf.AnalogOutNodeEnableSet(hdwf, channel, dwf.AnalogOutNodeCarrier, True)
        dwf.AnalogOutNodeFunctionSet(hdwf, channel, dwf.AnalogOutNodeCarrier, dwf.funcSine)
        dwf.AnalogOutNodeFrequencySet(hdwf, channel, dwf.AnalogOutNodeCarrier, 10000)
        dwf.AnalogOutNodeAmplitudeSet(hdwf, channel, dwf.AnalogOutNodeCarrier, 1.41)
        dwf.AnalogOutNodeOffsetSet(hdwf, channel, dwf.AnalogOutNodeCarrier, 1.41)
        print "Play sine wave for 10 seconds..."
        dwf.AnalogOutConfigure(hdwf, channel, True)
        time.sleep(10)
        print "done."
        dwf.DeviceClose(hdwf)

if __name__ == '__main__':
    AnalogOut_Sine()
