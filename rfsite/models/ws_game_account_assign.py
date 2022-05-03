from flask_admin.contrib.sqla import ModelView

from rfsite import db, admin


class ws_game_account_assign(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    project_id = db.Column(db.Integer(), nullable=False)
    user_id = db.Column(db.Integer(), nullable=False)
    account_name = db.Column(db.String(length=255), nullable=False)
    is_premium = db.Column(db.String(length=1), nullable=False, default='N')
    premStart = db.Column(db.DateTime)
    premFinish = db.Column(db.DateTime)
    cash = db.Column(db.Integer(), nullable=False, default=0)


admin.add_view(ModelView(ws_game_account_assign, db.session, name="Game account assign"))
