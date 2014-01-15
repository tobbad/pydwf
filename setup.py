#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup, Extension

exScripts=[('digilent_samples',["AnalogIn_Acquisition.py", "AnalogIn_Sample.py", 
                               "AnalogIn_Trigger.py", "AnalogIO_AnalogDiscovery_Power.py", 
                               "AnalogIO_AnalogDiscovery_SystemMonitor.py", 
                               "AnalogOut_Custom.py", "AnalogOutIn.py", "AnalogOut_Sine.py", 
                               "AnalogOut_Sweep.py", "AnalogOut_Sync.py", "Device_Enumeration.py", 
                               "DigitalIn_Acquisition.py", "DigitalIO.py", "DigitalOut_BinrayCounter.py"]),
         ]

setup(name = 'pydwf',
      version = "2.7.0",
      url='www.baerospace.ch',
      author = "Tobias Badertscher",
      author_email = "python@baerospace.ch",
      maintainer = "Tobias badertscher",
      maintainer_email = "python@baerospace.ch",
      description = "Python support package for WaveForm SDk of digilent",
      scripts =[],
      packages=['pydwf', ],
      package_data={'pydwf': ['_dwf.so', 'dwf.py','__init__.py']},
      ext_modules=[
          Extension('_dwf',
                    ['dwf.i', ],
                    swig_opts=['-I/usr/local/include', '-I.'],
                    include_dirs = [],
                    define_macros = [],
                    undef_macros = [],
                    library_dirs = [],
                    libraries = ['dwf'],
          )
      ]
     )