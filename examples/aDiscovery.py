#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Created on 10.10.2013

    

    @author: Tobias Badertscher
    
"""
import sys
import os
from pydwf import dwf
import numpy as np
import time
import matplotlib.pyplot as plt
from math import *
import re

def Usage(error=None):
    text=["filename","bla bla blar",\
          "Gugus da da."]
    lineStart="    "
    if error != None:
        if isinstance(error, (list, tuple)):
            maxLen=max(len(i) for i in error)
            
            print("*"*(maxLen+len(lineStart)+2), maxLen)
            for item in error:
                print("%s%s *" % (lineStart,item))
            print("*"*(maxLen+len(lineStart)+2), maxLen)
        elif isinstance(error, str):
            print("*"*(len(error)+len(lineStart)+2))
            print("%s%s *" %(lineStart,error))
            print("*"*(len(error)+len(lineStart)+2))
    progName=sys.argv[0].split(os.sep)[-1]
    print("Usage %s %s" % (progName, text[0]))
    for line in text[1:]:
        print("%s%s" % (lineStart,line))
    sys.exit()

def SysMon(fd, t=60):
    for i in xrange(t):
        time.sleep(1)
        dwf.AnalogIOStatus(fd)
        v = dwf.AnalogIOChannelNodeStatus(fd, 2, 0)
        i = dwf.AnalogIOChannelNodeStatus(fd, 2, 1)
        i*=1000
        T = dwf.AnalogIOChannelNodeStatus(fd, 2, 2)
        print("Output Voltage %4.2f V, Output Current %5.2f mA, Temperature %5.1f C" %(v,i,T))

def AcquireAnalog(fd,  cnt, fSample=2E6, chNr=0):
    '''
    Aquire analog input data:
    fd      Descriptor for the file
    cnt     Sample count to aquire
    fSample Sample frequency in [Hz]
    chNr    Input channel 0..1
    '''
    data = None
    if 0 <= chNr < 2 :
        data = np.zeros(cnt, dtype=np.double)
        dwf.AnalogInFrequencySet(fd, fSample)
        dwf.AnalogInBufferSizeSet(fd, cnt)
        dwf.AnalogInChannelEnableSet(fd, chNr, True)
        dwf.AnalogInChannelRangeSet(fd, chNr, 5)
        time.sleep(2)
        dwf.AnalogInConfigure(fd, False, True)
        sts=dwf.stsCfg
        while not sts==dwf.stsDone:
            sts=dwf.AnalogInStatus(fd, True)
            print("Current analog status: %d" % sts)
        dwf.AnalogInStatusData(fd, chNr, data)
    return data

def generateSinus(fd, chNr, fSignal, ampl, offset = 0):
    '''
    Generate Sinus on channel output chNr:
    fd      Descriptor for the file
    chNr    Channel output 0..1
    fSignal Frequency of sinus in Hz
    ampl    Amplitude of signal in V
    offset  Offset of signal in V
    '''
    dwf.AnalogOutEnableSet(fd, chNr, True)
    dwf.AnalogOutFunctionSet(fd, chNr, dwf.funcSine)
    dwf.AnalogOutFrequencySet(fd, chNr, fSignal)
    dwf.AnalogOutAmplitudeSet(fd, chNr, ampl)
    dwf.AnalogOutOffsetSet(fd, chNr, offset)
    dwf.AnalogOutConfigure(fd, chNr, True)


def DigitalIO(fd):
    '''
    Check if Output/Input [0:7] correctly maps to Input/Output [8:15]
    
    fd  : File descriptor fotr AnalogDiscovery
    '''
    ioEnable = 0x00FF
    dwf.DigitalIOOutputEnableSet(fd, ioEnable)
    for i in xrange(8):
        bitSet = 1 << i
        bitExp = 1 << (i+8)
        dwf.DigitalIOOutputSet(fd, bitSet)
        dwf.DigitalIOStatus(fd)
        ioState = dwf.DigitalIOInputStatus(fd)
        ioState = ioState & (~ ioEnable)
        if ioState != bitExp:
            print("Set Output %d, Expected Input bit %d is not set!" %(i ,i+8))
    ioEnable = 0xFF00
    dwf.DigitalIOOutputEnableSet(fd, ioEnable)
    for i in xrange(8):
        bitSet = 1 << (i+8)
        bitExp = 1 << i
        dwf.DigitalIOOutputSet(fd, bitSet)
        dwf.DigitalIOStatus(fd)
        ioState = dwf.DigitalIOInputStatus(fd)
        ioState = ioState & (~ ioEnable)
        if ioState != bitExp:
            print("Set Output %d, Expected Input bit %d is not set!" %(i+8 ,i))
    ioEnable = 0x0000
    dwf.DigitalIOOutputEnableSet(fd, ioEnable)
    return 


def generateDigitalPattern8(fd, outChannels, oClkHz):
    '''
    Generate a digital pattern on the given channels. 
    Precondition is that output channel i and i+8 are not allowed.
    fd      Descriptor for the file
    chnnels List which contains the output pins on which the signal is generated
    '''    
    isOk = True
    for i in outChannels:
        iCh = i+8 if i<8 else i-8
        if iCh in outChannels:
            isOk = False
            break
    if not isOk:
        print("Invalid output channel %d and %d+/-8" % (i,i))
    else:
        cntOfDigChannels = dwf.DigitalOutCount(fd)
        print("Maximal count of output Channels=  %d" %(cntOfDigChannels))
        oMsk = sum([2**i if i in outChannels else 0 for i in xrange(cntOfDigChannels)])
        print("OutputMask 0x%04x/Used outputpins %d" % (oMsk, len(outChannels)))
        dwf.DigitalIOOutputEnableSet(fd, oMsk)
        iClkHz = dwf.DigitalOutInternalClockInfo(fd)
        print("Output base clock is %f MHz" % (iClkHz/1E6))
        div = int(floor(iClkHz/oClkHz))  
        print("Divider = %d" % div)
        maxOutStateCnt = dwf.DigitalOutDataInfo(fd,0)
        maxOutStateCnt=16
        print("Maximal output state count= %d" % maxOutStateCnt)
        data = [np.zeros(maxOutStateCnt, dtype='bool') for i in xrange(len(outChannels))]   
        if 1==1:
            print(data)
            for i in xrange(len(outChannels)):
                for j in xrange(maxOutStateCnt):
                    data[i][j] = ( (j & (1<<i)) != 0)
                    print(i,1<<i,j, (j & (1<<i)))
            print(" ".join(["%5d" % i for i in xrange(len(data[0]))]))
            for vec in data:
                print(" ".join(["%5s" % i for i in vec]))
            #sys.exit()
        for i in xrange(cntOfDigChannels):
            if i in outChannels:
                dwf.DigitalOutEnableSet(fd, i, True)
                dwf.DigitalOutDividerSet(fd, i, div) 
                dwf.DigitalOutCounterSet(fd, i, 9, 1)
                dwf.DigitalOutCounterInitSet(fd, i, i==0, 0 if i==0 else i)
                #dwf.DigitalOutTypeSet(fd, i, dwf.DwfDigitalOutTypeCustom)
                #dwf.DigitalOutOutputSet(fd, i, dwf.DwfDigitalOutOutputPushPull)
                #dwf.DigitalOutDataSet(fd, i, data[i] )
            else:
                dwf.DigitalOutEnableSet(fd, i, False)
                dwf.DigitalOutDividerSet(fd, i, div)    
        mins, maxs = dwf.DigitalOutRunInfo(fd)
        rmin, rMax = dwf.DigitalOutRepeatInfo(fd)
        print(rmin, rMax)
        dwf.DigitalOutRepeatSet(fd, rmin)
        dwf.DigitalOutConfigure(fd, True)
    
def AcquireDigital(hdwf,  cnt):
    '''\
    Capture digital input as in digitalin_aquisation.c
    '''
    hzSys = dwf.DigitalInInternalClockInfo(hdwf)
    div = int(floor(hzSys/1E6))
    print(div)
    dwf.DigitalInDividerSet(hdwf, div)
    dwf.DigitalInSampleFormatSet(hdwf, 16)
    cSamples = dwf.DigitalInBufferSizeInfo(hdwf)
    print("Deveice has buffer of size %d bytes" % cSamples)
    # default buffer size is set to maximum
    dwf.DigitalInBufferSizeSet(hdwf, cSamples)
    rgwSamples = np.zeros(cnt, dtype=np.uint16)

    # set trigger position to the middle 
    dwf.DigitalInTriggerPositionSet(hdwf, cSamples/2)
    
    # trigger on any pin transition
    dwf.DigitalInTriggerSourceSet(hdwf, dwf.trigsrcDetectorDigitalIn)
    dwf.DigitalInTriggerAutoTimeoutSet(hdwf, 1.0)
    dwf.DigitalInTriggerSet(hdwf, 0,0,0xFFFF,0xFFFF)
    
    # start
    dwf.DigitalInConfigure(hdwf, False, True )
    
    print("Waiting for triggered or auto acquisition");
    sts=dwf.stsCfg
    idx = 0
    while not sts==dwf.stsDone:
        sts=dwf.DigitalInStatus(hdwf, True)
        print("Current digital status: %d" % sts)
        idx+=1
        if (idx==50):
            break
    # get the samples
    dwf.DigitalInStatusData(hdwf, rgwSamples)
    print(rgwSamples)

    print("done\n");
    return rgwSamples                                                       
    
    

def main():
    sel = 0x0010
    a = dwf.Enum(dwf.enumfilterAll)
    print(a)
    a = dwf.EnumDeviceType(0)
    print(a)
    a = dwf.EnumDeviceIsOpened(0)
    print(a)
    fd = dwf.DeviceOpen(0)
    print(fd)
    if sel & 0x0001:
        a = dwf.EnumDeviceIsOpened(0)
        print(a)
        a = dwf.EnumUserName(0)
        print(a)
        a = dwf.EnumSN(0)
        print(a)
        a = dwf.GetVersion() 
        print(a)
        a = dwf.EnumDeviceName(0)
        print(a)
        a = dwf.GetLastErrorMsg()
        print(a)
    if sel & 0x0002:
        generateSinus(fd, 0, 12346, 1.41, sqrt(2))
        data = AcquireAnalog(fd, 1000, 1000E3)
        plt.plot(data)
        print(np.mean(data), np.std(data))
        plt.show()
        
        generateSinus(fd, 1, 12346, 1.00, sqrt(2))
        data = AcquireAnalog(fd, 1000, 1000E3, 1)
        plt.plot(data)
        print(np.mean(data), np.std(data))
        plt.show()

    if sel & 0x0004:
        generateDigitalPattern8(fd, [0,1,2,3,4,5,6,7], 1E3)        
        
        data = AcquireDigital(fd, 1024)
        print(data, len(data))
    
    if sel & 0x0008:
        DigitalIO(fd)
    
    if sel & 0x0010:
        SysMon(fd, 10)
        
    dwf.DeviceClose(fd)

if __name__ == '__main__':
    main()
