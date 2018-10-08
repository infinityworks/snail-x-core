import flask_bcrypt
from core.models.user import User
import mysql.connector
from ..repositories import db_connection


class UserRepository():

    def register(self, first_name, last_name, email, password):
        user = User(first_name, last_name, email, password)

        db = db_connection.cursor()

        #user.password = bcrypt.generate_password_hash(password)

        sqlstatement = "INSERT INTO users (firstName, lastName, email, password) VALUES ('{}', '{}', '{}', '{}');".format(
            user.first_name, user.last_name, user.email, user.password)

        print(sqlstatement)

        db.execute(sqlstatement)

        db_connection.commit()

        db_connection.close()


if __name__ == '__main__':
    test = UserRepository()
    test.register("Mike", "Winker", "Winker@winky.com", "bjdjhfhhf")


