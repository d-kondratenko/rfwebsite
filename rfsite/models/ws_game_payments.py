from flask_admin.contrib.sqla import ModelView

from rfsite import db, admin


class ws_game_payments(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), nullable=False)
    project = db.Column(db.String(length=255), nullable=False)
    account_name = db.Column(db.String(length=255), nullable=False)
    payment_type = db.Column(db.String(length=255), nullable=False)
    value = db.Column(db.String(length=255), nullable=False)
    Coin_cost = db.Column(db.Float(), nullable=False)


admin.add_view(ModelView(ws_game_payments, db.session, name="Game payments"))
