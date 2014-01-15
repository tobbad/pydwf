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
       printf("$name returns %d\n", result);
       FDwfGetLastErrorMsg(err); 
       SWIG_exception(SWIG_RuntimeError, err);
    }
}

/* Return by value */
%typemap(out, noblock=1) BOOL {
    $result = SWIG_Py_Void();
}

#define DWFAPI extern
/************************************************************************/
/*                                                                      */
/*    dwf.h  --    Public Interface Declarations for DWF.DLL            */
/*                                                                      */
/************************************************************************/
/*    Author: Laszlo Attila Kovacs                                      */
/*    Copyright 2013 Digilent Inc.                                      */
/************************************************************************/
/*  File Description:                                                   */
/*                                                                      */
/*    This header file contains the public interface declarations for   */
/*    the DWF.DLL.  This interface constists of  hardware device        */
/*    enumeration, connection (open/close), and hardware instrument     */
/*    control.  This spans all 4 main instruments  supported by the     */
/*    WaveForms system:                                                 */
/*      Analog In, Analog Out, Analog I/O, and Digital I/O              */
/*                                                                      */
/*    For details on using this interface, refer to:                    */
/*    The WaveForms SDK User's Manual (available in the WaveForms SDK)  */
/*                                                                      */
/************************************************************************/
/*  Revision History:                                                   */
/*                                                                      */
/*  06/6/2009(KovacsLA) : Created                                       */
/*  08/1/2013(JPederson):  Edited for initial public release (WF 2.5)   */
/*  11/07/2013(KovacsLA) : added FDWFAnalogOutMaster* functions         */
/*   DwfState declarations                                              */
/*  10/14/2013(KovacsLA) : added FDWFAnalogOutNode* functions           */
/*                                                                      */
/************************************************************************/


#pragma once

#ifndef DWFINC 
#define DWFINC TRUE

#ifndef DWFAPI

    #if defined(WIN32)
        #if defined(__cplusplus)
            #define    DWFAPI extern "C" __declspec(dllimport)
        #else
            #define    DWFAPI __declspec(dllimport)
        #endif
    #else        
        #if defined(__cplusplus)
            #define DWFAPI extern "C"
        #else
            #define DWFAPI
        #endif
    #endif
#endif

#ifndef BOOL
typedef int BOOL;
#endif

#ifndef BYTE
typedef	unsigned char	BYTE;
#endif

// hardware device handle
typedef int HDWF;
const HDWF hdwfNone = 0;

// device enumeration filters
typedef int ENUMFILTER;
const ENUMFILTER enumfilterAll      = 0;
const ENUMFILTER enumfilterEExplorer= 1;
const ENUMFILTER enumfilterDiscovery= 2;

// device ID
typedef int DEVID;
const DEVID devidEExplorer  = 1;
const DEVID devidDiscovery  = 2;

// device version
typedef int DEVVER;
const DEVVER devverEExplorerC   = 2;
const DEVVER devverEExplorerE   = 4;
const DEVVER devverEExplorerF   = 5;
const DEVVER devverDiscoveryA   = 1;
const DEVVER devverDiscoveryB   = 2;
const DEVVER devverDiscoveryC   = 3;

// trigger source
typedef unsigned char TRIGSRC;
const TRIGSRC trigsrcNone               = 0;
const TRIGSRC trigsrcPC                 = 1;
const TRIGSRC trigsrcDetectorAnalogIn   = 2;
const TRIGSRC trigsrcDetectorDigitalIn  = 3;
const TRIGSRC trigsrcAnalogIn           = 4;
const TRIGSRC trigsrcDigitalIn          = 5;
const TRIGSRC trigsrcDigitalOut         = 6;
const TRIGSRC trigsrcAnalogOut1         = 7;
const TRIGSRC trigsrcAnalogOut2         = 8;
const TRIGSRC trigsrcAnalogOut3         = 9;
const TRIGSRC trigsrcAnalogOut4         = 10;
const TRIGSRC trigsrcExternal1          = 11;
const TRIGSRC trigsrcExternal2          = 12;
const TRIGSRC trigsrcExternal3          = 13;
const TRIGSRC trigsrcExternal4          = 14;

// instrument states:
typedef unsigned char DwfState;
const DwfState DwfStateReady        = 0;
const DwfState DwfStateConfig       = 4;
const DwfState DwfStatePrefill      = 5;
const DwfState DwfStateArmed        = 1;
const DwfState DwfStateWait         = 7;
const DwfState DwfStateTriggered    = 3;
const DwfState DwfStateRunning      = 3;
const DwfState DwfStateDone         = 2;

// acquisition modes:
typedef int ACQMODE;
const ACQMODE acqmodeSingle     = 0;
const ACQMODE acqmodeScanShift  = 1;
const ACQMODE acqmodeScanScreen = 2;
const ACQMODE acqmodeRecord     = 3;

// analog acquisition filter:
typedef int FILTER;
const FILTER filterDecimate = 0;
const FILTER filterAverage  = 1;
const FILTER filterMinMax   = 2;

// analog in trigger mode:
typedef int TRIGTYPE;
const TRIGTYPE trigtypeEdge         = 0;
const TRIGTYPE trigtypePulse        = 1;
const TRIGTYPE trigtypeTransition   = 2;

// analog in trigger condition
typedef int TRIGCOND;
const TRIGCOND trigcondRisingPositive   = 0;
const TRIGCOND trigcondFallingNegative  = 1;

// analog in trigger length condition
typedef int TRIGLEN;
const TRIGLEN triglenLess       = 0;
const TRIGLEN triglenTimeout    = 1;
const TRIGLEN triglenMore       = 2;

// error codes for DWF Public API:
typedef int DWFERC;                           
const   DWFERC dwfercNoErc                  = 0;        //  No error occurred
const   DWFERC dwfercUnknownError           = 1;        //  API waiting on pending API timed out
const   DWFERC dwfercApiLockTimeout         = 2;        //  API waiting on pending API timed out
const   DWFERC dwfercAlreadyOpened          = 3;        //  Device already opened
const   DWFERC dwfercNotSupported           = 4;        //  Device not supported
const   DWFERC dwfercInvalidParameter0      = 0x10;     //  Invalid parameter sent in API call
const   DWFERC dwfercInvalidParameter1      = 0x11;     //  Invalid parameter sent in API call
const   DWFERC dwfercInvalidParameter2      = 0x12;     //  Invalid parameter sent in API call
const   DWFERC dwfercInvalidParameter3      = 0x13;     //  Invalid parameter sent in API call
const   DWFERC dwfercInvalidParameter4      = 0x14;     //  Invalid parameter sent in API call

// analog out signal types
typedef unsigned char FUNC;
const FUNC funcDC       = 0;
const FUNC funcSine     = 1;
const FUNC funcSquare   = 2;
const FUNC funcTriangle = 3;
const FUNC funcRampUp   = 4;
const FUNC funcRampDown = 5;
const FUNC funcNoise    = 6;
const FUNC funcCustom   = 30;
const FUNC funcPlay     = 31;

// analog io channel node types
typedef unsigned char ANALOGIO;
const ANALOGIO analogioEnable       = 1;
const ANALOGIO analogioVoltage      = 2;
const ANALOGIO analogioCurrent      = 3;
const ANALOGIO analogioPower        = 4;
const ANALOGIO analogioTemperature  = 5;

typedef int AnalogOutNode;
const AnalogOutNode AnalogOutNodeCarrier  = 0;
const AnalogOutNode AnalogOutNodeFM       = 1;
const AnalogOutNode AnalogOutNodeAM       = 2;

typedef int DwfDigitalInClockSource;
const DwfDigitalInClockSource DwfDigitalInClockSourceInternal = 0;
const DwfDigitalInClockSource DwfDigitalInClockSourceExternal = 1;

typedef int DwfDigitalInSampleMode;
const DwfDigitalInSampleMode DwfDigitalInSampleModeSimple   = 0;
// alternate samples: noise|sample|noise|sample|...  
// where noise is more than 1 transition between 2 samples
const DwfDigitalInSampleMode DwfDigitalInSampleModeNoise    = 1; 

typedef int DwfDigitalOutOutput;
const DwfDigitalOutOutput DwfDigitalOutOutputPushPull   = 0;
const DwfDigitalOutOutput DwfDigitalOutOutputOpenDrain  = 1;
const DwfDigitalOutOutput DwfDigitalOutOutputOpenSource = 2;
const DwfDigitalOutOutput DwfDigitalOutOutputThreeState = 3; // for custom and random

typedef int DwfDigitalOutType;
const DwfDigitalOutType DwfDigitalOutTypePulse      = 0;
const DwfDigitalOutType DwfDigitalOutTypeCustom     = 1;
const DwfDigitalOutType DwfDigitalOutTypeRandom     = 2;

typedef int DwfDigitalOutIdle;
const DwfDigitalOutIdle DwfDigitalOutIdleInit     = 0;
const DwfDigitalOutIdle DwfDigitalOutIdleLow      = 1;
const DwfDigitalOutIdle DwfDigitalOutIdleHigh     = 2;
const DwfDigitalOutIdle DwfDigitalOutIdleZet      = 3;

// Macro used to verify if bit is 1 or 0 in given bit field
#define IsBitSet(fs, bit) ((fs & (1<<bit)) != 0)

// Error and version APIs:
%feature("autodoc", "GetLastError() -> ( DWFERC *  dwferc )") FDwfGetLastError;
%apply DWFERC *  OUTPUT {DWFERC *  pdwferc};
DWFAPI BOOL  FDwfGetLastError(DWFERC * pdwferc);
%feature("autodoc", "GetLastErrorMsg() -> ( char szError[512] )") FDwfGetLastErrorMsg;
%cstring_bounded_output(char* szError, 512);
DWFAPI BOOL  FDwfGetLastErrorMsg(char *szError);
%feature("autodoc", "GetVersion() -> ( char szVersion[32] )") FDwfGetVersion;
%cstring_bounded_output(char* szVersion, 32);
DWFAPI BOOL  FDwfGetVersion(char *szVersion);


// DEVICE MANAGMENT FUNCTIONS
// Enumeration:
%feature("autodoc", "Enum(ENUMFILTER enumfilter) -> ( int *  cDevice )") FDwfEnum;
%apply int *  OUTPUT {int *  pcDevice};
DWFAPI BOOL  FDwfEnum(ENUMFILTER enumfilter, int * pcDevice);
%feature("autodoc", "EnumDeviceType(int idxDevice) -> ( DEVID*  DeviceId, DEVVER*  DeviceRevision )") FDwfEnumDeviceType;
%apply DEVID*  OUTPUT {DEVID*  pDeviceId};
%apply DEVVER*  OUTPUT {DEVVER*  pDeviceRevision};
DWFAPI BOOL  FDwfEnumDeviceType(int idxDevice, DEVID* pDeviceId, DEVVER* pDeviceRevision);
%feature("autodoc", "EnumDeviceIsOpened(int idxDevice) -> ( BOOL*  fIsUsed )") FDwfEnumDeviceIsOpened;
%apply BOOL*  OUTPUT {BOOL*  pfIsUsed};
DWFAPI BOOL  FDwfEnumDeviceIsOpened(int idxDevice, BOOL* pfIsUsed);
%feature("autodoc", "EnumUserName(int idxDevice) -> ( char szUserName[32] )") FDwfEnumUserName;
%cstring_bounded_output(char* szUserName, 32);
DWFAPI BOOL  FDwfEnumUserName(int idxDevice, char *szUserName);
%feature("autodoc", "EnumDeviceName(int idxDevice) -> ( char szDeviceName[32] )") FDwfEnumDeviceName;
%cstring_bounded_output(char* szDeviceName, 32);
DWFAPI BOOL  FDwfEnumDeviceName(int idxDevice, char *szDeviceName);
%feature("autodoc", "EnumSN(int idxDevice) -> ( char szSN[32] )") FDwfEnumSN;
%cstring_bounded_output(char* szSN, 32);
DWFAPI BOOL  FDwfEnumSN(int idxDevice, char *szSN);

// Open/Close:
%feature("autodoc", "DeviceOpen(int idxDevice) -> ( HDWF * hdwf )") FDwfDeviceOpen;
%apply HDWF * OUTPUT {HDWF * phdwf};
DWFAPI BOOL  FDwfDeviceOpen(int idxDevice, HDWF *phdwf);
%feature("autodoc", "DeviceClose(HDWF hdwf) -> (  )") FDwfDeviceClose;
DWFAPI BOOL  FDwfDeviceClose(HDWF hdwf);
%feature("autodoc", "DeviceCloseAll() -> (  )") FDwfDeviceCloseAll;
DWFAPI BOOL  FDwfDeviceCloseAll();
%feature("autodoc", "DeviceAutoConfigureSet(HDWF hdwf, BOOL fAutoConfigure) -> (  )") FDwfDeviceAutoConfigureSet;
DWFAPI BOOL  FDwfDeviceAutoConfigureSet(HDWF hdwf, BOOL fAutoConfigure);
%feature("autodoc", "DeviceAutoConfigureGet(HDWF hdwf) -> ( BOOL*  fAutoConfigure )") FDwfDeviceAutoConfigureGet;
%apply BOOL*  OUTPUT {BOOL*  pfAutoConfigure};
DWFAPI BOOL  FDwfDeviceAutoConfigureGet(HDWF hdwf, BOOL* pfAutoConfigure);
%feature("autodoc", "DeviceReset(HDWF hdwf) -> (  )") FDwfDeviceReset;
DWFAPI BOOL  FDwfDeviceReset(HDWF hdwf);
%feature("autodoc", "DeviceTriggerInfo(HDWF hdwf) -> ( int*  fstrigsrc )") FDwfDeviceTriggerInfo;
%apply int*  OUTPUT {int*  pfstrigsrc};
DWFAPI BOOL  FDwfDeviceTriggerInfo(HDWF hdwf, int* pfstrigsrc);
%feature("autodoc", "DeviceTriggerSet(HDWF hdwf, int idxPin, TRIGSRC trigsrc) -> (  )") FDwfDeviceTriggerSet;
DWFAPI BOOL  FDwfDeviceTriggerSet(HDWF hdwf, int idxPin, TRIGSRC trigsrc);
%feature("autodoc", "DeviceTriggerGet(HDWF hdwf, int idxPin) -> ( TRIGSRC*  trigsrc )") FDwfDeviceTriggerGet;
%apply TRIGSRC*  OUTPUT {TRIGSRC*  ptrigsrc};
DWFAPI BOOL  FDwfDeviceTriggerGet(HDWF hdwf, int idxPin, TRIGSRC* ptrigsrc);
%feature("autodoc", "DeviceTriggerPC(HDWF hdwf) -> (  )") FDwfDeviceTriggerPC;
DWFAPI BOOL  FDwfDeviceTriggerPC(HDWF hdwf);


