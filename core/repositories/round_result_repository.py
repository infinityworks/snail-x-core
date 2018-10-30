from core.source import round_result_source


def get_leaderboard_result_by_round_id(round_id):
    return round_result_source.get_leaderboard_results_by_round_id_asc(round_id)

