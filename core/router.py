from core.repositories.user_repository import UserRepository
from core.repositories.user_repository import RoundRepository
from flask import Blueprint, request
from flask_api import status
import json

user = Blueprint('user', __name__)


# <-- End Points Below -->

@user.route("/register-user", methods=["POST"])
def register_user():
    form_data = request.get_json()
    user_repository = UserRepository()
    success = user_repository.register(form_data['firstName'], form_data['lastName'], form_data['email'],
                                       form_data['password'])
    if success:
        return {"message": "Successfully registered the user."}, status.HTTP_201_CREATED
    else:
        return {"message": "Failed registering the user with the supplied details."}, status.HTTP_400_BAD_REQUEST


@user.route("/check-duplicate-email", methods=["POST"])
def check_duplicate_email():
    form_data = request.get_json()
    user_repository = UserRepository()
    return {"result": user_repository.check_email(form_data['email'])}, status.HTTP_200_OK


@user.route("/login-user", methods=["POST"])
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


@user.route("/user-predictions", methods=["POST"])
def get_predictions():
    form_data = request.get_json()
    user_repository = UserRepository()
    predictions = user_repository.get_predictions(form_data['email'])

    if predictions:
        print(predictions)
        return_data = json.dumps(predictions)
        print(return_data)
        return return_data, status.HTTP_200_OK
    else:
        return {"message": "Error. No predictions made"}, status.HTTP_204_NO_CONTENT

@user.route("/get-current-round-results", methods=["GET"])
def get_current_race_results():
    results = get_current_round_race_results()
    print(results)

    if results:
        return_data = json.dumps(results)
        return return_data, status.HTTP_200_OK
    else:
        return {"message": "Error. No current round results"}, status.HTTP_204_NO_CONTENT