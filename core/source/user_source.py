from core.db.db_func import get_db
from werkzeug.security import generate_password_hash


def hash_password(password):
    return generate_password_hash(password)


def set_new_user(user):
    db = get_db()
    cursor = db.cursor()

    hashed_password = generate_password_hash(user.password)

    query = "INSERT INTO users (first_name, last_name, email, password) VALUES ('{}', '{}', '{}', '{}');".format(
        user.first_name, user.last_name, user.email, hashed_password
    )

    try:
        cursor.execute(query)
        db.commit()
    except db.Error as err:
        print("Error writing to DB: {}".format(err))
        return False

    return True


def check_is_email_duplicate(email):
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

    query = "SELECT * FROM users WHERE email = \'" + str(email) + "\'"

    try:
        cursor.execute(query)
        db.commit()
    except db.Error as err:
        print(err)
        return False

    user_data = cursor.fetchone()

    if user_data:
        return user_data[0]
    else:
        return "User Not In Database"


def get_user_predictions(user_id, round_id):
    db = get_db()
    cursor = db.cursor()


    query = "SELECT racepredictions.race_id, " \
            "       racepredictions.snail_id " \
            "FROM racepredictions " \
            "JOIN race ON racepredictions.race_id = race.race_id " \
            "WHERE user_id = \'" + str(user_id) + "\' AND round_id = \'" + str(round_id) + "\';"


    try:
        cursor.execute(query)
        db.commit()
    except db.Error as err:
        print(err)
        return False

    return cursor.fetchall()


def get_user_predictions_and_results(user_id, round_id):
    db = get_db()
    cursor = db.cursor()

    args = (user_id, round_id)

    query = """SELECT round.round_id, 
                        racepredictions.race_id, 
                        racepredictions.user_id, 
                        racepredictions.snail_id, 
                        snails.name AS predicted_winner, 
                        raceresult.position AS finishing_position, 
                        winningResult.snail_id AS winning_snail, 
                        winnerSnails.name AS winner_name, trainers.name 
                FROM racepredictions 
                JOIN snails ON racepredictions.snail_id = snails.snail_id 
                LEFT JOIN raceresult ON raceresult.race_id = racepredictions.race_id AND raceresult.snail_id = snails.snail_id 
                LEFT JOIN (SELECT * 
                            FROM raceresult 
                            WHERE position = 1) AS winningResult ON racepredictions.race_id = winningResult.race_id 
                LEFT JOIN snails AS winnerSnails ON winningResult.snail_id = winnerSnails.snail_id 
                JOIN race ON racepredictions.race_id = race.race_id 
                JOIN round ON round.round_id = race.round_id 
                LEFT JOIN trainers ON winnerSnails.snail_id = trainers.trainer_id
                WHERE racepredictions.user_id = %s AND round.round_id = %s
                ORDER BY racepredictions.race_id;"""

    try:
        cursor.execute(query, args)
        db.commit()
    except db.Error as err:
        print(err)
        return False

    return cursor.fetchall()
