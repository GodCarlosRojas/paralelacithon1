all:
	python3 setup.py build_ext --inplace
	
clean:
	rm -rfbuild *.so *.c *.pyc
