# import datetime
# from datetime import date
#
# from rfsite import db
# from rfsite.model import ws_payment_history, ws_users
# import schedule
# import time
# import monobank
#
# # mb_token = 'u4IBNVAvb5Dsy-6Vhv-a3LUdU8BETnjhRtKzppXWaxeg'
# #
# # mono = monobank.Client(mb_token)
# # #client = mono.get_client_info()
# # #print(client)
# # user_id = "5Jz8ws7qLgIdEMdwYewR4Q"
# # cur_date = datetime.datetime.now()
# # c = mono.make_request(method="GET",path="/personal/client-info")
# # print(c)
# # print(cur_date)
# # us = mono.get_statements(0, date(2022,4,21), date(2022,4,23))
# # #print(us)
# # if us:
# #     for i in us:
# #         print(i)
#
# #ls_date = 1650693972 # get time from get_statements['time']
# # ls_date = datetime.datetime.now().strftime("%Y%m%d")
# # print(ls_date)
# # timestamp = datetime.datetime.fromtimestamp(ls_date) #int2date
# # print(timestamp)
# # datetime object containing current date and time
# # now = datetime.datetime.now()
# #
# # print("now =", now)
# #
# # # dd/mm/YY H:M:S
# # dt_string =
# # print("date and time =", dt_string)
#
#
#
#
# # def check_payments_status():
# #     pays = ws_payment_history.query.filter_by(payment_status='Success').all()
# #     if pays:
# #         for pay in pays:
# #             user = ws_users.query.filter_by(user_id=pay.user_id).first()
# #             user.budget += int(pay.payment_sum)
# #             pay.payment_status = "Processed"
# #             db.session.commit()
# #
# #
# # schedule.every(5).seconds.do(check_payments_status)
# #
# # while True:
# #     schedule.run_pending()
# #     time.sleep(1)
