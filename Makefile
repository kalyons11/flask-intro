default: install test

install:
	pip install -r requirements.txt
	pip install . --upgrade

test:
	nosetests tweet_harvester/ -v --nocapture --with-doctest

deploy:
	pip install pipreqs
	pipreqs . --force

start:
	python run.py
