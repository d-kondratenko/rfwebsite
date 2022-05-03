from flask import render_template
from flask_login import current_user

from rfsite.models.ws_transfer_history import ws_transfer_history


def thservice():
    data = ws_transfer_history.query.filter_by(user_id=current_user.user_id).all()
    return render_template('transfer_history.html', data=data)
