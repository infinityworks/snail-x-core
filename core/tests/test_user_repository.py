# import unittest
# from core.repositories.user_repository import UserRepository
#
# class TestUserRepo(unittest.TestCase):
#
#
#     def test_register_sql_statement(self):
#         user_repo = UserRepository()
#         expected_result = "INSERT INTO users (firstName, lastName, email, password) VALUES ('Matt', 'Twomey', 'matt.twomey@infinityworks.com', 'password');"
#
#         result = UserRepository.register('Matt', 'Twomey', 'matt.twomey@infinityworks.com', 'password')
#
#         self.assertEqual(expected_result, result)
#
#
# if __name__ == '__main__':
#     unittest.main()