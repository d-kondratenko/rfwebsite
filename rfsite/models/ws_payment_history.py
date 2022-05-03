from datetime import datetime

from flask_admin.contrib.sqla import ModelView

from rfsite import db, admin


class ws_payment_history(db.Model):
    payment_id = db.Column(db.Integer(), primary_key=True)
    bank_pay_id = db.Column(db.String(length=255), nullable=False)
    user_id = db.Column(db.Integer(), nullable=False)
    user_bill = db.Column(db.String(length=255), nullable=False)
    payment_sum = db.Column(db.Integer(), nullable=False)
    c_date = db.Column(db.String(length=255), nullable=False, default=datetime.now().strftime("%d.%m.%Y %H:%M:%S"))


admin.add_view(ModelView(ws_payment_history, db.session, name="Payment history", menu_class_name="Pay"))
