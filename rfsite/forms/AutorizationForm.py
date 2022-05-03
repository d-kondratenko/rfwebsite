from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired, Length

from rfsite.models.ws_users import ws_users


class AutorizationForm(FlaskForm):

    def validate_email(self, email_to_check):
        user = ws_users.query.filter_by(email=email_to_check.data).first()
        if not user:
            raise ValidationError("Email not found")

    email = StringField(label="Email", validators=[Email(), DataRequired()])
    password = PasswordField(label="Password", validators=[Length(min=6), DataRequired()])
    submit = SubmitField(label="Sign in")
