from flask import Flask
from flask_cors import CORS
from flask_api import FlaskAPI

# Setting up the flask end point to call data from front end to
app = FlaskAPI(__name__)
CORS(app)
app.debug = True

from core.router import user

app.register_blueprint(user)
