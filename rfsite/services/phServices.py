from flask import render_template
from flask_login import current_user

from rfsite.models.ws_payment_history import ws_payment_history


def phservices():
    data = ws_payment_history.query.filter_by(user_id=current_user.user_id).all()
    return render_template('payment_history.html', data=data)
