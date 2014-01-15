#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Created on 10.10.2013

    

    @author: Tobias Badertscher
    
"""
import sys
sys.path.append('..')
from dwf import dwf
import os
import time
import re
import inspect

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

allFunc=[]
allFuncDict = {}

def fName2ParaInOut(fName, docStr=None):
    if docStr == None:
        docStr = allFuncDict[fName].__doc__
    inPara =[i.strip() for i in docStr.split('->')[0].split('(')[1].strip(') ').split(',')]
    if len(inPara[0])>0:
        pInLi = [p.split()[-1] for p in inPara]
    else:
        pInLi = []
    outPara =[i.strip() for i in docStr.split('->')[1].strip(' ()').split(',')]
    if len(outPara[0])>0:
        pOutLi = [p.split()[-1] for p in outPara]
    else:
        pOutLi = []
    return pInLi, pOutLi

if 1==0:
    iP, oP = fName2ParaInOut('dummy',docStr='AnalogIOChannelNodeSet(HDWF hdwf, int idxChannel, int idxNode, double value) -> (  )')
    print(iP)
    print(oP)
    sys.exit()


def getAllGetSetInfoFunc():
    resMatch = {}
    otherFunc = {}
    fuCount = 0
    fuRe=r'(.+)(Get|Set|Info)'
    for obj in inspect.getmembers(dwf):
        if inspect.isfunction(obj[1]):
            reMo=re.match(fuRe, obj[0])
            if '_swig_' in obj[0]:
                continue
            allFunc.append(obj[0])
            allFuncDict[obj[0]] = obj[1]
            fuCount +=1
            if reMo:
                fuBaseName = reMo.groups()[0]
                if fuBaseName not in resMatch:
                    resMatch[fuBaseName]=[obj[0],]
                else:
                    resMatch[fuBaseName].append(obj[0])
                pInLi, pOutLi = fName2ParaInOut(obj[0])
                if obj[0][-4:] == 'Info':
                    resMatch[fuBaseName+'_pIn']=pInLi
                if obj[0][-3:] == 'Get':
                    resMatch[fuBaseName+'_pOut']=pOutLi
            else:
                fuName = obj[0]
                pInLi, pOutLi = fName2ParaInOut(fuName)
                otherFunc[fuName]       =obj[1]
                otherFunc[fuName+'_pIn']=pInLi
                otherFunc[fuName+'_pOut']=pOutLi
                print("Function %-35s not covered!" % fuName)
    return resMatch, otherFunc, fuCount


header=r'''#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Generated on {date}    

    @author: Tobias Badertscher
    
"""
import sys
sys.path.append('..')
from dwf import dwf
import numpy as np 
import unittest
# Generated unit test.
class Test{classname}(unittest.TestCase):
'''
defVal={}
defVal['idxChannel']= 0
defVal['idxNode']   = 0
defVal['idxDevice'] = 0
defVal['node']      = 0
defVal['idxPin']    = 0
defVal['enumfilter']= 'dwf.enumfilterAll'
defVal['hdwf']      = "dwf.DeviceOpen(0)"
defVal['secWait']   = 1
defVal['secRun']    = 1
defVal['v']         = 'dwf.DwfDigitalOutOutputPushPull'
defVal['trigsrc']   = 'dwf.trigsrcNone'
defVal['fRepeatTrigger']   = True
defVal['cRepeat']   = 0
defVal['fEnable']   = True
defVal['vLow']      = 10
defVal['vHigh']     = 100
defVal['fHigh']     = True
defVal['fStart']    = False
defVal['fsLevelLow']= 0
defVal['fsLevelHigh']= 1
defVal['value']=0
defVal['fMasterEnable']=0
defVal['acqmode']=0
defVal['nSize']=0
defVal['filter']=0
defVal['voltOffset']=0
defVal['voltsRange']=0
defVal['rgVoltsStep']=0
defVal['fReconfigure']=0
defVal['hzFrequency']=0
defVal['sLegth']=0
defVal['fReadData']=0
defVal['rgdVoltData']="np.zeros(100, dtype='double')"
defVal['secTimeout']=0
defVal['trigcond']=0
defVal['secHoldOff']=0
defVal['voltsLevel']=0
defVal['triglen']=0
defVal['secLength']=0
defVal['secPosition']=0
defVal['trigtype']=0
defVal['voltsAmplitude']=0
defVal['rgdData']="np.zeros(100, dtype='double')"
defVal['func']=0
defVal['vAmplitude']=0
defVal['vOffset']=0
defVal['degreePhase']=0
defVal['percentageSymmetry']=0
defVal['voltsOffset']=0
defVal['fConfigureWhenSet']=0
defVal['fsOutputEnable']=0
defVal['fsOutput']=0
defVal['div']=0
defVal['fsEdgeFall']=0
defVal['nBits']=0
defVal['cSamplesAfterTrigger']=0
defVal['fsEdgeRise']=0


fuFullTpl=r'''
{space}def test{fuName}(self):
{space}    """ Test {fuName} Get/Set/Info function """
{space}    rPara   = dwf.{fuName}Info({fuInPara})
{space}    {pGet}  = dwf.{fuName}Get({fuInPara}{fuCaModStr})
{space}    #print("{fuName:20}: Info = %s, pOut = %s" % (str(rPara), str(({pGet}))))
{space}    dwf.{fuName}Set({fuInPara}{fuCaModStr}{pGetC})
{space}
'''
fuTpl=r'''
{space}def test{fuName}(self):
{space}    """ Test {fuName} Get/Set function """
{space}    {pGet}  = dwf.{fuName}Get({fuInPara}{fuCaModStr})
{space}    #print("{fuName:20}: Info = %s, pOut = %s" % (str(rPara), str(({pGet}))))
{space}    dwf.{fuName}Set({fuInPara}{fuCaModStr}{pGetC})
{space}
'''

fuOtherTpl=r'''
{space}def test{fuName}(self):
{space}    """ Test {fuName} """
{space}    {pGet}  = dwf.{fuName}({fuInPara})
{space}
'''

fuCaMod={}
fuCaMod['DeviceTrigger']        =", self.idxPin"
fuCaMod['AnalogInChannelRange'] =", self.idxChannel"
fuCaMod['AnalogInChannelOffset']=", self.idxChannel"
fuCaMod['AnalogInChannelFilter'] =", self.idxChannel"

def generateTestGetSetInfoFile(fName, fuLi):
    testFuCount=0
    fuNotDone = {}
    with open(fName, 'w') as fd:
        date = time.strftime("%d.%m.%Y %H:%M:%S")
        fd.write(header.format(date=date, classname= 'GetSetInfo'))
        fd.write("%sdef setUp(self):\n" % (" "*4))
        fd.write("%sa = dwf.Enum(dwf.enumfilterAll)\n" % (" "*8))
        for k,v in defVal.items():
            fd.write("{space}self.{k} = {v}\n".format(k=k, v=v, space=" "*8))
        maxW=max([len(k) if len(v)==3 else 0 for k,v in fuLi.items()])
        for fu in fuLi.keys():
            if fu[-4:]=='_pIn' or fu[-5:]== '_pOut':
                #print(fu, fuLi[fu])
                continue
            isDone = False
            if len(fuLi[fu])==3:
                #print(fu, fuLi[fu+'_pIn'], fuLi[fu+'_pOut'])
                fuInPara = ", ".join("self."+i for i in fuLi[fu+'_pIn'])
                #fuInPara = (", " if len(fuInPara)>0 else "")+fuInPara
                pGet = ", ".join(i for i in fuLi[fu+'_pOut'])
                pGetC = ", "+pGet if len(pGet)>0 else ""
                muDef = '' if len(fuLi[fu+'_pOut'])==1 else "*"
                fuCaModStr = ""
                if fu in fuCaMod:
                    fuCaModStr = fuCaMod[fu]
                code = fuFullTpl.format(fuName = fu, fuWidth= maxW, fuInPara = fuInPara, space=" "*4, muDef= muDef, pGet = pGet, fuCaModStr=fuCaModStr, pGetC=pGetC)
                fd.write(code)
                testFuCount +=3
                isDone = True
            elif len(fuLi[fu])==2:
                if fu+'Get' in allFunc and fu+'Set' in allFunc:
                    iPara, oPara = fName2ParaInOut(fu+'Get')
                    #print(fu, fuLi[fu+'_pIn'], fuLi[fu+'_pOut'])
                    fuInPara = ", ".join("self."+i for i in iPara)
                    #fuInPara = (", " if len(fuInPara)>0 else "")+fuInPara
                    pGet = ", ".join(i for i in oPara)
                    pGetC = ", "+pGet if len(pGet)>0 else ""
                    muDef = '' if len(oPara)==1 else "*"
                    fuCaModStr = ""
                    if fu in fuCaMod:
                        fuCaModStr = fuCaMod[fu]
                    code = fuTpl.format(fuName = fu, fuWidth= maxW, fuInPara = fuInPara, space=" "*4, muDef= muDef, pGet = pGet, fuCaModStr=fuCaModStr, pGetC=pGetC)
                    fd.write(code)
                    testFuCount +=2
                    isDone = True
            if not isDone:
                print("Function %-30s: no test coverage" % (fu))
                for i in fuLi[fu]:
                    pInLi, pOutLi           = fName2ParaInOut(i)
                    fuNotDone[i]            = allFuncDict[i]
                    fuNotDone[i+'_pIn']     = pInLi
                    fuNotDone[i+'_pOut']    = pOutLi
                del fuLi[fu]
        fd.write("%sdef tearDown(self):\n" % (" "*4))
        fd.write("%sdwf.DeviceClose(self.hdwf)\n\n" % (" "*8))
        fd.write("if __name__ == '__main__':\n")
        fd.write("    unittest.main()\n")       
    return fuNotDone, testFuCount


fuNoTest=['DigitalOutDataSet','DigitalInStatusData','AnalogInChannelRangeSteps']

def generateTestOthers(fName, fuLi):
    if os.path.exists(fName+'f'):
        print("File %s already exists\nI do not over write\n")
        return 
    with open(fName, 'w') as fd:
        date = time.strftime("%d.%m.%Y %H:%M:%S")
        fd.write(header.format(date=date, classname= 'OtherFunctions'))
        fd.write("%sdef setUp(self):\n" % (" "*4))
        fd.write("%sa = dwf.Enum(dwf.enumfilterAll)\n" % (" "*8))
        for k,v in defVal.items():
            fd.write("{space}self.{k} = {v}\n".format(k=k, v=v, space=" "*8))
        
        for fu in fuLi:
            if fu[-4:]=='_pIn' or fu[-5:]== '_pOut':
                #print(fu, fuLi[fu])
                continue
            if fu in fuNoTest:
                continue
            iPara, oPara = fName2ParaInOut(fu)
            #print(fu, iPara, oPara)
            oPara = [p.split('[')[0] for p in oPara]
            if len(oPara)==0:
                oPara = ['dummy',]
            fuInPara = ", ".join("self."+i for i in iPara)
            pGet = ", ".join(i for i in oPara)
            pGetC = ", "+pGet if len(pGet)>0 else ""
            code = fuOtherTpl.format(fuName = fu, fuInPara = fuInPara, space=" "*4, pGet = pGet, pGetC=pGetC)
            fd.write(code)
        fd.write("%sdef tearDown(self):\n" % (" "*4))
        fd.write("%sdwf.DeviceClose(self.hdwf)\n\n" % (" "*8))
        fd.write("if __name__ == '__main__':\n")
        fd.write("    unittest.main()\n")       
            
  

    
    

def main():
    i=0
    fuLi, otherFunc, fuCnt      = getAllGetSetInfoFunc()
    fuNotDone, testFuCnt        = generateTestGetSetInfoFile(os.sep.join(['..','test',"test_generated.py"]), fuLi)
    header= ("Function_name","F","P","O")
    mwidth = max([len(i) for i in header])
    mFuName = max([len(i) for i in allFunc])
    mFuName+=2
    hFmt = "%%-%ds %%2s %%2s %%2s" % (mFuName) 
    lFmt = "%%-%ds %%2s %%2s %%2s" % (mFuName) 
    print(hFmt % header)
    #print(otherFunc.keys())
    fuRe=r'(.+)(Get|Set|Info)'
    for idx, fu in enumerate(allFunc):
        li = [fu, '-', '-','-',]
        reMo=re.match(fuRe, fu)
        if reMo:
            bName = reMo.groups(0)[0]
            if bName in fuLi:
                if fu in fuLi[bName]:
                    li[1]='X'
        if fu in fuNotDone.keys():
            li[2]='X'
        if fu in otherFunc.keys():
            li[3]='X'
        li=tuple(li)
        print(lFmt % li)
    print("Generated tests for %d of %d functions (%.1f %% coverage)" %(testFuCnt, fuCnt, 100.0*testFuCnt/fuCnt))
    print("Functions not with full set/get/info   %d" %(len(fuNotDone)/3))
    print("Functions without ending  Set/Get/Info %d" %(len(otherFunc)/3))
    fuNotDone.update(otherFunc)
    generateTestOthers(os.sep.join(['..','test','test_generateOthers.py']),fuNotDone)


if __name__ == '__main__':
    main()
