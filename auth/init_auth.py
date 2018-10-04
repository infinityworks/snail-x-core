from flask import Flask

app = Flask(__name__)

@app.route("/auth-user", methods=["POST"])
def auth():
    user = request.form.get("user_details")

    if user.username == "Ash" and user.password == "password":
        return True
    else:
        return False





if __name__ == '__main__':
    app.run()