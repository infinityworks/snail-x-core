from core.db.db_func import get_db


def database_connect():
    db = get_db()
    cursor = db.cursor()
    return db, cursor


def get_leaderboard_results_by_round_id_asc(round_id):
    db, cursor = database_connect()

    query = """SELECT DISTINCT on(roundsUsers.email)roundsUsers.round_id,roundsUsers.created,roundsUsers.email,roundresult.score 
    FROM(SELECT roundsData.round_id,roundsData.created,users.email,users.user_id 
    FROM(SELECT DISTINCT round.round_id,race.race_id,racepredictions.created,racepredictions.user_id 
    FROM round JOIN race ON round.round_id=race.round_id 
    JOIN racepredictions ON race.race_id=racepredictions.race_id 
    GROUP BY race.race_id,round.round_id,racepredictions.created,racepredictions.user_id)AS roundsData 
    JOIN users ON roundsData.user_id=users.user_id)AS roundsUsers 
    JOIN roundresult ON roundsUsers.user_id=roundresult.user_id WHERE roundsUsers.round_id=""" + str(round_id)
    try:
        cursor.execute(query)
        db.commit()
    except db.Error as err:
        print(err)
        return False

    return cursor.fetchall()
