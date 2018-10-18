from core.db.db_func import get_db


def get_trainer_name(trainerid):
    db = get_db()
    cursor = db.cursor()

    query = "select name from trainers where trainerid = \'" + str(trainerid) + "\'"

    try:
        cursor.execute(query)
        db.commit()
    except db.Error as err:
        print(err)
        return False

    return cursor.fetchall()