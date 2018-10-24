import time

from core.mappers import round_mapper
from core.source import round_source
from core.source.round_source import get_open_round_details, store_predictions
from core.source.user_source import find_one_by_email
from core.source.round_source import get_future_round_details


class RoundRepository:
    def find_open_round_or_future_round(self):
        latest_round = round_source.get_latest_round()

        print("3 : " + latest_round)

        current_date = time.time()
        if latest_round:
            round = round_mapper.map_sql_round_to_round_model(latest_round)
            if not round:
                print("BIG OL ERROR")
                return False

            if round.start_date() < current_date:
                return round.start_date
            elif round.start_date > current_date and round.end_date > current_date:
                return True
        else:
            return False

    def get_open_round_details(self):
        return get_open_round_details()

    def store_predictions(self, user_email, race_predictions):
        user = find_one_by_email(user_email)
        return store_predictions(user[0], race_predictions)

    def check_future_round(self):
        return get_future_round_details()
