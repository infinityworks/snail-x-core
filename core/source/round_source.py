from core.db.db_func import get_db
import datetime

def get_open_round():
    db = get_db()
    cursor = db.cursor()
    current_time = datetime.datetime.now()

    sql = """SELECT * FROM round
             INNER JOIN (SELECT * FROM races ORDER BY starttime ASC) AS racesData
             ON round.ID = racesData.ID
             WHERE round.start <= [current_datetime] AND race.raceDate >= [current_datetime]"""

    cursor.execute(sql)

    round = cursor.fetchone()

    return round