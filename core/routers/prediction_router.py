import json

from flask import Blueprint, request
from flask_api import status

from core.repositories.round_repository import RoundRepository
from core.repositories.user_repository import UserRepository

prediction_router = Blueprint('prediction_router', __name__)


@prediction_router.route("/store-predictions", methods=["POST"])
def store_predictions():
    predictions_data = request.get_json()
    predictions_repository = RoundRepository()

    success = predictions_repository.store_predictions(predictions_data['userEmail'],
                                                       predictions_data['racePredictions'])

    if success:
        return {"message": "Successfully registered predictions."}, status.HTTP_201_CREATED
    else:
        return {"message": "Failed registering the predictions."}, status.HTTP_400_BAD_REQUEST


@prediction_router.route("/user-predictions", methods=["POST"])
def get_predictions():
    form_data = request.get_json()
    user_repository = UserRepository()
    predictions = user_repository.get_predictions(form_data['email'])
    if predictions:
        return_data = json.dumps(predictions)
        return return_data, status.HTTP_200_OK
    else:
        return {"message": "Error. No predictions made"}, status.HTTP_204_NO_CONTENT
