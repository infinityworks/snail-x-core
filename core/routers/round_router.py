from flask import Blueprint
from flask_api import status

from core.repositories.round_repository import RoundRepository

round_router = Blueprint('round_router', __name__)


@round_router.route("/get-active-round", methods=['GET'])
def get_active_round():
    print("in")
    round_repository = RoundRepository()
    round_status = round_repository.find_open_round_or_future_round()
    return {"active_round": round_status}, status.HTTP_200_OK
