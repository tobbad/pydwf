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

def AnalogOut_Sync():
    
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
        # enable two channels
        dwf.AnalogOutNodeEnableSet(hdwf, 0, dwf.AnalogOutNodeCarrier, 1)
        dwf.AnalogOutNodeEnableSet(hdwf, 1, dwf.AnalogOutNodeCarrier, 1)
        # for second channel set master the first channel
        dwf.AnalogOutMasterSet(hdwf, 1, 0);
        # slave channel is controlled by the master channel
        # it is enough to set trigger, wait, run and repeat paramters for master channel
        
        # configure enabled channels
        dwf.AnalogOutNodeFunctionSet(hdwf, -1, dwf.AnalogOutNodeCarrier, dwf.funcSine)
        dwf.AnalogOutNodeFrequencySet(hdwf, -1, dwf.AnalogOutNodeCarrier, 1000.0)
        dwf.AnalogOutNodeAmplitudeSet(hdwf, -1, dwf.AnalogOutNodeCarrier, 1.0)
    
        #set phase for second channel
        dwf.AnalogOutNodePhaseSet(hdwf, 1, dwf.AnalogOutNodeCarrier, 180.0)
    
        print "Play sine wave for 10 seconds..."
        # start signal generation, 
        # the second, slave channel will start too
        dwf.AnalogOutConfigure(hdwf, 0, True)
        
        time.sleep(10)
        
        print "done."
        dwf.DeviceClose(hdwf)
        
        
if __name__ == '__main__':
    AnalogOut_Sync()
