from core.db.db_func import get_db
import datetime

def get_open_round():
    db = get_db()
    cursor = db.cursor()
    current_time = datetime.datetime.now()

    print("HELLO")

    sql = """SELECT round.roundid, round.roundname, race.raceid 
            FROM round JOIN race ON round.roundid = race.roundid 
            WHERE round.start <= %s 
            AND race.racedate >= %s"""

    # args = current_time, current_time
    args = ('2018-10-15 12:00:00', '2018-10-15 12:00:00')

    cursor.execute(sql, args)

    raceIDs = []
    first_row = cursor.fetchone()
    round_ID = first_row[0]
    round_name = first_row[1]

    for record in cursor:
        raceIDs.append(record[2])

    print("PRINTING")
    print(round_ID)
    print(round_name)
    print(raceIDs)

    return round_ID, round_name, raceIDs