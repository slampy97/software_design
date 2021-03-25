test:
	cd tests
	python -m unittest tests/test.py
	cd ..

all: test

