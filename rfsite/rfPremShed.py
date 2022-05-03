import time

import schedule

from rfsite.models.ws_game_account_assign import ws_game_account_assign
from rfsite.rfo import get_info


def check_prem_shed():
    all_user = ws_game_account_assign.query.all()
    for i in all_user:
        get_info(i.account_name)


schedule.every(5).minutes.do(check_prem_shed)

while True:
    schedule.run_pending()
    time.sleep(1)
