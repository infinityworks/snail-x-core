from .repositories.user_repository import UserRepository
from flask import Flask, render_template, request
from core import app
import json


# <-- End Points Below -->

@app.route("/register-user", methods=["POST"])
def register_user():
    form_data = json.loads(request.data)
    user_repository = UserRepository()
    user_repository.register(form_data['firstName'], form_data['lastName'], form_data['email'], form_data['password'])
    return ""


@app.route("/login-user", methods=["POST"])
def login():
    form_data = json.loads(request.data)
    user_repository = UserRepository()
    return user_repository.login(form_data['email'], form_data['password'])
