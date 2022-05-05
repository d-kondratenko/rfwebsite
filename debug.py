# # from flask import Flask
# # from flask_admin import Admin
# #
# app.config['SQLALCHEMY_BINDS'] = {
#     'rfUsers': 'mssql+pymssql://sa:S8q64S8q64@192.168.99.112/RF_User',
#     'billing': 'mssql+pymssql://sa:S8q64S8q64@192.168.99.112/Billing',
#     'ora': 'oracle://qguaradm:quantum@192.168.59.220:1521/qtest'
# }
#cx_Oracle.init_oracle_client(lib_dir=r"C:\ora\instantclient_21_3")
# # import os
# # from flask_sqlalchemy import SQLAlchemy
# # from flask_cors import CORS
# #
# # from rfsite.models.ws_users import ws_users
# #
# # app = Flask(__name__)
# # CORS(app)
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://'
# # app.config['SQLALCHEMY_BINDS'] = {
# #
# # }
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # db = SQLAlchemy(app)
# # admin = Admin(app)
# #
# #
# # class sl_test_table(db.Model):
# #     __bind_key__ = 'sl'
# #     id = db.Column(db.Integer(), primary_key=True)
# #     code = db.Column(db.String(length=255), nullable=False)
# #
# #
# # user = ws_users.query.all()
# # for i in user:
# #     print(i.username)
# #
# # new_q = sl_test_table.query.all()
# # for f in new_q:
# #     print(f.id)
# #
# #
# # if __name__ == "__main__":
# #     app.run(host="localhost", port=5000, debug=True)
# #
# #
# # str = 'qwe123QWE+'.encode('ascii')
# # hex_str = str.hex()
# # print(f'0x{hex_str.ljust(34,"0").upper()}')
# # str1 = '0x44657374726F79657200000000000000'
# # print(len(str1))
# # str2 = '0x353234343838313834000000000000000000000000000000'
# # print()
# # print(len(str2))
# # print(bytes.fromhex(str1.lstrip("0x").rstrip("0")).decode('utf-8'))
# # print(bytes.fromhex(str2.lstrip("0x").rstrip("0")).decode('utf-8'))
#
# # add prem time
# # from datetime import datetime
# # from datetime import timedelta
# #
# # from rfsite import db
# # from rfsite.models.rf_userstatus import rf_userstatus
# #
# # data = rf_userstatus.query.filter_by(id="Destroyer").first()
# #
# # print(data.DTEndPrem)
# # dtend = data.DTEndPrem.strftime("%m-%d")
# # print(dtend)
# # print(datetime.now())
# # dtnow = datetime.now().strftime("%m-%d")
# # print(dtnow)
# # if dtend != dtnow:
# #     print('No')
# # else:
# #     print('Yes')
#
# # data.DTEndPrem += timedelta(days=7)
# # db.session.commit()
#
#
# # from rfsite.models.ora_test import ora_test
# #
# # data = ora_test.query.all()
# # for i in data:
# #     print(f'{i.loadunit_nr} {i.sp_nr} {i.SHIPMENT_ID}')
# # from datetime import datetime, timedelta, date
# #
# #
# # DTStartPrem = datetime.now()
# # print(DTStartPrem)
# # now = datetime.now()
# # cur = f"2020-{now.strftime('%m-%d %H:%M:%S.%f')}"
# # print(cur)
# from datetime import datetime, date
#
# now = datetime.now()
# print(now)
# fw = now.strftime('%m-%d %H:%M:%S.%f')
# f = "2020-" + str(fw)
# print(f)
# DTStartPrem = datetime.fromisoformat(f)
# print(DTStartPrem)
