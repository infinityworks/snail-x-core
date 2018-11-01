from flask import g
from core import app
import psycopg2


def get_db():
    db = getattr(g, '_database', None)

    if db is None:
        db = g._database = connect_to_database()

    return db


@app.teardown_appcontext
def teardown_db(teardown):
    db = getattr(g, '_database', None)

    if db is not None:
        db.close()


# def connect_to_database():
#     return psycopg2.connect(
#         host="ec2-23-21-147-71.compute-1.amazonaws.com",
#         user="isfktaipxvnmbp",
#         password="d3405d7dede20bc84142a6e336c8b476067decd768ac5ee13ccea55fa065b10c",
#         database="d67lulaq5muhb8"
#     )

def connect_to_database():
    return psycopg2.connect(
        host="localhost",
        user="root",
        password="psqlpass",
        database="snailRacing"
    )
