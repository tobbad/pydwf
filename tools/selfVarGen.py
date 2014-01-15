#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Created on %(date)s

    

    @author: %(username)s
    
"""
import sys
import os

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

msg='''
......E......E.....E...E.....E..E..EEE..E.E.E.E.......E.....E..E..E..E..E..E..E..E.....E..E.....E....E..E..E.E....E..E...E..EE...E..E..EE...............E.......EFDwfDeviceClose returns 0
.FDwfDeviceClose returns 0
.FDwfDeviceOpen returns 0
...........E..E....E...E...E..E...E...E......E....EE...........................................................
======================================================================
ERROR: testAnalogIOChannelNodeSet (__main__.TestOtherFunctions)
Test AnalogIOChannelNodeSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 68, in testAnalogIOChannelNodeSet
    dummy  = dwf.AnalogIOChannelNodeSet(self.hdwf, self.idxChannel, self.idxNode, self.value)
AttributeError: 'TestOtherFunctions' object has no attribute 'value'

======================================================================
ERROR: testAnalogIOEnableSet (__main__.TestOtherFunctions)
Test AnalogIOEnableSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 103, in testAnalogIOEnableSet
    dummy  = dwf.AnalogIOEnableSet(self.hdwf, self.fMasterEnable)
AttributeError: 'TestOtherFunctions' object has no attribute 'fMasterEnable'

======================================================================
ERROR: testAnalogInAcquisitionModeSet (__main__.TestOtherFunctions)
Test AnalogInAcquisitionModeSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 133, in testAnalogInAcquisitionModeSet
    dummy  = dwf.AnalogInAcquisitionModeSet(self.hdwf, self.acqmode)
AttributeError: 'TestOtherFunctions' object has no attribute 'acqmode'

======================================================================
ERROR: testAnalogInBufferSizeSet (__main__.TestOtherFunctions)
Test AnalogInBufferSizeSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 153, in testAnalogInBufferSizeSet
    dummy  = dwf.AnalogInBufferSizeSet(self.hdwf, self.nSize)
AttributeError: 'TestOtherFunctions' object has no attribute 'nSize'

======================================================================
ERROR: testAnalogInChannelFilterSet (__main__.TestOtherFunctions)
Test AnalogInChannelFilterSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 183, in testAnalogInChannelFilterSet
    dummy  = dwf.AnalogInChannelFilterSet(self.hdwf, self.idxChannel, self.filter)
AttributeError: 'TestOtherFunctions' object has no attribute 'filter'

======================================================================
ERROR: testAnalogInChannelOffsetSet (__main__.TestOtherFunctions)
Test AnalogInChannelOffsetSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 198, in testAnalogInChannelOffsetSet
    dummy  = dwf.AnalogInChannelOffsetSet(self.hdwf, self.idxChannel, self.voltOffset)
AttributeError: 'TestOtherFunctions' object has no attribute 'voltOffset'

======================================================================
ERROR: testAnalogInChannelRangeSet (__main__.TestOtherFunctions)
Test AnalogInChannelRangeSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 213, in testAnalogInChannelRangeSet
    dummy  = dwf.AnalogInChannelRangeSet(self.hdwf, self.idxChannel, self.voltsRange)
AttributeError: 'TestOtherFunctions' object has no attribute 'voltsRange'

======================================================================
ERROR: testAnalogInChannelRangeSteps (__main__.TestOtherFunctions)
Test AnalogInChannelRangeSteps
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 218, in testAnalogInChannelRangeSteps
    nSteps  = dwf.AnalogInChannelRangeSteps(self.hdwf, self.rgVoltsStep[32])
AttributeError: 'TestOtherFunctions' object has no attribute 'rgVoltsStep'

======================================================================
ERROR: testAnalogInConfigure (__main__.TestOtherFunctions)
Test AnalogInConfigure
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 223, in testAnalogInConfigure
    dummy  = dwf.AnalogInConfigure(self.hdwf, self.fReconfigure, self.fStart)
AttributeError: 'TestOtherFunctions' object has no attribute 'fReconfigure'

======================================================================
ERROR: testAnalogInFrequencySet (__main__.TestOtherFunctions)
Test AnalogInFrequencySet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 238, in testAnalogInFrequencySet
    dummy  = dwf.AnalogInFrequencySet(self.hdwf, self.hzFrequency)
AttributeError: 'TestOtherFunctions' object has no attribute 'hzFrequency'

======================================================================
ERROR: testAnalogInRecordLengthSet (__main__.TestOtherFunctions)
Test AnalogInRecordLengthSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 248, in testAnalogInRecordLengthSet
    dummy  = dwf.AnalogInRecordLengthSet(self.hdwf, self.sLegth)
AttributeError: 'TestOtherFunctions' object has no attribute 'sLegth'

======================================================================
ERROR: testAnalogInStatus (__main__.TestOtherFunctions)
Test AnalogInStatus
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 258, in testAnalogInStatus
    sts  = dwf.AnalogInStatus(self.hdwf, self.fReadData)
AttributeError: 'TestOtherFunctions' object has no attribute 'fReadData'

======================================================================
ERROR: testAnalogInStatusData (__main__.TestOtherFunctions)
Test AnalogInStatusData
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 268, in testAnalogInStatusData
    dummy  = dwf.AnalogInStatusData(self.hdwf, self.idxChannel, self.rgdVoltData)
AttributeError: 'TestOtherFunctions' object has no attribute 'rgdVoltData'

======================================================================
ERROR: testAnalogInTriggerAutoTimeoutSet (__main__.TestOtherFunctions)
Test AnalogInTriggerAutoTimeoutSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 308, in testAnalogInTriggerAutoTimeoutSet
    dummy  = dwf.AnalogInTriggerAutoTimeoutSet(self.hdwf, self.secTimeout)
AttributeError: 'TestOtherFunctions' object has no attribute 'secTimeout'

======================================================================
ERROR: testAnalogInTriggerConditionSet (__main__.TestOtherFunctions)
Test AnalogInTriggerConditionSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 338, in testAnalogInTriggerConditionSet
    dummy  = dwf.AnalogInTriggerConditionSet(self.hdwf, self.trigcond)
AttributeError: 'TestOtherFunctions' object has no attribute 'trigcond'

======================================================================
ERROR: testAnalogInTriggerFilterSet (__main__.TestOtherFunctions)
Test AnalogInTriggerFilterSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 353, in testAnalogInTriggerFilterSet
    dummy  = dwf.AnalogInTriggerFilterSet(self.hdwf, self.filter)
AttributeError: 'TestOtherFunctions' object has no attribute 'filter'

======================================================================
ERROR: testAnalogInTriggerHoldOffSet (__main__.TestOtherFunctions)
Test AnalogInTriggerHoldOffSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 368, in testAnalogInTriggerHoldOffSet
    dummy  = dwf.AnalogInTriggerHoldOffSet(self.hdwf, self.secHoldOff)
AttributeError: 'TestOtherFunctions' object has no attribute 'secHoldOff'

======================================================================
ERROR: testAnalogInTriggerHysteresisSet (__main__.TestOtherFunctions)
Test AnalogInTriggerHysteresisSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 383, in testAnalogInTriggerHysteresisSet
    dummy  = dwf.AnalogInTriggerHysteresisSet(self.hdwf, self.voltsLevel)
AttributeError: 'TestOtherFunctions' object has no attribute 'voltsLevel'

======================================================================
ERROR: testAnalogInTriggerLengthConditionSet (__main__.TestOtherFunctions)
Test AnalogInTriggerLengthConditionSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 398, in testAnalogInTriggerLengthConditionSet
    dummy  = dwf.AnalogInTriggerLengthConditionSet(self.hdwf, self.triglen)
AttributeError: 'TestOtherFunctions' object has no attribute 'triglen'

======================================================================
ERROR: testAnalogInTriggerLengthSet (__main__.TestOtherFunctions)
Test AnalogInTriggerLengthSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 413, in testAnalogInTriggerLengthSet
    dummy  = dwf.AnalogInTriggerLengthSet(self.hdwf, self.secLength)
AttributeError: 'TestOtherFunctions' object has no attribute 'secLength'

======================================================================
ERROR: testAnalogInTriggerLevelSet (__main__.TestOtherFunctions)
Test AnalogInTriggerLevelSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 428, in testAnalogInTriggerLevelSet
    dummy  = dwf.AnalogInTriggerLevelSet(self.hdwf, self.voltsLevel)
AttributeError: 'TestOtherFunctions' object has no attribute 'voltsLevel'

======================================================================
ERROR: testAnalogInTriggerPositionSet (__main__.TestOtherFunctions)
Test AnalogInTriggerPositionSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 443, in testAnalogInTriggerPositionSet
    dummy  = dwf.AnalogInTriggerPositionSet(self.hdwf, self.secPosition)
AttributeError: 'TestOtherFunctions' object has no attribute 'secPosition'

======================================================================
ERROR: testAnalogInTriggerTypeSet (__main__.TestOtherFunctions)
Test AnalogInTriggerTypeSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 473, in testAnalogInTriggerTypeSet
    dummy  = dwf.AnalogInTriggerTypeSet(self.hdwf, self.trigtype)
AttributeError: 'TestOtherFunctions' object has no attribute 'trigtype'

======================================================================
ERROR: testAnalogOutAmplitudeSet (__main__.TestOtherFunctions)
Test AnalogOutAmplitudeSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 488, in testAnalogOutAmplitudeSet
    dummy  = dwf.AnalogOutAmplitudeSet(self.hdwf, self.idxChannel, self.voltsAmplitude)
AttributeError: 'TestOtherFunctions' object has no attribute 'voltsAmplitude'

======================================================================
ERROR: testAnalogOutDataSet (__main__.TestOtherFunctions)
Test AnalogOutDataSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 518, in testAnalogOutDataSet
    dummy  = dwf.AnalogOutDataSet(self.hdwf, self.idxChannel, self.rgdData)
AttributeError: 'TestOtherFunctions' object has no attribute 'rgdData'

======================================================================
ERROR: testAnalogOutFrequencySet (__main__.TestOtherFunctions)
Test AnalogOutFrequencySet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 543, in testAnalogOutFrequencySet
    dummy  = dwf.AnalogOutFrequencySet(self.hdwf, self.idxChannel, self.hzFrequency)
AttributeError: 'TestOtherFunctions' object has no attribute 'hzFrequency'

======================================================================
ERROR: testAnalogOutFunctionSet (__main__.TestOtherFunctions)
Test AnalogOutFunctionSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 558, in testAnalogOutFunctionSet
    dummy  = dwf.AnalogOutFunctionSet(self.hdwf, self.idxChannel, self.func)
AttributeError: 'TestOtherFunctions' object has no attribute 'func'

======================================================================
ERROR: testAnalogOutNodeAmplitudeSet (__main__.TestOtherFunctions)
Test AnalogOutNodeAmplitudeSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 573, in testAnalogOutNodeAmplitudeSet
    dummy  = dwf.AnalogOutNodeAmplitudeSet(self.hdwf, self.idxChannel, self.node, self.vAmplitude)
AttributeError: 'TestOtherFunctions' object has no attribute 'vAmplitude'

======================================================================
ERROR: testAnalogOutNodeDataSet (__main__.TestOtherFunctions)
Test AnalogOutNodeDataSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 583, in testAnalogOutNodeDataSet
    dummy  = dwf.AnalogOutNodeDataSet(self.hdwf, self.idxChannel, self.node, self.rgdData)
AttributeError: 'TestOtherFunctions' object has no attribute 'rgdData'

======================================================================
ERROR: testAnalogOutNodeFrequencySet (__main__.TestOtherFunctions)
Test AnalogOutNodeFrequencySet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 608, in testAnalogOutNodeFrequencySet
    dummy  = dwf.AnalogOutNodeFrequencySet(self.hdwf, self.idxChannel, self.node, self.hzFrequency)
AttributeError: 'TestOtherFunctions' object has no attribute 'hzFrequency'

======================================================================
ERROR: testAnalogOutNodeFunctionSet (__main__.TestOtherFunctions)
Test AnalogOutNodeFunctionSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 623, in testAnalogOutNodeFunctionSet
    dummy  = dwf.AnalogOutNodeFunctionSet(self.hdwf, self.idxChannel, self.node, self.func)
AttributeError: 'TestOtherFunctions' object has no attribute 'func'

======================================================================
ERROR: testAnalogOutNodeOffsetSet (__main__.TestOtherFunctions)
Test AnalogOutNodeOffsetSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 643, in testAnalogOutNodeOffsetSet
    dummy  = dwf.AnalogOutNodeOffsetSet(self.hdwf, self.idxChannel, self.node, self.vOffset)
AttributeError: 'TestOtherFunctions' object has no attribute 'vOffset'

======================================================================
ERROR: testAnalogOutNodePhaseSet (__main__.TestOtherFunctions)
Test AnalogOutNodePhaseSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 658, in testAnalogOutNodePhaseSet
    dummy  = dwf.AnalogOutNodePhaseSet(self.hdwf, self.idxChannel, self.node, self.degreePhase)
AttributeError: 'TestOtherFunctions' object has no attribute 'degreePhase'

======================================================================
ERROR: testAnalogOutNodePlayData (__main__.TestOtherFunctions)
Test AnalogOutNodePlayData
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 663, in testAnalogOutNodePlayData
    dummy  = dwf.AnalogOutNodePlayData(self.hdwf, self.idxChannel, self.node, self.rgdData)
AttributeError: 'TestOtherFunctions' object has no attribute 'rgdData'

======================================================================
ERROR: testAnalogOutNodeSymmetrySet (__main__.TestOtherFunctions)
Test AnalogOutNodeSymmetrySet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 683, in testAnalogOutNodeSymmetrySet
    dummy  = dwf.AnalogOutNodeSymmetrySet(self.hdwf, self.idxChannel, self.node, self.percentageSymmetry)
AttributeError: 'TestOtherFunctions' object has no attribute 'percentageSymmetry'

======================================================================
ERROR: testAnalogOutOffsetSet (__main__.TestOtherFunctions)
Test AnalogOutOffsetSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 698, in testAnalogOutOffsetSet
    dummy  = dwf.AnalogOutOffsetSet(self.hdwf, self.idxChannel, self.voltsOffset)
AttributeError: 'TestOtherFunctions' object has no attribute 'voltsOffset'

======================================================================
ERROR: testAnalogOutPhaseSet (__main__.TestOtherFunctions)
Test AnalogOutPhaseSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 713, in testAnalogOutPhaseSet
    dummy  = dwf.AnalogOutPhaseSet(self.hdwf, self.idxChannel, self.degreePhase)
AttributeError: 'TestOtherFunctions' object has no attribute 'degreePhase'

======================================================================
ERROR: testAnalogOutPlayData (__main__.TestOtherFunctions)
Test AnalogOutPlayData
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 718, in testAnalogOutPlayData
    dummy  = dwf.AnalogOutPlayData(self.hdwf, self.idxChannel, self.rgdData)
AttributeError: 'TestOtherFunctions' object has no attribute 'rgdData'

======================================================================
ERROR: testAnalogOutSymmetrySet (__main__.TestOtherFunctions)
Test AnalogOutSymmetrySet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 798, in testAnalogOutSymmetrySet
    dummy  = dwf.AnalogOutSymmetrySet(self.hdwf, self.idxChannel, self.percentageSymmetry)
AttributeError: 'TestOtherFunctions' object has no attribute 'percentageSymmetry'

======================================================================
ERROR: testDeviceAutoConfigureSet (__main__.TestOtherFunctions)
Test DeviceAutoConfigureSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 838, in testDeviceAutoConfigureSet
    dummy  = dwf.DeviceAutoConfigureSet(self.hdwf, self.fConfigureWhenSet)
AttributeError: 'TestOtherFunctions' object has no attribute 'fConfigureWhenSet'

======================================================================
ERROR: testDigitalIOOutputEnableSet (__main__.TestOtherFunctions)
Test DigitalIOOutputEnableSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 908, in testDigitalIOOutputEnableSet
    dummy  = dwf.DigitalIOOutputEnableSet(self.hdwf, self.fsOutputEnable)
AttributeError: 'TestOtherFunctions' object has no attribute 'fsOutputEnable'

======================================================================
ERROR: testDigitalIOOutputSet (__main__.TestOtherFunctions)
Test DigitalIOOutputSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 923, in testDigitalIOOutputSet
    dummy  = dwf.DigitalIOOutputSet(self.hdwf, self.fsOutput)
AttributeError: 'TestOtherFunctions' object has no attribute 'fsOutput'

======================================================================
ERROR: testDigitalInAcquisitionModeSet (__main__.TestOtherFunctions)
Test DigitalInAcquisitionModeSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 948, in testDigitalInAcquisitionModeSet
    dummy  = dwf.DigitalInAcquisitionModeSet(self.hdwf, self.acqmode)
AttributeError: 'TestOtherFunctions' object has no attribute 'acqmode'

======================================================================
ERROR: testDigitalInBufferSizeSet (__main__.TestOtherFunctions)
Test DigitalInBufferSizeSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 968, in testDigitalInBufferSizeSet
    dummy  = dwf.DigitalInBufferSizeSet(self.hdwf, self.nSize)
AttributeError: 'TestOtherFunctions' object has no attribute 'nSize'

======================================================================
ERROR: testDigitalInConfigure (__main__.TestOtherFunctions)
Test DigitalInConfigure
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 988, in testDigitalInConfigure
    dummy  = dwf.DigitalInConfigure(self.hdwf, self.fReconfigure, self.fStart)
AttributeError: 'TestOtherFunctions' object has no attribute 'fReconfigure'

======================================================================
ERROR: testDigitalInDividerSet (__main__.TestOtherFunctions)
Test DigitalInDividerSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 1003, in testDigitalInDividerSet
    dummy  = dwf.DigitalInDividerSet(self.hdwf, self.div)
AttributeError: 'TestOtherFunctions' object has no attribute 'div'

======================================================================
ERROR: testDigitalInSampleFormatSet (__main__.TestOtherFunctions)
Test DigitalInSampleFormatSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 1023, in testDigitalInSampleFormatSet
    dummy  = dwf.DigitalInSampleFormatSet(self.hdwf, self.nBits)
AttributeError: 'TestOtherFunctions' object has no attribute 'nBits'

======================================================================
ERROR: testDigitalInStatus (__main__.TestOtherFunctions)
Test DigitalInStatus
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 1043, in testDigitalInStatus
    sts  = dwf.DigitalInStatus(self.hdwf, self.fReadData)
AttributeError: 'TestOtherFunctions' object has no attribute 'fReadData'

======================================================================
ERROR: testDigitalInTriggerAutoTimeoutSet (__main__.TestOtherFunctions)
Test DigitalInTriggerAutoTimeoutSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 1078, in testDigitalInTriggerAutoTimeoutSet
    dummy  = dwf.DigitalInTriggerAutoTimeoutSet(self.hdwf, self.secTimeout)
AttributeError: 'TestOtherFunctions' object has no attribute 'secTimeout'

======================================================================
ERROR: testDigitalInTriggerPositionSet (__main__.TestOtherFunctions)
Test DigitalInTriggerPositionSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 1103, in testDigitalInTriggerPositionSet
    dummy  = dwf.DigitalInTriggerPositionSet(self.hdwf, self.cSamplesAfterTrigger)
AttributeError: 'TestOtherFunctions' object has no attribute 'cSamplesAfterTrigger'

======================================================================
ERROR: testDigitalInTriggerSet (__main__.TestOtherFunctions)
Test DigitalInTriggerSet
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/badi/projekte/sw/python/analogDiscovery/test_handMade.py", line 1108, in testDigitalInTriggerSet
    dummy  = dwf.DigitalInTriggerSet(self.hdwf, self.fsLevelLow, self.fsLevelHigh, self.fsEdgeRise, self.fsEdgeFall)
AttributeError: 'TestOtherFunctions' object has no attribute 'fsEdgeRise'

----------------------------------------------------------------------
Ran 274 tests in 104.790s

FAILED (errors=51)

'''

def main():
    isDone=[]
    for li in msg.split('\n'):
        if 'AttributeError' in li:
            varName =  li.split()[-1]
            if not varName in isDone:
                print("defVal[%s]=0" % varName)
                isDone.append(varName)
            
        pass


if __name__ == '__main__':
    main()
