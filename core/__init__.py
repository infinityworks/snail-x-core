from flask import Flask
from flask_cors import CORS
from .repositories.user_repository import UserRepository

# Setting up the flask end point to call data from front end to
app = Flask(__name__)
CORS(app)
app.debug = True
