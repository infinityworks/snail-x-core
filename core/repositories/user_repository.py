from core.models.user import User
from core.source.user_source import set_new_user, find_one_by_email
from werkzeug.security import check_password_hash


class UserRepository:

    def register(self, first_name, last_name, email, password):
        user = User(first_name, last_name, email, password)
        return set_new_user(user)

    def login(self, user_email, user_password):
        user = find_one_by_email(user_email)

        if not user or not check_password_hash(user[3], user_password):
            return False

        return user
