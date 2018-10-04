from flask import Flask, render_template, request
from flask_cors import CORS
from core import app

import json
import mysql.connector


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

    sqlstatement = "INSERT INTO Users (firstName, lastName, username, email, password) VALUES ({}, {}, {}, {}, {});".format(form_data[0], form_data[1], form_data[2], form_data[3], form_data[4])
    mycursor.execute(sqlstatement)

    mydb.commit()
    return "Success"