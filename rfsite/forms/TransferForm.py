from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, SubmitField


class TransferForm(FlaskForm):
    project_src = SelectField(label="Project Src", choices=[
        ('main', 'Main'),
        ('rf', 'RF Online'),
        ('wow', 'World of Warcraft'),
        ('l2', 'Linage 2'),
        ('fw', 'Forsaken World')
    ])
    project_dst = SelectField(label="Project Dst", choices=[
        ('rf', 'RF Online'),
        ('wow', 'World of Warcraft'),
        ('l2', 'Linage 2'),
        ('fw', 'Forsaken World')
    ])
    amount = IntegerField(label="Transfer sum")
    submit = SubmitField(label="Transfer")
