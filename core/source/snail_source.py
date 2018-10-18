from core.db.db_func import get_db


def get_snail_name(snailid):
    db = get_db()
    cursor = db.cursor()

    query = "select name from snails where snailid = \'" + str(snailid) + "\'"

    try:
        cursor.execute(query)
        db.commit()
    except db.Error as err:
        print(err)
        return False

    return cursor.fetchall()