import hashlib
import string
import random  # define the random module
import smtplib
from datetime import datetime

from rfsite import db
from rfsite.models.ws_donate_code import ws_donate_code


def generateToken(username, email):
    email = hashlib.md5(email.encode())
    username = hashlib.md5(username.encode())

    result = email.hexdigest() + username.hexdigest()

    return result


def genDonateCode():
    S = 8  # number of characters in the string.
    for i in range(100):
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
        wd = ws_donate_code(
            code=ran
        )
        db.session.add(wd)
        db.session.commit()


def gen_reg_token():
    S = 8
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
    pre_token = hashlib.md5(ran.encode())
    token = pre_token.hexdigest()
    return token


def send_mail(subj, to, message_text):
    fromMy = 'ws_rf@yahoo.com'
    to = to
    subj = subj
    date = datetime.now().strftime("%d.%m.%Y")
    message_text = message_text

    msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % (fromMy, to, subj, date, message_text)

    username = str('ws_rf@yahoo.com')
    password = str('pxgxqxcbrdbumscq')

    try:
        server = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465)
        server.login(username, password)
        server.sendmail(fromMy, to, msg)
        server.quit()
    except Exception as e:
        print(str(e))