// ANALOG IN INSTRUMENT FUNCTIONS
// Control and status: 
%feature("autodoc", "AnalogInReset(HDWF hdwf) -> (  )") FDwfAnalogInReset;
DWFAPI BOOL  FDwfAnalogInReset(HDWF hdwf);
%feature("autodoc", "AnalogInConfigure(HDWF hdwf, BOOL fReconfigure, BOOL fStart) -> (  )") FDwfAnalogInConfigure;
DWFAPI BOOL  FDwfAnalogInConfigure(HDWF hdwf, BOOL fReconfigure, BOOL fStart);
%feature("autodoc", "AnalogInStatus(HDWF hdwf, BOOL fReadData) -> ( DwfState*  sts )") FDwfAnalogInStatus;
%apply DwfState*  OUTPUT {DwfState*  psts};
DWFAPI BOOL  FDwfAnalogInStatus(HDWF hdwf, BOOL fReadData, DwfState* psts);
%feature("autodoc", "AnalogInStatusSamplesLeft(HDWF hdwf) -> ( int*  cSamplesLeft )") FDwfAnalogInStatusSamplesLeft;
%apply int*  OUTPUT {int*  pcSamplesLeft};
DWFAPI BOOL  FDwfAnalogInStatusSamplesLeft(HDWF hdwf, int* pcSamplesLeft);
%feature("autodoc", "AnalogInStatusSamplesValid(HDWF hdwf) -> ( int*  cSamplesValid )") FDwfAnalogInStatusSamplesValid;
%apply int*  OUTPUT {int*  pcSamplesValid};
DWFAPI BOOL  FDwfAnalogInStatusSamplesValid(HDWF hdwf, int* pcSamplesValid);
%feature("autodoc", "AnalogInStatusIndexWrite(HDWF hdwf) -> ( int*  idxWrite )") FDwfAnalogInStatusIndexWrite;
%apply int*  OUTPUT {int*  pidxWrite};
DWFAPI BOOL  FDwfAnalogInStatusIndexWrite(HDWF hdwf, int* pidxWrite);
%feature("autodoc", "AnalogInStatusAutoTriggered(HDWF hdwf) -> ( BOOL*  fAuto )") FDwfAnalogInStatusAutoTriggered;
%apply BOOL*  OUTPUT {BOOL*  pfAuto};
DWFAPI BOOL  FDwfAnalogInStatusAutoTriggered(HDWF hdwf, BOOL* pfAuto);
%feature("autodoc", "AnalogInStatusData(HDWF hdwf, int idxChannel, double* rgdVoltData) -> (  )") FDwfAnalogInStatusData;
%apply (double* INPLACE_ARRAY1, int DIM1) {(double* rgdVoltData, int cdData)};
DWFAPI BOOL  FDwfAnalogInStatusData(HDWF hdwf, int idxChannel, double* rgdVoltData, int cdData);
%feature("autodoc", "AnalogInStatusSample(HDWF hdwf, int idxChannel) -> ( double*  dVoltSample )") FDwfAnalogInStatusSample;
%apply double*  OUTPUT {double*  pdVoltSample};
DWFAPI BOOL  FDwfAnalogInStatusSample(HDWF hdwf, int idxChannel, double* pdVoltSample);

%feature("autodoc", "AnalogInStatusRecord(HDWF hdwf) -> ( int*  cdDataAvailable, int*  cdDataLost, int*  cdDataCorrupt )") FDwfAnalogInStatusRecord;
%apply int*  OUTPUT {int*  pcdDataAvailable};
%apply int*  OUTPUT {int*  pcdDataLost};
%apply int*  OUTPUT {int*  pcdDataCorrupt};
DWFAPI BOOL  FDwfAnalogInStatusRecord(HDWF hdwf, int* pcdDataAvailable, int* pcdDataLost, int* pcdDataCorrupt);
%feature("autodoc", "AnalogInRecordLengthSet(HDWF hdwf, double sLegth) -> (  )") FDwfAnalogInRecordLengthSet;
DWFAPI BOOL  FDwfAnalogInRecordLengthSet(HDWF hdwf, double sLegth);
%feature("autodoc", "AnalogInRecordLengthGet(HDWF hdwf) -> ( double*  sLegth )") FDwfAnalogInRecordLengthGet;
%apply double*  OUTPUT {double*  psLegth};
DWFAPI BOOL  FDwfAnalogInRecordLengthGet(HDWF hdwf, double* psLegth);

// Acquistion configuration:
%feature("autodoc", "AnalogInFrequencyInfo(HDWF hdwf) -> ( double*  hzMin, double*  hzMax )") FDwfAnalogInFrequencyInfo;
%apply double*  OUTPUT {double*  phzMin};
%apply double*  OUTPUT {double*  phzMax};
DWFAPI BOOL  FDwfAnalogInFrequencyInfo(HDWF hdwf, double* phzMin, double* phzMax);
%feature("autodoc", "AnalogInFrequencySet(HDWF hdwf, double hzFrequency) -> (  )") FDwfAnalogInFrequencySet;
DWFAPI BOOL  FDwfAnalogInFrequencySet(HDWF hdwf, double hzFrequency);
%feature("autodoc", "AnalogInFrequencyGet(HDWF hdwf) -> ( double*  hzFrequency )") FDwfAnalogInFrequencyGet;
%apply double*  OUTPUT {double*  phzFrequency};
DWFAPI BOOL  FDwfAnalogInFrequencyGet(HDWF hdwf, double* phzFrequency);

%feature("autodoc", "AnalogInBitsInfo(HDWF hdwf) -> ( int*  nBits )") FDwfAnalogInBitsInfo;
%apply int*  OUTPUT {int*  pnBits};
DWFAPI BOOL  FDwfAnalogInBitsInfo(HDWF hdwf, int* pnBits);

%feature("autodoc", "AnalogInBufferSizeInfo(HDWF hdwf) -> ( int*  nSizeMin, int*  nSizeMax )") FDwfAnalogInBufferSizeInfo;
%apply int*  OUTPUT {int*  pnSizeMin};
%apply int*  OUTPUT {int*  pnSizeMax};
DWFAPI BOOL  FDwfAnalogInBufferSizeInfo(HDWF hdwf, int* pnSizeMin, int* pnSizeMax);
%feature("autodoc", "AnalogInBufferSizeSet(HDWF hdwf, int nSize) -> (  )") FDwfAnalogInBufferSizeSet;
DWFAPI BOOL  FDwfAnalogInBufferSizeSet(HDWF hdwf, int nSize);
%feature("autodoc", "AnalogInBufferSizeGet(HDWF hdwf) -> ( int*  nSize )") FDwfAnalogInBufferSizeGet;
%apply int*  OUTPUT {int*  pnSize};
DWFAPI BOOL  FDwfAnalogInBufferSizeGet(HDWF hdwf, int* pnSize);

%feature("autodoc", "AnalogInAcquisitionModeInfo(HDWF hdwf) -> ( int*  fsacqmode )") FDwfAnalogInAcquisitionModeInfo;
%apply int*  OUTPUT {int*  pfsacqmode};
DWFAPI BOOL  FDwfAnalogInAcquisitionModeInfo(HDWF hdwf, int* pfsacqmode);
%feature("autodoc", "AnalogInAcquisitionModeSet(HDWF hdwf, ACQMODE acqmode) -> (  )") FDwfAnalogInAcquisitionModeSet;
DWFAPI BOOL  FDwfAnalogInAcquisitionModeSet(HDWF hdwf, ACQMODE acqmode);
%feature("autodoc", "AnalogInAcquisitionModeGet(HDWF hdwf) -> ( ACQMODE*  acqmode )") FDwfAnalogInAcquisitionModeGet;
%apply ACQMODE*  OUTPUT {ACQMODE*  pacqmode};
DWFAPI BOOL  FDwfAnalogInAcquisitionModeGet(HDWF hdwf, ACQMODE* pacqmode);

// Channel configuration:
%feature("autodoc", "AnalogInChannelCount(HDWF hdwf) -> ( int*  cChannel )") FDwfAnalogInChannelCount;
%apply int*  OUTPUT {int*  pcChannel};
DWFAPI BOOL  FDwfAnalogInChannelCount(HDWF hdwf, int* pcChannel);
%feature("autodoc", "AnalogInChannelEnableSet(HDWF hdwf, int idxChannel, BOOL fEnable) -> (  )") FDwfAnalogInChannelEnableSet;
DWFAPI BOOL  FDwfAnalogInChannelEnableSet(HDWF hdwf, int idxChannel, BOOL fEnable);
%feature("autodoc", "AnalogInChannelEnableGet(HDWF hdwf, int idxChannel) -> ( BOOL * fEnable )") FDwfAnalogInChannelEnableGet;
%apply BOOL * OUTPUT {BOOL * pfEnable};
DWFAPI BOOL  FDwfAnalogInChannelEnableGet(HDWF hdwf, int idxChannel, BOOL *pfEnable);
%feature("autodoc", "AnalogInChannelFilterInfo(HDWF hdwf) -> ( int*  fsfilter )") FDwfAnalogInChannelFilterInfo;
%apply int*  OUTPUT {int*  pfsfilter};
DWFAPI BOOL  FDwfAnalogInChannelFilterInfo(HDWF hdwf, int* pfsfilter);
%feature("autodoc", "AnalogInChannelFilterSet(HDWF hdwf, int idxChannel, FILTER filter) -> (  )") FDwfAnalogInChannelFilterSet;
DWFAPI BOOL  FDwfAnalogInChannelFilterSet(HDWF hdwf, int idxChannel, FILTER filter);
%feature("autodoc", "AnalogInChannelFilterGet(HDWF hdwf, int idxChannel) -> ( FILTER*  filter )") FDwfAnalogInChannelFilterGet;
%apply FILTER*  OUTPUT {FILTER*  pfilter};
DWFAPI BOOL  FDwfAnalogInChannelFilterGet(HDWF hdwf, int idxChannel, FILTER* pfilter);
%feature("autodoc", "AnalogInChannelRangeInfo(HDWF hdwf) -> ( double*  voltsMin, double*  voltsMax, double*  nSteps )") FDwfAnalogInChannelRangeInfo;
%apply double*  OUTPUT {double*  pvoltsMin};
%apply double*  OUTPUT {double*  pvoltsMax};
%apply double*  OUTPUT {double*  pnSteps};
DWFAPI BOOL  FDwfAnalogInChannelRangeInfo(HDWF hdwf, double* pvoltsMin, double* pvoltsMax, double* pnSteps);
%feature("autodoc", "AnalogInChannelRangeSteps(HDWF hdwf, double rgVoltsStep[32]) -> ( int*  nSteps )") FDwfAnalogInChannelRangeSteps;
%apply int*  OUTPUT {int*  pnSteps};
DWFAPI BOOL  FDwfAnalogInChannelRangeSteps(HDWF hdwf, double rgVoltsStep[32], int* pnSteps);
%feature("autodoc", "AnalogInChannelRangeSet(HDWF hdwf, int idxChannel, double voltsRange) -> (  )") FDwfAnalogInChannelRangeSet;
DWFAPI BOOL  FDwfAnalogInChannelRangeSet(HDWF hdwf, int idxChannel, double voltsRange);
%feature("autodoc", "AnalogInChannelRangeGet(HDWF hdwf, int idxChannel) -> ( double*  voltsRange )") FDwfAnalogInChannelRangeGet;
%apply double*  OUTPUT {double*  pvoltsRange};
DWFAPI BOOL  FDwfAnalogInChannelRangeGet(HDWF hdwf, int idxChannel, double* pvoltsRange);
%feature("autodoc", "AnalogInChannelOffsetInfo(HDWF hdwf) -> ( double*  voltsMin, double*  voltsMax, double*  nSteps )") FDwfAnalogInChannelOffsetInfo;
%apply double*  OUTPUT {double*  pvoltsMin};
%apply double*  OUTPUT {double*  pvoltsMax};
%apply double*  OUTPUT {double*  pnSteps};
DWFAPI BOOL  FDwfAnalogInChannelOffsetInfo(HDWF hdwf, double* pvoltsMin, double* pvoltsMax, double* pnSteps);
%feature("autodoc", "AnalogInChannelOffsetSet(HDWF hdwf, int idxChannel, double voltOffset) -> (  )") FDwfAnalogInChannelOffsetSet;
DWFAPI BOOL  FDwfAnalogInChannelOffsetSet(HDWF hdwf, int idxChannel, double voltOffset);
%feature("autodoc", "AnalogInChannelOffsetGet(HDWF hdwf, int idxChannel) -> ( double*  voltOffset )") FDwfAnalogInChannelOffsetGet;
%apply double*  OUTPUT {double*  pvoltOffset};
DWFAPI BOOL  FDwfAnalogInChannelOffsetGet(HDWF hdwf, int idxChannel, double* pvoltOffset);

// Trigger configuration:
%feature("autodoc", "AnalogInTriggerSourceInfo(HDWF hdwf) -> ( int*  fstrigsrc )") FDwfAnalogInTriggerSourceInfo;
%apply int*  OUTPUT {int*  pfstrigsrc};
DWFAPI BOOL  FDwfAnalogInTriggerSourceInfo(HDWF hdwf, int* pfstrigsrc);
%feature("autodoc", "AnalogInTriggerSourceSet(HDWF hdwf, TRIGSRC trigsrc) -> (  )") FDwfAnalogInTriggerSourceSet;
DWFAPI BOOL  FDwfAnalogInTriggerSourceSet(HDWF hdwf, TRIGSRC trigsrc);
%feature("autodoc", "AnalogInTriggerSourceGet(HDWF hdwf) -> ( TRIGSRC*  trigsrc )") FDwfAnalogInTriggerSourceGet;
%apply TRIGSRC*  OUTPUT {TRIGSRC*  ptrigsrc};
DWFAPI BOOL  FDwfAnalogInTriggerSourceGet(HDWF hdwf, TRIGSRC* ptrigsrc);

