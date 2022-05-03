from flask_admin.contrib.sqla import ModelView

from rfsite import db, admin


class ws_projects(db.Model):
    project_id = db.Column(db.Integer(), primary_key=True)
    project_name = db.Column(db.String(length=255), nullable=False)
    project_abbrev = db.Column(db.String(length=5), nullable=False)
    status = db.Column(db.String(length=2), nullable=False, default='OK')


admin.add_view(ModelView(ws_projects, db.session, name="Projects"))
