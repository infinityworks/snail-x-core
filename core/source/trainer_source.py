from core.db.db_func import get_db


def get_trainer_name(trainer_id):
    db = get_db()
    cursor = db.cursor()

    query = "select name from trainers where trainer_id = \'" + str(trainer_id) + "\'"

    try:
        cursor.execute(query)
        db.commit()
    except db.Error as err:
        print(err)
        return False

    return cursor.fetchall()