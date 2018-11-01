from core.mappers.round_result_mapper import leaderboard_result_sql_to_round_leaderboard_entry
from core.source import round_result_source


def get_leaderboard_result_by_round_id(round_id):
    results = round_result_source.get_leaderboard_results_by_round_id_asc(round_id)
    entry_list = leaderboard_result_sql_to_round_leaderboard_entry(results)
    return entry_list
