from core.db.db_func import get_db


def get_round_id():
    db = get_db()
    cursor = db.cursor()

    query = "select round_id from round where status = 'Open'"

    try:
        cursor.execute(query)
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
