import unittest
from unittest.mock import Mock
from mock import patch
# from core.db.db_func import get_db
# from core.models.user import User
from core.repositories.user_repository import UserRepository
from core import app
import json


def not_a_db_hit():
    print('I did not hit the db')


@patch("core.db.db_func.connect_to_database")
class TestUserRepo(unittest.TestCase):

    def setUp(self):
        data = {}
        data['firstName'] = 'Test Name'
        data['lastName'] = 'Last Name'
        data['email'] = 'test@example.com'
        data['password'] = 'pass123'
        self.json_data = json.dumps(data)


    def test_register_returns_200(self, mock_connect_db):
        response = app.test_client().post('/register-user', data=self.json_data)
        self.assertEqual(response.status_code, 200)

    def test_login_returns_200(self, mock_connect_db):
        response = app.test_client().post('/login-user', data=dict(
            email="test@example.com",
            password="pass123"
        ))

        self.assertEqual(response.status_code, 200)

    @patch.object(UserRepository, 'register')
    def test_insert_db(self, mock_connect_db, mock_user_source):
        app.test_client().post('/register-user', data=self.json_data)

        mock_connect_db.assert_called_once_with(
            "Test Name",
            "Last Name",
            "test@example.com",
            "pass123"
        )


    @patch.object(UserRepository, 'check_email', return_value=True)
    def test_insert_db(self, mock_connect_db, mock_user_source):
        json_email = {'email': 'test@example.com'}
        internal_data = json.dumps(json_email)
        app.test_client().post('/check-duplicate-email', data=internal_data)

        mock_connect_db.assert_called_once_with(
            "test@example.com"
        )

