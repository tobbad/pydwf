"""
   DWF Python Example 6
   Author:  Tobias Badertscher based on work by Digilent, Inc.
   Revision: 12/31/2013

   Requires:                       
       Python 2.7
"""

import sys
sys.path.append('..')
from pydwf import dwf
import time


def AnalogIO_AnalogDiscovery_Power():
    #print DWF version
    version = dwf.GetVersion()
    print "DWF Version: "+version
    
    #open device
    print "Opening first device"
    hdwf =dwf.DeviceOpen(-1)
    
    if hdwf == dwf.hdwfNone:
        print "failed to open device"
    else:
        print "Preparing to read sample..."
    
        #set up analog IO channel node
        dwf.AnalogIOChannelNodeSet(hdwf, 0, 0, 1) 
        # enable negative supply
        dwf.AnalogIOChannelNodeSet(hdwf, 1, 0, 1) 
        # master enable
        dwf.AnalogIOEnableSet(hdwf, True) 
    
        for i in range(1, 60):
          #wait 1 second between readings
          time.sleep(1)
          #fetch analogIO status from device
          sts = dwf.AnalogIOStatus(hdwf)
    
          #supply monitor
          supplyVoltage = dwf.AnalogIOChannelNodeStatus(hdwf, 3, 0)
          supplyCurrent = dwf.AnalogIOChannelNodeStatus(hdwf, 3, 1 )
          supplyPower = supplyVoltage * supplyCurrent
          print "Total supply power: " + str(supplyPower) + "W"
    
          supplyLoadPercentage = 100 * (supplyCurrent / 0.2)
          print"Load: " + str(supplyLoadPercentage) + "%"
    
          # in case of overcurrent condition the supplies are disabled
          IsEnabled = dwf.AnalogIOEnableStatus(hdwf)
          if not IsEnabled:
            #re-enable supplies
            dwf.AnalogIOEnableSet(hdwf, False) 
            dwf.AnalogIOEnableSet(hdwf, True)
    
        #close the device
        dwf.DeviceCloseAll()


    
if __name__ == '__main__':
    AnalogIO_AnalogDiscovery_Power()