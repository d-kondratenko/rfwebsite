from flask import Flask, request, session
from flask_admin import Admin
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://rfadmin:rfadmin@localhost/rfwebsite'
app.config['SQLALCHEMY_BINDS'] = {
    'rfUsers': 'mssql+pymssql://sa:S8q64S8q64@192.168.99.112/RF_User',
    'billing': 'mssql+pymssql://sa:S8q64S8q64@192.168.99.112/Billing'
}
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "ecd90f065a52b1907c15644b6ee9e4d73ef6f8850115d6c499847ecc9cbefe75"
CORS(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
admin = Admin(app)

# "mysql:///?User=myUser&;Password=myPassword&Database=NorthWind&Server=myServer&Port=3306"
from rfsite import routes