%feature("autodoc", "AnalogInTriggerPositionInfo(HDWF hdwf) -> ( double*  secMin, double*  secMax, double*  nSteps )") FDwfAnalogInTriggerPositionInfo;
%apply double*  OUTPUT {double*  psecMin};
%apply double*  OUTPUT {double*  psecMax};
%apply double*  OUTPUT {double*  pnSteps};
DWFAPI BOOL  FDwfAnalogInTriggerPositionInfo(HDWF hdwf, double* psecMin, double* psecMax, double* pnSteps);
%feature("autodoc", "AnalogInTriggerPositionSet(HDWF hdwf, double secPosition) -> (  )") FDwfAnalogInTriggerPositionSet;
DWFAPI BOOL  FDwfAnalogInTriggerPositionSet(HDWF hdwf, double secPosition);
%feature("autodoc", "AnalogInTriggerPositionGet(HDWF hdwf) -> ( double*  secPosition )") FDwfAnalogInTriggerPositionGet;
%apply double*  OUTPUT {double*  psecPosition};
DWFAPI BOOL  FDwfAnalogInTriggerPositionGet(HDWF hdwf, double* psecPosition);
%feature("autodoc", "AnalogInTriggerPositionStatus(HDWF hdwf) -> ( double*  secPosition )") FDwfAnalogInTriggerPositionStatus;
%apply double*  OUTPUT {double*  psecPosition};
DWFAPI BOOL  FDwfAnalogInTriggerPositionStatus(HDWF hdwf, double* psecPosition);

%feature("autodoc", "AnalogInTriggerAutoTimeoutInfo(HDWF hdwf) -> ( double*  secMin, double*  secMax, double*  nSteps )") FDwfAnalogInTriggerAutoTimeoutInfo;
%apply double*  OUTPUT {double*  psecMin};
%apply double*  OUTPUT {double*  psecMax};
%apply double*  OUTPUT {double*  pnSteps};
DWFAPI BOOL  FDwfAnalogInTriggerAutoTimeoutInfo(HDWF hdwf, double* psecMin, double* psecMax, double* pnSteps);
%feature("autodoc", "AnalogInTriggerAutoTimeoutSet(HDWF hdwf, double secTimeout) -> (  )") FDwfAnalogInTriggerAutoTimeoutSet;
DWFAPI BOOL  FDwfAnalogInTriggerAutoTimeoutSet(HDWF hdwf, double secTimeout);
%feature("autodoc", "AnalogInTriggerAutoTimeoutGet(HDWF hdwf) -> ( double*  secTimeout )") FDwfAnalogInTriggerAutoTimeoutGet;
%apply double*  OUTPUT {double*  psecTimeout};
DWFAPI BOOL  FDwfAnalogInTriggerAutoTimeoutGet(HDWF hdwf, double* psecTimeout);

%feature("autodoc", "AnalogInTriggerHoldOffInfo(HDWF hdwf) -> ( double*  secMin, double*  secMax, double*  nStep )") FDwfAnalogInTriggerHoldOffInfo;
%apply double*  OUTPUT {double*  psecMin};
%apply double*  OUTPUT {double*  psecMax};
%apply double*  OUTPUT {double*  pnStep};
DWFAPI BOOL  FDwfAnalogInTriggerHoldOffInfo(HDWF hdwf, double* psecMin, double* psecMax, double* pnStep);
%feature("autodoc", "AnalogInTriggerHoldOffSet(HDWF hdwf, double secHoldOff) -> (  )") FDwfAnalogInTriggerHoldOffSet;
DWFAPI BOOL  FDwfAnalogInTriggerHoldOffSet(HDWF hdwf, double secHoldOff);
%feature("autodoc", "AnalogInTriggerHoldOffGet(HDWF hdwf) -> ( double*  secHoldOff )") FDwfAnalogInTriggerHoldOffGet;
%apply double*  OUTPUT {double*  psecHoldOff};
DWFAPI BOOL  FDwfAnalogInTriggerHoldOffGet(HDWF hdwf, double* psecHoldOff);

%feature("autodoc", "AnalogInTriggerTypeInfo(HDWF hdwf) -> ( int*  fstrigtype )") FDwfAnalogInTriggerTypeInfo;
%apply int*  OUTPUT {int*  pfstrigtype};
DWFAPI BOOL  FDwfAnalogInTriggerTypeInfo(HDWF hdwf, int* pfstrigtype);
%feature("autodoc", "AnalogInTriggerTypeSet(HDWF hdwf, TRIGTYPE trigtype) -> (  )") FDwfAnalogInTriggerTypeSet;
DWFAPI BOOL  FDwfAnalogInTriggerTypeSet(HDWF hdwf, TRIGTYPE trigtype);
%feature("autodoc", "AnalogInTriggerTypeGet(HDWF hdwf) -> ( TRIGTYPE*  trigtype )") FDwfAnalogInTriggerTypeGet;
%apply TRIGTYPE*  OUTPUT {TRIGTYPE*  ptrigtype};
DWFAPI BOOL  FDwfAnalogInTriggerTypeGet(HDWF hdwf, TRIGTYPE* ptrigtype);

%feature("autodoc", "AnalogInTriggerChannelInfo(HDWF hdwf) -> ( int*  idxMin, int*  idxMax )") FDwfAnalogInTriggerChannelInfo;
%apply int*  OUTPUT {int*  pidxMin};
%apply int*  OUTPUT {int*  pidxMax};
DWFAPI BOOL  FDwfAnalogInTriggerChannelInfo(HDWF hdwf, int* pidxMin, int* pidxMax);
%feature("autodoc", "AnalogInTriggerChannelSet(HDWF hdwf, int idxChannel) -> (  )") FDwfAnalogInTriggerChannelSet;
DWFAPI BOOL  FDwfAnalogInTriggerChannelSet(HDWF hdwf, int idxChannel);
%feature("autodoc", "AnalogInTriggerChannelGet(HDWF hdwf) -> ( int*  idxChannel )") FDwfAnalogInTriggerChannelGet;
%apply int*  OUTPUT {int*  pidxChannel};
DWFAPI BOOL  FDwfAnalogInTriggerChannelGet(HDWF hdwf, int* pidxChannel);

%feature("autodoc", "AnalogInTriggerFilterInfo(HDWF hdwf) -> ( int*  fsfilter )") FDwfAnalogInTriggerFilterInfo;
%apply int*  OUTPUT {int*  pfsfilter};
DWFAPI BOOL  FDwfAnalogInTriggerFilterInfo(HDWF hdwf, int* pfsfilter);
%feature("autodoc", "AnalogInTriggerFilterSet(HDWF hdwf, FILTER filter) -> (  )") FDwfAnalogInTriggerFilterSet;
DWFAPI BOOL  FDwfAnalogInTriggerFilterSet(HDWF hdwf, FILTER filter);
%feature("autodoc", "AnalogInTriggerFilterGet(HDWF hdwf) -> ( FILTER*  filter )") FDwfAnalogInTriggerFilterGet;
%apply FILTER*  OUTPUT {FILTER*  pfilter};
DWFAPI BOOL  FDwfAnalogInTriggerFilterGet(HDWF hdwf, FILTER* pfilter);

%feature("autodoc", "AnalogInTriggerLevelInfo(HDWF hdwf) -> ( double*  voltsMin, double*  voltsMax, double*  nSteps )") FDwfAnalogInTriggerLevelInfo;
%apply double*  OUTPUT {double*  pvoltsMin};
%apply double*  OUTPUT {double*  pvoltsMax};
%apply double*  OUTPUT {double*  pnSteps};
DWFAPI BOOL  FDwfAnalogInTriggerLevelInfo(HDWF hdwf, double* pvoltsMin, double* pvoltsMax, double* pnSteps);
%feature("autodoc", "AnalogInTriggerLevelSet(HDWF hdwf, double voltsLevel) -> (  )") FDwfAnalogInTriggerLevelSet;
DWFAPI BOOL  FDwfAnalogInTriggerLevelSet(HDWF hdwf, double voltsLevel);
%feature("autodoc", "AnalogInTriggerLevelGet(HDWF hdwf) -> ( double*  voltsLevel )") FDwfAnalogInTriggerLevelGet;
%apply double*  OUTPUT {double*  pvoltsLevel};
DWFAPI BOOL  FDwfAnalogInTriggerLevelGet(HDWF hdwf, double* pvoltsLevel);

%feature("autodoc", "AnalogInTriggerHysteresisInfo(HDWF hdwf) -> ( double*  voltsMin, double*  voltsMax, double*  nSteps )") FDwfAnalogInTriggerHysteresisInfo;
%apply double*  OUTPUT {double*  pvoltsMin};
%apply double*  OUTPUT {double*  pvoltsMax};
%apply double*  OUTPUT {double*  pnSteps};
DWFAPI BOOL  FDwfAnalogInTriggerHysteresisInfo(HDWF hdwf, double* pvoltsMin, double* pvoltsMax, double* pnSteps);
%feature("autodoc", "AnalogInTriggerHysteresisSet(HDWF hdwf, double voltsLevel) -> (  )") FDwfAnalogInTriggerHysteresisSet;
DWFAPI BOOL  FDwfAnalogInTriggerHysteresisSet(HDWF hdwf, double voltsLevel);
%feature("autodoc", "AnalogInTriggerHysteresisGet(HDWF hdwf) -> ( double*  voltsHysteresis )") FDwfAnalogInTriggerHysteresisGet;
%apply double*  OUTPUT {double*  pvoltsHysteresis};
DWFAPI BOOL  FDwfAnalogInTriggerHysteresisGet(HDWF hdwf, double* pvoltsHysteresis);

%feature("autodoc", "AnalogInTriggerConditionInfo(HDWF hdwf) -> ( int*  fstrigcond )") FDwfAnalogInTriggerConditionInfo;
%apply int*  OUTPUT {int*  pfstrigcond};
DWFAPI BOOL  FDwfAnalogInTriggerConditionInfo(HDWF hdwf, int* pfstrigcond);
%feature("autodoc", "AnalogInTriggerConditionSet(HDWF hdwf, TRIGCOND trigcond) -> (  )") FDwfAnalogInTriggerConditionSet;
DWFAPI BOOL  FDwfAnalogInTriggerConditionSet(HDWF hdwf, TRIGCOND trigcond);
%feature("autodoc", "AnalogInTriggerConditionGet(HDWF hdwf) -> ( TRIGCOND*  trigcond )") FDwfAnalogInTriggerConditionGet;
%apply TRIGCOND*  OUTPUT {TRIGCOND*  ptrigcond};
DWFAPI BOOL  FDwfAnalogInTriggerConditionGet(HDWF hdwf, TRIGCOND* ptrigcond);

%feature("autodoc", "AnalogInTriggerLengthInfo(HDWF hdwf) -> ( double*  secMin, double*  secMax, double*  nSteps )") FDwfAnalogInTriggerLengthInfo;
%apply double*  OUTPUT {double*  psecMin};
%apply double*  OUTPUT {double*  psecMax};
%apply double*  OUTPUT {double*  pnSteps};
DWFAPI BOOL  FDwfAnalogInTriggerLengthInfo(HDWF hdwf, double* psecMin, double* psecMax, double* pnSteps);
%feature("autodoc", "AnalogInTriggerLengthSet(HDWF hdwf, double secLength) -> (  )") FDwfAnalogInTriggerLengthSet;
DWFAPI BOOL  FDwfAnalogInTriggerLengthSet(HDWF hdwf, double secLength);
%feature("autodoc", "AnalogInTriggerLengthGet(HDWF hdwf) -> ( double*  secLength )") FDwfAnalogInTriggerLengthGet;
%apply double*  OUTPUT {double*  psecLength};
DWFAPI BOOL  FDwfAnalogInTriggerLengthGet(HDWF hdwf, double* psecLength);

%feature("autodoc", "AnalogInTriggerLengthConditionInfo(HDWF hdwf) -> ( int*  fstriglen )") FDwfAnalogInTriggerLengthConditionInfo;
%apply int*  OUTPUT {int*  pfstriglen};
DWFAPI BOOL  FDwfAnalogInTriggerLengthConditionInfo(HDWF hdwf, int* pfstriglen);
%feature("autodoc", "AnalogInTriggerLengthConditionSet(HDWF hdwf, TRIGLEN triglen) -> (  )") FDwfAnalogInTriggerLengthConditionSet;
DWFAPI BOOL  FDwfAnalogInTriggerLengthConditionSet(HDWF hdwf, TRIGLEN triglen);
%feature("autodoc", "AnalogInTriggerLengthConditionGet(HDWF hdwf) -> ( TRIGLEN*  triglen )") FDwfAnalogInTriggerLengthConditionGet;
%apply TRIGLEN*  OUTPUT {TRIGLEN*  ptriglen};
DWFAPI BOOL  FDwfAnalogInTriggerLengthConditionGet(HDWF hdwf, TRIGLEN* ptriglen);


// ANALOG OUT INSTRUMENT FUNCTIONS
// Configuration:
%feature("autodoc", "AnalogOutCount(HDWF hdwf) -> ( int*  cChannel )") FDwfAnalogOutCount;
%apply int*  OUTPUT {int*  pcChannel};
DWFAPI BOOL  FDwfAnalogOutCount(HDWF hdwf, int* pcChannel);

%feature("autodoc", "AnalogOutMasterSet(HDWF hdwf, int idxChannel, int idxMaster) -> (  )") FDwfAnalogOutMasterSet;
DWFAPI BOOL  FDwfAnalogOutMasterSet(HDWF hdwf, int idxChannel, int idxMaster);
%feature("autodoc", "AnalogOutMasterGet(HDWF hdwf, int idxChannel) -> ( int * idxMaster )") FDwfAnalogOutMasterGet;
%apply int * OUTPUT {int * pidxMaster};
DWFAPI BOOL  FDwfAnalogOutMasterGet(HDWF hdwf, int idxChannel, int *pidxMaster);

