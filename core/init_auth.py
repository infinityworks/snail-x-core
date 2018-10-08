from flask import Flask, render_template, request
from flask_cors import CORS
#from core import app

import json
import mysql.connector

app = Flask(__name__)

CORS(app)

class Database():

    def __init__(self):
        print('DB Init')




@app.route("/auth-user", methods=["POST"])
def auth():
    user = request.form.get("user_details")
    if user.username == "Ash" and user.password == "password":
        return True
    else:
        return False

@app.route("/register-user", methods=["POST"])
def register():
    form_data = json.loads(request.data)
    print(form_data)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysqlpasswd",
        database = "snailRacing"
    )
    mycursor = mydb.cursor()

    print(form_data['firstName'])
    sqlstatement = "INSERT INTO users (firstName, lastName, username, email, password) VALUES ('{}', '{}', '{}', '{}', '{}');".format(form_data['firstName'], form_data['lastName'], form_data['username'], form_data['email'], form_data['password'])

    print(sqlstatement)

    mycursor.execute(sqlstatement)

    mydb.commit()
    return "Success"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")


if email is in db:
    return "email already in db"