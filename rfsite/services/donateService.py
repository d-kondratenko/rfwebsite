from flask import request, url_for, render_template, flash
from flask_login import current_user
from werkzeug.utils import redirect

from rfsite import db
from rfsite.forms.DonateForm import DonateForm
from rfsite.models.ws_donate_code import ws_donate_code
from rfsite.models.ws_game_balance import ws_game_balance
from rfsite.models.ws_payment_history import ws_payment_history


def donate():
    form = DonateForm()
    if request.method == 'POST':
        dc = ws_donate_code.query.filter_by(code=form.amount.data, is_active='T',
                                            username=current_user.username).first()
        if dc:
            dc.is_active = 'N'
            payment = ws_payment_history(
                user_id=current_user.user_id,
                bank_pay_id=0,
                user_bill=current_user.user_bill,
                payment_sum=float(dc.cost))
            gb = ws_game_balance.query.filter_by(user_id=current_user.user_id,
                                                 project='Main').first()
            if gb:
                gb.balance += float(dc.cost)
            else:
                gb = ws_game_balance(project='Main',
                                     user_id=current_user.user_id,
                                     user_bill=current_user.user_bill,
                                     balance=dc.cost)
                db.session.add(gb)
                db.session.commit()
            db.session.add(payment)
            db.session.commit()
            return redirect(url_for('pp_page'))
        else:
            flash("Code is not active", category='danger')
            return redirect(url_for('pp_page'))
    else:
        return render_template('donate.html', form=form)
