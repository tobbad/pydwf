#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Generated on 15.12.2013 14:20:05    

    @author: Tobias Badertscher
    
"""
import sys
sys.path.append('..')
from dwf import dwf
import numpy as np 
import unittest
# Generated unit test.
class TestOtherFunctions(unittest.TestCase):
    def setUp(self):
        a = dwf.Enum(dwf.enumfilterAll)
        self.vOffset = 0
        self.node = 0
        self.secTimeout = 0
        self.sLegth = 0
        self.percentageSymmetry = 0
        self.hdwf = dwf.DeviceOpen(0)
        self.triglen = 0
        self.voltsAmplitude = 0
        self.trigsrc = dwf.trigsrcNone
        self.fsEdgeFall = 0
        self.value = 0
        self.fReadData = 0
        self.voltsRange = 0
        self.fsLevelLow = 0
        self.vLow = 10
        self.fReconfigure = 0
        self.rgdData = np.zeros(100, dtype='double')
        self.hzFrequency = 0
        self.rgdVoltData = np.zeros(100, dtype='double')
        self.fMasterEnable = 0
        self.nBits = 0
        self.fConfigureWhenSet = 0
        self.secPosition = 0
        self.enumfilter = dwf.enumfilterAll
        self.vAmplitude = 0
        self.voltsLevel = 0
        self.secWait = 1
        self.cSamplesAfterTrigger = 0
        self.fsEdgeRise = 0
        self.idxChannel = 0
        self.degreePhase = 0
        self.voltsOffset = 0
        self.vHigh = 100
        self.secLength = 0
        self.idxPin = 0
        self.secHoldOff = 0
        self.func = 0
        self.rgVoltsStep = 0
        self.div = 0
        self.idxNode = 0
        self.trigtype = 0
        self.fRepeatTrigger = True
        self.fStart = False
        self.idxDevice = 0
        self.filter = 0
        self.fsOutputEnable = 0
        self.fsOutput = 0
        self.acqmode = 0
        self.nSize = 0
        self.voltOffset = 0
        self.v = dwf.DwfDigitalOutOutputPushPull
        self.secRun = 1
        self.trigcond = 0
        self.fHigh = True
        self.fEnable = True
        self.fsLevelHigh = 1
        self.cRepeat = 0

    def testAnalogInStatusSamplesValid(self):
        """ Test AnalogInStatusSamplesValid """
        cSamplesValid  = dwf.AnalogInStatusSamplesValid(self.hdwf)
    

    def testDigitalInConfigure(self):
        """ Test DigitalInConfigure """
        dummy  = dwf.DigitalInConfigure(self.hdwf, self.fReconfigure, self.fStart)
    

    def testAnalogIOChannelNodeName(self):
        """ Test AnalogIOChannelNodeName """
        szNodeName, szNodeUnits  = dwf.AnalogIOChannelNodeName(self.hdwf, self.idxChannel, self.idxNode)
    

    def testAnalogIOStatus(self):
        """ Test AnalogIOStatus """
        dummy  = dwf.AnalogIOStatus(self.hdwf)
    

    def testAnalogInBitsInfo(self):
        """ Test AnalogInBitsInfo """
        nBits  = dwf.AnalogInBitsInfo(self.hdwf)
    

    def testAnalogOutReset(self):
        """ Test AnalogOutReset """
        dummy  = dwf.AnalogOutReset(self.hdwf, self.idxChannel)
    

    def testEnumDeviceType(self):
        """ Test EnumDeviceType """
        DeviceId, DeviceRevision  = dwf.EnumDeviceType(self.idxDevice)
    

    def testAnalogInStatusAutoTriggered(self):
        """ Test AnalogInStatusAutoTriggered """
        fAuto  = dwf.AnalogInStatusAutoTriggered(self.hdwf)
    

    def testDigitalOutReset(self):
        """ Test DigitalOutReset """
        dummy  = dwf.DigitalOutReset(self.hdwf)
    

    def testDigitalIOReset(self):
        """ Test DigitalIOReset """
        dummy  = dwf.DigitalIOReset(self.hdwf)
    

    def testEnumAnalogInBufferSize(self):
        """ Test EnumAnalogInBufferSize """
        nBufferSize  = dwf.EnumAnalogInBufferSize(self.idxDevice)
    

    def testDigitalIOConfigure(self):
        """ Test DigitalIOConfigure """
        dummy  = dwf.DigitalIOConfigure(self.hdwf)
    

    def testAnalogIOConfigure(self):
        """ Test AnalogIOConfigure """
        dummy  = dwf.AnalogIOConfigure(self.hdwf)
    

    def testAnalogInConfigure(self):
        """ Test AnalogInConfigure """
        dummy  = dwf.AnalogInConfigure(self.hdwf, self.fReconfigure, self.fStart)
    

    def testAnalogIOChannelNodeSetInfo(self):
        """ Test AnalogIOChannelNodeSetInfo """
        min, max, nSteps  = dwf.AnalogIOChannelNodeSetInfo(self.hdwf, self.idxChannel, self.idxNode)
    

    def testAnalogOutNodePlayStatus(self):
        """ Test AnalogOutNodePlayStatus """
        dDataFree, dDataLost, dDataCorrupted  = dwf.AnalogOutNodePlayStatus(self.hdwf, self.idxChannel, self.node)
    

    def testAnalogOutCount(self):
        """ Test AnalogOutCount """
        cChannel  = dwf.AnalogOutCount(self.hdwf)
    

    def testAnalogOutDataInfo(self):
        """ Test AnalogOutDataInfo """
        nSamplesMin, nSamplesMax  = dwf.AnalogOutDataInfo(self.hdwf, self.idxChannel)
    

    def testAnalogOutNodeDataSet(self):
        """ Test AnalogOutNodeDataSet """
        dummy  = dwf.AnalogOutNodeDataSet(self.hdwf, self.idxChannel, self.node, self.rgdData)
    

    def testDeviceClose(self):
        """ Test DeviceClose """
        dummy  = dwf.DeviceClose(self.hdwf)
    

    def testAnalogInStatusSamplesLeft(self):
        """ Test AnalogInStatusSamplesLeft """
        cSamplesLeft  = dwf.AnalogInStatusSamplesLeft(self.hdwf)
    

    def testAnalogOutStatus(self):
        """ Test AnalogOutStatus """
        sts  = dwf.AnalogOutStatus(self.hdwf, self.idxChannel)
    

    def testDigitalInStatus(self):
        """ Test DigitalInStatus """
        sts  = dwf.DigitalInStatus(self.hdwf, self.fReadData)
    

    def testAnalogIOChannelNodeStatus(self):
        """ Test AnalogIOChannelNodeStatus """
        value  = dwf.AnalogIOChannelNodeStatus(self.hdwf, self.idxChannel, self.idxNode)
    

    def testDigitalOutDataInfo(self):
        """ Test DigitalOutDataInfo """
        countOfBitsMax  = dwf.DigitalOutDataInfo(self.hdwf, self.idxChannel)
    

    def testDeviceCloseAll(self):
        """ Test DeviceCloseAll """
        dummy  = dwf.DeviceCloseAll()
    

    def testAnalogOutDataSet(self):
        """ Test AnalogOutDataSet """
        dummy  = dwf.AnalogOutDataSet(self.hdwf, self.idxChannel, self.rgdData)
    

    def testDigitalOutRepeatStatus(self):
        """ Test DigitalOutRepeatStatus """
        cRepeat  = dwf.DigitalOutRepeatStatus(self.hdwf)
    

    def testEnumAnalogInChannels(self):
        """ Test EnumAnalogInChannels """
        nChannels  = dwf.EnumAnalogInChannels(self.idxDevice)
    

    def testDigitalInStatusSamplesValid(self):
        """ Test DigitalInStatusSamplesValid """
        cSamplesValid  = dwf.DigitalInStatusSamplesValid(self.hdwf)
    

    def testAnalogIOChannelInfo(self):
        """ Test AnalogIOChannelInfo """
        nNodes  = dwf.AnalogIOChannelInfo(self.hdwf, self.idxChannel)
    

    def testEnumDeviceIsOpened(self):
        """ Test EnumDeviceIsOpened """
        fIsUsed  = dwf.EnumDeviceIsOpened(self.idxDevice)
    

    def testDigitalOutCount(self):
        """ Test DigitalOutCount """
        cChannel  = dwf.DigitalOutCount(self.hdwf)
    

    def testAnalogIOChannelNodeStatusInfo(self):
        """ Test AnalogIOChannelNodeStatusInfo """
        min, max, nSteps  = dwf.AnalogIOChannelNodeStatusInfo(self.hdwf, self.idxChannel, self.idxNode)
    

    def testAnalogOutNodeDataInfo(self):
        """ Test AnalogOutNodeDataInfo """
        nSamplesMin, nSamplesMax  = dwf.AnalogOutNodeDataInfo(self.hdwf, self.idxChannel, self.node)
    

    def testAnalogInStatusIndexWrite(self):
        """ Test AnalogInStatusIndexWrite """
        idxWrite  = dwf.AnalogInStatusIndexWrite(self.hdwf)
    

    def testDeviceReset(self):
        """ Test DeviceReset """
        dummy  = dwf.DeviceReset(self.hdwf)
    

    def testDigitalInReset(self):
        """ Test DigitalInReset """
        dummy  = dwf.DigitalInReset(self.hdwf)
    

    def testEnumAnalogInBits(self):
        """ Test EnumAnalogInBits """
        nBits  = dwf.EnumAnalogInBits(self.idxDevice)
    

    def testDigitalInStatusIndexWrite(self):
        """ Test DigitalInStatusIndexWrite """
        idxWrite  = dwf.DigitalInStatusIndexWrite(self.hdwf)
    

    def testGetVersion(self):
        """ Test GetVersion """
        szVersion  = dwf.GetVersion()
    

    def testAnalogOutPlayStatus(self):
        """ Test AnalogOutPlayStatus """
        dDataFree, dDataLost, dDataCorrupted  = dwf.AnalogOutPlayStatus(self.hdwf, self.idxChannel)
    

    def testDigitalIOStatus(self):
        """ Test DigitalIOStatus """
        dummy  = dwf.DigitalIOStatus(self.hdwf)
    

    def testAnalogInStatusSample(self):
        """ Test AnalogInStatusSample """
        dVoltSample  = dwf.AnalogInStatusSample(self.hdwf, self.idxChannel)
    

    def testDigitalOutConfigure(self):
        """ Test DigitalOutConfigure """
        dummy  = dwf.DigitalOutConfigure(self.hdwf, self.fStart)
    

    def testDigitalInBitsInfo(self):
        """ Test DigitalInBitsInfo """
        nBits  = dwf.DigitalInBitsInfo(self.hdwf)
    

    def testAnalogOutRunStatus(self):
        """ Test AnalogOutRunStatus """
        secRun  = dwf.AnalogOutRunStatus(self.hdwf, self.idxChannel)
    

    def testAnalogOutConfigure(self):
        """ Test AnalogOutConfigure """
        dummy  = dwf.AnalogOutConfigure(self.hdwf, self.idxChannel, self.fStart)
    

    def testAnalogInReset(self):
        """ Test AnalogInReset """
        dummy  = dwf.AnalogInReset(self.hdwf)
    

    def testAnalogInStatus(self):
        """ Test AnalogInStatus """
        sts  = dwf.AnalogInStatus(self.hdwf, self.fReadData)
    

    def testDigitalIOInputInfo(self):
        """ Test DigitalIOInputInfo """
        fsInputMask  = dwf.DigitalIOInputInfo(self.hdwf)
    

    def testDeviceOpen(self):
        """ Test DeviceOpen """
        hdwf  = dwf.DeviceOpen(self.idxDevice)
    

    def testEnum(self):
        """ Test Enum """
        cDevice  = dwf.Enum(self.enumfilter)
    

    def testDigitalOutInternalClockInfo(self):
        """ Test DigitalOutInternalClockInfo """
        hzFreq  = dwf.DigitalOutInternalClockInfo(self.hdwf)
    

    def testAnalogInStatusRecord(self):
        """ Test AnalogInStatusRecord """
        cdDataAvailable, cdDataLost, cdDataCorrupt  = dwf.AnalogInStatusRecord(self.hdwf)
    

    def testAnalogOutNodeInfo(self):
        """ Test AnalogOutNodeInfo """
        fsnode  = dwf.AnalogOutNodeInfo(self.hdwf, self.idxChannel)
    

    def testAnalogInTriggerPositionStatus(self):
        """ Test AnalogInTriggerPositionStatus """
        secPosition  = dwf.AnalogInTriggerPositionStatus(self.hdwf)
    

    def testEnumAnalogInFrequency(self):
        """ Test EnumAnalogInFrequency """
        hzFrequency  = dwf.EnumAnalogInFrequency(self.idxDevice)
    

    def testDigitalOutRunStatus(self):
        """ Test DigitalOutRunStatus """
        secRun  = dwf.DigitalOutRunStatus(self.hdwf)
    

    def testDigitalInInternalClockInfo(self):
        """ Test DigitalInInternalClockInfo """
        hzFreq  = dwf.DigitalInInternalClockInfo(self.hdwf)
    

    def testEnumSN(self):
        """ Test EnumSN """
        szSN  = dwf.EnumSN(self.idxDevice)
    

    def testAnalogOutRepeatStatus(self):
        """ Test AnalogOutRepeatStatus """
        cRepeat  = dwf.AnalogOutRepeatStatus(self.hdwf, self.idxChannel)
    

    def testAnalogIOEnableStatus(self):
        """ Test AnalogIOEnableStatus """
        fMasterEnable  = dwf.AnalogIOEnableStatus(self.hdwf)
    

    def testGetLastErrorMsg(self):
        """ Test GetLastErrorMsg """
        szError  = dwf.GetLastErrorMsg()
    

    def testGetLastError(self):
        """ Test GetLastError """
        dwferc  = dwf.GetLastError()
    

    def testAnalogInStatusData(self):
        """ Test AnalogInStatusData """
        dummy  = dwf.AnalogInStatusData(self.hdwf, self.idxChannel, self.rgdVoltData)
    

    def testAnalogIOReset(self):
        """ Test AnalogIOReset """
        dummy  = dwf.AnalogIOReset(self.hdwf)
    

    def testAnalogIOChannelCount(self):
        """ Test AnalogIOChannelCount """
        nChannel  = dwf.AnalogIOChannelCount(self.hdwf)
    

    def testDigitalIOInputStatus(self):
        """ Test DigitalIOInputStatus """
        fsInput  = dwf.DigitalIOInputStatus(self.hdwf)
    

    def testEnumDeviceName(self):
        """ Test EnumDeviceName """
        szDeviceName  = dwf.EnumDeviceName(self.idxDevice)
    

    def testAnalogOutPlayData(self):
        """ Test AnalogOutPlayData """
        dummy  = dwf.AnalogOutPlayData(self.hdwf, self.idxChannel, self.rgdData)
    

    def testAnalogOutNodePlayData(self):
        """ Test AnalogOutNodePlayData """
        dummy  = dwf.AnalogOutNodePlayData(self.hdwf, self.idxChannel, self.node, self.rgdData)
    

    def testDigitalInStatusAutoTriggered(self):
        """ Test DigitalInStatusAutoTriggered """
        fAuto  = dwf.DigitalInStatusAutoTriggered(self.hdwf)
    

    def testDigitalOutStatus(self):
        """ Test DigitalOutStatus """
        sts  = dwf.DigitalOutStatus(self.hdwf)
    

    def testDigitalInStatusSamplesLeft(self):
        """ Test DigitalInStatusSamplesLeft """
        cSamplesLeft  = dwf.DigitalInStatusSamplesLeft(self.hdwf)
    

    def testAnalogIOChannelName(self):
        """ Test AnalogIOChannelName """
        szName, szLabel  = dwf.AnalogIOChannelName(self.hdwf, self.idxChannel)
    

    def testDeviceTriggerPC(self):
        """ Test DeviceTriggerPC """
        dummy  = dwf.DeviceTriggerPC(self.hdwf)
    

    def testAnalogInChannelCount(self):
        """ Test AnalogInChannelCount """
        cChannel  = dwf.AnalogInChannelCount(self.hdwf)
    

    def testEnumUserName(self):
        """ Test EnumUserName """
        szUserName  = dwf.EnumUserName(self.idxDevice)
    
    def tearDown(self):
        dwf.DeviceClose(self.hdwf)

if __name__ == '__main__':
    unittest.main()
