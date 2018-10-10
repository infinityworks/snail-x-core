from core.models.user import User
from core.source.user_source import set_new_user


class UserRepository():
    def register(self, first_name, last_name, email, password):
        user = User(first_name, last_name, email, password)
        return set_new_user(user)
