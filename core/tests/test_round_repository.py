import unittest
from core.source.user_source import hash_password
import psycopg2
#
class TestUserRepo(unittest.TestCase):


     def test_register_sql_statement(self):
         result = len(hash_password("aaa"))
         self.assertEqual(93, result)

