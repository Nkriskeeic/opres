.PHONY: all test  clean-pyc clean-build

all: clean-build
	python setup.py install

.PHONY test:
	python -m unittest discover -v -s tests

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean-build: clean-pyc
	rm -f -r build/
	rm -f -r dist/
	rm -f -r *.egg-info
