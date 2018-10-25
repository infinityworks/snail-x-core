from core.source.round_source import get_snail_name_results
from core.source.round_source import get_open_round_details, store_predictions
from core.source.user_source import find_one_by_email
from core.source.round_source import get_future_round_details, get_snail_name_results

class RoundRepository:

    def get_open_round_details(self):
        return get_open_round_details()

    def store_predictions(self, user_email, race_predictions):
        user = find_one_by_email(user_email)
        return store_predictions(user[0], race_predictions)

    def check_future_round(self):
        return get_future_round_details()

    def get_current_round_race_results(self):
        return get_snail_name_results()
