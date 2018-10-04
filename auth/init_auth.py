from flask import Flask, render_template, request
from flask_cors import CORS

import json

app = Flask(__name__)
CORS(app)


@app.route("/auth-user", methods=["POST"])
def auth():
    user = request.form.get("user_details")
    if user.username == "Ash" and user.password == "password":
        return True
    else:
        return False

@app.route("/register-user", methods=["POST"])
def register():
    print("WOOOOOOOOO")
    return "200 OK"



def application(environ, start_response):
  if environ['REQUEST_METHOD'] == 'OPTIONS':
    start_response(
      '200 OK',
      [
        ('Content-Type', 'application/json'),
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Headers', 'Authorization, Content-Type'),
        ('Access-Control-Allow-Methods', 'POST'),
      ]
    )
    return ''



if __name__ == '__main__':
    app.run(debug=True)