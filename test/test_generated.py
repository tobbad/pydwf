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
class TestGetSetInfo(unittest.TestCase):
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

    def testAnalogOutFrequency(self):
        """ Test AnalogOutFrequency Get/Set/Info function """
        rPara   = dwf.AnalogOutFrequencyInfo(self.hdwf, self.idxChannel)
        hzFrequency  = dwf.AnalogOutFrequencyGet(self.hdwf, self.idxChannel)
        #print("AnalogOutFrequency  : Info = %s, pOut = %s" % (str(rPara), str((hzFrequency))))
        dwf.AnalogOutFrequencySet(self.hdwf, self.idxChannel, hzFrequency)
    

    def testDeviceAutoConfigure(self):
        """ Test DeviceAutoConfigure Get/Set function """
        fAutoConfigure  = dwf.DeviceAutoConfigureGet(self.hdwf)
        #print("DeviceAutoConfigure : Info = %s, pOut = %s" % (str(rPara), str((fAutoConfigure))))
        dwf.DeviceAutoConfigureSet(self.hdwf, fAutoConfigure)
    

    def testDigitalOutIdle(self):
        """ Test DigitalOutIdle Get/Set/Info function """
        rPara   = dwf.DigitalOutIdleInfo(self.hdwf, self.idxChannel)
        v  = dwf.DigitalOutIdleGet(self.hdwf, self.idxChannel)
        #print("DigitalOutIdle      : Info = %s, pOut = %s" % (str(rPara), str((v))))
        dwf.DigitalOutIdleSet(self.hdwf, self.idxChannel, v)
    

    def testAnalogOutAmplitude(self):
        """ Test AnalogOutAmplitude Get/Set/Info function """
        rPara   = dwf.AnalogOutAmplitudeInfo(self.hdwf, self.idxChannel)
        voltsAmplitude  = dwf.AnalogOutAmplitudeGet(self.hdwf, self.idxChannel)
        #print("AnalogOutAmplitude  : Info = %s, pOut = %s" % (str(rPara), str((voltsAmplitude))))
        dwf.AnalogOutAmplitudeSet(self.hdwf, self.idxChannel, voltsAmplitude)
    

    def testAnalogInAcquisitionMode(self):
        """ Test AnalogInAcquisitionMode Get/Set/Info function """
        rPara   = dwf.AnalogInAcquisitionModeInfo(self.hdwf)
        acqmode  = dwf.AnalogInAcquisitionModeGet(self.hdwf)
        #print("AnalogInAcquisitionMode: Info = %s, pOut = %s" % (str(rPara), str((acqmode))))
        dwf.AnalogInAcquisitionModeSet(self.hdwf, acqmode)
    

    def testDigitalOutEnable(self):
        """ Test DigitalOutEnable Get/Set function """
        fEnable  = dwf.DigitalOutEnableGet(self.hdwf, self.idxChannel)
        #print("DigitalOutEnable    : Info = %s, pOut = %s" % (str(rPara), str((fEnable))))
        dwf.DigitalOutEnableSet(self.hdwf, self.idxChannel, fEnable)
    

    def testAnalogInTriggerCondition(self):
        """ Test AnalogInTriggerCondition Get/Set/Info function """
        rPara   = dwf.AnalogInTriggerConditionInfo(self.hdwf)
        trigcond  = dwf.AnalogInTriggerConditionGet(self.hdwf)
        #print("AnalogInTriggerCondition: Info = %s, pOut = %s" % (str(rPara), str((trigcond))))
        dwf.AnalogInTriggerConditionSet(self.hdwf, trigcond)
    

    def testAnalogInChannelEnable(self):
        """ Test AnalogInChannelEnable Get/Set function """
        fEnable  = dwf.AnalogInChannelEnableGet(self.hdwf, self.idxChannel)
        #print("AnalogInChannelEnable: Info = %s, pOut = %s" % (str(rPara), str((fEnable))))
        dwf.AnalogInChannelEnableSet(self.hdwf, self.idxChannel, fEnable)
    

    def testDeviceTrigger(self):
        """ Test DeviceTrigger Get/Set/Info function """
        rPara   = dwf.DeviceTriggerInfo(self.hdwf)
        trigsrc  = dwf.DeviceTriggerGet(self.hdwf, self.idxPin)
        #print("DeviceTrigger       : Info = %s, pOut = %s" % (str(rPara), str((trigsrc))))
        dwf.DeviceTriggerSet(self.hdwf, self.idxPin, trigsrc)
    

    def testAnalogOutEnable(self):
        """ Test AnalogOutEnable Get/Set function """
        fEnable  = dwf.AnalogOutEnableGet(self.hdwf, self.idxChannel)
        #print("AnalogOutEnable     : Info = %s, pOut = %s" % (str(rPara), str((fEnable))))
        dwf.AnalogOutEnableSet(self.hdwf, self.idxChannel, fEnable)
    

    def testAnalogInTriggerLengthCondition(self):
        """ Test AnalogInTriggerLengthCondition Get/Set/Info function """
        rPara   = dwf.AnalogInTriggerLengthConditionInfo(self.hdwf)
        triglen  = dwf.AnalogInTriggerLengthConditionGet(self.hdwf)
        #print("AnalogInTriggerLengthCondition: Info = %s, pOut = %s" % (str(rPara), str((triglen))))
        dwf.AnalogInTriggerLengthConditionSet(self.hdwf, triglen)
    

    def testAnalogInTriggerPosition(self):
        """ Test AnalogInTriggerPosition Get/Set/Info function """
        rPara   = dwf.AnalogInTriggerPositionInfo(self.hdwf)
        secPosition  = dwf.AnalogInTriggerPositionGet(self.hdwf)
        #print("AnalogInTriggerPosition: Info = %s, pOut = %s" % (str(rPara), str((secPosition))))
        dwf.AnalogInTriggerPositionSet(self.hdwf, secPosition)
    

    def testAnalogInTriggerLength(self):
        """ Test AnalogInTriggerLength Get/Set/Info function """
        rPara   = dwf.AnalogInTriggerLengthInfo(self.hdwf)
        secLength  = dwf.AnalogInTriggerLengthGet(self.hdwf)
        #print("AnalogInTriggerLength: Info = %s, pOut = %s" % (str(rPara), str((secLength))))
        dwf.AnalogInTriggerLengthSet(self.hdwf, secLength)
    

    def testAnalogOutWait(self):
        """ Test AnalogOutWait Get/Set/Info function """
        rPara   = dwf.AnalogOutWaitInfo(self.hdwf, self.idxChannel)
        secWait  = dwf.AnalogOutWaitGet(self.hdwf, self.idxChannel)
        #print("AnalogOutWait       : Info = %s, pOut = %s" % (str(rPara), str((secWait))))
        dwf.AnalogOutWaitSet(self.hdwf, self.idxChannel, secWait)
    

    def testDigitalOutRun(self):
        """ Test DigitalOutRun Get/Set/Info function """
        rPara   = dwf.DigitalOutRunInfo(self.hdwf)
        secRun  = dwf.DigitalOutRunGet(self.hdwf)
        #print("DigitalOutRun       : Info = %s, pOut = %s" % (str(rPara), str((secRun))))
        dwf.DigitalOutRunSet(self.hdwf, secRun)
    

    def testAnalogIOChannelNode(self):
        """ Test AnalogIOChannelNode Get/Set/Info function """
        rPara   = dwf.AnalogIOChannelNodeInfo(self.hdwf, self.idxChannel, self.idxNode)
        value  = dwf.AnalogIOChannelNodeGet(self.hdwf, self.idxChannel, self.idxNode)
        #print("AnalogIOChannelNode : Info = %s, pOut = %s" % (str(rPara), str((value))))
        dwf.AnalogIOChannelNodeSet(self.hdwf, self.idxChannel, self.idxNode, value)
    

    def testDigitalInDivider(self):
        """ Test DigitalInDivider Get/Set/Info function """
        rPara   = dwf.DigitalInDividerInfo(self.hdwf)
        div  = dwf.DigitalInDividerGet(self.hdwf)
        #print("DigitalInDivider    : Info = %s, pOut = %s" % (str(rPara), str((div))))
        dwf.DigitalInDividerSet(self.hdwf, div)
    

    def testAnalogInTriggerFilter(self):
        """ Test AnalogInTriggerFilter Get/Set/Info function """
        rPara   = dwf.AnalogInTriggerFilterInfo(self.hdwf)
        filter  = dwf.AnalogInTriggerFilterGet(self.hdwf)
        #print("AnalogInTriggerFilter: Info = %s, pOut = %s" % (str(rPara), str((filter))))
        dwf.AnalogInTriggerFilterSet(self.hdwf, filter)
    

    def testAnalogInChannelFilter(self):
        """ Test AnalogInChannelFilter Get/Set/Info function """
        rPara   = dwf.AnalogInChannelFilterInfo(self.hdwf)
        filter  = dwf.AnalogInChannelFilterGet(self.hdwf, self.idxChannel)
        #print("AnalogInChannelFilter: Info = %s, pOut = %s" % (str(rPara), str((filter))))
        dwf.AnalogInChannelFilterSet(self.hdwf, self.idxChannel, filter)
    

    def testAnalogInTriggerType(self):
        """ Test AnalogInTriggerType Get/Set/Info function """
        rPara   = dwf.AnalogInTriggerTypeInfo(self.hdwf)
        trigtype  = dwf.AnalogInTriggerTypeGet(self.hdwf)
        #print("AnalogInTriggerType : Info = %s, pOut = %s" % (str(rPara), str((trigtype))))
        dwf.AnalogInTriggerTypeSet(self.hdwf, trigtype)
    

    def testDigitalInSampleMode(self):
        """ Test DigitalInSampleMode Get/Set/Info function """
        rPara   = dwf.DigitalInSampleModeInfo(self.hdwf)
        v  = dwf.DigitalInSampleModeGet(self.hdwf)
        #print("DigitalInSampleMode : Info = %s, pOut = %s" % (str(rPara), str((v))))
        dwf.DigitalInSampleModeSet(self.hdwf, v)
    

    def testDigitalInAcquisitionMode(self):
        """ Test DigitalInAcquisitionMode Get/Set/Info function """
        rPara   = dwf.DigitalInAcquisitionModeInfo(self.hdwf)
        acqmode  = dwf.DigitalInAcquisitionModeGet(self.hdwf)
        #print("DigitalInAcquisitionMode: Info = %s, pOut = %s" % (str(rPara), str((acqmode))))
        dwf.DigitalInAcquisitionModeSet(self.hdwf, acqmode)
    

    def testDigitalOutDividerInit(self):
        """ Test DigitalOutDividerInit Get/Set function """
        v  = dwf.DigitalOutDividerInitGet(self.hdwf, self.idxChannel)
        #print("DigitalOutDividerInit: Info = %s, pOut = %s" % (str(rPara), str((v))))
        dwf.DigitalOutDividerInitSet(self.hdwf, self.idxChannel, v)
    

    def testDigitalOutCounter(self):
        """ Test DigitalOutCounter Get/Set/Info function """
        rPara   = dwf.DigitalOutCounterInfo(self.hdwf, self.idxChannel)
        vLow, vHigh  = dwf.DigitalOutCounterGet(self.hdwf, self.idxChannel)
        #print("DigitalOutCounter   : Info = %s, pOut = %s" % (str(rPara), str((vLow, vHigh))))
        dwf.DigitalOutCounterSet(self.hdwf, self.idxChannel, vLow, vHigh)
    

    def testAnalogOutTriggerSource(self):
        """ Test AnalogOutTriggerSource Get/Set/Info function """
        rPara   = dwf.AnalogOutTriggerSourceInfo(self.hdwf, self.idxChannel)
        trigsrc  = dwf.AnalogOutTriggerSourceGet(self.hdwf, self.idxChannel)
        #print("AnalogOutTriggerSource: Info = %s, pOut = %s" % (str(rPara), str((trigsrc))))
        dwf.AnalogOutTriggerSourceSet(self.hdwf, self.idxChannel, trigsrc)
    

    def testAnalogInRecordLength(self):
        """ Test AnalogInRecordLength Get/Set function """
        sLegth  = dwf.AnalogInRecordLengthGet(self.hdwf)
        #print("AnalogInRecordLength: Info = %s, pOut = %s" % (str(rPara), str((sLegth))))
        dwf.AnalogInRecordLengthSet(self.hdwf, sLegth)
    

    def testAnalogOutNodeSymmetry(self):
        """ Test AnalogOutNodeSymmetry Get/Set/Info function """
        rPara   = dwf.AnalogOutNodeSymmetryInfo(self.hdwf, self.idxChannel, self.node)
        percentageSymmetry  = dwf.AnalogOutNodeSymmetryGet(self.hdwf, self.idxChannel, self.node)
        #print("AnalogOutNodeSymmetry: Info = %s, pOut = %s" % (str(rPara), str((percentageSymmetry))))
        dwf.AnalogOutNodeSymmetrySet(self.hdwf, self.idxChannel, self.node, percentageSymmetry)
    

    def testAnalogOutNodeFunction(self):
        """ Test AnalogOutNodeFunction Get/Set/Info function """
        rPara   = dwf.AnalogOutNodeFunctionInfo(self.hdwf, self.idxChannel, self.node)
        func  = dwf.AnalogOutNodeFunctionGet(self.hdwf, self.idxChannel, self.node)
        #print("AnalogOutNodeFunction: Info = %s, pOut = %s" % (str(rPara), str((func))))
        dwf.AnalogOutNodeFunctionSet(self.hdwf, self.idxChannel, self.node, func)
    

    def testAnalogInTriggerSource(self):
        """ Test AnalogInTriggerSource Get/Set/Info function """
        rPara   = dwf.AnalogInTriggerSourceInfo(self.hdwf)
        trigsrc  = dwf.AnalogInTriggerSourceGet(self.hdwf)
        #print("AnalogInTriggerSource: Info = %s, pOut = %s" % (str(rPara), str((trigsrc))))
        dwf.AnalogInTriggerSourceSet(self.hdwf, trigsrc)
    

    def testAnalogOutCustomAMFMEnable(self):
        """ Test AnalogOutCustomAMFMEnable Get/Set function """
        fEnable  = dwf.AnalogOutCustomAMFMEnableGet(self.hdwf, self.idxChannel)
        #print("AnalogOutCustomAMFMEnable: Info = %s, pOut = %s" % (str(rPara), str((fEnable))))
        dwf.AnalogOutCustomAMFMEnableSet(self.hdwf, self.idxChannel, fEnable)
    

    def testDigitalInTriggerPosition(self):
        """ Test DigitalInTriggerPosition Get/Set/Info function """
        rPara   = dwf.DigitalInTriggerPositionInfo(self.hdwf)
        cSamplesAfterTrigger  = dwf.DigitalInTriggerPositionGet(self.hdwf)
        #print("DigitalInTriggerPosition: Info = %s, pOut = %s" % (str(rPara), str((cSamplesAfterTrigger))))
        dwf.DigitalInTriggerPositionSet(self.hdwf, cSamplesAfterTrigger)
    

    def testAnalogOutSymmetry(self):
        """ Test AnalogOutSymmetry Get/Set/Info function """
        rPara   = dwf.AnalogOutSymmetryInfo(self.hdwf, self.idxChannel)
        percentageSymmetry  = dwf.AnalogOutSymmetryGet(self.hdwf, self.idxChannel)
        #print("AnalogOutSymmetry   : Info = %s, pOut = %s" % (str(rPara), str((percentageSymmetry))))
        dwf.AnalogOutSymmetrySet(self.hdwf, self.idxChannel, percentageSymmetry)
    

    def testDigitalOutDivider(self):
        """ Test DigitalOutDivider Get/Set/Info function """
        rPara   = dwf.DigitalOutDividerInfo(self.hdwf, self.idxChannel)
        v  = dwf.DigitalOutDividerGet(self.hdwf, self.idxChannel)
        #print("DigitalOutDivider   : Info = %s, pOut = %s" % (str(rPara), str((v))))
        dwf.DigitalOutDividerSet(self.hdwf, self.idxChannel, v)
    

    def testDigitalIOOutputEnable(self):
        """ Test DigitalIOOutputEnable Get/Set/Info function """
        rPara   = dwf.DigitalIOOutputEnableInfo(self.hdwf)
        fsOutputEnable  = dwf.DigitalIOOutputEnableGet(self.hdwf)
        #print("DigitalIOOutputEnable: Info = %s, pOut = %s" % (str(rPara), str((fsOutputEnable))))
        dwf.DigitalIOOutputEnableSet(self.hdwf, fsOutputEnable)
    

    def testAnalogOutNodeOffset(self):
        """ Test AnalogOutNodeOffset Get/Set/Info function """
        rPara   = dwf.AnalogOutNodeOffsetInfo(self.hdwf, self.idxChannel, self.node)
        vOffset  = dwf.AnalogOutNodeOffsetGet(self.hdwf, self.idxChannel, self.node)
        #print("AnalogOutNodeOffset : Info = %s, pOut = %s" % (str(rPara), str((vOffset))))
        dwf.AnalogOutNodeOffsetSet(self.hdwf, self.idxChannel, self.node, vOffset)
    

    def testAnalogOutNodeEnable(self):
        """ Test AnalogOutNodeEnable Get/Set function """
        fEnable  = dwf.AnalogOutNodeEnableGet(self.hdwf, self.idxChannel, self.node)
        #print("AnalogOutNodeEnable : Info = %s, pOut = %s" % (str(rPara), str((fEnable))))
        dwf.AnalogOutNodeEnableSet(self.hdwf, self.idxChannel, self.node, fEnable)
    

    def testDigitalInTriggerAutoTimeout(self):
        """ Test DigitalInTriggerAutoTimeout Get/Set/Info function """
        rPara   = dwf.DigitalInTriggerAutoTimeoutInfo(self.hdwf)
        secTimeout  = dwf.DigitalInTriggerAutoTimeoutGet(self.hdwf)
        #print("DigitalInTriggerAutoTimeout: Info = %s, pOut = %s" % (str(rPara), str((secTimeout))))
        dwf.DigitalInTriggerAutoTimeoutSet(self.hdwf, secTimeout)
    

    def testDigitalOutType(self):
        """ Test DigitalOutType Get/Set/Info function """
        rPara   = dwf.DigitalOutTypeInfo(self.hdwf, self.idxChannel)
        v  = dwf.DigitalOutTypeGet(self.hdwf, self.idxChannel)
        #print("DigitalOutType      : Info = %s, pOut = %s" % (str(rPara), str((v))))
        dwf.DigitalOutTypeSet(self.hdwf, self.idxChannel, v)
    

    def testDigitalOutWait(self):
        """ Test DigitalOutWait Get/Set/Info function """
        rPara   = dwf.DigitalOutWaitInfo(self.hdwf)
        secWait  = dwf.DigitalOutWaitGet(self.hdwf)
        #print("DigitalOutWait      : Info = %s, pOut = %s" % (str(rPara), str((secWait))))
        dwf.DigitalOutWaitSet(self.hdwf, secWait)
    

    def testAnalogOutNodePhase(self):
        """ Test AnalogOutNodePhase Get/Set/Info function """
        rPara   = dwf.AnalogOutNodePhaseInfo(self.hdwf, self.idxChannel, self.node)
        degreePhase  = dwf.AnalogOutNodePhaseGet(self.hdwf, self.idxChannel, self.node)
        #print("AnalogOutNodePhase  : Info = %s, pOut = %s" % (str(rPara), str((degreePhase))))
        dwf.AnalogOutNodePhaseSet(self.hdwf, self.idxChannel, self.node, degreePhase)
    

    def testDigitalInClockSource(self):
        """ Test DigitalInClockSource Get/Set/Info function """
        rPara   = dwf.DigitalInClockSourceInfo(self.hdwf)
        v  = dwf.DigitalInClockSourceGet(self.hdwf)
        #print("DigitalInClockSource: Info = %s, pOut = %s" % (str(rPara), str((v))))
        dwf.DigitalInClockSourceSet(self.hdwf, v)
    

    def testAnalogOutRepeat(self):
        """ Test AnalogOutRepeat Get/Set/Info function """
        rPara   = dwf.AnalogOutRepeatInfo(self.hdwf, self.idxChannel)
        cRepeat  = dwf.AnalogOutRepeatGet(self.hdwf, self.idxChannel)
        #print("AnalogOutRepeat     : Info = %s, pOut = %s" % (str(rPara), str((cRepeat))))
        dwf.AnalogOutRepeatSet(self.hdwf, self.idxChannel, cRepeat)
    

    def testAnalogOutPhase(self):
        """ Test AnalogOutPhase Get/Set/Info function """
        rPara   = dwf.AnalogOutPhaseInfo(self.hdwf, self.idxChannel)
        degreePhase  = dwf.AnalogOutPhaseGet(self.hdwf, self.idxChannel)
        #print("AnalogOutPhase      : Info = %s, pOut = %s" % (str(rPara), str((degreePhase))))
        dwf.AnalogOutPhaseSet(self.hdwf, self.idxChannel, degreePhase)
    

    def testDigitalOutTriggerSource(self):
        """ Test DigitalOutTriggerSource Get/Set/Info function """
        rPara   = dwf.DigitalOutTriggerSourceInfo(self.hdwf)
        trigsrc  = dwf.DigitalOutTriggerSourceGet(self.hdwf)
        #print("DigitalOutTriggerSource: Info = %s, pOut = %s" % (str(rPara), str((trigsrc))))
        dwf.DigitalOutTriggerSourceSet(self.hdwf, trigsrc)
    

    def testDigitalInTriggerSource(self):
        """ Test DigitalInTriggerSource Get/Set/Info function """
        rPara   = dwf.DigitalInTriggerSourceInfo(self.hdwf)
        trigsrc  = dwf.DigitalInTriggerSourceGet(self.hdwf)
        #print("DigitalInTriggerSource: Info = %s, pOut = %s" % (str(rPara), str((trigsrc))))
        dwf.DigitalInTriggerSourceSet(self.hdwf, trigsrc)
    

    def testAnalogInTriggerLevel(self):
        """ Test AnalogInTriggerLevel Get/Set/Info function """
        rPara   = dwf.AnalogInTriggerLevelInfo(self.hdwf)
        voltsLevel  = dwf.AnalogInTriggerLevelGet(self.hdwf)
        #print("AnalogInTriggerLevel: Info = %s, pOut = %s" % (str(rPara), str((voltsLevel))))
        dwf.AnalogInTriggerLevelSet(self.hdwf, voltsLevel)
    

    def testDigitalInSampleFormat(self):
        """ Test DigitalInSampleFormat Get/Set function """
        nBits  = dwf.DigitalInSampleFormatGet(self.hdwf)
        #print("DigitalInSampleFormat: Info = %s, pOut = %s" % (str(rPara), str((nBits))))
        dwf.DigitalInSampleFormatSet(self.hdwf, nBits)
    

    def testAnalogInFrequency(self):
        """ Test AnalogInFrequency Get/Set/Info function """
        rPara   = dwf.AnalogInFrequencyInfo(self.hdwf)
        hzFrequency  = dwf.AnalogInFrequencyGet(self.hdwf)
        #print("AnalogInFrequency   : Info = %s, pOut = %s" % (str(rPara), str((hzFrequency))))
        dwf.AnalogInFrequencySet(self.hdwf, hzFrequency)
    

    def testAnalogInTriggerAutoTimeout(self):
        """ Test AnalogInTriggerAutoTimeout Get/Set/Info function """
        rPara   = dwf.AnalogInTriggerAutoTimeoutInfo(self.hdwf)
        secTimeout  = dwf.AnalogInTriggerAutoTimeoutGet(self.hdwf)
        #print("AnalogInTriggerAutoTimeout: Info = %s, pOut = %s" % (str(rPara), str((secTimeout))))
        dwf.AnalogInTriggerAutoTimeoutSet(self.hdwf, secTimeout)
    

    def testDigitalOutRepeatTrigger(self):
        """ Test DigitalOutRepeatTrigger Get/Set function """
        fRepeatTrigger  = dwf.DigitalOutRepeatTriggerGet(self.hdwf)
        #print("DigitalOutRepeatTrigger: Info = %s, pOut = %s" % (str(rPara), str((fRepeatTrigger))))
        dwf.DigitalOutRepeatTriggerSet(self.hdwf, fRepeatTrigger)
    

    def testAnalogIOEnable(self):
        """ Test AnalogIOEnable Get/Set/Info function """
        rPara   = dwf.AnalogIOEnableInfo(self.hdwf)
        fMasterEnable  = dwf.AnalogIOEnableGet(self.hdwf)
        #print("AnalogIOEnable      : Info = %s, pOut = %s" % (str(rPara), str((fMasterEnable))))
        dwf.AnalogIOEnableSet(self.hdwf, fMasterEnable)
    

    def testAnalogOutNodeFrequency(self):
        """ Test AnalogOutNodeFrequency Get/Set/Info function """
        rPara   = dwf.AnalogOutNodeFrequencyInfo(self.hdwf, self.idxChannel, self.node)
        hzFrequency  = dwf.AnalogOutNodeFrequencyGet(self.hdwf, self.idxChannel, self.node)
        #print("AnalogOutNodeFrequency: Info = %s, pOut = %s" % (str(rPara), str((hzFrequency))))
        dwf.AnalogOutNodeFrequencySet(self.hdwf, self.idxChannel, self.node, hzFrequency)
    

    def testAnalogOutFunction(self):
        """ Test AnalogOutFunction Get/Set/Info function """
        rPara   = dwf.AnalogOutFunctionInfo(self.hdwf, self.idxChannel)
        func  = dwf.AnalogOutFunctionGet(self.hdwf, self.idxChannel)
        #print("AnalogOutFunction   : Info = %s, pOut = %s" % (str(rPara), str((func))))
        dwf.AnalogOutFunctionSet(self.hdwf, self.idxChannel, func)
    

    def testAnalogOutOffset(self):
        """ Test AnalogOutOffset Get/Set/Info function """
        rPara   = dwf.AnalogOutOffsetInfo(self.hdwf, self.idxChannel)
        voltsOffset  = dwf.AnalogOutOffsetGet(self.hdwf, self.idxChannel)
        #print("AnalogOutOffset     : Info = %s, pOut = %s" % (str(rPara), str((voltsOffset))))
        dwf.AnalogOutOffsetSet(self.hdwf, self.idxChannel, voltsOffset)
    

    def testAnalogOutRepeatTrigger(self):
        """ Test AnalogOutRepeatTrigger Get/Set function """
        fRepeatTrigger  = dwf.AnalogOutRepeatTriggerGet(self.hdwf, self.idxChannel)
        #print("AnalogOutRepeatTrigger: Info = %s, pOut = %s" % (str(rPara), str((fRepeatTrigger))))
        dwf.AnalogOutRepeatTriggerSet(self.hdwf, self.idxChannel, fRepeatTrigger)
    

    def testDigitalInTrigger(self):
        """ Test DigitalInTrigger Get/Set/Info function """
        rPara   = dwf.DigitalInTriggerInfo(self.hdwf)
        fsLevelLow, fsLevelHigh, fsEdgeRise, fsEdgeFall  = dwf.DigitalInTriggerGet(self.hdwf)
        #print("DigitalInTrigger    : Info = %s, pOut = %s" % (str(rPara), str((fsLevelLow, fsLevelHigh, fsEdgeRise, fsEdgeFall))))
        dwf.DigitalInTriggerSet(self.hdwf, fsLevelLow, fsLevelHigh, fsEdgeRise, fsEdgeFall)
    

    def testAnalogInChannelRange(self):
        """ Test AnalogInChannelRange Get/Set/Info function """
        rPara   = dwf.AnalogInChannelRangeInfo(self.hdwf)
        voltsRange  = dwf.AnalogInChannelRangeGet(self.hdwf, self.idxChannel)
        #print("AnalogInChannelRange: Info = %s, pOut = %s" % (str(rPara), str((voltsRange))))
        dwf.AnalogInChannelRangeSet(self.hdwf, self.idxChannel, voltsRange)
    

    def testAnalogInTriggerChannel(self):
        """ Test AnalogInTriggerChannel Get/Set/Info function """
        rPara   = dwf.AnalogInTriggerChannelInfo(self.hdwf)
        idxChannel  = dwf.AnalogInTriggerChannelGet(self.hdwf)
        #print("AnalogInTriggerChannel: Info = %s, pOut = %s" % (str(rPara), str((idxChannel))))
        dwf.AnalogInTriggerChannelSet(self.hdwf, idxChannel)
    

    def testAnalogOutMaster(self):
        """ Test AnalogOutMaster Get/Set function """
        idxMaster  = dwf.AnalogOutMasterGet(self.hdwf, self.idxChannel)
        #print("AnalogOutMaster     : Info = %s, pOut = %s" % (str(rPara), str((idxMaster))))
        dwf.AnalogOutMasterSet(self.hdwf, self.idxChannel, idxMaster)
    

    def testDigitalOutOutput(self):
        """ Test DigitalOutOutput Get/Set/Info function """
        rPara   = dwf.DigitalOutOutputInfo(self.hdwf, self.idxChannel)
        v  = dwf.DigitalOutOutputGet(self.hdwf, self.idxChannel)
        #print("DigitalOutOutput    : Info = %s, pOut = %s" % (str(rPara), str((v))))
        dwf.DigitalOutOutputSet(self.hdwf, self.idxChannel, v)
    

    def testAnalogInTriggerHysteresis(self):
        """ Test AnalogInTriggerHysteresis Get/Set/Info function """
        rPara   = dwf.AnalogInTriggerHysteresisInfo(self.hdwf)
        voltsHysteresis  = dwf.AnalogInTriggerHysteresisGet(self.hdwf)
        #print("AnalogInTriggerHysteresis: Info = %s, pOut = %s" % (str(rPara), str((voltsHysteresis))))
        dwf.AnalogInTriggerHysteresisSet(self.hdwf, voltsHysteresis)
    

    def testDigitalOutRepeat(self):
        """ Test DigitalOutRepeat Get/Set/Info function """
        rPara   = dwf.DigitalOutRepeatInfo(self.hdwf)
        cRepeat  = dwf.DigitalOutRepeatGet(self.hdwf)
        #print("DigitalOutRepeat    : Info = %s, pOut = %s" % (str(rPara), str((cRepeat))))
        dwf.DigitalOutRepeatSet(self.hdwf, cRepeat)
    

    def testAnalogOutNodeAmplitude(self):
        """ Test AnalogOutNodeAmplitude Get/Set/Info function """
        rPara   = dwf.AnalogOutNodeAmplitudeInfo(self.hdwf, self.idxChannel, self.node)
        vAmplitude  = dwf.AnalogOutNodeAmplitudeGet(self.hdwf, self.idxChannel, self.node)
        #print("AnalogOutNodeAmplitude: Info = %s, pOut = %s" % (str(rPara), str((vAmplitude))))
        dwf.AnalogOutNodeAmplitudeSet(self.hdwf, self.idxChannel, self.node, vAmplitude)
    

    def testDigitalInBufferSize(self):
        """ Test DigitalInBufferSize Get/Set/Info function """
        rPara   = dwf.DigitalInBufferSizeInfo(self.hdwf)
        nSize  = dwf.DigitalInBufferSizeGet(self.hdwf)
        #print("DigitalInBufferSize : Info = %s, pOut = %s" % (str(rPara), str((nSize))))
        dwf.DigitalInBufferSizeSet(self.hdwf, nSize)
    

    def testAnalogInTriggerHoldOff(self):
        """ Test AnalogInTriggerHoldOff Get/Set/Info function """
        rPara   = dwf.AnalogInTriggerHoldOffInfo(self.hdwf)
        secHoldOff  = dwf.AnalogInTriggerHoldOffGet(self.hdwf)
        #print("AnalogInTriggerHoldOff: Info = %s, pOut = %s" % (str(rPara), str((secHoldOff))))
        dwf.AnalogInTriggerHoldOffSet(self.hdwf, secHoldOff)
    

    def testAnalogInChannelOffset(self):
        """ Test AnalogInChannelOffset Get/Set/Info function """
        rPara   = dwf.AnalogInChannelOffsetInfo(self.hdwf)
        voltOffset  = dwf.AnalogInChannelOffsetGet(self.hdwf, self.idxChannel)
        #print("AnalogInChannelOffset: Info = %s, pOut = %s" % (str(rPara), str((voltOffset))))
        dwf.AnalogInChannelOffsetSet(self.hdwf, self.idxChannel, voltOffset)
    

    def testDigitalIOOutput(self):
        """ Test DigitalIOOutput Get/Set/Info function """
        rPara   = dwf.DigitalIOOutputInfo(self.hdwf)
        fsOutput  = dwf.DigitalIOOutputGet(self.hdwf)
        #print("DigitalIOOutput     : Info = %s, pOut = %s" % (str(rPara), str((fsOutput))))
        dwf.DigitalIOOutputSet(self.hdwf, fsOutput)
    

    def testDigitalOutCounterInit(self):
        """ Test DigitalOutCounterInit Get/Set function """
        fHigh, v  = dwf.DigitalOutCounterInitGet(self.hdwf, self.idxChannel)
        #print("DigitalOutCounterInit: Info = %s, pOut = %s" % (str(rPara), str((fHigh, v))))
        dwf.DigitalOutCounterInitSet(self.hdwf, self.idxChannel, fHigh, v)
    

    def testAnalogInBufferSize(self):
        """ Test AnalogInBufferSize Get/Set/Info function """
        rPara   = dwf.AnalogInBufferSizeInfo(self.hdwf)
        nSize  = dwf.AnalogInBufferSizeGet(self.hdwf)
        #print("AnalogInBufferSize  : Info = %s, pOut = %s" % (str(rPara), str((nSize))))
        dwf.AnalogInBufferSizeSet(self.hdwf, nSize)
    

    def testAnalogOutRun(self):
        """ Test AnalogOutRun Get/Set/Info function """
        rPara   = dwf.AnalogOutRunInfo(self.hdwf, self.idxChannel)
        secRun  = dwf.AnalogOutRunGet(self.hdwf, self.idxChannel)
        #print("AnalogOutRun        : Info = %s, pOut = %s" % (str(rPara), str((secRun))))
        dwf.AnalogOutRunSet(self.hdwf, self.idxChannel, secRun)
    
    def tearDown(self):
        dwf.DeviceClose(self.hdwf)

if __name__ == '__main__':
    unittest.main()
