import time

from core.mappers import round_mapper
from core.source import round_source


class RoundRepository:
    def find_open_round_or_future_round(self):
        latest_round = round_source.get_latest_round()

        print("3 : "+latest_round)

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
