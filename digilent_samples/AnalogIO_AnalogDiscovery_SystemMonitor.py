"""
   DWF Python Example 7
   Author:  Tobias Badertscher based on work by Digilent, Inc.
   Revision: 12/31/2013

   Requires:                       
       Python 2.7
"""

import sys
sys.path.append('..')
from pydwf import dwf
import time

def AnalogIO_AnalogDiscovery_SystemMonitor():
    #print DWF version
    version = dwf.GetVersion()
    print "DWF Version: %s" % (version)
    
    #open device
    print "Opening first device"
    hdwf = dwf.DeviceOpen(-1)
    
    if hdwf ==  dwf.hdwfNone:
        print "failed to open device"
        return 
    else:
        print "Preparing to monitor Voltage, Current, Temp..."

    #monitor voltage, current, temperature
    #60 times, once per second
    for i in range(1, 60):
        # wait between readings; the update rate is approximately 1Hz
        time.sleep(1)
        # fetch analog IO status from device
        dwf.AnalogIOStatus(hdwf)
        # get system monitor readings
        deviceVoltage = dwf.AnalogIOChannelNodeStatus(hdwf, 2, 0)
        deviceCurrent = dwf.AnalogIOChannelNodeStatus(hdwf, 2, 1)
        deviceTemperature = dwf.AnalogIOChannelNodeStatus(hdwf, 2, 2)
        print "Device USB supply voltage: %5g V"  % (deviceVoltage)
        print "Device USB supply current: %5g A"  % (deviceCurrent) 
        print "Device temperature:        %.2f C" % (deviceTemperature) 
    #close the device
    dwf.DeviceCloseAll()


    
if __name__ == '__main__':
    AnalogIO_AnalogDiscovery_SystemMonitor()