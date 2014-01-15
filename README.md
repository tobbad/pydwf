pydwf
=====

Swig generated python bindings for Digilent Wave forms library.

Support
-------
Currenty this module is tested and used on a debian testing 64 bit installation. If you have such a Linux distribution or a similar one it will probably work.

There is no support for Microsoft Windows, yet.

Build
-----
The library is still in an experimental state. To build the shared wrapper library just call make in the pydwf folder. This will create a pydwf subfolder where the swig generated python code and the compiled wrapper shared libraryy is put.

To build the code you need make, gcc and swig. And of course the dwf library from [digilent]: http://www.digilentinc.com/Products/Detail.cfm?NavPath=2,66,849&Prod=WAVEFORMS 

Install
-------
Just call (as root):

python setup.py install 
