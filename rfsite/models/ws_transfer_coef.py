from flask_admin.contrib.sqla import ModelView

from rfsite import db, admin


class ws_transfer_coef(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    project_name = db.Column(db.String(255), nullable=False)
    main = db.Column(db.Float(), nullable=False)
    rf = db.Column(db.Float(), nullable=False)
    wow = db.Column(db.Float(), nullable=False)
    l2 = db.Column(db.Float(), nullable=False)
    fw = db.Column(db.Float(), nullable=False)


#admin.add_view(ModelView(ws_transfer_coef, db.session))
