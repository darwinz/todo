install:
    python3 -m venv .venv
    .venv/bin/pip install -r requirements.txt

run:
    FLASK_APP=app.main .venv/bin/flask run

test:
    .venv/bin/python -m pytest

docker-build:
    docker build -t flask-todo .

docker-up:
    docker compose up

docker-down:
    docker compose down

docker-logs:
    docker compose logs -f
