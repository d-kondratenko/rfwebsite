from flask import request, flash, redirect, url_for, render_template

from rfsite import func, db
from rfsite.models.ws_users import ws_users


def changePassService():
    if request.method == 'POST':
        pass1 = request.form.get('pass1')
        pass2 = request.form.get('pass2')
        token = request.args.get('token')
        if pass1 == pass2:
            user = ws_users.query.filter_by(token=token, is_activate=0).first()
            if user:
                token = func.generateToken(user.username, user.email)
                user.password = pass1
                db.session.commit()
                func.send_mail('Reset password', user.email,
                               f"Follow the link to complete the check password "
                               f"http://192.168.99.206:8080/verify?token={token}")
                flash('Message send to you email', category='info')
                return redirect(url_for('login_page'))
            else:
                flash('User not found', category='danger')
                return render_template('change_pass.html')
        else:
            flash('Password not equal', category='danger')
            return render_template('change_pass.html')
    else:
        return render_template('change_pass.html')
