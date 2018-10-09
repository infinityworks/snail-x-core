from .repositories.user_repository import UserRepository
from core.repositories.user_repository import UserRepository
from flask import Blueprint, request
import json

user = Blueprint('user', __name__)


# <-- End Points Below -->

@user.route("/register-user", methods=["POST"])
def register_user():
    print("in")
    form_data = request.form
    user = UserRepository()
    user.register(form_data['firstName'], form_data['lastName'], form_data['email'], form_data['password'])

    return ""
