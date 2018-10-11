from core.models.user import User
from core.source.user_source import set_new_user, find_one_by_email, email_is_duplicate


class UserRepository:

    def register(self, first_name, last_name, email, password):
        user = User(first_name, last_name, email, password)
        return set_new_user(user)

    def check_email(self, email):
        return email_is_duplicate(email)

    def login(self, user_email, user_password):
        user = find_one_by_email(user_email)

        if not user or user[3] != user_password:
            return False

        return user_email
