from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, Email, EqualTo

from rfsite.models.ws_users import ws_users


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = ws_users.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("Username already exists! Pleas try a different username")

    def validate_email(self, email_to_check):
        user = ws_users.query.filter_by(email=email_to_check.data).first()
        if user:
            raise ValidationError("Email already exists! Pleas try a different email address")

    username = StringField(label="User name:", validators=[Length(min=3, max=50), DataRequired()])
    email = StringField(label="email", validators=[Email(), DataRequired()])
    password = PasswordField(label="Password", validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label="Confirm Password", validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField(label="Create account")
