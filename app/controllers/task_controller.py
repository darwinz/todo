from flask_restful import Resource, reqparse
from app import db
from app.models.task import Task


def _task_parser(require_name=False):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=require_name,
                        help='Name is required', location='json')
    parser.add_argument('description', type=str, location='json')
    parser.add_argument('user_id', type=int, location='json')
    parser.add_argument('complete', type=bool, location='json')
    return parser


class TaskListResource(Resource):
    def get(self):
        tasks = db.session.execute(db.select(Task)).scalars().all()
        return [t.to_dict() for t in tasks]

    def post(self):
        args = _task_parser(require_name=True).parse_args()
        task = Task(
            name=args['name'],
            description=args.get('description'),
            user_id=args.get('user_id'),
            complete=args.get('complete') or False,
        )
        db.session.add(task)
        db.session.commit()
        return task.to_dict(), 201


class TaskResource(Resource):
    def get(self, task_id):
        task = db.session.get(Task, task_id)
        if task is None:
            return {'message': 'Task not found'}, 404
        return task.to_dict()

    def put(self, task_id):
        task = db.session.get(Task, task_id)
        if task is None:
            return {'message': 'Task not found'}, 404
        args = _task_parser(require_name=True).parse_args()
        task.name = args['name']
        if args.get('description') is not None:
            task.description = args['description']
        if args.get('user_id') is not None:
            task.user_id = args['user_id']
        if args.get('complete') is not None:
            task.complete = args['complete']
        db.session.commit()
        return task.to_dict()

    def delete(self, task_id):
        task = db.session.get(Task, task_id)
        if task is None:
            return {'message': 'Task not found'}, 404
        db.session.delete(task)
        db.session.commit()
        return '', 204
