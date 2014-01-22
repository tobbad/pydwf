pydwf
=====

Swig generated python bindings for Digilent Wave forms library.

| Directory   | Description                                                                                       |
| ------------|:--------------------------------------------------------------------------------------------------|
| [examples]  | A short module with some examples how to use the library.                                         |
| [tools]     | Different helper (badly documented) helperscripts.                                                |
| [test]      | Python scripts which call every generated function (Most of the tests is generated).              |


Support
-------
Currenty this module is tested and used on a debian testing 64 bit installation. If you have such a Linux distribution or a similar one it will probably work.

There is no support for Microsoft Windows, yet.

Build
-----
The library is still in an experimental state. To build the shared wrapper library just call make in the pydwf folder. This will create a pydwf subfolder where the swig generated python code and the compiled wrapper shared libraryy is put.

To build the code you need make, gcc and swig. And of course the WaveForms SDK from [digilent] already installed on your system. The dwf.i file in this repo is generated against Version 2.7.0 of the Digilent Waveforms SDK.

Install
-------
Just call (as root):

make install 

Usage
-----
To use this python wrapper install the module as described above. To use the module in Python import it:
<pre>
from pydef import dwf
</pre>
All the function available in the WaveForms SDK Reference Manual are available in the python wrapper. However there are some changes to pyhonize the usage:

1. Drop any FDwf from any function call: The call to FDwfGetLastError becomes dwf.GetLastError
2. The error code returned by the C-Function will raise an python exception with a text description obtained by the FDwfGetLastErrorMsg function.
3. Any variables given as reference to the C-Function to be modified is returned in the python module as new instance of python datatype: Eg. a call :<pre>FDwfDeviceOpen(idxDevice, &hdwf)</pre> becomes <pre> hdwf = dwf.FDwfDeviceOpen(idxDevice)</pre>
4. There are some exceptions to the last rule: If the input parameter is an array of defined size eg. functions <pre>FDwfEnumDeviceName</pre> or <pre>FDwfEnumUserName</pre> are returned in the passed variable.
5. Further the C-functions <pre>FDwfAnalogInStatusData</pre> should be used with numpy-Float data array. A size need not be given as the wrapper knows the size of the Numpy array. See the AcquireAnalog function in the aDiscovery.py example script.
6. The <pre>FDwfDigitalInStatusData</pre> should be used with a uint16 numpy array. See AcquireDigital function in the aDiscovery.py example script.
7. Any C-constants are used with the same name as in the manual. Eg. the C-Enum <pre>trigsrcPC</pre> becomes <pre>dwf.trigsrcPC</pre>



[examples]: https://github.com/tobbad/pydwf/tree/master/examples
[tools]: https://github.com/tobbad/pydwf/tree/master/tools
[test]: https://github.com/tobbad/pydwf/tree/master/test
[waveforms]: http://www.digilentinc.com/Products/Detail.cfm?NavPath=2,66,849&Prod=WAVEFORMS
[digilent]: http://www.digilentinc.com/

