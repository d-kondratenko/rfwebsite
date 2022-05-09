import time

import schedule

from rfsite.func import payment

schedule.every(10).minutes.do(payment)

while True:
    schedule.run_pending()
    time.sleep(1)
