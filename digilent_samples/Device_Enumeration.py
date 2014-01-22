"""
   DWF Python Example 1
   Author:  Tobias Badertscher based on work by Digilent, Inc.
   Revision: 12/31/2013

   Requires:                       
       Python 2.7
"""

import sys
sys.path.append('..')
from pydwf import dwf

def Device_Enumeration():
    
    #print DWF version
    version = dwf.GetVersion()
    print "DWF Version: "+version
    
    #enumerate and print device information
    cdevices = dwf.Enum(0)
    print "Number of Devices: "+str(cdevices)
    
    for i in range(0, cdevices):
        devicename = dwf.EnumDeviceName (i)
        serialnum  = dwf.EnumSN (i)
        print "------------------------------"
        print "Device %d :" % ( i)
        print "\t" + devicename
        print "\t" + serialnum
        IsInUse =dwf.EnumDeviceIsOpened(i)
    
        if not IsInUse:
            hdwf = dwf.DeviceOpen(i)
            channel = dwf.AnalogInChannelCount(hdwf)
            hzfreq = dwf.AnalogInFrequencyInfo(hdwf)
            print "\tAnalog input channels: "+str(channel)
            print "\tMax freq: "+str(hzfreq)
            dwf.DeviceClose(hdwf)
            hdwf = -1
    
    # ensure all devices are closed
    dwf.DeviceCloseAll()
    
if __name__ == '__main__':
    Device_Enumeration()
