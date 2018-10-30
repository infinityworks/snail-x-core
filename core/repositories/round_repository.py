import time
from core.mappers import round_mapper
from core.source import round_source
from core.source.user_source import find_one_by_email

class RoundRepository:

    def get_is_open_round(self):
        round_id = round_source.get_open_round_id()
        if round_id:
            return True
        return False

    def get_is_inflight_round(self):
        round_id = round_source.get_inflight_round_id()
        if round_id:
            return True, round_id
        return False, 0

    def get_open_round_details(self):
        return round_source.get_open_round_details()

    def store_predictions(self, user_email, race_predictions):
        user = find_one_by_email(user_email)
        return round_source.store_predictions(user[0], race_predictions)

    def check_future_round(self):
        return round_source.get_future_round_details()

    def get_current_round_race_results(self):
        return round_source.get_snail_name_results()

    def get_closed_round_race_results(self):
        all_results = round_source.get_closed_round_results()
        return_data = []
        for race in all_results:
            raceObject = {}
            raceObject['raceID'] = race[0]
            raceObject['snailName'] = race[1]
            raceObject['trainerName'] = race[2]

            return_data.append(raceObject)

        print(return_data)
        return return_data

    def get_all_rounds_closed(self):
        return round_source.get_all_rounds_closed()
