from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, SubmitField

from rfsite.models.ws_projects import ws_projects

src = []
dst = []


class TransferForm(FlaskForm):
    src_p = ws_projects.query.filter_by(status='OK').all()
    for i in src_p:
        c = (i.project_abbrev, i.project_name)
        src.append(c)

    dst_p = ws_projects.query.filter(ws_projects.project_abbrev != 'main', ws_projects.status == 'OK').all()
    for j in dst_p:
        c = (j.project_abbrev, j.project_name)
        dst.append(c)

    project_src = SelectField(label="Project Src", choices=src
    # [
    #     ('main', 'Main'),
    #     ('rf', 'RF Online'),
    #     ('wow', 'World of Warcraft'),
    #     ('l2', 'Linage 2'),
    #     ('fw', 'Forsaken World')
    # ]
                              )
    project_dst = SelectField(label="Project Dst", choices=dst
    # [
    #     ('rf', 'RF Online'),
    #     ('wow', 'World of Warcraft'),
    #     ('l2', 'Linage 2'),
    #     ('fw', 'Forsaken World')
    # ]
                              )
    amount = IntegerField(label="Transfer sum")
    submit = SubmitField(label="Transfer")
