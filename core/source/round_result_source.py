from core.db.db_func import get_db
import datetime


def database_connect():
    db = get_db()
    cursor = db.cursor()
    return db, cursor


def get_leaderboard_results_by_round_id_asc(round_id):
    db, cursor = database_connect()

    query = "select @n := @n + 1 n, u.email, rr.score, rp.created " \
            " from roundResults rr, (SELECT @n := 0) m " \
            " join users u on u.user_id = rr.user_id " \
            " join racePredictions rp on rp.user_id = rr.user_id " \
            " where round_id = " + round_id + \
            " order by rr.score desc"
    try:
        cursor.execute(query)
        db.commit()
    except db.Error as err:
        print(err)
        return False

    return cursor.fetchall()
