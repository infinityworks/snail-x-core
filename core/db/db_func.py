from flask import g
from core import app
import mysql.connector


def get_db():
    db = getattr(g, '_database', None)

    if db is None:
        db = g._database = connect_to_database()

    return db


@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)

    if db is not None:
        db.close()


def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysqlpasswd",
        database = "snailRacing"
    )