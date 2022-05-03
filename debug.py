# from flask import Flask
# from flask_admin import Admin
#
# import os
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS
#
# from rfsite.models.ws_users import ws_users
#
# app = Flask(__name__)
# CORS(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://rfadmin:rfadmin@localhost/rfwebsite'
# app.config['SQLALCHEMY_BINDS'] = {
#
# }
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# admin = Admin(app)
#
#
# class sl_test_table(db.Model):
#     __bind_key__ = 'sl'
#     id = db.Column(db.Integer(), primary_key=True)
#     code = db.Column(db.String(length=255), nullable=False)
#
#
# user = ws_users.query.all()
# for i in user:
#     print(i.username)
#
# new_q = sl_test_table.query.all()
# for f in new_q:
#     print(f.id)
#
#
# if __name__ == "__main__":
#     app.run(host="localhost", port=5000, debug=True)
