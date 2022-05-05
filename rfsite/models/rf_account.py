from sqlalchemy.dialects import mssql

from rfsite import db


class rf_account(db.Model):
    __tablename__ = 'tbl_RFTestAccount'
    __bind_key__ = 'rfUsers'
    id = db.Column(mssql.BINARY(16), nullable='False', primary_key=True)
    password = db.Column(mssql.BINARY(24), nullable='False')
    BCodeTU = db.Column(db.Integer, nullable=False, default=0)
