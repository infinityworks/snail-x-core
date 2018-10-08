from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'random'
#db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
toolbar = DebugToolbarExtension(app)
