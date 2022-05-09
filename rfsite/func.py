import hashlib
import string
import random  # define the random module
import smtplib
from datetime import datetime
import email
import imaplib
from rfsite.models.ws_game_balance import ws_game_balance
from rfsite.models.ws_payment_history import ws_payment_history
from rfsite.models.ws_payments import ws_payments
from rfsite.models.ws_users import ws_users
from rfsite.myconf import imap, email_user, email_password, email_from

from rfsite import db
from rfsite.models.ws_donate_code import ws_donate_code
from rfsite.myconf import email_user, email_password


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

    username = email_user
    password = email_password

    try:
        server = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465)
        server.login(username, password)
        server.sendmail(fromMy, to, msg)
        server.quit()
    except Exception as e:
        print(str(e))


def payment():
    mail = imaplib.IMAP4_SSL(imap)
    mail.login(email_user, email_password)
    mail.list()
    mail.select("inbox")

    result, data = mail.search(None, f'FROM "{email_from}"')

    ids = data[0]
    id_list = ids.split()
    if id_list:
        latest_email_id = id_list[-1]
        result, data = mail.fetch(latest_email_id, "(RFC822)")
        raw_email = data[0][1]
        e = email.message_from_bytes(raw_email)
        ep = e.get_payload()
        for c in ep:
            if c.get_content_maintype() == 'text':
                with open('pay.html', 'w') as file:
                    file.writelines(c.get_payload())

        mail.copy(latest_email_id, 'Archive')
        mail.store(latest_email_id, "+FLAGS", "\\Deleted")
        mail.expunge()
        mail.close()

        new_pay = ws_payments(email=raw_email)
        db.session.add(new_pay)
        db.session.commit()

        w = '&nbsp;&nbsp;'
        card = 0
        username = ''
        sum = 0
        with open('pay.html', 'r') as file:
            i = 0
            for line in file:
                if w in line:
                    i += 1
                    s = line.strip(' ').strip('\n')
                    start = s.find('&nbsp;&nbsp;') + 12
                    end = s.find('</')
                    value = s[start:end]
                    if value.find('&nbsp') != -1:
                        value = value[0:value.find('&nbsp')]
                    if i == 1:
                        card = value
                    elif i == 2:
                        username = value
                    elif i == 3:
                        sum = value
                    else:
                        print("Error")

        print(f'card: {card}')
        print(f'username: {username}')
        print(f'sum: {sum}')
        user = ws_users.query.filter_by(username=username.strip(' ')).first()
        new_pay = ws_payment_history(bank_pay_id=card,
                                     user_id=user.user_id,
                                     user_bill=user.user_bill,
                                     payment_sum=sum)
        gb = ws_game_balance.query.filter_by(user_id=user.user_id, project='Main').first()
        if gb is None:
            new_gb = ws_game_balance(
                project='Main',
                user_id=user.user_id,
                user_bill=user.user_bill,
                balance=sum
            )
            db.session.add(new_gb)
            db.session.commit()
        else:
            gb.balance += float(sum)
        user.budget += float(sum)
        db.session.add(new_pay)
        db.session.commit()
