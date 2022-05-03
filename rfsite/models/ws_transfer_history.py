from datetime import datetime

from flask_admin.contrib.sqla import ModelView

from rfsite import db, admin


class ws_transfer_history(db.Model):
    transfer_id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), nullable=False)
    project = db.Column(db.String(length=255), nullable=False)
    transfer_sum = db.Column(db.Integer(), nullable=False)
    transfer_date = db.Column(db.String(length=255), nullable=False,
                              default=datetime.now().strftime("%d.%m.%Y %H:%M:%S"))


admin.add_view(ModelView(ws_transfer_history, db.session, name="Transfer history", menu_class_name="Pay"))
