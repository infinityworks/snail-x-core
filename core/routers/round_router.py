import json

from flask import Blueprint, request
from flask_api import status

from core.repositories.round_repository import RoundRepository

round_router = Blueprint('round_router', __name__)


# Returns true if an open round exists, false if not
@round_router.route("/get-active-round", methods=['GET'])
def get_active_round():
    round_repository = RoundRepository()
    round_status = round_repository.get_is_open_round()
    return {"open": round_status}, status.HTTP_200_OK


# Returns true if an inflight round exists, false if not
@round_router.route("/get-inflight-round", methods=['GET'])
def get_inflight_round():
    round_repository = RoundRepository()
    round_status = round_repository.get_is_inflight_round()
    return {"inflight": round_status}, status.HTTP_200_OK


@round_router.route("/get-open-round", methods=["GET"])
def get_open_round():
    round_repository = RoundRepository()
    round_data = round_repository.get_open_round_details()

    return json.dumps(round_data)


@round_router.route("/get-current-round-results", methods=["GET"])
def get_current_race_results():
    round_repo = RoundRepository()
    results = round_repo.get_current_round_race_results()

    if results:
        return_data = json.dumps(results)
        return return_data, status.HTTP_200_OK
    else:
        return {"message": "Error. No current round results"}, status.HTTP_204_NO_CONTENT


@round_router.route("/check-future-rounds", methods=["GET"])
def check_future_rounds():
    round_repository = RoundRepository()
    future_round_data = round_repository.check_future_round()

    return json.dumps(future_round_data)


@round_router.route("/store-predictions", methods=["POST"])
def store_predictions():
    predictions_data = request.get_json()
    predictions_repository = RoundRepository()

    success = predictions_repository.store_predictions(predictions_data['userEmail'],
                                                       predictions_data['racePredictions'])

    if success:
        return {"message": "Successfully registered predictions."}, status.HTTP_201_CREATED
    else:
        return {"message": "Failed registering the predictions."}, status.HTTP_400_BAD_REQUEST
