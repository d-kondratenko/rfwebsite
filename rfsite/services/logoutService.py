from flask import flash, url_for
from flask_login import logout_user
from werkzeug.utils import redirect


def logout():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for('index_page'))
