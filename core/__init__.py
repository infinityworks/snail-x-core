from flask import Flask
from flask_cors import CORS

# Setting up the flask end point to call data from front end to
app = Flask(__name__)
CORS(app)
app.debug = True

from core.router import user

app.register_blueprint(user)
