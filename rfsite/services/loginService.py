from flask import flash, url_for, render_template
from flask_login import login_user
from werkzeug.utils import redirect

from rfsite.forms.AutorizationForm import AutorizationForm
from rfsite.models.ws_users import ws_users


def login():
    form = AutorizationForm()
    if form.validate_on_submit():
        attempted_user = ws_users.query.filter_by(email=form.email.data).first()
        if attempted_user.is_activate == 0:
            flash('User not active, check email!', category='danger')
            return render_template('login.html', form=form)
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged is as: {attempted_user.username}', category='info')
            return redirect(url_for('pp_page'))
        else:
            flash('Username and password are not match!',category='danger')
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with user login {err_msg}', category='danger')
    return render_template('login.html', form=form)