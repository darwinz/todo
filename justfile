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

db-start:
    docker compose up -d db

db-init:
    FLASK_APP=app.main DATABASE_URL=postgresql://postgres:postgres@localhost:5432/todo .venv/bin/flask db init

db-migrate msg="auto":
    FLASK_APP=app.main DATABASE_URL=postgresql://postgres:postgres@localhost:5432/todo .venv/bin/flask db migrate -m "{{msg}}"

db-upgrade:
    FLASK_APP=app.main DATABASE_URL=postgresql://postgres:postgres@localhost:5432/todo .venv/bin/flask db upgrade

frontend-install:
    cd frontend && npm install

frontend-dev:
    cd frontend && npm run dev

frontend-build:
    cd frontend && npm run build