%feature("autodoc", "AnalogOutTriggerSourceInfo(HDWF hdwf, int idxChannel) -> ( int*  fstrigsrc )") FDwfAnalogOutTriggerSourceInfo;
%apply int*  OUTPUT {int*  pfstrigsrc};
DWFAPI BOOL  FDwfAnalogOutTriggerSourceInfo(HDWF hdwf, int idxChannel, int* pfstrigsrc);
%feature("autodoc", "AnalogOutTriggerSourceSet(HDWF hdwf, int idxChannel, TRIGSRC trigsrc) -> (  )") FDwfAnalogOutTriggerSourceSet;
DWFAPI BOOL  FDwfAnalogOutTriggerSourceSet(HDWF hdwf, int idxChannel, TRIGSRC trigsrc);
%feature("autodoc", "AnalogOutTriggerSourceGet(HDWF hdwf, int idxChannel) -> ( TRIGSRC*  trigsrc )") FDwfAnalogOutTriggerSourceGet;
%apply TRIGSRC*  OUTPUT {TRIGSRC*  ptrigsrc};
DWFAPI BOOL  FDwfAnalogOutTriggerSourceGet(HDWF hdwf, int idxChannel, TRIGSRC* ptrigsrc);

%feature("autodoc", "AnalogOutRunInfo(HDWF hdwf, int idxChannel) -> ( double*  secMin, double*  secMax )") FDwfAnalogOutRunInfo;
%apply double*  OUTPUT {double*  psecMin};
%apply double*  OUTPUT {double*  psecMax};
DWFAPI BOOL  FDwfAnalogOutRunInfo(HDWF hdwf, int idxChannel, double* psecMin, double* psecMax);
%feature("autodoc", "AnalogOutRunSet(HDWF hdwf, int idxChannel, double secRun) -> (  )") FDwfAnalogOutRunSet;
DWFAPI BOOL  FDwfAnalogOutRunSet(HDWF hdwf, int idxChannel, double secRun);
%feature("autodoc", "AnalogOutRunGet(HDWF hdwf, int idxChannel) -> ( double*  secRun )") FDwfAnalogOutRunGet;
%apply double*  OUTPUT {double*  psecRun};
DWFAPI BOOL  FDwfAnalogOutRunGet(HDWF hdwf, int idxChannel, double* psecRun);
%feature("autodoc", "AnalogOutRunStatus(HDWF hdwf, int idxChannel) -> ( double*  secRun )") FDwfAnalogOutRunStatus;
%apply double*  OUTPUT {double*  psecRun};
DWFAPI BOOL  FDwfAnalogOutRunStatus(HDWF hdwf, int idxChannel, double* psecRun);

%feature("autodoc", "AnalogOutWaitInfo(HDWF hdwf, int idxChannel) -> ( double*  secMin, double*  secMax )") FDwfAnalogOutWaitInfo;
%apply double*  OUTPUT {double*  psecMin};
%apply double*  OUTPUT {double*  psecMax};
DWFAPI BOOL  FDwfAnalogOutWaitInfo(HDWF hdwf, int idxChannel, double* psecMin, double* psecMax);
%feature("autodoc", "AnalogOutWaitSet(HDWF hdwf, int idxChannel, double secWait) -> (  )") FDwfAnalogOutWaitSet;
DWFAPI BOOL  FDwfAnalogOutWaitSet(HDWF hdwf, int idxChannel, double secWait);
%feature("autodoc", "AnalogOutWaitGet(HDWF hdwf, int idxChannel) -> ( double*  secWait )") FDwfAnalogOutWaitGet;
%apply double*  OUTPUT {double*  psecWait};
DWFAPI BOOL  FDwfAnalogOutWaitGet(HDWF hdwf, int idxChannel, double* psecWait);

%feature("autodoc", "AnalogOutRepeatInfo(HDWF hdwf, int idxChannel) -> ( int*  nMin, int*  nMax )") FDwfAnalogOutRepeatInfo;
%apply int*  OUTPUT {int*  pnMin};
%apply int*  OUTPUT {int*  pnMax};
DWFAPI BOOL  FDwfAnalogOutRepeatInfo(HDWF hdwf, int idxChannel, int* pnMin, int* pnMax);
%feature("autodoc", "AnalogOutRepeatSet(HDWF hdwf, int idxChannel, int cRepeat) -> (  )") FDwfAnalogOutRepeatSet;
DWFAPI BOOL  FDwfAnalogOutRepeatSet(HDWF hdwf, int idxChannel, int cRepeat);
%feature("autodoc", "AnalogOutRepeatGet(HDWF hdwf, int idxChannel) -> ( int*  cRepeat )") FDwfAnalogOutRepeatGet;
%apply int*  OUTPUT {int*  pcRepeat};
DWFAPI BOOL  FDwfAnalogOutRepeatGet(HDWF hdwf, int idxChannel, int* pcRepeat);
%feature("autodoc", "AnalogOutRepeatStatus(HDWF hdwf, int idxChannel) -> ( int*  cRepeat )") FDwfAnalogOutRepeatStatus;
%apply int*  OUTPUT {int*  pcRepeat};
DWFAPI BOOL  FDwfAnalogOutRepeatStatus(HDWF hdwf, int idxChannel, int* pcRepeat);

%feature("autodoc", "AnalogOutRepeatTriggerSet(HDWF hdwf, int idxChannel, BOOL fRepeatTrigger) -> (  )") FDwfAnalogOutRepeatTriggerSet;
DWFAPI BOOL  FDwfAnalogOutRepeatTriggerSet(HDWF hdwf, int idxChannel, BOOL fRepeatTrigger);
%feature("autodoc", "AnalogOutRepeatTriggerGet(HDWF hdwf, int idxChannel) -> ( BOOL*  fRepeatTrigger )") FDwfAnalogOutRepeatTriggerGet;
%apply BOOL*  OUTPUT {BOOL*  pfRepeatTrigger};
DWFAPI BOOL  FDwfAnalogOutRepeatTriggerGet(HDWF hdwf, int idxChannel, BOOL* pfRepeatTrigger);

%feature("autodoc", "AnalogOutNodeInfo(HDWF hdwf, int idxChannel) -> ( int*  fsnode )") FDwfAnalogOutNodeInfo;
%apply int*  OUTPUT {int*  pfsnode};
DWFAPI BOOL  FDwfAnalogOutNodeInfo(HDWF hdwf, int idxChannel, int* pfsnode);

%feature("autodoc", "AnalogOutNodeEnableSet(HDWF hdwf, int idxChannel, AnalogOutNode node, BOOL fEnable) -> (  )") FDwfAnalogOutNodeEnableSet;
DWFAPI BOOL  FDwfAnalogOutNodeEnableSet(HDWF hdwf, int idxChannel, AnalogOutNode node, BOOL fEnable);
%feature("autodoc", "AnalogOutNodeEnableGet(HDWF hdwf, int idxChannel, AnalogOutNode node) -> ( BOOL*  fEnable )") FDwfAnalogOutNodeEnableGet;
%apply BOOL*  OUTPUT {BOOL*  pfEnable};
DWFAPI BOOL  FDwfAnalogOutNodeEnableGet(HDWF hdwf, int idxChannel, AnalogOutNode node, BOOL* pfEnable);

%feature("autodoc", "AnalogOutNodeFunctionInfo(HDWF hdwf, int idxChannel, AnalogOutNode node) -> ( int*  fsfunc )") FDwfAnalogOutNodeFunctionInfo;
%apply int*  OUTPUT {int*  pfsfunc};
DWFAPI BOOL  FDwfAnalogOutNodeFunctionInfo(HDWF hdwf, int idxChannel, AnalogOutNode node, int* pfsfunc);
%feature("autodoc", "AnalogOutNodeFunctionSet(HDWF hdwf, int idxChannel, AnalogOutNode node, FUNC func) -> (  )") FDwfAnalogOutNodeFunctionSet;
DWFAPI BOOL  FDwfAnalogOutNodeFunctionSet(HDWF hdwf, int idxChannel, AnalogOutNode node, FUNC func);
%feature("autodoc", "AnalogOutNodeFunctionGet(HDWF hdwf, int idxChannel, AnalogOutNode node) -> ( FUNC*  func )") FDwfAnalogOutNodeFunctionGet;
%apply FUNC*  OUTPUT {FUNC*  pfunc};
DWFAPI BOOL  FDwfAnalogOutNodeFunctionGet(HDWF hdwf, int idxChannel, AnalogOutNode node, FUNC* pfunc);

%feature("autodoc", "AnalogOutNodeFrequencyInfo(HDWF hdwf, int idxChannel, AnalogOutNode node) -> ( double*  hzMin, double*  hzMax )") FDwfAnalogOutNodeFrequencyInfo;
%apply double*  OUTPUT {double*  phzMin};
%apply double*  OUTPUT {double*  phzMax};
DWFAPI BOOL  FDwfAnalogOutNodeFrequencyInfo(HDWF hdwf, int idxChannel, AnalogOutNode node, double* phzMin, double* phzMax);
%feature("autodoc", "AnalogOutNodeFrequencySet(HDWF hdwf, int idxChannel, AnalogOutNode node, double hzFrequency) -> (  )") FDwfAnalogOutNodeFrequencySet;
DWFAPI BOOL  FDwfAnalogOutNodeFrequencySet(HDWF hdwf, int idxChannel, AnalogOutNode node, double hzFrequency);
%feature("autodoc", "AnalogOutNodeFrequencyGet(HDWF hdwf, int idxChannel, AnalogOutNode node) -> ( double*  hzFrequency )") FDwfAnalogOutNodeFrequencyGet;
%apply double*  OUTPUT {double*  phzFrequency};
DWFAPI BOOL  FDwfAnalogOutNodeFrequencyGet(HDWF hdwf, int idxChannel, AnalogOutNode node, double* phzFrequency);
// Carrier Amplitude or Modulation Index 
%feature("autodoc", "AnalogOutNodeAmplitudeInfo(HDWF hdwf, int idxChannel, AnalogOutNode node) -> ( double*  Min, double*  Max )") FDwfAnalogOutNodeAmplitudeInfo;
%apply double*  OUTPUT {double*  pMin};
%apply double*  OUTPUT {double*  pMax};
DWFAPI BOOL  FDwfAnalogOutNodeAmplitudeInfo(HDWF hdwf, int idxChannel, AnalogOutNode node, double* pMin, double* pMax);
%feature("autodoc", "AnalogOutNodeAmplitudeSet(HDWF hdwf, int idxChannel, AnalogOutNode node, double vAmplitude) -> (  )") FDwfAnalogOutNodeAmplitudeSet;
DWFAPI BOOL  FDwfAnalogOutNodeAmplitudeSet(HDWF hdwf, int idxChannel, AnalogOutNode node, double vAmplitude);
%feature("autodoc", "AnalogOutNodeAmplitudeGet(HDWF hdwf, int idxChannel, AnalogOutNode node) -> ( double*  vAmplitude )") FDwfAnalogOutNodeAmplitudeGet;
%apply double*  OUTPUT {double*  pvAmplitude};
DWFAPI BOOL  FDwfAnalogOutNodeAmplitudeGet(HDWF hdwf, int idxChannel, AnalogOutNode node, double* pvAmplitude);

%feature("autodoc", "AnalogOutNodeOffsetInfo(HDWF hdwf, int idxChannel, AnalogOutNode node) -> ( double*  Min, double*  Max )") FDwfAnalogOutNodeOffsetInfo;
%apply double*  OUTPUT {double*  pMin};
%apply double*  OUTPUT {double*  pMax};
DWFAPI BOOL  FDwfAnalogOutNodeOffsetInfo(HDWF hdwf, int idxChannel, AnalogOutNode node, double* pMin, double* pMax);
%feature("autodoc", "AnalogOutNodeOffsetSet(HDWF hdwf, int idxChannel, AnalogOutNode node, double vOffset) -> (  )") FDwfAnalogOutNodeOffsetSet;
DWFAPI BOOL  FDwfAnalogOutNodeOffsetSet(HDWF hdwf, int idxChannel, AnalogOutNode node, double vOffset);
%feature("autodoc", "AnalogOutNodeOffsetGet(HDWF hdwf, int idxChannel, AnalogOutNode node) -> ( double*  vOffset )") FDwfAnalogOutNodeOffsetGet;
%apply double*  OUTPUT {double*  pvOffset};
DWFAPI BOOL  FDwfAnalogOutNodeOffsetGet(HDWF hdwf, int idxChannel, AnalogOutNode node, double* pvOffset);

%feature("autodoc", "AnalogOutNodeSymmetryInfo(HDWF hdwf, int idxChannel, AnalogOutNode node) -> ( double*  percentageMin, double*  percentageMax )") FDwfAnalogOutNodeSymmetryInfo;
%apply double*  OUTPUT {double*  ppercentageMin};
%apply double*  OUTPUT {double*  ppercentageMax};
DWFAPI BOOL  FDwfAnalogOutNodeSymmetryInfo(HDWF hdwf, int idxChannel, AnalogOutNode node, double* ppercentageMin, double* ppercentageMax);
%feature("autodoc", "AnalogOutNodeSymmetrySet(HDWF hdwf, int idxChannel, AnalogOutNode node, double percentageSymmetry) -> (  )") FDwfAnalogOutNodeSymmetrySet;
DWFAPI BOOL  FDwfAnalogOutNodeSymmetrySet(HDWF hdwf, int idxChannel, AnalogOutNode node, double percentageSymmetry);
%feature("autodoc", "AnalogOutNodeSymmetryGet(HDWF hdwf, int idxChannel, AnalogOutNode node) -> ( double*  percentageSymmetry )") FDwfAnalogOutNodeSymmetryGet;
%apply double*  OUTPUT {double*  ppercentageSymmetry};
DWFAPI BOOL  FDwfAnalogOutNodeSymmetryGet(HDWF hdwf, int idxChannel, AnalogOutNode node, double* ppercentageSymmetry);

%feature("autodoc", "AnalogOutNodePhaseInfo(HDWF hdwf, int idxChannel, AnalogOutNode node) -> ( double*  degreeMin, double*  degreeMax )") FDwfAnalogOutNodePhaseInfo;
%apply double*  OUTPUT {double*  pdegreeMin};
%apply double*  OUTPUT {double*  pdegreeMax};
DWFAPI BOOL  FDwfAnalogOutNodePhaseInfo(HDWF hdwf, int idxChannel, AnalogOutNode node, double* pdegreeMin, double* pdegreeMax);
%feature("autodoc", "AnalogOutNodePhaseSet(HDWF hdwf, int idxChannel, AnalogOutNode node, double degreePhase) -> (  )") FDwfAnalogOutNodePhaseSet;
DWFAPI BOOL  FDwfAnalogOutNodePhaseSet(HDWF hdwf, int idxChannel, AnalogOutNode node, double degreePhase);
%feature("autodoc", "AnalogOutNodePhaseGet(HDWF hdwf, int idxChannel, AnalogOutNode node) -> ( double*  degreePhase )") FDwfAnalogOutNodePhaseGet;
%apply double*  OUTPUT {double*  pdegreePhase};
DWFAPI BOOL  FDwfAnalogOutNodePhaseGet(HDWF hdwf, int idxChannel, AnalogOutNode node, double* pdegreePhase);

