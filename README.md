pydwf
=====

Swig generated python bindings for Digilent Wave forms library.

Support
-------
Currenty this module is tested and used on a debian testing 64 bit machine. If you have such an installation it will probably work, otherwise - maybe your lucky.

Build
-----
The library is still in an experimental state. To build the shared wrapper library just call make in the pydwf folder. This will create a pydwf subfolder where the swig generated python code and the compiled wrapper shared libraryy is put.

To build the code you need make, gcc and swig. And of course the dwf library from digilent.

Install
-------
Just call (as root)

python setup.py install 
