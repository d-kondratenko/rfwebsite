from sqlalchemy.dialects import mssql

from rfsite import db


class rf_useraccount(db.Model):
    __tablename__ = 'tbl_UserAccount'
    __bind_key__ = 'rfUsers'

    serial = db.Column(mssql.INTEGER, nullable=False, primary_key=True)
    id = db.Column(mssql.BINARY(length=16), nullable=False)
    createtime = db.Column(mssql.DATETIME, nullable=False)
    createip = db.Column(mssql.CHAR(length=16), nullable=False)
    lastlogintime = db.Column(mssql.DATETIME, nullable=False)
    lastlogofftime = db.Column(mssql.DATETIME, nullable=False)
    totallogmin = db.Column(mssql.INTEGER, nullable=False)
    lastconnectip = db.Column(mssql.CHAR(length=16), nullable=False)
    pushclosetime = db.Column(mssql.DATETIME, nullable=False)
    pusherip = db.Column(mssql.CHAR(length=16), nullable=False)
    JoinCode = db.Column(mssql.INTEGER, nullable=False)
    LoginFailureCnt = db.Column(mssql.TINYINT, nullable=False)
    fire_on = db.Column(mssql.SMALLDATETIME, nullable=False)
    fire_warning = db.Column(mssql.SMALLDATETIME, nullable=False)
    uilock = db.Column(mssql.TINYINT, nullable=False)
    uilock_pw = db.Column(mssql.BINARY(length=13), nullable=False)
    uilock_failcnt = db.Column(mssql.TINYINT, nullable=False)
    uilock_update = db.Column(mssql.SMALLDATETIME, nullable=False)
    uilock_hintindex = db.Column(mssql.TINYINT, nullable=False)
    uilock_hintanswer = db.Column(mssql.BINARY(length=17), nullable=False)
    uilock_find_pass_failcnt = db.Column(mssql.TINYINT, nullable=False)