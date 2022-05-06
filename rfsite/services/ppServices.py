from flask import render_template
from flask_login import current_user

from rfsite.models.ws_coeficient import ws_coeficient
from rfsite.models.ws_donate_code import ws_donate_code
from rfsite.models.ws_game_balance import ws_game_balance
from rfsite.models.ws_payment_history import ws_payment_history
from rfsite.models.ws_transfer_coef import ws_transfer_coef
from rfsite.models.ws_transfer_history import ws_transfer_history


def pp():
    data = ws_payment_history.query.filter_by(user_id=current_user.user_id).order_by(
        ws_payment_history.payment_id.desc()).all()
    data1 = ws_transfer_history.query.filter_by(user_id=current_user.user_id).order_by(
        ws_transfer_history.transfer_id.desc()).all()
    data2 = ws_game_balance.query.filter_by(user_id=current_user.user_id).all()
    data3 = ws_transfer_coef.query.filter_by(is_available=1).all()
    data4 = ws_donate_code.query.filter_by(username=current_user.username, is_active='T').all()
    data5 = ws_coeficient.query.filter_by(is_available=1).all()
    return render_template('personal_page.html', data=data, data1=data1, data2=data2, data3=data3, data4=data4, data5=data5)
