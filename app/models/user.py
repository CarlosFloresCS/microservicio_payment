from app import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=False)
    surname = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    country = db.Column(db.String(60), nullable=True, default=None)
    phone_number = db.Column(db.String(15), nullable=True, default=None)
    city = db.Column(db.String(30), nullable=True, default=None)
    postal_code = db.Column(db.String(7), nullable=True, default=None)

    cards = db.relationship('Card', backref='user', lazy=True)
    transactions = db.relationship('Transaction', backref='user', lazy=True)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return '<Usuario {}>'.format(self.email)
