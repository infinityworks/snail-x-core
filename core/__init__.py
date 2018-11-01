from flask_cors import CORS
from flask_api import FlaskAPI

app = FlaskAPI(__name__)
CORS(app)

from core.routers.result_router import result_router
from core.routers.round_router import round_router
from core.routers.user_router import user_router
from core.routers.prediction_router import prediction_router

app.register_blueprint(user_router)
app.register_blueprint(round_router)
app.register_blueprint(result_router)
app.register_blueprint(prediction_router)
