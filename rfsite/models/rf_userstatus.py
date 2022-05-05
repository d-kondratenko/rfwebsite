from sqlalchemy.dialects import mssql

from rfsite import db


class rf_userstatus(db.Model):
    __tablename__ = 'tbl_UserStatus'
    __bind_key__ = 'billing'
    serial = db.Column(mssql.INTEGER, nullable=False)
    id = db.Column(mssql.VARCHAR(length=16), nullable=False, primary_key=True)
    Status = db.Column(mssql.INTEGER, nullable=False)
    DTStartPrem = db.Column(mssql.DATETIME, default=None)
    DTEndPrem = db.Column(mssql.DATETIME, default=None)
    Cash = db.Column(mssql.INTEGER, nullable=False)



