from rfsite import db


class ws_coef_view(db.Model):
    __tablename__ = 'coef_view'
    project_src = db.Column(db.String(length=255), nullable=False)
    project_dst = db.Column(db.String(length=255), nullable=False)
    cost = db.Column(db.Float(), nullable=False)
