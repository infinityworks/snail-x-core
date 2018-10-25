from core.db.db_func import get_db


def get_snail_name(snail_id):
    db = get_db()
    cursor = db.cursor()

    query = "select name, trainer_id from snails where snail_id = \'" + str(snail_id) + "\'"

    try:
        cursor.execute(query)
        db.commit()
    except db.Error as err:
        print(err)
        return False

    return cursor.fetchall()