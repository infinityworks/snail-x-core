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


class TestUserRepo(unittest.TestCase):

    @patch("core.db.db_func.connect_to_database")
    @patch.object(UserRepository, "get_user_from_db", MagicMock(return_value=[(1,)]))
    @patch.object(UserRepository, "get_round_from_db", MagicMock(return_value=[(1,)]))
    @patch.object(UserRepository, "get_predictions_from_db", MagicMock(return_value=[(4, 3)]))
    @patch.object(UserRepository, "get_snail_name_from_db", MagicMock(return_value=[('Christian Snail', 1)]))
    @patch.object(UserRepository, "get_trainer_name_from_db", MagicMock(return_value=[('James',)]))
    def test_get_predictions(self, db_connection):
        result = UserRepository().get_predictions('testing@example.com')
        print(result)
        self.assertEqual([[4, 3, 'Christian Snail', [('James',)], [(1,)]]], result)
