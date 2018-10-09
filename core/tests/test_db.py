import unittest
from unittest.mock import Mock

from mock import patch
from core.db.db_func import get_db
from core.models.user import User
from core.repositories.user_repository import UserRepository
from core import app


def not_a_db_hit():
    print('I did not hit the db')


@patch("core.db.db_func.connect_to_database")
class TestUserRepo(unittest.TestCase):

    def test_register_returns_200(self, mock_connect_db):
        response = app.test_client().post('/register-user', data=dict(
            firstName="Test Name",
            lastName="Last Name",
            email="test@example.com",
            password="pass123"
        ))
        self.assertEqual(response.status_code, 200)



    @patch.object(UserRepository, 'register')
    def test_insert_db(self, mock_connect_db, mock_user_source):
        app.test_client().post('/register-user', data=dict(
            firstName="Test Name",
            lastName="Last Name",
            email="test@example.com",
            password="pass123"
        ))

        mock_connect_db.assert_called_once_with(
            "Test Name",
            "Last Name",
            "test@example.com",
            "pass123"
        )

        # self.assertEqual(expected_result, result)
