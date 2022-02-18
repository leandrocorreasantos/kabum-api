DOCKER_CMD=docker exec -it kabum-api

build:
	docker-compose up -d

upgrade-pip:
	[ -f .env ] || cp .env.sample .env
	${DOCKER_CMD} pip install --upgrade pip

setup: upgrade-pip
	${DOCKER_CMD} pip install -r requirements-local.txt

flake8:
	${DOCKER_CMD} flake8 --exclude=venv,tests .

bash:
	${DOCKER_CMD} sh

start:
	${DOCKER_CMD} python api/app.py

test:
	${DOCKER_CMD} pytest tests
