import time

from core.models.round import Round


def map_sql_round_to_round_model(round_sql):

    id = round_sql[0]
    name = round_sql[1]

    try:
        start_date = time.strptime(round_sql[2])
        finish_date = time.strptime(round_sql[3])
    except AttributeError:
        start_date = None
        finish_date = None
        pass

    if not start_date and not finish_date:
        return None
    else:
        return Round(id, name, start_date, finish_date)
