def sql_datetime_to_timestamp(sql_datetime):
    return sql_datetime.strftime('%Y-%m-%d %H:%M:%S')


def leaderboard_result_sql_to_round_leaderboard_entry(sql_list):
    entry_list = []
    for (index, row) in enumerate(sql_list):
        entry_list.append([index+1, row[2], row[3], sql_datetime_to_timestamp(row[1])])
    return entry_list
