from core.db.db_func import get_db
import datetime

def get_open_round():
    db = get_db()
    cursor = db.cursor()
    current_time = datetime.datetime.now()

    print("HELLO")

    sql = """SELECT round.start, round.finish, round.roundname, round.prize  FROM round
             INNER JOIN race
             ON round.roundid = race.raceid
             WHERE round.start <= %s
             GROUP BY race.raceid, round.roundid HAVING MIN(race.racedate) >= %s"""

    args = current_time, current_time

    cursor.execute(sql, args)

    round = cursor.fetchone()

    print(current_time)

    return round