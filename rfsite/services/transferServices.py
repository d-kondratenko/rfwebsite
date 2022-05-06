from flask import request, url_for, flash, render_template
from flask_login import current_user
from werkzeug.utils import redirect

from rfsite import db
from rfsite.forms.TransferForm import TransferForm
from rfsite.models.ws_coeficient import ws_coeficient
from rfsite.models.ws_game_balance import ws_game_balance
from rfsite.models.ws_projects import ws_projects
from rfsite.models.ws_transfer_coef import ws_transfer_coef
from rfsite.models.ws_transfer_history import ws_transfer_history
from rfsite.models.ws_users import ws_users


def transfer():
    form = TransferForm()
    if request.method == 'POST':
        project_src = ws_projects.query.filter_by(project_abbrev=form.project_src.data).first()
        project_dst = ws_projects.query.filter_by(project_abbrev=form.project_dst.data).first()
        gb_dst = ws_game_balance.query.filter_by(user_id=current_user.user_id,
                                                 project=project_dst.project_name).first()
        gb_src = ws_game_balance.query.filter_by(user_id=current_user.user_id,
                                                 project=project_src.project_name).first()
        coef = ws_coeficient.query.filter_by(project_src=project_src.project_abbrev,
                                             project_dst=project_dst.project_abbrev).first()
        us = ws_users.query.filter_by(user_id=current_user.user_id).first()
        if gb_src.balance - (form.amount.data*coef.cost) >= 0:
            if gb_dst:
                transfer = ws_transfer_history(user_id=current_user.user_id,
                                               project=project_dst.project_name,
                                               transfer_sum=form.amount.data
                                               )
                db.session.add(transfer)
                db.session.commit()
                gb_dst.balance += form.amount.data
                gb_src.balance -= form.amount.data*coef.cost
                if gb_src.project == 'Main':
                    us.budget -= form.amount.data*coef.cost
                db.session.commit()
            else:
                gb_dst = ws_game_balance(project=project_dst.project_name,
                                         user_id=current_user.user_id,
                                         user_bill=current_user.user_bill,
                                         balance=form.amount.data)
                db.session.add(gb_dst)
                db.session.commit()
                transfer = ws_transfer_history(user_id=current_user.user_id,
                                               project=project_dst.project_name,
                                               transfer_sum=form.amount.data
                                               )
                db.session.add(transfer)
                db.session.commit()
                gb_dst.balance += form.amount.data
                gb_src.balance -= form.amount.data*coef.cost
                if gb_src.project == 'Main':
                    us.budget -= form.amount.data*coef.cost
                db.session.commit()
            db.session.commit()
            return redirect(url_for('pp_page'))
        else:
            flash("Insufficient funds", category='danger')
            return render_template('transfer.html', form=form)
    else:
        return render_template('transfer.html', form=form)
