import string
from random import random

from rfsite import db
from rfsite.models.ws_donate_code import ws_donate_code


def genDonateCode():
    S = 8  # number of characters in the string.
    for i in range(100):
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
        wd = ws_donate_code(
            code=ran
        )
        db.session.add(wd)
        db.session.commit()