%feature("autodoc", "AnalogOutNodeDataInfo(HDWF hdwf, int idxChannel, AnalogOutNode node) -> ( int*  nSamplesMin, int*  nSamplesMax )") FDwfAnalogOutNodeDataInfo;
%apply int*  OUTPUT {int*  pnSamplesMin};
%apply int*  OUTPUT {int*  pnSamplesMax};
DWFAPI BOOL  FDwfAnalogOutNodeDataInfo(HDWF hdwf, int idxChannel, AnalogOutNode node, int* pnSamplesMin, int* pnSamplesMax);
%feature("autodoc", "AnalogOutNodeDataSet(HDWF hdwf, int idxChannel, AnalogOutNode node, double* rgdData) -> (  )") FDwfAnalogOutNodeDataSet;
%apply (double* INPLACE_ARRAY1, int DIM1) {(double* rgdData, int cdData)};
DWFAPI BOOL  FDwfAnalogOutNodeDataSet(HDWF hdwf, int idxChannel, AnalogOutNode node, double* rgdData, int cdData);

// needed for EExplorer, don't care for ADiscovery
%feature("autodoc", "AnalogOutCustomAMFMEnableSet(HDWF hdwf, int idxChannel, BOOL fEnable) -> (  )") FDwfAnalogOutCustomAMFMEnableSet;
DWFAPI BOOL  FDwfAnalogOutCustomAMFMEnableSet(HDWF hdwf, int idxChannel, BOOL fEnable);
%feature("autodoc", "AnalogOutCustomAMFMEnableGet(HDWF hdwf, int idxChannel) -> ( BOOL*  fEnable )") FDwfAnalogOutCustomAMFMEnableGet;
%apply BOOL*  OUTPUT {BOOL*  pfEnable};
DWFAPI BOOL  FDwfAnalogOutCustomAMFMEnableGet(HDWF hdwf, int idxChannel, BOOL* pfEnable);

// Control:
%feature("autodoc", "AnalogOutReset(HDWF hdwf, int idxChannel) -> (  )") FDwfAnalogOutReset;
DWFAPI BOOL  FDwfAnalogOutReset(HDWF hdwf, int idxChannel);
%feature("autodoc", "AnalogOutConfigure(HDWF hdwf, int idxChannel, BOOL fStart) -> (  )") FDwfAnalogOutConfigure;
DWFAPI BOOL  FDwfAnalogOutConfigure(HDWF hdwf, int idxChannel, BOOL fStart);
%feature("autodoc", "AnalogOutStatus(HDWF hdwf, int idxChannel) -> ( DwfState*  sts )") FDwfAnalogOutStatus;
%apply DwfState*  OUTPUT {DwfState*  psts};
DWFAPI BOOL  FDwfAnalogOutStatus(HDWF hdwf, int idxChannel, DwfState* psts);
%feature("autodoc", "AnalogOutNodePlayStatus(HDWF hdwf, int idxChannel, AnalogOutNode node) -> ( int*  dDataFree, int * dDataLost, int * dDataCorrupted )") FDwfAnalogOutNodePlayStatus;
%apply int*  OUTPUT {int*  cdDataFree};
%apply int * OUTPUT {int * cdDataLost};
%apply int * OUTPUT {int * cdDataCorrupted};
DWFAPI BOOL  FDwfAnalogOutNodePlayStatus(HDWF hdwf, int idxChannel, AnalogOutNode node, int* cdDataFree, int *cdDataLost, int *cdDataCorrupted);
%feature("autodoc", "AnalogOutNodePlayData(HDWF hdwf, int idxChannel, AnalogOutNode node, double* rgdData) -> (  )") FDwfAnalogOutNodePlayData;
%apply (double* INPLACE_ARRAY1, int DIM1) {(double* rgdData, int cdData)};
DWFAPI BOOL  FDwfAnalogOutNodePlayData(HDWF hdwf, int idxChannel, AnalogOutNode node, double* rgdData, int cdData);


// ANALOG IO INSTRUMENT FUNCTIONS
// Control:
%feature("autodoc", "AnalogIOReset(HDWF hdwf) -> (  )") FDwfAnalogIOReset;
DWFAPI BOOL  FDwfAnalogIOReset(HDWF hdwf);
%feature("autodoc", "AnalogIOConfigure(HDWF hdwf) -> (  )") FDwfAnalogIOConfigure;
DWFAPI BOOL  FDwfAnalogIOConfigure(HDWF hdwf);
%feature("autodoc", "AnalogIOStatus(HDWF hdwf) -> (  )") FDwfAnalogIOStatus;
DWFAPI BOOL  FDwfAnalogIOStatus(HDWF hdwf);

// Configure:
%feature("autodoc", "AnalogIOEnableInfo(HDWF hdwf) -> ( BOOL*  fSet, BOOL*  fStatus )") FDwfAnalogIOEnableInfo;
%apply BOOL*  OUTPUT {BOOL*  pfSet};
%apply BOOL*  OUTPUT {BOOL*  pfStatus};
DWFAPI BOOL  FDwfAnalogIOEnableInfo(HDWF hdwf, BOOL* pfSet, BOOL* pfStatus);
%feature("autodoc", "AnalogIOEnableSet(HDWF hdwf, BOOL fMasterEnable) -> (  )") FDwfAnalogIOEnableSet;
DWFAPI BOOL  FDwfAnalogIOEnableSet(HDWF hdwf, BOOL fMasterEnable);
%feature("autodoc", "AnalogIOEnableGet(HDWF hdwf) -> ( BOOL*  fMasterEnable )") FDwfAnalogIOEnableGet;
%apply BOOL*  OUTPUT {BOOL*  pfMasterEnable};
DWFAPI BOOL  FDwfAnalogIOEnableGet(HDWF hdwf, BOOL* pfMasterEnable);
%feature("autodoc", "AnalogIOEnableStatus(HDWF hdwf) -> ( BOOL*  fMasterEnable )") FDwfAnalogIOEnableStatus;
%apply BOOL*  OUTPUT {BOOL*  pfMasterEnable};
DWFAPI BOOL  FDwfAnalogIOEnableStatus(HDWF hdwf, BOOL* pfMasterEnable);
%feature("autodoc", "AnalogIOChannelCount(HDWF hdwf) -> ( int*  nChannel )") FDwfAnalogIOChannelCount;
%apply int*  OUTPUT {int*  pnChannel};
DWFAPI BOOL  FDwfAnalogIOChannelCount(HDWF hdwf, int* pnChannel);
%feature("autodoc", "AnalogIOChannelName(HDWF hdwf, int idxChannel) -> ( char szName[32], char szLabel[16] )") FDwfAnalogIOChannelName;
%cstring_bounded_output(char* szName, 32);
%cstring_bounded_output(char* szLabel, 16);
DWFAPI BOOL  FDwfAnalogIOChannelName(HDWF hdwf, int idxChannel, char *szName, char *szLabel);
%feature("autodoc", "AnalogIOChannelInfo(HDWF hdwf, int idxChannel) -> ( int * nNodes )") FDwfAnalogIOChannelInfo;
%apply int * OUTPUT {int * pnNodes};
DWFAPI BOOL  FDwfAnalogIOChannelInfo(HDWF hdwf, int idxChannel, int *pnNodes);
%feature("autodoc", "AnalogIOChannelNodeName(HDWF hdwf, int idxChannel, int idxNode) -> ( char szNodeName[32], char szNodeUnits[16] )") FDwfAnalogIOChannelNodeName;
%cstring_bounded_output(char* szNodeName, 32);
%cstring_bounded_output(char* szNodeUnits, 16);
DWFAPI BOOL  FDwfAnalogIOChannelNodeName(HDWF hdwf, int idxChannel, int idxNode, char *szNodeName, char *szNodeUnits);
%feature("autodoc", "AnalogIOChannelNodeInfo(HDWF hdwf, int idxChannel, int idxNode) -> ( ANALOGIO*  analogio )") FDwfAnalogIOChannelNodeInfo;
%apply ANALOGIO*  OUTPUT {ANALOGIO*  panalogio};
DWFAPI BOOL  FDwfAnalogIOChannelNodeInfo(HDWF hdwf, int idxChannel, int idxNode, ANALOGIO* panalogio);
%feature("autodoc", "AnalogIOChannelNodeSetInfo(HDWF hdwf, int idxChannel, int idxNode) -> ( double*  min, double*  max, int*  nSteps )") FDwfAnalogIOChannelNodeSetInfo;
%apply double*  OUTPUT {double*  pmin};
%apply double*  OUTPUT {double*  pmax};
%apply int*  OUTPUT {int*  pnSteps};
DWFAPI BOOL  FDwfAnalogIOChannelNodeSetInfo(HDWF hdwf, int idxChannel, int idxNode, double* pmin, double* pmax, int* pnSteps);
%feature("autodoc", "AnalogIOChannelNodeSet(HDWF hdwf, int idxChannel, int idxNode, double value) -> (  )") FDwfAnalogIOChannelNodeSet;
DWFAPI BOOL  FDwfAnalogIOChannelNodeSet(HDWF hdwf, int idxChannel, int idxNode, double value);
%feature("autodoc", "AnalogIOChannelNodeGet(HDWF hdwf, int idxChannel, int idxNode) -> ( double*  value )") FDwfAnalogIOChannelNodeGet;
%apply double*  OUTPUT {double*  pvalue};
DWFAPI BOOL  FDwfAnalogIOChannelNodeGet(HDWF hdwf, int idxChannel, int idxNode, double* pvalue);
%feature("autodoc", "AnalogIOChannelNodeStatusInfo(HDWF hdwf, int idxChannel, int idxNode) -> ( double*  min, double*  max, int*  nSteps )") FDwfAnalogIOChannelNodeStatusInfo;
%apply double*  OUTPUT {double*  pmin};
%apply double*  OUTPUT {double*  pmax};
%apply int*  OUTPUT {int*  pnSteps};
DWFAPI BOOL  FDwfAnalogIOChannelNodeStatusInfo(HDWF hdwf, int idxChannel, int idxNode, double* pmin, double* pmax, int* pnSteps);
%feature("autodoc", "AnalogIOChannelNodeStatus(HDWF hdwf, int idxChannel, int idxNode) -> ( double*  value )") FDwfAnalogIOChannelNodeStatus;
%apply double*  OUTPUT {double*  pvalue};
DWFAPI BOOL  FDwfAnalogIOChannelNodeStatus(HDWF hdwf, int idxChannel, int idxNode, double* pvalue);


// DIGITAL IO INSTRUMENT FUNCTIONS
// Control:
%feature("autodoc", "DigitalIOReset(HDWF hdwf) -> (  )") FDwfDigitalIOReset;
DWFAPI BOOL  FDwfDigitalIOReset(HDWF hdwf);
%feature("autodoc", "DigitalIOConfigure(HDWF hdwf) -> (  )") FDwfDigitalIOConfigure;
DWFAPI BOOL  FDwfDigitalIOConfigure(HDWF hdwf);
%feature("autodoc", "DigitalIOStatus(HDWF hdwf) -> (  )") FDwfDigitalIOStatus;
DWFAPI BOOL  FDwfDigitalIOStatus(HDWF hdwf);

// Configure:
%feature("autodoc", "DigitalIOOutputEnableInfo(HDWF hdwf) -> ( unsigned int*  fsOutputEnableMask )") FDwfDigitalIOOutputEnableInfo;
%apply unsigned int*  OUTPUT {unsigned int*  pfsOutputEnableMask};
DWFAPI BOOL  FDwfDigitalIOOutputEnableInfo(HDWF hdwf, unsigned int* pfsOutputEnableMask);
%feature("autodoc", "DigitalIOOutputEnableSet(HDWF hdwf, unsigned int fsOutputEnable) -> (  )") FDwfDigitalIOOutputEnableSet;
DWFAPI BOOL  FDwfDigitalIOOutputEnableSet(HDWF hdwf, unsigned int fsOutputEnable);
%feature("autodoc", "DigitalIOOutputEnableGet(HDWF hdwf) -> ( unsigned int*  fsOutputEnable )") FDwfDigitalIOOutputEnableGet;
%apply unsigned int*  OUTPUT {unsigned int*  pfsOutputEnable};
DWFAPI BOOL  FDwfDigitalIOOutputEnableGet(HDWF hdwf, unsigned int* pfsOutputEnable);
%feature("autodoc", "DigitalIOOutputInfo(HDWF hdwf) -> ( unsigned int*  fsOutputMask )") FDwfDigitalIOOutputInfo;
%apply unsigned int*  OUTPUT {unsigned int*  pfsOutputMask};
DWFAPI BOOL  FDwfDigitalIOOutputInfo(HDWF hdwf, unsigned int* pfsOutputMask);
%feature("autodoc", "DigitalIOOutputSet(HDWF hdwf, unsigned int fsOutput) -> (  )") FDwfDigitalIOOutputSet;
DWFAPI BOOL  FDwfDigitalIOOutputSet(HDWF hdwf, unsigned int fsOutput);
%feature("autodoc", "DigitalIOOutputGet(HDWF hdwf) -> ( unsigned int*  fsOutput )") FDwfDigitalIOOutputGet;
%apply unsigned int*  OUTPUT {unsigned int*  pfsOutput};
DWFAPI BOOL  FDwfDigitalIOOutputGet(HDWF hdwf, unsigned int* pfsOutput);
%feature("autodoc", "DigitalIOInputInfo(HDWF hdwf) -> ( unsigned int*  fsInputMask )") FDwfDigitalIOInputInfo;
%apply unsigned int*  OUTPUT {unsigned int*  pfsInputMask};
DWFAPI BOOL  FDwfDigitalIOInputInfo(HDWF hdwf, unsigned int* pfsInputMask);
%feature("autodoc", "DigitalIOInputStatus(HDWF hdwf) -> ( unsigned int*  fsInput )") FDwfDigitalIOInputStatus;
%apply unsigned int*  OUTPUT {unsigned int*  pfsInput};
DWFAPI BOOL  FDwfDigitalIOInputStatus(HDWF hdwf, unsigned int* pfsInput);


