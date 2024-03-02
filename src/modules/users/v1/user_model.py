from src.config.db_config import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.set_password(password)

    def set_password(self, plain_password):
        self.password = generate_password_hash(plain_password)

    def check_password(self, plain_password):
        return check_password_hash(self.password, plain_password)
    
    def __str__(self):
        return f"User(id={self.id}, email={self.email})"

    def __repr__(self):
        return f"User(id={self.id}, email={self.email})"

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password,
        }
    
    @classmethod
    def add_and_commit(cls, new_user):
        db.session.add(new_user)
        db.session.commit()