"""
   DWF Python Example translated to swig bindings
   Author:  Tobias Badertscher based on work by Digilent, Inc.
   Revision: 12/31/2013

"""

import sys
sys.path.append('..')
from pydwf import dwf
import time
import matplotlib.pyplot as plt
import numpy as np

def AnalogOutIn():
    version = dwf.GetVersion()
    print "Version: "+version
    
    cdevices =dwf.Enum(0)
    print "Number of Devices: "+str(cdevices)
    
    print "Opening first device"
    hdev = dwf.DeviceOpen(0)
    
    
    print "Configure and start first analog out channel"
    dwf.AnalogOutEnableSet(hdev, 0, 1)
    print "1 = Sine wave"
    dwf.AnalogOutFunctionSet(hdev, 0, 1)
    dwf.AnalogOutFrequencySet(hdev, 0, 3000)
    print ""
    dwf.AnalogOutConfigure(hdev, 0, 1)
    
    print "Configure analog in"
    dwf.AnalogInFrequencySet(hdev, 1000000)
    print "Set range for all channels"
    dwf.AnalogInChannelRangeSet(hdev, -1, 4)
    anInBufSize = 4000
    dwf.AnalogInBufferSizeSet(hdev, anInBufSize)
    
    print "Wait after first device opening the analog in offset to stabilize"
    time.sleep(2)
    
    print "Starting acquisition"
    dwf.AnalogInConfigure(hdev, 1, 1)
    
    print "   waiting to finish"
    while True:
        sts = dwf.AnalogInStatus(hdev, 1)
        if sts == dwf.DwfStateDone :
            break
        time.sleep(0.1)
    print "   done"
    
    
    print "   reading data"
    rg =   np.zeros(anInBufSize, dtype=np.double)
    dwf.AnalogInStatusData(hdev, 0, rg)
    
    dwf.DeviceCloseAll()
    
    dc = np.mean(rg)
    print "DC: "+str(dc)+"V"
    
    plt.plot(rg)
    plt.show()

if __name__ == '__main__':
    AnalogOutIn()
