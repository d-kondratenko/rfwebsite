import pyodbc as po

from rfsite import db
from rfsite.models.ws_game_account_assign import ws_game_account_assign


def create_user_rf(u_name, u_pw):
    server = 'tcp:192.168.99.112'
    database = 'RF_User'
    username = 'sa'
    password = 'S8q64S8q64'
    try:
        cnxn = po.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                      server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = cnxn.cursor()
        sql = "exec upInsert_user @id=?, @pw=?"
        params = (u_name, u_pw)
        cursor.execute(sql, params)
        cnxn.commit()
        cursor.close()
        cnxn.close()
        return True
    except Exception as e:
        print(e)
        return False


def check_username(u_name):
    server = 'tcp:192.168.99.112'
    database = 'RF_User'
    username = 'sa'
    password = 'S8q64S8q64'
    try:
        cnxn = po.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                      server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = cnxn.cursor()
        sql = "select convert(varchar(255), id) from tbl_RFTestAccount where convert(varchar(255), id) = ?"
        params = (u_name)
        cursor.execute(sql,params)
        row = cursor.fetchone()
        cnxn.commit()
        cursor.close()
        cnxn.close()
        if row is None:
            return False
        else:
            return True
    except Exception as e:
        return (e)


def get_info(u_name):
    server = 'tcp:192.168.99.112'
    database = 'BILLING'
    username = 'sa'
    password = 'S8q64S8q64'
    try:
        cnxn = po.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                          server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = cnxn.cursor()
        sql = "select * from tbl_UserStatus where id = ?"
        params = (u_name)
        cursor.execute(sql, params)
        row = cursor.fetchall()
        for serial, id, Status, PremSt, PremFi, Cash in row:
            ga = ws_game_account_assign.query.filter_by(account_name=u_name).first()
            if Status == 1:
                ga.is_premium = 'N'
            else:
                ga.is_premium = 'T'
            ga.premStart = PremSt
            ga.premFinish = PremFi
            ga.cash = Cash

            db.session.commit()

        cnxn.commit()
        cursor.close()
        cnxn.close()
    except Exception as e:
        print(e)