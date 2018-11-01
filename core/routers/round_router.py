from flask import Blueprint
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
    round_status, round_id = round_repository.get_is_inflight_round()
    return {"inflight": round_status, "round_id": round_id}, status.HTTP_200_OK