// DIGITAL IN INSTRUMENT FUNCTIONS
// Control and status: 
%feature("autodoc", "DigitalInReset(HDWF hdwf) -> (  )") FDwfDigitalInReset;
DWFAPI BOOL  FDwfDigitalInReset(HDWF hdwf);
%feature("autodoc", "DigitalInConfigure(HDWF hdwf, BOOL fReconfigure, BOOL fStart) -> (  )") FDwfDigitalInConfigure;
DWFAPI BOOL  FDwfDigitalInConfigure(HDWF hdwf, BOOL fReconfigure, BOOL fStart);
%feature("autodoc", "DigitalInStatus(HDWF hdwf, BOOL fReadData) -> ( DwfState*  sts )") FDwfDigitalInStatus;
%apply DwfState*  OUTPUT {DwfState*  psts};
DWFAPI BOOL  FDwfDigitalInStatus(HDWF hdwf, BOOL fReadData, DwfState* psts);
%feature("autodoc", "DigitalInStatusSamplesLeft(HDWF hdwf) -> ( int * cSamplesLeft )") FDwfDigitalInStatusSamplesLeft;
%apply int * OUTPUT {int * pcSamplesLeft};
DWFAPI BOOL  FDwfDigitalInStatusSamplesLeft(HDWF hdwf, int *pcSamplesLeft);
%feature("autodoc", "DigitalInStatusSamplesValid(HDWF hdwf) -> ( int *  cSamplesValid )") FDwfDigitalInStatusSamplesValid;
%apply int *  OUTPUT {int *  pcSamplesValid};
DWFAPI BOOL  FDwfDigitalInStatusSamplesValid(HDWF hdwf, int * pcSamplesValid);
%feature("autodoc", "DigitalInStatusIndexWrite(HDWF hdwf) -> ( int * idxWrite )") FDwfDigitalInStatusIndexWrite;
%apply int * OUTPUT {int * pidxWrite};
DWFAPI BOOL  FDwfDigitalInStatusIndexWrite(HDWF hdwf, int *pidxWrite);
%feature("autodoc", "DigitalInStatusAutoTriggered(HDWF hdwf) -> ( BOOL*  fAuto )") FDwfDigitalInStatusAutoTriggered;
%apply BOOL*  OUTPUT {BOOL*  pfAuto};
DWFAPI BOOL  FDwfDigitalInStatusAutoTriggered(HDWF hdwf, BOOL* pfAuto);
%feature("autodoc", "DigitalInStatusData(HDWF hdwf, void *rgData) -> (  )") FDwfDigitalInStatusData;
%apply (unsigned short* INPLACE_ARRAY1, int DIM1) {(void * rgData, int countOfDataBytes)};
DWFAPI BOOL  FDwfDigitalInStatusData(HDWF hdwf, void *rgData, int countOfDataBytes);

// Acquistion configuration:
%feature("autodoc", "DigitalInInternalClockInfo(HDWF hdwf) -> ( double*  hzFreq )") FDwfDigitalInInternalClockInfo;
%apply double*  OUTPUT {double*  phzFreq};
DWFAPI BOOL  FDwfDigitalInInternalClockInfo(HDWF hdwf, double* phzFreq);

%feature("autodoc", "DigitalInClockSourceInfo(HDWF hdwf) -> ( int * fsDwfDigitalInClockSource )") FDwfDigitalInClockSourceInfo;
%apply int * OUTPUT {int * pfsDwfDigitalInClockSource};
DWFAPI BOOL  FDwfDigitalInClockSourceInfo(HDWF hdwf, int *pfsDwfDigitalInClockSource);
%feature("autodoc", "DigitalInClockSourceSet(HDWF hdwf, DwfDigitalInClockSource v) -> (  )") FDwfDigitalInClockSourceSet;
DWFAPI BOOL  FDwfDigitalInClockSourceSet(HDWF hdwf, DwfDigitalInClockSource v);
%feature("autodoc", "DigitalInClockSourceGet(HDWF hdwf) -> ( DwfDigitalInClockSource * v )") FDwfDigitalInClockSourceGet;
%apply DwfDigitalInClockSource * OUTPUT {DwfDigitalInClockSource * pv};
DWFAPI BOOL  FDwfDigitalInClockSourceGet(HDWF hdwf, DwfDigitalInClockSource *pv);

%feature("autodoc", "DigitalInDividerInfo(HDWF hdwf) -> ( unsigned int * divMax )") FDwfDigitalInDividerInfo;
%apply unsigned int * OUTPUT {unsigned int * pdivMax};
DWFAPI BOOL  FDwfDigitalInDividerInfo(HDWF hdwf, unsigned int *pdivMax);
%feature("autodoc", "DigitalInDividerSet(HDWF hdwf, unsigned int div) -> (  )") FDwfDigitalInDividerSet;
DWFAPI BOOL  FDwfDigitalInDividerSet(HDWF hdwf, unsigned int div);
%feature("autodoc", "DigitalInDividerGet(HDWF hdwf) -> ( unsigned int * div )") FDwfDigitalInDividerGet;
%apply unsigned int * OUTPUT {unsigned int * pdiv};
DWFAPI BOOL  FDwfDigitalInDividerGet(HDWF hdwf, unsigned int *pdiv);

%feature("autodoc", "DigitalInBitsInfo(HDWF hdwf) -> ( int * nBits )") FDwfDigitalInBitsInfo;
%apply int * OUTPUT {int * pnBits};
DWFAPI BOOL  FDwfDigitalInBitsInfo(HDWF hdwf, int *pnBits);
%feature("autodoc", "DigitalInSampleFormatSet(HDWF hdwf, int nBits) -> (  )") FDwfDigitalInSampleFormatSet;
DWFAPI BOOL  FDwfDigitalInSampleFormatSet(HDWF hdwf, int nBits);
%feature("autodoc", "DigitalInSampleFormatGet(HDWF hdwf) -> ( int * nBits )") FDwfDigitalInSampleFormatGet;
%apply int * OUTPUT {int * pnBits};
DWFAPI BOOL  FDwfDigitalInSampleFormatGet(HDWF hdwf, int *pnBits);

%feature("autodoc", "DigitalInBufferSizeInfo(HDWF hdwf) -> ( int * nSizeMax )") FDwfDigitalInBufferSizeInfo;
%apply int * OUTPUT {int * pnSizeMax};
DWFAPI BOOL  FDwfDigitalInBufferSizeInfo(HDWF hdwf, int *pnSizeMax);
%feature("autodoc", "DigitalInBufferSizeSet(HDWF hdwf, int nSize) -> (  )") FDwfDigitalInBufferSizeSet;
DWFAPI BOOL  FDwfDigitalInBufferSizeSet(HDWF hdwf, int nSize);
%feature("autodoc", "DigitalInBufferSizeGet(HDWF hdwf) -> ( int * nSize )") FDwfDigitalInBufferSizeGet;
%apply int * OUTPUT {int * pnSize};
DWFAPI BOOL  FDwfDigitalInBufferSizeGet(HDWF hdwf, int *pnSize);

%feature("autodoc", "DigitalInSampleModeInfo(HDWF hdwf) -> ( int * fsDwfDigitalInSampleMode )") FDwfDigitalInSampleModeInfo;
%apply int * OUTPUT {int * pfsDwfDigitalInSampleMode};
DWFAPI BOOL  FDwfDigitalInSampleModeInfo(HDWF hdwf, int *pfsDwfDigitalInSampleMode);
%feature("autodoc", "DigitalInSampleModeSet(HDWF hdwf, DwfDigitalInSampleMode v) -> (  )") FDwfDigitalInSampleModeSet;
DWFAPI BOOL  FDwfDigitalInSampleModeSet(HDWF hdwf, DwfDigitalInSampleMode v);
%feature("autodoc", "DigitalInSampleModeGet(HDWF hdwf) -> ( DwfDigitalInSampleMode * v )") FDwfDigitalInSampleModeGet;
%apply DwfDigitalInSampleMode * OUTPUT {DwfDigitalInSampleMode * pv};
DWFAPI BOOL  FDwfDigitalInSampleModeGet(HDWF hdwf, DwfDigitalInSampleMode *pv);

%feature("autodoc", "DigitalInAcquisitionModeInfo(HDWF hdwf) -> ( int * fsacqmode )") FDwfDigitalInAcquisitionModeInfo;
%apply int * OUTPUT {int * pfsacqmode};
DWFAPI BOOL  FDwfDigitalInAcquisitionModeInfo(HDWF hdwf, int *pfsacqmode);
%feature("autodoc", "DigitalInAcquisitionModeSet(HDWF hdwf, ACQMODE acqmode) -> (  )") FDwfDigitalInAcquisitionModeSet;
DWFAPI BOOL  FDwfDigitalInAcquisitionModeSet(HDWF hdwf, ACQMODE acqmode);
%feature("autodoc", "DigitalInAcquisitionModeGet(HDWF hdwf) -> ( ACQMODE * acqmode )") FDwfDigitalInAcquisitionModeGet;
%apply ACQMODE * OUTPUT {ACQMODE * pacqmode};
DWFAPI BOOL  FDwfDigitalInAcquisitionModeGet(HDWF hdwf, ACQMODE *pacqmode);

// Trigger configuration:
%feature("autodoc", "DigitalInTriggerSourceInfo(HDWF hdwf) -> ( int*  fstrigsrc )") FDwfDigitalInTriggerSourceInfo;
%apply int*  OUTPUT {int*  pfstrigsrc};
DWFAPI BOOL  FDwfDigitalInTriggerSourceInfo(HDWF hdwf, int* pfstrigsrc);
%feature("autodoc", "DigitalInTriggerSourceSet(HDWF hdwf, TRIGSRC trigsrc) -> (  )") FDwfDigitalInTriggerSourceSet;
DWFAPI BOOL  FDwfDigitalInTriggerSourceSet(HDWF hdwf, TRIGSRC trigsrc);
%feature("autodoc", "DigitalInTriggerSourceGet(HDWF hdwf) -> ( TRIGSRC*  trigsrc )") FDwfDigitalInTriggerSourceGet;
%apply TRIGSRC*  OUTPUT {TRIGSRC*  ptrigsrc};
DWFAPI BOOL  FDwfDigitalInTriggerSourceGet(HDWF hdwf, TRIGSRC* ptrigsrc);

%feature("autodoc", "DigitalInTriggerPositionInfo(HDWF hdwf) -> ( unsigned int * nSamplesAfterTriggerMax )") FDwfDigitalInTriggerPositionInfo;
%apply unsigned int * OUTPUT {unsigned int * pnSamplesAfterTriggerMax};
DWFAPI BOOL  FDwfDigitalInTriggerPositionInfo(HDWF hdwf, unsigned int *pnSamplesAfterTriggerMax);
%feature("autodoc", "DigitalInTriggerPositionSet(HDWF hdwf, unsigned int cSamplesAfterTrigger) -> (  )") FDwfDigitalInTriggerPositionSet;
DWFAPI BOOL  FDwfDigitalInTriggerPositionSet(HDWF hdwf, unsigned int cSamplesAfterTrigger);
%feature("autodoc", "DigitalInTriggerPositionGet(HDWF hdwf) -> ( unsigned int * cSamplesAfterTrigger )") FDwfDigitalInTriggerPositionGet;
%apply unsigned int * OUTPUT {unsigned int * pcSamplesAfterTrigger};
DWFAPI BOOL  FDwfDigitalInTriggerPositionGet(HDWF hdwf, unsigned int *pcSamplesAfterTrigger);

%feature("autodoc", "DigitalInTriggerAutoTimeoutInfo(HDWF hdwf) -> ( double*  secMin, double*  secMax, double*  nSteps )") FDwfDigitalInTriggerAutoTimeoutInfo;
%apply double*  OUTPUT {double*  psecMin};
%apply double*  OUTPUT {double*  psecMax};
%apply double*  OUTPUT {double*  pnSteps};
DWFAPI BOOL  FDwfDigitalInTriggerAutoTimeoutInfo(HDWF hdwf, double* psecMin, double* psecMax, double* pnSteps);
%feature("autodoc", "DigitalInTriggerAutoTimeoutSet(HDWF hdwf, double secTimeout) -> (  )") FDwfDigitalInTriggerAutoTimeoutSet;
DWFAPI BOOL  FDwfDigitalInTriggerAutoTimeoutSet(HDWF hdwf, double secTimeout);
%feature("autodoc", "DigitalInTriggerAutoTimeoutGet(HDWF hdwf) -> ( double*  secTimeout )") FDwfDigitalInTriggerAutoTimeoutGet;
%apply double*  OUTPUT {double*  psecTimeout};
DWFAPI BOOL  FDwfDigitalInTriggerAutoTimeoutGet(HDWF hdwf, double* psecTimeout);

%feature("autodoc", "DigitalInTriggerInfo(HDWF hdwf) -> ( unsigned int * fsLevelLow, unsigned int * fsLevelHigh, unsigned int * fsEdgeRise, unsigned int * fsEdgeFall )") FDwfDigitalInTriggerInfo;
%apply unsigned int * OUTPUT {unsigned int * pfsLevelLow};
%apply unsigned int * OUTPUT {unsigned int * pfsLevelHigh};
%apply unsigned int * OUTPUT {unsigned int * pfsEdgeRise};
%apply unsigned int * OUTPUT {unsigned int * pfsEdgeFall};
DWFAPI BOOL  FDwfDigitalInTriggerInfo(HDWF hdwf, unsigned int *pfsLevelLow, unsigned int *pfsLevelHigh, unsigned int *pfsEdgeRise, unsigned int *pfsEdgeFall);
%feature("autodoc", "DigitalInTriggerSet(HDWF hdwf, unsigned int fsLevelLow, unsigned int fsLevelHigh, unsigned int fsEdgeRise, unsigned int fsEdgeFall) -> (  )") FDwfDigitalInTriggerSet;
DWFAPI BOOL  FDwfDigitalInTriggerSet(HDWF hdwf, unsigned int fsLevelLow, unsigned int fsLevelHigh, unsigned int fsEdgeRise, unsigned int fsEdgeFall);
%feature("autodoc", "DigitalInTriggerGet(HDWF hdwf) -> ( unsigned int * fsLevelLow, unsigned int * fsLevelHigh, unsigned int * fsEdgeRise, unsigned int * fsEdgeFall )") FDwfDigitalInTriggerGet;
%apply unsigned int * OUTPUT {unsigned int * pfsLevelLow};
%apply unsigned int * OUTPUT {unsigned int * pfsLevelHigh};
%apply unsigned int * OUTPUT {unsigned int * pfsEdgeRise};
%apply unsigned int * OUTPUT {unsigned int * pfsEdgeFall};
DWFAPI BOOL  FDwfDigitalInTriggerGet(HDWF hdwf, unsigned int *pfsLevelLow, unsigned int *pfsLevelHigh, unsigned int *pfsEdgeRise, unsigned int *pfsEdgeFall);
// the logic for trigger bits: Low and High and (Rise or Fall)
// bits set in Rise and Fall means any edge

