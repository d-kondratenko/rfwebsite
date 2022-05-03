from flask import request, redirect, url_for

from rfsite import db
from rfsite.models.ws_users import ws_users


def verify_service():
    token = request.args.get('token')
    user = ws_users.query.filter_by(token=token, is_activate=0).first()
    user.is_activate = 1
    db.session.commit()
    return redirect(url_for('login_page'))
