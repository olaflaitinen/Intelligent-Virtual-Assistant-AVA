import unittest
from src.backend.server import app
from src.backend.database import create_table, insert_conversation

class TestBackend(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_chat_endpoint(self):
        response = self.app.post('/chat', json={'message': 'Hello'})
        self.assertEqual(response.status_code, 200)

    def test_create_table(self):
        create_table()
        self.assertTrue(True)  # Placeholder for actual database table creation test

    def test_insert_conversation(self):
        insert_conversation('Hello', 'Hi there!')
        self.assertTrue(True)  # Placeholder for actual database insertion test

if __name__ == '__main__':
    unittest.main()
