GCC	=	gcc
CPP	=	g++
# -g is for debugging 
CFLAGS	=	-Wall -g
INC	=
LIBS	=	-lm
LIB_DIR = pydwf

all:	dwf.i makefile
	python setup.py build_ext
	mkdir -p $(LIB_DIR)
	touch $(LIB_DIR)/__init__.py;mv  dwf.py _dwf.so $(LIB_DIR)/
	python setup.py sdist

install: all
	python setup.py install

archive: dwf.i makefile setup.py setup.cfg
	tar zcvf pydwf.tar.gz pydwf.i makefile setup.py setup.cfg numpy.i doc/* aDiscovery.py example.c dwf_handmade.i MANIFEST.in

clean:
	rm -rf dwf.py* dwf_wrap.py dwf_wrap.c _dwf.so build example pydwf.tar.gz $(LIB_DIR)

example:example.c makefile
	$(GCC) -ldwf example.c -o example