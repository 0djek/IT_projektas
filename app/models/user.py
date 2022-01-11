from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin):
    def __init__(self, user_id, username, email, password_hash, date_registered, role):
        self.id = user_id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.date_registered = date_registered
        self.role = role
        self.authenticated = False

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return self.authenticated

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
