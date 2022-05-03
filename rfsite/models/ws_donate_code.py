from rfsite import db, admin


class ws_donate_code(db.Model):
    code_id = db.Column(db.Integer(), primary_key=True)
    code = db.Column(db.String(length=8), nullable=False, unique=True)
    cost = db.Column(db.Integer(), nullable=False, default=0)
    username = db.Column(db.String(length=255), default=None)
    is_active = db.Column(db.String(length=1), nullable=False, default='N')



