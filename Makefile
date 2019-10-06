deploy:
	rm -f dist/*
	python setup.py sdist bdist_wheel
	python -m twine upload dist/*

test_install:
	python -m pip install --index-url https://pypi.org/simple/ --no-deps --upgrade pyprojroot

