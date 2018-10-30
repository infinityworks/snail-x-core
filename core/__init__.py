from flask_cors import CORS
from flask_api import FlaskAPI

# Setting up the flask end point to call data from front end to
app = FlaskAPI(__name__)
CORS(app)

from core.routers import round_router, user_router, result_router

app.register_blueprint(user_router)
app.register_blueprint(round_router)
app.register_blueprint(result_router)
