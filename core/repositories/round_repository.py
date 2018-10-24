import time

from core.mappers import round_mapper
from core.source import round_source
from core.source.round_source import get_open_round_details, store_predictions
from core.source.user_source import find_one_by_email
from core.source.round_source import get_future_round_details


class RoundRepository:

    def get_is_open_round(self):
        round_id = round_source.find_open_round_id()
        if round_id:
            return True
        return False

    def get_is_inflight_round(self):
        round_id = round_source.find_inflight_round_id()
        if round_id:
            return True
        return False

    def get_open_round_details(self):
        return get_open_round_details()

    def store_predictions(self, user_email, race_predictions):
        user = find_one_by_email(user_email)
        return store_predictions(user[0], race_predictions)

    def check_future_round(self):
        return get_future_round_details()
