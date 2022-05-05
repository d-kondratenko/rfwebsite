from datetime import datetime, timedelta, date

from flask import request, redirect, url_for, render_template, flash
from flask_login import current_user

from rfsite import db
from rfsite.models.rf_useraccount import rf_useraccount
from rfsite.models.rf_userstatus import rf_userstatus
from rfsite.models.ws_game_account_assign import ws_game_account_assign
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
                u_id = request.form.get('username_prem')
                gacc = ws_game_account_assign.query.filter_by(account_name=u_id).first()
                acc = rf_userstatus.query.filter_by(id=u_id).first()
                if acc is None:
                    serial = rf_useraccount.query.filter_by(id=u_id.encode('utf-8'))
                    new_userstatus = rf_userstatus(
                        serial=serial.serial,
                        id=request.form.get('username_prem'),
                        Status=2,
                        Cash=0
                    )
                    db.session.add(new_userstatus)
                    db.session.commit()
                if acc.Status == 1:
                    acc.Status = 2
                    gacc.is_premium = 'T'

                dtnow = datetime.now().strftime("%m-%d")
                dtend = acc.DTEndPrem.strftime("%m-%d")
                dtstart = acc.DTStartPrem.strftime("%m-%d")
                if dtend != dtnow:
                    acc.DTEndPrem += timedelta(days=int(request.form.get('amount_prem')))
                    gacc.premFinish += timedelta(days=int(request.form.get('amount_prem')))
                if dtstart != dtnow:
                    now = datetime.now()
                    fw = now.strftime('%m-%d %H:%M:%S.%f')
                    f = "2020-" + str(fw)
                    acc.DTStartPrem = datetime.fromisoformat(f)
                    gacc.premStart = datetime.fromisoformat(f)

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
                u_id = request.form.get('username_cash')
                gacc = ws_game_account_assign.query.filter_by(account_name=u_id).first()
                acc = rf_userstatus.query.filter_by(id=u_id).first()
                if acc is None:
                    serial = rf_useraccount.query.filter_by(id=u_id.encode('utf-8'))
                    new_userstatus = rf_userstatus(
                        serial=serial.serial,
                        id=request.form.get('username_cash'),
                        Status=1,
                        Cash=0
                    )
                    db.session.add(new_userstatus)
                    db.session.commit()

                acc.Cash += int(request.form.get('amount_cash'))
                gacc.cash += int(request.form.get('amount_cash'))
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
