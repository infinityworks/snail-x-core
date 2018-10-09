import flask_bcrypt
from core.models.user import User
import mysql.connector
from ..repositories import db_connection
import flask


class UserRepository:

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

        return True

    def login(self, user_email, user_password):
        user = self.find_one_by_email(user_email)

        if not user or user[3] != user_password:
            return False

        return user

    def find_one_by_email(self, email):
        db = db_connection.cursor()

        sql = "select * from users where email = {}".format(email)

        user = db.execute(sql)

        db_connection.commit()

        db_connection.close()

        return user

