#!/bin/bash

files=( "AnalogOutIn.py" "AnalogOut_Sine.py" "AnalogOut_Sweep.py" "AnalogOut_Sync.py" "Device_Enumeration.py" "DigitalIn_Acquisition.py" "DigitalIO.py" "DigitalOut_BinrayCounter.py" )
srcFolder='/usr/local/share/digilent/waveforms/samples/py/'
for f in ${files[*]}
do
    echo "def ${f%.py}():" > $f
    ./translate.sed $srcFolder$f >> $f
    echo "if __name__ == '__main__':"  >> $f
    echo "    ${f%.py}()"  >> $f
done
