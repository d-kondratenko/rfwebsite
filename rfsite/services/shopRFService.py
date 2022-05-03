from flask import request, redirect, url_for, render_template, flash
from flask_login import current_user

from rfsite import db
from rfsite.models.ws_game_balance import ws_game_balance
from rfsite.models.ws_game_payments import ws_game_payments


def shopRFService():
    data = request.args.get('user')
    amount = ws_game_balance.query.filter_by(user_id=current_user.user_id,
                                             project='RF Online').first()
    if amount:
        pretty_budget = f'{amount.balance} RF Coin'
    else:
        pretty_budget = f'0 RF Coin'
    if request.method == 'POST':
        if request.form.get('username_prem'):
            if amount.balance - float(request.form.get('result_prem')) >= 0:
                gp = ws_game_payments(
                    user_id=current_user.user_id,
                    project='RF Online',
                    account_name=request.form.get('username_prem'),
                    payment_type='Premium',
                    value=f"{request.form.get('amount_prem')} PD",
                    Coin_cost=request.form.get('result_prem')
                )
                db.session.add(gp)
                amount.balance -= float(request.form.get('result_prem'))
                db.session.commit()
                return redirect(url_for('rfmain_page'))
            else:
                flash("Insufficient funds", category='danger')
                return render_template('rfShop.html', amount=pretty_budget, data=data)

        if request.form.get('username_cash'):
            if amount.balance - float(request.form.get('result_cash')) >= 0:
                gp = ws_game_payments(
                        user_id=current_user.user_id,
                        project='RF Online',
                        account_name=request.form.get('username_cash'),
                        payment_type='Cash',
                        value=f"{request.form.get('amount_cash')} Cash",
                        Coin_cost=request.form.get('result_cash')
                    )
                db.session.add(gp)
                amount.balance -= float(request.form.get('result_cash'))
                db.session.commit()
                return redirect(url_for('rfmain_page'))
            else:
                flash("Insufficient funds", category='danger')
                return render_template('rfShop.html', amount=pretty_budget, data=data)
    else:
        return render_template('rfShop.html', amount=pretty_budget, data=data)
