#!/bin/sed -f
s/c_int(\([0-9-]\+\))/\1/g
s/c_bool(\([^0-9]\+\))/\1/g
s/c_double(\([-0-9.]\+\))/\1/g
s/byref(\(\w\+\))/OUTPARA \1 = /g
s/\(\w\+\)\.value/\1/g
s/dwf\.FDwf/dwf\./g
/import sys/d
/from dwfconstants .*$/d
s/from ctypes import \*/import sys\nsys.path.append('..')\nfrom dwf import dwf/g


