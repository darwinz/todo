import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

db = SQLAlchemy()
migrate = Migrate()


def create_app(config=None):
    app = Flask(__name__)
    app.config.setdefault(
        'SQLALCHEMY_DATABASE_URI',
        os.environ.get('DATABASE_URL', 'postgresql://postgres:postgres@db:5432/todo')
    )
    app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)

    if config:
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    # Deferred import prevents circular import (model imports db from here)
    from app.controllers.task_controller import TaskListResource, TaskResource
    api = Api(app)
    api.add_resource(TaskListResource, '/tasks')
    api.add_resource(TaskResource, '/tasks/<int:task_id>')

    return app
