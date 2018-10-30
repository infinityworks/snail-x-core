from flask import Blueprint, request
from flask_api import status

result_router = Blueprint('result_router', __name__)


@result_router.route("/round-results", methods=['GET'])
def get_round_results_for_id():
    form_data = request.get_json()
    round_id = form_data['round_id']
    if round_id:
        return {"message": "Success."}, status.HTTP_200_OK
    else:
        return {"message": "No round id provided to gather the results for."}, status.HTTP_400_BAD_REQUEST
