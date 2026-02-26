from unittest import TestCase
import sqlalchemy.exc
from app import create_app, db
from app.models.task import Task


class TestTask(TestCase):
    def setUp(self):
        self.app = create_app({
            'TESTING': True,
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
        })
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    def test_default_values_after_insert(self):
        task = Task(name='Test task')
        db.session.add(task)
        db.session.commit()
        self.assertIsNotNone(task.id)
        self.assertFalse(task.complete)
        self.assertIsNone(task.description)
        self.assertIsNone(task.user_id)

    def test_to_dict_key_shape(self):
        task = Task(name='Key test', description='desc', user_id=42, complete=True)
        db.session.add(task)
        db.session.commit()
        result = task.to_dict()
        self.assertEqual(set(result.keys()), {'id', 'name', 'description', 'user_id', 'complete'})
        self.assertEqual(result['name'], 'Key test')
        self.assertEqual(result['description'], 'desc')
        self.assertEqual(result['user_id'], 42)
        self.assertTrue(result['complete'])

    def test_null_name_raises_integrity_error(self):
        task = Task(name=None)
        db.session.add(task)
        with self.assertRaises(sqlalchemy.exc.IntegrityError):
            db.session.commit()
