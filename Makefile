all:
	swig -c++ -python bigClass.i
	g++ -fPIC -c bigClass.cpp
	g++ -fPIC -c bNum.cpp
	g++ -fPIC -c bigClass_wrap.cxx -I/usr/include/python2.7
	g++ -shared bigClass.o bNum.o bigClass_wrap.o -o _bigClass.so

windows32:
	swig -c++ -python bigClass.i
	g++ -c bigClass.cpp
	g++ -c bNum.cpp
	g++ -c bigClass_wrap.cxx -IC:\Python27\include
	g++ bigClass.o bNum.o bigClass_wrap.o -Ic:\python27\include -Lc:\python27\libs -lpython27 -shared -o _bigClass.pyd
	del *.o *.cxx