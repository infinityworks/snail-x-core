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
        self.json_data = {'firstName': 'Test Name', 'lastName': 'Last Name', 'email': 'test@example.com', 'password': 'pass123'}


    @patch.object(UserRepository, 'register')
    def test_insert_db(self, mock_connect_db, mock_user_source):
        app.test_client().post('/register-user', json=self.json_data)

        mock_connect_db.assert_called_once_with(
            "Test Name",
            "Last Name",
            "test@example.com",
            "pass123"
        )


    @patch.object(UserRepository, 'check_is_email_duplicate', return_value=True)
    def test_check_email(self, mock_connect_db, mock_user_source):
        json_email = {'email': 'test@example.com'}
        app.test_client().post('/check-duplicate-email', json=json_email)

        mock_connect_db.assert_called_once_with(
            "test@example.com"
        )

