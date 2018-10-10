from core.repositories.user_repository import UserRepository
from flask import Blueprint, request
from flask_api import status

user = Blueprint('user', __name__)


# <-- End Points Below -->

@user.route("/register-user", methods=["POST"])
def register_user():
    form_data = request.form
    user_repository = UserRepository()
    success = user_repository.register(form_data['firstName'], form_data['lastName'], form_data['email'], form_data['password'])
    if success:
        return {"message": "Successfully registered the user."}, status.HTTP_201_CREATED
    else:
        return {"message": "Failed registering the user with the supplied details."}, status.HTTP_400_BAD_REQUEST


@user.route("/login-user", methods=["POST"])
def login():
    form_data = request.get_json()
    user_repository = UserRepository()
    account = user_repository.login(form_data['username'], form_data['password'])
    if account:
        return form_data['username']
    else:
        return {"message": "Invalid login details. Please try again."}, status.HTTP_401_UNAUTHORIZED
