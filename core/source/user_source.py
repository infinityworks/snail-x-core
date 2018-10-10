from core.db.db_func import get_db


def set_new_user(user):
    db = get_db()
    cursor = db.cursor()

    sqlstatement = "INSERT INTO users (firstName, lastName, email, password) VALUES ('{}', '{}', '{}', '{}');"\
        .format(
            user.first_name, user.last_name, user.email, user.password
        )

    try:
        cursor.execute(sqlstatement)
        db.commit()
    except db.Error as err:
        print("Error writing to DB: {}".format(err))
        return False

    return True
