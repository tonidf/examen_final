from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):

    def __init__(self, id, email, password, username):

        self.id = id
        self.email = email
        self.password = password
        self.username = username
    
    @classmethod
    def generate_hash(cls, password):

        return generate_password_hash(password)
    
    @classmethod
    def check_password(cls, hashed_pass, password):

        return check_password_hash(hashed_pass, password)