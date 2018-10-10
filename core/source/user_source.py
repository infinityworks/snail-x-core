from core.db.db_func import get_db


def set_new_user(user):
    db = get_db()
    cursor = db.cursor()

    query = "INSERT INTO users (firstName, lastName, email, password) VALUES ('{}', '{}', '{}', '{}');"\
        .format(
            user.first_name, user.last_name, user.email, user.password
        )

    try:
        cursor.execute(query)
        db.commit()
    except db.Error as err:
        print("Error writing to DB: {}".format(err))
        return False

    return True


def find_one_by_email(email):
    db = get_db()
    cursor = db.cursor(buffered=True)

    query = "select * from users where email = \'" + email + "\'"

    try:
        cursor.execute(query)
        db.commit()
    except db.Error as err:
        print(err)
        return False

    return db.fetchone()
