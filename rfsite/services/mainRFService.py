from flask import render_template, flash
from flask_login import current_user

from rfsite import rfo, db
from rfsite.forms.createGameUserForm import createGameUserForm
from rfsite.models.rf_account import rf_account
from rfsite.models.rf_userstatus import rf_userstatus
from rfsite.models.ws_game_account_assign import ws_game_account_assign
from rfsite.models.ws_game_balance import ws_game_balance
from rfsite.models.ws_projects import ws_projects


def mainRFService():
    form = createGameUserForm()
    get_pi = ws_projects.query.filter_by(project_abbrev='rf').first()
    ga = ws_game_account_assign.query.filter_by(user_id=current_user.user_id, project_id=get_pi.project_id).all()
    ga_count = ws_game_account_assign.query.filter_by(user_id=current_user.user_id, project_id=get_pi.project_id).count()
    amount = ws_game_balance.query.filter_by(user_id=current_user.user_id,
                                             project='RF Online').first()
    if amount:
        pretty_budget = f'{amount.balance} RF Coin'
    else:
        pretty_budget = f'0 RF Coin'
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        tb_username = username.encode('utf-8')
        tb_password = password.encode('utf-8')
        user = rf_account.query.filter_by(id=tb_username).first()
        if user in None:
            new_user = rf_account(
                id=tb_username,
                password=tb_password,
                BCodeTU=0
            )

            db.session.add(new_user)
            db.session.commit()

            ga_assign = ws_game_account_assign(
                project_id=get_pi.project_id,
                user_id=current_user.user_id,
                account_name=form.username.data
            )
            db.session.add(ga_assign)
            db.session.commit()
            flash(f'Success! User : {form.username.data} created', category='info')
            render_template('rf_online_main.html', amount=pretty_budget, form=form, ga=ga,count=ga_count)
        else:
            flash(f'Error! User : {form.username.data} not created', category='danger')
            render_template('rf_online_main.html', amount=pretty_budget, form=form, ga=ga,count=ga_count)

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'{err_msg}', category='danger')
    return render_template('rf_online_main.html', amount=pretty_budget, form=form, ga=ga, count=ga_count)
