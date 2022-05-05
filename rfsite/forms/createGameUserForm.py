from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, ValidationError


from rfsite.models.rf_account import rf_account


class createGameUserForm(FlaskForm):

    def validate_username(self, username):
        v = rf_account.query.filter_by(id=username.data.encode('utf-8')).all()
        if v:
            raise ValidationError(f"Username: {username.data} exists in database")

        if v==Exception:
            raise ValidationError(v)

    username = StringField(label="Username", validators=[Length(min=3, max=12), DataRequired()])
    password = PasswordField(label="Password", validators=[Length(min=6), DataRequired()])
    submit = SubmitField(label="Create new game account")
