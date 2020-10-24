.PHONY: deploy
deploy:
	rm -f dist/*
	python setup.py sdist bdist_wheel
	python -m twine upload dist/*

.PHONY: test_install
test_install:
	python -m pip install --index-url https://pypi.org/simple/ --no-deps --upgrade pyprojroot

.PHONY: lint
lint:
	python -m mypy --strict pyprojroot
	python -m flake8 pyprojroot tests
	python -m black --check --diff pyprojroot tests

.PHONY: fmt
fmt:
	python -m black pyprojroot tests

.PHONY: test
test:
	python -m pytest
