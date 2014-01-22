"""
   DWF Python Example 8
   Author:  Tobias Badertscher based on work by Digilent, Inc.
   Revision: 12/31/2013

   Requires:                       
       Python 2.7
"""

import sys
sys.path.append('..')
from pydwf import dwf

def DigitalIO():
    #print DWF version
    version = dwf.GetVersion()
    print "DWF Version: "+version
    
    #open device
    print "Opening first device"
    hdwf =dwf.DeviceOpen(-1)
    
    if hdwf == dwf.hdwfNone:
        print "failed to open device"
    else:
        print "Preparing to read Digital IO pins..."
    
        # enable output/mask on 8 LSB IO pins, from DIO 0 to 7
        dwf.DigitalIOOutputEnableSet(hdwf, 0x00FF) 
        # set value on enabled IO pins
        dwf.DigitalIOOutputSet(hdwf, 0x12) 
        # fetch digital IO information from the device 
        dwf.DigitalIOStatus (hdwf) 
        # read state of all pins, regardless of output enable
        dwRead = dwf.DigitalIOInputStatus(hdwf) 
    
        #print dwRead as bitfield (32 digits, removing 0b at the front)
        print "Digital IO Pins:  " + bin(dwRead)[2:].zfill(32)
        
        dwf.DeviceCloseAll()



if __name__ == '__main__':
    DigitalIO()
