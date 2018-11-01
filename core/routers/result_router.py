import json

from flask import Blueprint, request
from flask_api import status

from core.repositories import round_result_repository
from core.repositories.round_repository import RoundRepository

result_router = Blueprint('result_router', __name__)


@result_router.route("/round-results", methods=['POST'])
def get_round_results_by_name():
    form_data = request.get_json()
    round_name = form_data['round_name']
    round_repository = RoundRepository()
    if round_name:
        round_id = round_repository.find_one_by_name(round_name)
        round_results = round_result_repository.get_leaderboard_result_by_round_id(round_id)
        return json.dumps(round_results), status.HTTP_200_OK
    else:
        return {"message": "No round id provided to gather the results for."}, status.HTTP_400_BAD_REQUEST
