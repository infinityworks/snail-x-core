import unittest
from unittest.mock import Mock
from unittest.mock import patch, MagicMock
from core.db.db_func import get_db
from core.source.trainer_source import get_trainer_name
from core.source.snail_source import get_snail_name
from core.models.user import User
from core.repositories.user_repository import UserRepository
from core.source.user_source import get_user_predictions
from core import app
import json

@patch("core.db.db_func.connect_to_database")
class TestUserRepo(unittest.TestCase):

    def setUp(self):
        self.json_data = {'firstName': 'Test Name', 'lastName': 'Last Name', 'email': 'test@example.com', 'password': 'pass123'}


    @patch.object(UserRepository, "get_user_from_db", MagicMock(return_value=[(1,)]))
    @patch.object(UserRepository, "get_round_from_db", MagicMock(return_value=[(1,)]))
    @patch.object(UserRepository, "get_predictions_from_db", MagicMock(return_value=[(4, 3)]))
    @patch.object(UserRepository, "get_snail_name_from_db", MagicMock(return_value=[('Christian Snail', 1)]))
    @patch.object(UserRepository, "get_trainer_name_from_db", MagicMock(return_value=[('James',)]))
    def test_get_predictions(self, db_connection):
        result = UserRepository().get_predictions('testing@example.com')
        self.assertEqual([[4, 3, 'Christian Snail', [('James',)], [(1,)]]], result)

    @patch.object(UserRepository, 'login', return_value="(1, 'Test Name', 'Last Name', 'pbkdf2:sha256:50000$sXuJhpWy$569630f45ba40bea280aa7a96d64978856b581c5691197faca623fdeb7570f77', 'test@example.com')")
    def test_valid_login(self, mock_connect_db, mock_user_source):
        response = app.test_client().post('/login-user', json=self.json_data)

        self.assertEqual(response.status_code, 200)

    @patch.object(UserRepository, 'login', return_value=False)
    def test_invalid_login(self, mock_connect_db, mock_user_source):
        response = app.test_client().post('/login-user', json=self.json_data)

        self.assertEqual(response.status_code, 401)

    @patch.object(UserRepository, 'get_predictions', return_value="[[1, 1, 'Shelly Brooks', [('Ash',)], 4]]")
    def test_getting_user_predictions_when_in_db(self, mock_connect_db, mock_user_source):
        response = app.test_client().post('/user-predictions', json=self.json_data)
        response = response.data

        self.assertEqual("[[1, 1, 'Shelly Brooks', [('Ash',)], 4]]", json.loads(response))

    @patch.object(UserRepository, 'get_predictions', return_value=[])
    def test_getting_user_predictions_when_not_in_db(self, mock_connect_db, mock_user_source):
        response = app.test_client().post('/user-predictions', json={"email": "fake@email.com"})
        response = response.data

        self.assertEqual({'message': 'Error. No predictions made'}, json.loads(response))