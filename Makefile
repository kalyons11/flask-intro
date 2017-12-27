default: install test

install:
	pip install -r requirements.txt
	pip install . --upgrade

test:
	nosetests -v --nocapture

deploy:
	pip install pipreqs
	pipreqs . --force

