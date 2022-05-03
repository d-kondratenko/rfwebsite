from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin

from rfsite import db, bcrypt, login_manager, admin


@login_manager.user_loader
def load_user(user_id):
    return ws_users.query.get(int(user_id))


class ws_users(db.Model, UserMixin):
    user_id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    user_bill = db.Column(db.String(length=255), nullable=False, default=0)
    budget = db.Column(db.Float(), nullable=False, default=0)
    is_admin = db.Column(db.Integer(), nullable=False, default=0)
    is_activate = db.Column(db.Integer(), nullable=False, default=0)
    token = db.Column(db.String(length=255), nullable=False)

    @property
    def prettier_budget(self):
        return f"{self.budget} C"

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    def is_active(self):
        return True

    def get_id(self):
        return self.user_id


admin.add_view(ModelView(ws_users, db.session, name="Users"))
