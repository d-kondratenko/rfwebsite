from flask_admin.contrib.sqla import ModelView

from rfsite import db, admin


class ws_game_balance(db.Model):
    bal_id = db.Column(db.Integer(), primary_key=True)
    project = db.Column(db.String(length=255), nullable=False)
    user_id = db.Column(db.Integer(), nullable=False)
    user_bill = db.Column(db.String(length=255), nullable=False)
    balance = db.Column(db.Float(), nullable=False)


admin.add_view(ModelView(ws_game_balance, db.session, name="Game balance"))