// DIGITAL OUT INSTRUMENT FUNCTIONS
// Control:
%feature("autodoc", "DigitalOutReset(HDWF hdwf) -> (  )") FDwfDigitalOutReset;
DWFAPI BOOL  FDwfDigitalOutReset(HDWF hdwf);
%feature("autodoc", "DigitalOutConfigure(HDWF hdwf, BOOL fStart) -> (  )") FDwfDigitalOutConfigure;
DWFAPI BOOL  FDwfDigitalOutConfigure(HDWF hdwf, BOOL fStart);
%feature("autodoc", "DigitalOutStatus(HDWF hdwf) -> ( DwfState*  sts )") FDwfDigitalOutStatus;
%apply DwfState*  OUTPUT {DwfState*  psts};
DWFAPI BOOL  FDwfDigitalOutStatus(HDWF hdwf, DwfState* psts);

// Configuration:
%feature("autodoc", "DigitalOutInternalClockInfo(HDWF hdwf) -> ( double*  hzFreq )") FDwfDigitalOutInternalClockInfo;
%apply double*  OUTPUT {double*  phzFreq};
DWFAPI BOOL  FDwfDigitalOutInternalClockInfo(HDWF hdwf, double* phzFreq);

%feature("autodoc", "DigitalOutTriggerSourceInfo(HDWF hdwf) -> ( int*  fstrigsrc )") FDwfDigitalOutTriggerSourceInfo;
%apply int*  OUTPUT {int*  pfstrigsrc};
DWFAPI BOOL  FDwfDigitalOutTriggerSourceInfo(HDWF hdwf, int* pfstrigsrc);
%feature("autodoc", "DigitalOutTriggerSourceSet(HDWF hdwf, TRIGSRC trigsrc) -> (  )") FDwfDigitalOutTriggerSourceSet;
DWFAPI BOOL  FDwfDigitalOutTriggerSourceSet(HDWF hdwf, TRIGSRC trigsrc);
%feature("autodoc", "DigitalOutTriggerSourceGet(HDWF hdwf) -> ( TRIGSRC*  trigsrc )") FDwfDigitalOutTriggerSourceGet;
%apply TRIGSRC*  OUTPUT {TRIGSRC*  ptrigsrc};
DWFAPI BOOL  FDwfDigitalOutTriggerSourceGet(HDWF hdwf, TRIGSRC* ptrigsrc);

%feature("autodoc", "DigitalOutRunInfo(HDWF hdwf) -> ( double*  secMin, double*  secMax )") FDwfDigitalOutRunInfo;
%apply double*  OUTPUT {double*  psecMin};
%apply double*  OUTPUT {double*  psecMax};
DWFAPI BOOL  FDwfDigitalOutRunInfo(HDWF hdwf, double* psecMin, double* psecMax);
%feature("autodoc", "DigitalOutRunSet(HDWF hdwf, double secRun) -> (  )") FDwfDigitalOutRunSet;
DWFAPI BOOL  FDwfDigitalOutRunSet(HDWF hdwf, double secRun);
%feature("autodoc", "DigitalOutRunGet(HDWF hdwf) -> ( double*  secRun )") FDwfDigitalOutRunGet;
%apply double*  OUTPUT {double*  psecRun};
DWFAPI BOOL  FDwfDigitalOutRunGet(HDWF hdwf, double* psecRun);
%feature("autodoc", "DigitalOutRunStatus(HDWF hdwf) -> ( double*  secRun )") FDwfDigitalOutRunStatus;
%apply double*  OUTPUT {double*  psecRun};
DWFAPI BOOL  FDwfDigitalOutRunStatus(HDWF hdwf, double* psecRun);

%feature("autodoc", "DigitalOutWaitInfo(HDWF hdwf) -> ( double*  secMin, double*  secMax )") FDwfDigitalOutWaitInfo;
%apply double*  OUTPUT {double*  psecMin};
%apply double*  OUTPUT {double*  psecMax};
DWFAPI BOOL  FDwfDigitalOutWaitInfo(HDWF hdwf, double* psecMin, double* psecMax);
%feature("autodoc", "DigitalOutWaitSet(HDWF hdwf, double secWait) -> (  )") FDwfDigitalOutWaitSet;
DWFAPI BOOL  FDwfDigitalOutWaitSet(HDWF hdwf, double secWait);
%feature("autodoc", "DigitalOutWaitGet(HDWF hdwf) -> ( double*  secWait )") FDwfDigitalOutWaitGet;
%apply double*  OUTPUT {double*  psecWait};
DWFAPI BOOL  FDwfDigitalOutWaitGet(HDWF hdwf, double* psecWait);

%feature("autodoc", "DigitalOutRepeatInfo(HDWF hdwf) -> ( unsigned int*  nMin, unsigned int*  nMax )") FDwfDigitalOutRepeatInfo;
%apply unsigned int*  OUTPUT {unsigned int*  pnMin};
%apply unsigned int*  OUTPUT {unsigned int*  pnMax};
DWFAPI BOOL  FDwfDigitalOutRepeatInfo(HDWF hdwf, unsigned int* pnMin, unsigned int* pnMax);
%feature("autodoc", "DigitalOutRepeatSet(HDWF hdwf, unsigned int cRepeat) -> (  )") FDwfDigitalOutRepeatSet;
DWFAPI BOOL  FDwfDigitalOutRepeatSet(HDWF hdwf, unsigned int cRepeat);
%feature("autodoc", "DigitalOutRepeatGet(HDWF hdwf) -> ( unsigned int*  cRepeat )") FDwfDigitalOutRepeatGet;
%apply unsigned int*  OUTPUT {unsigned int*  pcRepeat};
DWFAPI BOOL  FDwfDigitalOutRepeatGet(HDWF hdwf, unsigned int* pcRepeat);
%feature("autodoc", "DigitalOutRepeatStatus(HDWF hdwf) -> ( unsigned int*  cRepeat )") FDwfDigitalOutRepeatStatus;
%apply unsigned int*  OUTPUT {unsigned int*  pcRepeat};
DWFAPI BOOL  FDwfDigitalOutRepeatStatus(HDWF hdwf, unsigned int* pcRepeat);

%feature("autodoc", "DigitalOutRepeatTriggerSet(HDWF hdwf, BOOL fRepeatTrigger) -> (  )") FDwfDigitalOutRepeatTriggerSet;
DWFAPI BOOL  FDwfDigitalOutRepeatTriggerSet(HDWF hdwf, BOOL fRepeatTrigger);
%feature("autodoc", "DigitalOutRepeatTriggerGet(HDWF hdwf) -> ( BOOL*  fRepeatTrigger )") FDwfDigitalOutRepeatTriggerGet;
%apply BOOL*  OUTPUT {BOOL*  pfRepeatTrigger};
DWFAPI BOOL  FDwfDigitalOutRepeatTriggerGet(HDWF hdwf, BOOL* pfRepeatTrigger);

%feature("autodoc", "DigitalOutCount(HDWF hdwf) -> ( int*  cChannel )") FDwfDigitalOutCount;
%apply int*  OUTPUT {int*  pcChannel};
DWFAPI BOOL  FDwfDigitalOutCount(HDWF hdwf, int* pcChannel);
%feature("autodoc", "DigitalOutEnableSet(HDWF hdwf, int idxChannel, BOOL fEnable) -> (  )") FDwfDigitalOutEnableSet;
DWFAPI BOOL  FDwfDigitalOutEnableSet(HDWF hdwf, int idxChannel, BOOL fEnable);
%feature("autodoc", "DigitalOutEnableGet(HDWF hdwf, int idxChannel) -> ( BOOL*  fEnable )") FDwfDigitalOutEnableGet;
%apply BOOL*  OUTPUT {BOOL*  pfEnable};
DWFAPI BOOL  FDwfDigitalOutEnableGet(HDWF hdwf, int idxChannel, BOOL* pfEnable);

%feature("autodoc", "DigitalOutOutputInfo(HDWF hdwf, int idxChannel) -> ( int*  fsDwfDigitalOutOutput )") FDwfDigitalOutOutputInfo;
%apply int*  OUTPUT {int*  pfsDwfDigitalOutOutput};
DWFAPI BOOL  FDwfDigitalOutOutputInfo(HDWF hdwf, int idxChannel, int* pfsDwfDigitalOutOutput);
%feature("autodoc", "DigitalOutOutputSet(HDWF hdwf, int idxChannel, DwfDigitalOutOutput v) -> (  )") FDwfDigitalOutOutputSet;
DWFAPI BOOL  FDwfDigitalOutOutputSet(HDWF hdwf, int idxChannel, DwfDigitalOutOutput v);
%feature("autodoc", "DigitalOutOutputGet(HDWF hdwf, int idxChannel) -> ( DwfDigitalOutOutput*  v )") FDwfDigitalOutOutputGet;
%apply DwfDigitalOutOutput*  OUTPUT {DwfDigitalOutOutput*  pv};
DWFAPI BOOL  FDwfDigitalOutOutputGet(HDWF hdwf, int idxChannel, DwfDigitalOutOutput* pv);

%feature("autodoc", "DigitalOutTypeInfo(HDWF hdwf, int idxChannel) -> ( int * fsDwfDigitalOutType )") FDwfDigitalOutTypeInfo;
%apply int * OUTPUT {int * pfsDwfDigitalOutType};
DWFAPI BOOL  FDwfDigitalOutTypeInfo(HDWF hdwf, int idxChannel, int *pfsDwfDigitalOutType);
%feature("autodoc", "DigitalOutTypeSet(HDWF hdwf, int idxChannel, DwfDigitalOutType v) -> (  )") FDwfDigitalOutTypeSet;
DWFAPI BOOL  FDwfDigitalOutTypeSet(HDWF hdwf, int idxChannel, DwfDigitalOutType v);
%feature("autodoc", "DigitalOutTypeGet(HDWF hdwf, int idxChannel) -> ( DwfDigitalOutType * v )") FDwfDigitalOutTypeGet;
%apply DwfDigitalOutType * OUTPUT {DwfDigitalOutType * pv};
DWFAPI BOOL  FDwfDigitalOutTypeGet(HDWF hdwf, int idxChannel, DwfDigitalOutType *pv);

%feature("autodoc", "DigitalOutIdleInfo(HDWF hdwf, int idxChannel) -> ( int * fsDwfDigitalOutIdle )") FDwfDigitalOutIdleInfo;
%apply int * OUTPUT {int * pfsDwfDigitalOutIdle};
DWFAPI BOOL  FDwfDigitalOutIdleInfo(HDWF hdwf, int idxChannel, int *pfsDwfDigitalOutIdle);
%feature("autodoc", "DigitalOutIdleSet(HDWF hdwf, int idxChannel, DwfDigitalOutIdle v) -> (  )") FDwfDigitalOutIdleSet;
DWFAPI BOOL  FDwfDigitalOutIdleSet(HDWF hdwf, int idxChannel, DwfDigitalOutIdle v);
%feature("autodoc", "DigitalOutIdleGet(HDWF hdwf, int idxChannel) -> ( DwfDigitalOutIdle * v )") FDwfDigitalOutIdleGet;
%apply DwfDigitalOutIdle * OUTPUT {DwfDigitalOutIdle * pv};
DWFAPI BOOL  FDwfDigitalOutIdleGet(HDWF hdwf, int idxChannel, DwfDigitalOutIdle *pv);

%feature("autodoc", "DigitalOutDividerInfo(HDWF hdwf, int idxChannel) -> ( unsigned int * Min, unsigned int * Max )") FDwfDigitalOutDividerInfo;
%apply unsigned int * OUTPUT {unsigned int * vMin};
%apply unsigned int * OUTPUT {unsigned int * vMax};
DWFAPI BOOL  FDwfDigitalOutDividerInfo(HDWF hdwf, int idxChannel, unsigned int *vMin, unsigned int *vMax);
%feature("autodoc", "DigitalOutDividerInitSet(HDWF hdwf, int idxChannel, unsigned int v) -> (  )") FDwfDigitalOutDividerInitSet;
DWFAPI BOOL  FDwfDigitalOutDividerInitSet(HDWF hdwf, int idxChannel, unsigned int v);
%feature("autodoc", "DigitalOutDividerInitGet(HDWF hdwf, int idxChannel) -> ( unsigned int * v )") FDwfDigitalOutDividerInitGet;
%apply unsigned int * OUTPUT {unsigned int * pv};
DWFAPI BOOL  FDwfDigitalOutDividerInitGet(HDWF hdwf, int idxChannel, unsigned int *pv);
%feature("autodoc", "DigitalOutDividerSet(HDWF hdwf, int idxChannel, unsigned int v) -> (  )") FDwfDigitalOutDividerSet;
DWFAPI BOOL  FDwfDigitalOutDividerSet(HDWF hdwf, int idxChannel, unsigned int v);
%feature("autodoc", "DigitalOutDividerGet(HDWF hdwf, int idxChannel) -> ( unsigned int * v )") FDwfDigitalOutDividerGet;
%apply unsigned int * OUTPUT {unsigned int * pv};
DWFAPI BOOL  FDwfDigitalOutDividerGet(HDWF hdwf, int idxChannel, unsigned int *pv);

