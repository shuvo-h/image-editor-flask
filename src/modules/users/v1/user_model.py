from src.config.db_config import db
from werkzeug.security import generate_password_hash, check_password_hash
from .user_constant import USER_ROLE, USER_STATUS

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(100),nullable=False)
    role = db.Column(db.Enum(*USER_ROLE, name='user_roles'), default=USER_ROLE['USER'], nullable=False)
    phone_number = db.Column(db.String(20), unique=True)
    avater = db.Column(db.String(255),nullable=True)
    address =  db.Column(db.String(100), nullable=False)
    city =  db.Column(db.String(100), nullable=False)
    country =  db.Column(db.String(100), nullable=False)
    status = db.Column(db.Enum(*USER_STATUS, name='user_status'), default=USER_STATUS["ACTIVE"], nullable=False)

    def __init__(self, email, password,name,role,phone_number,avater,address,city,country,status):
        self.email = email
        self.set_password(password)
        self.name = name
        self.role = role
        self.phone_number = phone_number
        self.avater = avater
        self.address = address
        self.city = city
        self.country = country
        self.status = status

    def set_password(self, plain_password):
        self.password = generate_password_hash(plain_password)

    def check_password(hashed_password, plain_password):
        return check_password_hash(hashed_password, plain_password)
    
    # printers methods
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
    
    # class methods 
    @classmethod
    def add_and_commit(cls, new_user):
        db.session.add(new_user)
        db.session.commit()