from flask import Flask, request, session
from flask_admin import Admin
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS

from rfsite.myconf import uri_def, binds, secret_key

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = uri_def
app.config['SQLALCHEMY_BINDS'] = binds
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = secret_key
CORS(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
admin = Admin(app)

# "mysql:///?User=myUser&;Password=myPassword&Database=NorthWind&Server=myServer&Port=3306"
from rfsite import routes
