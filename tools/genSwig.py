#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Generate swig file for Analog Discovery header.

    

    @author: %(username)s
    
"""
import sys
import os
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

headerDWF='''\
// pydwf.i Python interface to Digilent WaveFroms API_EXPORT
%module (docstring="This module allows the python access to functions defined in dwf.[so,dll]") dwf
%{
#define SWIG_FILE_WITH_INIT
#include <digilent/waveforms/dwf.h>
%}
%rename("%(strip:[FDwf])s", %$isfunction) ""; 
%include "typemaps.i"
%include "cstring.i"
%include "carrays.i"
%include "numpy.i"
%include "exception.i"
%init %{
import_array();
%}


%exception {
    $action
    if (result != 1) 
    {
       char err[512];
       printf("$name returns %d\\n", result);
       FDwfGetLastErrorMsg(err); 
       SWIG_exception(SWIG_RuntimeError, err);
    }
}

/* Return by value */
%typemap(out, noblock=1) BOOL {
    $result = SWIG_Py_Void();
}

#define DWFAPI extern
'''
typeSpec=r'(([A-Za-z_]+[ \t]*[*]?){1,3})[ \t]'
paraName=r'([A-Za-z_][A-Za-z0-9_]*(\[[0-9]+\])*)'
fuReExSiLi =r'^(([A-Za-z_*]+[ \t]+[*]?[ \t]*){1,3})([A-Za-z_][A-Za-z0-9_]*)\(([][\w_,* \t]*)\);'
fuReExMuLi =r'^(([A-Za-z_*]+[ \t]+[*]?[ \t]*){1,3})([A-Za-z_][A-Za-z0-9_]*)\(([\w_,*]*)'
parasplit  =r'(([A-Za-z]+[ \t]*[\*]*){1,3})[ \t]+([A-Za-z]+(\[[0-9]+\])*),[ \t]*'
#parasplit  = r'('+typeSpec+paraName+r'[\t ]*,[\t ]*)*'
outPara    =r'((([A-Za-z]+[ \t]*){1,2}[ \t]*\*[ \t]*)([cpv][A-Za-z]+[^[]*))'
arrPara    =r'([A-Za-z]+[ \t]+sz[A-Za-z]+\[[0-9]+\])+'
npdPara     =r'([A-Za-z]+[ \t]*[\*])[ \t]*(rgd[A-Z][A-Za-z]+)'
npwPara     =r'([A-Za-z]+[ \t]*[\*])[ \t]*(rg[A-Z][A-Za-z]+)'

if 1==0:
    mStr = 'DWFAPI BOOL FDwfDigitalOutDataInfo(HDWF hdwf, int idxChannel, unsigned int *pcountOfBitsMax);'
    mStr = 'DWFAPI BOOL FDwfEnumUserName(int idxDevice, char szUserName[32]);'
    mStr = 'DWFAPI BOOL FDwfDigitalOutDataInfo(HDWF hdwf, int idxChannel, unsigned int *pcountOfBitsMax, int *pBlaBla, DEVID* pDeviceId, DEVVER* pDeviceRevision, HDWF *phdwf, int * pv);'
    mStr = 'DWFAPI BOOL FDwfDigitalInStatusData(HDWF hdwf, void *rgData, int countOfDataBytes);'
    #mStr = 'DWFAPI BOOL  FDwfDigitalOutOutputGet(HDWF hdwf, int idxChannel, DwfDigitalOutOutput* pv);'
    #mStr = 'unsigned int idxDevice, DEVID* pDeviceId, DEVVER* pDeviceRevision'
    mo = re.match(fuReExSiLi, mStr)
    print(mo)
    if mo:
        ret, d, fName, para  = mo.groups()
        print(ret, d, fName, para )
        for p in para.split(','):
            p=p.strip()
            print(p)
            mo=re.match(npwPara, p)
            if mo:
                print("Out",mo.groups())
    sys.exit()


def parseDWF(hFile):
    res=[]
    with open(hFile) as fd:
        for line in fd.readlines():
            line=line.strip(os.linesep)
            mo = re.match(fuReExSiLi, line)
            doc=None
            outP=[]
            arrP=[]
            inP = []
            npdP=[]
            npwP=[]
            #print(line, mo)
            if mo:
                ret, d, fName, para = mo.groups()
                paras = para.split(',')
                #paras = re.split(parasplit, para)
                #print(paras)
                paras = [i.strip() for i in paras if (i and len(i.strip())>0 and i[0]!='[')]
                #print(paras)
                #print(fName, para, paras)
                npFound=False
                for i in paras:
                    isMatch = False
                    mo=re.match(outPara, i)
                    if mo:
                        full, dType, dummy, paraName = mo.groups()
                        outP.append( (dType, paraName))
                        isMatch = True
                        #print("Out %s" % str(outP[-1]))
                    mo=re.match(arrPara, i)
                    #print(fName, i)
                    if mo:
                        #print(i,mo.groups())
                        isMatch = True
                        arrP.append(i)
                    if not isMatch:
                        if not npFound:
                            inP.append(i)
                        npFound=False
                    mo = re.match(npdPara, i)
                    #print(fName, mo)
                    if mo:
                        npdP.append(mo.groups())
                        npFound = True
                        #print(i, mo.groups())
                    mo = re.match(npwPara, i)
                    #print(fName, mo)
                    if mo:
                        npwP.append(mo.groups())
                        npFound = True
                        #print(i, mo.groups())
                inPa=", ".join(inP)
                #print(outP, arrP)
                docOutP=["%s %s" % (i[0], i[1][1:]) for i in outP]
                oPara=", ".join(docOutP+arrP)
                doc='%%feature("autodoc", "%s(%s) -> ( %s )") %s;' %(fName[4:],inPa, oPara, fName)
                res.append(doc)
                if "InStatusData" in fName:
                    print("Function %s\n  In : %s\n  Out: %s" % (fName[4:], inPa, oPara))
                    print(npdP, npwP)
                #doc='%%feature("docstring", "This is some more info.") %s;' % fName
                #res.append(doc)
                #print(inP, outP, arrP)   
                for i in outP:
                    #print(re.split(reEx,i))
                    res.append("%%apply %s OUTPUT {%s %s};"%(i[0],i[0],i[1]))
                    #print(res[-1])
                for i in arrP:
                    reEx=r'([A-Za-z]+[ \t]+){1,2}(sz[A-Za-z]+)\[([0-9]+)\]'
                    #reEx=r'(.*)\[.*\]'
                    dType, name, size=re.match(reEx,i).groups()
                    dType=" ".join(i.split()[0:-1])+'*'
                    res.append("%%cstring_bounded_output(%s %s, %s);"%(dType,name,size))
                for i in npdP:
                    res.append("%%apply (double* INPLACE_ARRAY1, int DIM1) {(%s %s, int cdData)};"%i)
                for i in npwP:
                    res.append("%%apply (unsigned short* INPLACE_ARRAY1, int DIM1) {(%s %s, int countOfDataBytes)};"%i)
                fPara = []
                for p in paras:
                    if p in arrP:
                        np = p.split('[')[0].replace('sz','*sz')
                        p=np
                    fPara.append(p)
                para = ", ".join(fPara)
                #ret = 'void'
                res.append("%s %s(%s);"% (ret,  fName, para))
                #if fName == 'FDwfDeviceOpen':
                #    sys.exit()
            else:
                #print(line)
                reEx = r'typedef[ \t]+BYTE[ \t]+([A-Za-z]+);'
                mo=re.match(reEx, line)
                if mo:
                    line = "typedef unsigned char %s;" %  mo.groups()
                res.append(line)
    return res

def generateDWF():
    parseData = parseDWF(os.sep.join(('','usr','local','include','digilent','waveforms','dwf.h')))
    with open('../dwf.i','w') as fd:
        fd.write(headerDWF)
        for li in parseData:
            fd.write(li+os.linesep)
    

def parseBladeRF(hFile):
    res=[]
    with open(hFile) as fd:
        muLi=''
        for line in fd.readlines():
            line=line.strip(os.linesep)
            if re.match(fuReExMuLi):
                muLi+=line
                continue
            mo = re.match(fuReExSiLi, line)
            doc=None
            outP=[]
            arrP=[]
            inP = []
            npP=[]
            #print(line, mo)
            if mo:
                ret, d, fName,para = mo.groups()
                paras = re.split(parasplit, para)
                #print(paras)
                paras = [i.strip() for i in paras if (i and len(i.strip())>0 and i[0]!='[')]
                print("%-30s %s" % (fName, para))

def genBladeRF():
    headFname = os.sep.join(('','usr','include','libbladeRF.h'))
    parseBladeRF(headFname)
#    text = open(headFname, 'rU').read()
#    parser = CParser(
#            lex_optimize=False,
#            lextab='pycparser.lextab',
#            yacc_optimize=False,
#            yacctab='pycparser.yacctab',
#            yacc_debug=True)
#    res= parser.parse(text, headFname, debuglevel=10)

if __name__ == '__main__':
    #genBladeRF()
    generateDWF()
    print("Done")
    
