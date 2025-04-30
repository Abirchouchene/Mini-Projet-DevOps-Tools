import unittest
from app import create_app, db
import json

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Nothing123@db:5432/user_db'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), [])

if __name__ == '__main__':
    unittest.main()