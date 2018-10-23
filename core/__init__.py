from flask_cors import CORS
from flask_api import FlaskAPI

# Setting up the flask end point to call data from front end to
app = FlaskAPI(__name__)
CORS(app)

from core.router import user
from core.routers.round_router import round_router

app.register_blueprint(user)
app.register_blueprint(round_router)

