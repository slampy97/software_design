test:
	cd tests
	python -m unittest test.py
	cd ..

all: test

