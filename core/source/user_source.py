from core.db.db_func import get_db
from werkzeug.security import generate_password_hash


def hash_password(password):
    return generate_password_hash(password)


def set_new_user(user):
    db = get_db()
    cursor = db.cursor()

    hashed_password = generate_password_hash(user.password)

    query = "INSERT INTO users (first_Name, last_Name, email, password) VALUES ('{}', '{}', '{}', '{}');".format(
            user.first_name, user.last_name, user.email, hashed_password
        )

    try:
        cursor.execute(query)
        db.commit()
    except db.Error as err:
        print("Error writing to DB: {}".format(err))
        return False

    return True


def email_is_duplicate(email):
    db = get_db()
    cursor = db.cursor()

    sql = "select * from users where email = \'" + email + "\'"

    cursor.execute(sql)

    user = cursor.fetchone()

    if user:
        return True
    else:
        return False


def find_one_by_email(email):
    db = get_db()
    cursor = db.cursor()

    query = "select * from users where email = \'" + email + "\'"

    try:
        cursor.execute(query)
        db.commit()
    except db.Error as err:
        print(err)
        return False

    return cursor.fetchone()

def get_id_by_email(email):
    db = get_db()
    cursor = db.cursor()

    query = "select * from users where email = \'" + str(email) + "\'"

    try:
        cursor.execute(query)
        db.commit()
    except db.Error as err:
        print(err)
        return False

    user_data = cursor.fetchone()

    print(user_data)


    return user_data[0]


def get_user_predictions(user_id, round_id):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT racepredictions.race_id, racepredictions.snail_id FROM racepredictions JOIN race ON racepredictions.race_id = race.race_id WHERE user_id = \'" + str(user_id) + "\' AND round_id = \'" + str(round_id[0][0]) + "\';"
    print(query)
    try:
        cursor.execute(query)
        db.commit()
    except db.Error as err:
        print(err)
        return False

    return cursor.fetchall()
