from flask import url_for, flash, render_template
from werkzeug.utils import redirect

from rfsite import db
from rfsite.bill_hash import create_hash
from rfsite.forms.RegisterForm import RegisterForm
from rfsite.func import gen_reg_token, send_mail
from rfsite.models.ws_users import ws_users


def reg_page():
    form = RegisterForm()
    if form.validate_on_submit():
        token = gen_reg_token()
        user_to_create = ws_users(username=form.username.data,
                                  email=form.email.data,
                                  password=form.password.data,
                                  user_bill=create_hash(form.email.data, form.password.data),
                                  token=token)
        db.session.add(user_to_create)
        db.session.commit()
        send_mail('Registration confirm', form.email.data, f"Follow the link to complete the registration "
                                                           f"http://192.168.99.206:8080/verify?token={token}")
        flash(f'Check email, and active you account', category='info')
        return redirect(url_for('login_page'))
    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with create_user {err_msg}', category='danger')
    return render_template('reg.html', form=form)
