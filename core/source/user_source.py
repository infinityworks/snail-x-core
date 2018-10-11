from core.db.db_func import get_db
from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password):
    return generate_password_hash(password)

def set_new_user(user):
    db = get_db()
    cursor = db.cursor()

    hashed_password = generate_password_hash(user.password)

    sqlstatement = "INSERT INTO users (firstName, lastName, email, password) VALUES ('{}', '{}', '{}', '{}');"\
        .format(
            user.first_name, user.last_name, user.email, hashed_password
        )

    try:
        cursor.execute(sqlstatement)
        db.commit()
    except db.Error as err:
        print("Error writing to DB: {}".format(err))
        return False

    return True

def find_one_by_email(self, email):
    db = get_db()
    cursor = db.cursor(buffered=True)

    sql = "select * from users where email = \'" + email + "\'"

    print("sql: " + sql)

    cursor.execute(sql)

    db.commit()

    user = db.fetchone()


    return user