from .repositories.user_repository import UserRepository
from flask import Flask, render_template, request
from core import app
import json


# <-- End Points Below -->

@app.route("/register-user", methods=["POST"])
def register_user():
    form_data = json.loads(request.data)
    user = UserRepository()
    user.register(form_data['firstName'], form_data['lastName'], form_data['email'], form_data['password'])
    return ""
