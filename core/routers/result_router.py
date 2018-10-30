import json

from flask import Blueprint, request
from flask_api import status

from core.repositories import round_result_repository

result_router = Blueprint('result_router', __name__)


@result_router.route("/round-results", methods=['POST'])
def get_round_results_by_id():
    form_data = request.get_json()
    round_id = form_data['round_id']
    if round_id:
        round_results = round_result_repository.get_leaderboard_result_by_round_id(round_id)
        return json.dumps(round_results)
    else:
        return {"message": "No round id provided to gather the results for."}, status.HTTP_400_BAD_REQUEST
