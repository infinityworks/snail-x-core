from core.db.db_func import get_db
from datetime import datetime


def get_round_id():
    db = get_db()
    cursor = db.cursor()

    current_time = datetime.now()
    args = (current_time, current_time)
    query = """SELECT round.round_id 
            FROM round JOIN race ON round.round_id = race.round_id                                           
            WHERE round.start_date <= '{}' 
            AND race.race_date >= '{}'""".format(current_time, current_time)

    try:
        cursor.execute(query, args)  # inserts the current date and time in to the above SQL query
        db.commit()
    except db.Error as err:
        print(err)
        return False

    return cursor.fetchall()


def get_latest_round():
    print("db")
    db = get_db()
    cursor = db.cursor()

    query = "SELECT * FROM round ORDER BY round_id DESC LIMIT 1"

    print(cursor)

    try:
        cursor.execute(query)
        db.commit()
    except db.Error as err:
        print("AWdawdw")
        print(err)
        return False

    return cursor.findone()
