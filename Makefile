default: install test

install:
	pip install -r requirements.txt
	pip install . --upgrade

test:
	nosetests --with-doctest

deploy:
	pip install pipreqs
	pipreqs . --force

