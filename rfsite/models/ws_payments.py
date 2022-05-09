from datetime import datetime

from sqlalchemy.dialects import mysql

from rfsite import db


class ws_payments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(mysql.LONGTEXT, nullable=False)
    date = db.Column(mysql.DATETIME, default=datetime.now())