%feature("autodoc", "DigitalOutCounterInfo(HDWF hdwf, int idxChannel) -> ( unsigned int * Min, unsigned int * Max )") FDwfDigitalOutCounterInfo;
%apply unsigned int * OUTPUT {unsigned int * vMin};
%apply unsigned int * OUTPUT {unsigned int * vMax};
DWFAPI BOOL  FDwfDigitalOutCounterInfo(HDWF hdwf, int idxChannel, unsigned int *vMin, unsigned int *vMax);
%feature("autodoc", "DigitalOutCounterInitSet(HDWF hdwf, int idxChannel, BOOL fHigh, unsigned int v) -> (  )") FDwfDigitalOutCounterInitSet;
DWFAPI BOOL  FDwfDigitalOutCounterInitSet(HDWF hdwf, int idxChannel, BOOL fHigh, unsigned int v);
%feature("autodoc", "DigitalOutCounterInitGet(HDWF hdwf, int idxChannel) -> ( int*  fHigh, unsigned int * v )") FDwfDigitalOutCounterInitGet;
%apply int*  OUTPUT {int*  pfHigh};
%apply unsigned int * OUTPUT {unsigned int * pv};
DWFAPI BOOL  FDwfDigitalOutCounterInitGet(HDWF hdwf, int idxChannel, int* pfHigh, unsigned int *pv);
%feature("autodoc", "DigitalOutCounterSet(HDWF hdwf, int idxChannel, unsigned int vLow, unsigned int vHigh) -> (  )") FDwfDigitalOutCounterSet;
DWFAPI BOOL  FDwfDigitalOutCounterSet(HDWF hdwf, int idxChannel, unsigned int vLow, unsigned int vHigh);
%feature("autodoc", "DigitalOutCounterGet(HDWF hdwf, int idxChannel) -> ( unsigned int * vLow, unsigned int * vHigh )") FDwfDigitalOutCounterGet;
%apply unsigned int * OUTPUT {unsigned int * pvLow};
%apply unsigned int * OUTPUT {unsigned int * pvHigh};
DWFAPI BOOL  FDwfDigitalOutCounterGet(HDWF hdwf, int idxChannel, unsigned int *pvLow, unsigned int *pvHigh);

%feature("autodoc", "DigitalOutDataInfo(HDWF hdwf, int idxChannel) -> ( unsigned int * countOfBitsMax )") FDwfDigitalOutDataInfo;
%apply unsigned int * OUTPUT {unsigned int * pcountOfBitsMax};
DWFAPI BOOL  FDwfDigitalOutDataInfo(HDWF hdwf, int idxChannel, unsigned int *pcountOfBitsMax);
%feature("autodoc", "DigitalOutDataSet(HDWF hdwf, int idxChannel, void *rgBits) -> (  )") FDwfDigitalOutDataSet;
%apply (unsigned short* INPLACE_ARRAY1, int DIM1) {(void * rgBits, int countOfDataBytes)};
DWFAPI BOOL  FDwfDigitalOutDataSet(HDWF hdwf, int idxChannel, void *rgBits, unsigned int countOfBits);
// bits order is lsb first
// for TS output the count of bits its the total number of IO|OE bits, it should be an even number
// BYTE:   0                 |1     ...
// bit:    0 |1 |2 |3 |...|7 |0 |1 |...
// sample: IO|OE|IO|OE|...|OE|IO|OE|...


// OBSOLETE, do not use them:
typedef unsigned char STS;
const STS stsRdy        = 0;
const STS stsArm        = 1;
const STS stsDone       = 2;
const STS stsTrig       = 3;
const STS stsCfg        = 4;
const STS stsPrefill    = 5;
const STS stsNotDone    = 6;
const STS stsTrigDly    = 7;
const STS stsError      = 8;
const STS stsBusy       = 9;
const STS stsStop       = 10;

%feature("autodoc", "AnalogOutEnableSet(HDWF hdwf, int idxChannel, BOOL fEnable) -> (  )") FDwfAnalogOutEnableSet;
DWFAPI BOOL  FDwfAnalogOutEnableSet(HDWF hdwf, int idxChannel, BOOL fEnable);
%feature("autodoc", "AnalogOutEnableGet(HDWF hdwf, int idxChannel) -> ( BOOL*  fEnable )") FDwfAnalogOutEnableGet;
%apply BOOL*  OUTPUT {BOOL*  pfEnable};
DWFAPI BOOL  FDwfAnalogOutEnableGet(HDWF hdwf, int idxChannel, BOOL* pfEnable);
%feature("autodoc", "AnalogOutFunctionInfo(HDWF hdwf, int idxChannel) -> ( int*  fsfunc )") FDwfAnalogOutFunctionInfo;
%apply int*  OUTPUT {int*  pfsfunc};
DWFAPI BOOL  FDwfAnalogOutFunctionInfo(HDWF hdwf, int idxChannel, int* pfsfunc);
%feature("autodoc", "AnalogOutFunctionSet(HDWF hdwf, int idxChannel, FUNC func) -> (  )") FDwfAnalogOutFunctionSet;
DWFAPI BOOL  FDwfAnalogOutFunctionSet(HDWF hdwf, int idxChannel, FUNC func);
%feature("autodoc", "AnalogOutFunctionGet(HDWF hdwf, int idxChannel) -> ( FUNC*  func )") FDwfAnalogOutFunctionGet;
%apply FUNC*  OUTPUT {FUNC*  pfunc};
DWFAPI BOOL  FDwfAnalogOutFunctionGet(HDWF hdwf, int idxChannel, FUNC* pfunc);
%feature("autodoc", "AnalogOutFrequencyInfo(HDWF hdwf, int idxChannel) -> ( double*  hzMin, double*  hzMax )") FDwfAnalogOutFrequencyInfo;
%apply double*  OUTPUT {double*  phzMin};
%apply double*  OUTPUT {double*  phzMax};
DWFAPI BOOL  FDwfAnalogOutFrequencyInfo(HDWF hdwf, int idxChannel, double* phzMin, double* phzMax);
%feature("autodoc", "AnalogOutFrequencySet(HDWF hdwf, int idxChannel, double hzFrequency) -> (  )") FDwfAnalogOutFrequencySet;
DWFAPI BOOL  FDwfAnalogOutFrequencySet(HDWF hdwf, int idxChannel, double hzFrequency);
%feature("autodoc", "AnalogOutFrequencyGet(HDWF hdwf, int idxChannel) -> ( double*  hzFrequency )") FDwfAnalogOutFrequencyGet;
%apply double*  OUTPUT {double*  phzFrequency};
DWFAPI BOOL  FDwfAnalogOutFrequencyGet(HDWF hdwf, int idxChannel, double* phzFrequency);
%feature("autodoc", "AnalogOutAmplitudeInfo(HDWF hdwf, int idxChannel) -> ( double*  voltsMin, double*  voltsMax )") FDwfAnalogOutAmplitudeInfo;
%apply double*  OUTPUT {double*  pvoltsMin};
%apply double*  OUTPUT {double*  pvoltsMax};
DWFAPI BOOL  FDwfAnalogOutAmplitudeInfo(HDWF hdwf, int idxChannel, double* pvoltsMin, double* pvoltsMax);
%feature("autodoc", "AnalogOutAmplitudeSet(HDWF hdwf, int idxChannel, double voltsAmplitude) -> (  )") FDwfAnalogOutAmplitudeSet;
DWFAPI BOOL  FDwfAnalogOutAmplitudeSet(HDWF hdwf, int idxChannel, double voltsAmplitude);
%feature("autodoc", "AnalogOutAmplitudeGet(HDWF hdwf, int idxChannel) -> ( double*  voltsAmplitude )") FDwfAnalogOutAmplitudeGet;
%apply double*  OUTPUT {double*  pvoltsAmplitude};
DWFAPI BOOL  FDwfAnalogOutAmplitudeGet(HDWF hdwf, int idxChannel, double* pvoltsAmplitude);
%feature("autodoc", "AnalogOutOffsetInfo(HDWF hdwf, int idxChannel) -> ( double*  voltsMin, double*  voltsMax )") FDwfAnalogOutOffsetInfo;
%apply double*  OUTPUT {double*  pvoltsMin};
%apply double*  OUTPUT {double*  pvoltsMax};
DWFAPI BOOL  FDwfAnalogOutOffsetInfo(HDWF hdwf, int idxChannel, double* pvoltsMin, double* pvoltsMax);
%feature("autodoc", "AnalogOutOffsetSet(HDWF hdwf, int idxChannel, double voltsOffset) -> (  )") FDwfAnalogOutOffsetSet;
DWFAPI BOOL  FDwfAnalogOutOffsetSet(HDWF hdwf, int idxChannel, double voltsOffset);
%feature("autodoc", "AnalogOutOffsetGet(HDWF hdwf, int idxChannel) -> ( double*  voltsOffset )") FDwfAnalogOutOffsetGet;
%apply double*  OUTPUT {double*  pvoltsOffset};
DWFAPI BOOL  FDwfAnalogOutOffsetGet(HDWF hdwf, int idxChannel, double* pvoltsOffset);
%feature("autodoc", "AnalogOutSymmetryInfo(HDWF hdwf, int idxChannel) -> ( double*  percentageMin, double*  percentageMax )") FDwfAnalogOutSymmetryInfo;
%apply double*  OUTPUT {double*  ppercentageMin};
%apply double*  OUTPUT {double*  ppercentageMax};
DWFAPI BOOL  FDwfAnalogOutSymmetryInfo(HDWF hdwf, int idxChannel, double* ppercentageMin, double* ppercentageMax);
%feature("autodoc", "AnalogOutSymmetrySet(HDWF hdwf, int idxChannel, double percentageSymmetry) -> (  )") FDwfAnalogOutSymmetrySet;
DWFAPI BOOL  FDwfAnalogOutSymmetrySet(HDWF hdwf, int idxChannel, double percentageSymmetry);
%feature("autodoc", "AnalogOutSymmetryGet(HDWF hdwf, int idxChannel) -> ( double*  percentageSymmetry )") FDwfAnalogOutSymmetryGet;
%apply double*  OUTPUT {double*  ppercentageSymmetry};
DWFAPI BOOL  FDwfAnalogOutSymmetryGet(HDWF hdwf, int idxChannel, double* ppercentageSymmetry);
%feature("autodoc", "AnalogOutPhaseInfo(HDWF hdwf, int idxChannel) -> ( double*  degreeMin, double*  degreeMax )") FDwfAnalogOutPhaseInfo;
%apply double*  OUTPUT {double*  pdegreeMin};
%apply double*  OUTPUT {double*  pdegreeMax};
DWFAPI BOOL  FDwfAnalogOutPhaseInfo(HDWF hdwf, int idxChannel, double* pdegreeMin, double* pdegreeMax);
%feature("autodoc", "AnalogOutPhaseSet(HDWF hdwf, int idxChannel, double degreePhase) -> (  )") FDwfAnalogOutPhaseSet;
DWFAPI BOOL  FDwfAnalogOutPhaseSet(HDWF hdwf, int idxChannel, double degreePhase);
%feature("autodoc", "AnalogOutPhaseGet(HDWF hdwf, int idxChannel) -> ( double*  degreePhase )") FDwfAnalogOutPhaseGet;
%apply double*  OUTPUT {double*  pdegreePhase};
DWFAPI BOOL  FDwfAnalogOutPhaseGet(HDWF hdwf, int idxChannel, double* pdegreePhase);
%feature("autodoc", "AnalogOutDataInfo(HDWF hdwf, int idxChannel) -> ( int*  nSamplesMin, int*  nSamplesMax )") FDwfAnalogOutDataInfo;
%apply int*  OUTPUT {int*  pnSamplesMin};
%apply int*  OUTPUT {int*  pnSamplesMax};
DWFAPI BOOL  FDwfAnalogOutDataInfo(HDWF hdwf, int idxChannel, int* pnSamplesMin, int* pnSamplesMax);
%feature("autodoc", "AnalogOutDataSet(HDWF hdwf, int idxChannel, double* rgdData) -> (  )") FDwfAnalogOutDataSet;
%apply (double* INPLACE_ARRAY1, int DIM1) {(double* rgdData, int cdData)};
DWFAPI BOOL  FDwfAnalogOutDataSet(HDWF hdwf, int idxChannel, double* rgdData, int cdData);
%feature("autodoc", "AnalogOutPlayStatus(HDWF hdwf, int idxChannel) -> ( int*  dDataFree, int * dDataLost, int * dDataCorrupted )") FDwfAnalogOutPlayStatus;
%apply int*  OUTPUT {int*  cdDataFree};
%apply int * OUTPUT {int * cdDataLost};
%apply int * OUTPUT {int * cdDataCorrupted};
DWFAPI BOOL  FDwfAnalogOutPlayStatus(HDWF hdwf, int idxChannel, int* cdDataFree, int *cdDataLost, int *cdDataCorrupted);
%feature("autodoc", "AnalogOutPlayData(HDWF hdwf, int idxChannel, double* rgdData) -> (  )") FDwfAnalogOutPlayData;
%apply (double* INPLACE_ARRAY1, int DIM1) {(double* rgdData, int cdData)};
DWFAPI BOOL  FDwfAnalogOutPlayData(HDWF hdwf, int idxChannel, double* rgdData, int cdData);

%feature("autodoc", "EnumAnalogInChannels(int idxDevice) -> ( int*  nChannels )") FDwfEnumAnalogInChannels;
%apply int*  OUTPUT {int*  pnChannels};
DWFAPI BOOL  FDwfEnumAnalogInChannels(int idxDevice, int* pnChannels);
%feature("autodoc", "EnumAnalogInBufferSize(int idxDevice) -> ( int*  nBufferSize )") FDwfEnumAnalogInBufferSize;
%apply int*  OUTPUT {int*  pnBufferSize};
DWFAPI BOOL  FDwfEnumAnalogInBufferSize(int idxDevice, int* pnBufferSize);
%feature("autodoc", "EnumAnalogInBits(int idxDevice) -> ( int*  nBits )") FDwfEnumAnalogInBits;
%apply int*  OUTPUT {int*  pnBits};
DWFAPI BOOL  FDwfEnumAnalogInBits(int idxDevice, int* pnBits);
%feature("autodoc", "EnumAnalogInFrequency(int idxDevice) -> ( double*  hzFrequency )") FDwfEnumAnalogInFrequency;
%apply double*  OUTPUT {double*  phzFrequency};
DWFAPI BOOL  FDwfEnumAnalogInFrequency(int idxDevice, double* phzFrequency);

#endif
