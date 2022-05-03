from rfsite import db, admin


class ws_coeficient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_src = db.Column(db.String(255), nullable=False)
    project_dst = db.Column(db.String(255), nullable=False)
    cost = db.Column(db.Float(), nullable=False)
    is_available = db.Column(db.Integer, nullable=False, default=1)

