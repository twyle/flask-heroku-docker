update:
	@pip install --upgrade pip

install:
	@pip install -r requirements.txt

install-dev: requirements-dev.txt
	@pip install -r requirements-dev.txt

run:
	@python main.py

test:
	@python -m pytest

build:
	@sudo docker build -t ${imagename}:latest .

run-docker:
	@sudo docker run --env FLASK_ENV=development -p 5000:5000 ${imagename}:latest
