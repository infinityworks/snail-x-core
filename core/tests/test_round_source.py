# import unittest
# import psycopg2
# import unittest
# from unittest.mock import Mock
# from unittest.mock import patch, MagicMock
# from core.repositories.user_repository import UserRepository
# from core import app
# import json
# from core.repositories.round_repository import RoundRepository
# from core.source import round_source
#
# class testRoundSource(unittest.TestCase):
#
#     @patch.object('core.db.db_func.connect_to_database', MagicMock(return_value=1))
#     def test_get_round_snails(self, db_connection):
#         result = RoundRepository().get_is_open_round()
#         self.assertEqual(True, result)
