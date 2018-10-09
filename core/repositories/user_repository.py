import flask_bcrypt
from core.models.user import User
import mysql.connector
from ..repositories import db_connection
import flask


class UserRepository():

    def __init__(self, db_connection):
        self.db = db_connection.cursor()

    def register(self, first_name, last_name, email, password):
        user = User(first_name, last_name, email, password)

        sqlstatement = "INSERT INTO users (firstName, lastName, email, password) VALUES ('{}', '{}', '{}', '{}');".format(
            user.first_name, user.last_name, user.email, user.password)

        return sqlstatement