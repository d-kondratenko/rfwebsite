from flask import request, flash, redirect, url_for, render_template
from rfsite import func, db
from rfsite.models.ws_users import ws_users


def resetService():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        user = ws_users.query.filter_by(username=username, email=email).first()
        if user is not None:
            user.is_activate = 0
            token = func.generateToken(username, email)
            user.token = token
            db.session.commit()
            func.send_mail('Reset password', email,
                               f"To reset password forward to link: http://192.168.99.206:8080/cpas?token={token}")
            flash('Message send to you email', category='info')
            return redirect(url_for('login_page'))
        else:
            flash('User not found', category='danger')
            return render_template('reset_pass.html')

    else:
        return render_template('reset_pass.html')
