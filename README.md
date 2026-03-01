# Flask Todo

A full-stack task manager with a Flask-RESTful API backend and a React + Vite frontend.

## Stack

| Layer    | Technology                              |
|----------|-----------------------------------------|
| Backend  | Python 3.13, Flask 3, Flask-RESTful     |
| Database | PostgreSQL 16 (SQLAlchemy + Alembic)    |
| Frontend | React 18, Vite 6, TypeScript 5          |
| Dev      | Docker Compose, just                    |

## Quick start

### With Docker (recommended)

```bash
docker compose up
```

- UI: http://localhost:5173
- API: http://localhost:5000

### Local development

**Backend**

```bash
just install      # create .venv and install Python deps
just run          # Flask on :5000
```

**Frontend**

```bash
just frontend-install   # npm install
just frontend-dev       # Vite on :5173
```

Run both in separate terminals. The Vite dev server proxies `/tasks` to Flask, so no CORS configuration is needed locally.

## API reference

Base URL: `http://localhost:5000`

| Method | Path            | Body (JSON)                                      | Description        |
|--------|-----------------|--------------------------------------------------|--------------------|
| GET    | `/tasks`        | —                                                | List all tasks     |
| POST   | `/tasks`        | `{ "name": "...", "description": "...", "complete": false }` | Create a task |
| GET    | `/tasks/:id`    | —                                                | Get a task         |
| PUT    | `/tasks/:id`    | `{ "name": "...", "complete": true }`            | Update a task      |
| DELETE | `/tasks/:id`    | —                                                | Delete a task      |

`name` is required on POST and PUT. All other fields are optional.

**Task object**

```json
{
  "id": 1,
  "name": "Buy groceries",
  "description": null,
  "user_id": null,
  "complete": false
}
```

## Database migrations

```bash
just db-init              # initialize migrations/ (first time only)
just db-migrate msg="..."  # generate a new migration
just db-upgrade           # apply pending migrations
```

## Testing

```bash
just test
```

Tests run against an in-memory SQLite database — no running Postgres instance required.

## Project structure

```
.
├── app/
│   ├── __init__.py          # app factory, db, CORS
│   ├── main.py              # entry point
│   ├── models/
│   │   └── task.py
│   └── controllers/
│       └── task_controller.py
├── frontend/
│   ├── src/
│   │   ├── api.ts           # fetch wrapper
│   │   ├── types.ts         # Task interface
│   │   ├── App.tsx
│   │   └── components/
│   │       ├── AddTaskForm.tsx
│   │       ├── TaskList.tsx
│   │       └── TaskItem.tsx
│   ├── vite.config.ts
│   └── package.json
├── tests/
├── migrations/
├── docker-compose.yml
└── justfile
```
