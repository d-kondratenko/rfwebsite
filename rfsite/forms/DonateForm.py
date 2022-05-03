from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class DonateForm(FlaskForm):
    description = StringField(label="User Bill")
    amount = StringField(label="Donate Code")
    submit = SubmitField(label="Donate")
