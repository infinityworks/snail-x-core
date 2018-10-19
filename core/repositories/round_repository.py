from core.source.round_source import get_open_round_details, store_predictions
from core.source.user_source import find_one_by_email

class RoundRepository:

    def get_open_round_details(self):
        return get_open_round_details()


    def store_predictions(self, user_email, race_predictions):
        user = find_one_by_email(user_email)
        print(user[0])
        return store_predictions(user[0], race_predictions)