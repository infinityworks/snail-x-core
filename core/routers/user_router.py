import json

from flask import Blueprint, request
from flask_api import status

from core.repositories.user_repository import UserRepository

user_router = Blueprint('user_router', __name__)


@user_router.route("/register-user", methods=["POST"])
def register_user():
    form_data = request.get_json()
    user_repository = UserRepository()
    success = user_repository.register(form_data['firstName'], form_data['lastName'], form_data['email'],
                                       form_data['password'])
    if success:
        return {"message": "Successfully registered the user."}, status.HTTP_201_CREATED
    else:
        return {"message": "Failed registering the user with the supplied details."}, status.HTTP_400_BAD_REQUEST


@user_router.route("/login-user", methods=["POST"])
def login():
    form_data = request.get_json()
    user_repository = UserRepository()
    account = user_repository.login(form_data['email'], form_data['password'])

    if account:
        content = {'user_email': form_data['email'],
                   'user_first_name': account[1]
                   }
        return content, status.HTTP_200_OK
    else:
        return {"message": "Invalid login details. Please try again."}, status.HTTP_401_UNAUTHORIZED


@user_router.route("/check-duplicate-email", methods=["POST"])
def check_duplicate_email():
    form_data = request.get_json()
    user_repository = UserRepository()
    is_duplicate_email = user_repository.check_is_email_duplicate(form_data['email'])
    return {"result": is_duplicate_email}, status.HTTP_200_OK


@user_router.route("/check-user-results", methods=["POST"])
def get_user_results():
    form_data = request.get_json()
    user_repository = UserRepository()
    results = user_repository.get_user_results(form_data['email'])

    if results:
        return_data = json.dumps(results)
        return return_data, status.HTTP_200_OK
    else:
        return {"message": "Error. No current round results"}, status.HTTP_204_NO_CONTENT


@user_router.route("/user-predictions", methods=["POST"])
def get_predictions():
    form_data = request.get_json()
    user_repository = UserRepository()
    predictions = user_repository.get_predictions(form_data['email'])
    if predictions:
        return_data = json.dumps(predictions)
        return return_data, status.HTTP_200_OK
    else:
        return {"message": "Error. No predictions made"}, status.HTTP_204_NO_CONTENT