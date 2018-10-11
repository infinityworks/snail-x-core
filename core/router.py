from core.repositories.user_repository import UserRepository
from flask import Blueprint, request
import json

user = Blueprint('user', __name__)


# <-- End Points Below -->

@user.route("/register-user", methods=["POST"])
def register_user():
    print("hello")
    form_data = json.loads(request.data)
    user_repository = UserRepository()
    user_repository.register(form_data['firstName'], form_data['lastName'], form_data['email'], form_data['password'])
    return ""

@user.route("/check-duplicate-email", methods=["POST"])
def check_duplicate_email():
    form_data = json.loads(request.data)
    user_repository = UserRepository()
    return user_repository.check_email(form_data['email'])


@user.route("/login-user", methods=["POST"])
def login():
    form_data = json.loads(request.data)
    user_repository = UserRepository()
    return json.dumps(user_repository.login(form_data['username'], form_data['password']))
