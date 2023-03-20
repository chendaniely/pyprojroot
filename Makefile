.PHONY: deploy
deploy:
	rm -f dist/*
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload dist/*

.PHONY: test_install
test_install:
	python3 -m pip install --index-url https://pypi.org/simple/ --no-deps --upgrade pyprojroot

.PHONY: lint
lint:
	python3 -m mypy --strict src/pyprojroot
	python3 -m flake8 src/pyprojroot tests
	python3 -m black --check --diff src/pyprojroot tests

.PHONY: fmt
fmt:
	python3 -m black src/pyprojroot tests

.PHONY: test
test:
	PYTHONPATH=src python3 -m pytest
