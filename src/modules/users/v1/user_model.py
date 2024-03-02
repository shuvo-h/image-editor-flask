from src.config.db_config import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100),  nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.set_password(password)

    def set_password(self, plain_password):
        # password = generate_password_hash(password)
        password = plain_password # convert into hash
        self.password = password

    def check_password(self, plain_password):
        # return check_password_hash(self.password, plain_password)
        isValidPassword = plain_password == self.password
        return isValidPassword
    
