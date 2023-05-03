from app import db
from .user import User

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    card_number = db.Column(db.String(16), index=True, unique=True)
    due_date = db.Column(db.String(5), nullable=False)
    code_security = db.Column(db.String(4), nullable=False)
    type_card = db.Column(db.String(10), nullable=False)

    transactions = db.relationship('Transaction', backref='card', lazy=True)

    def __repr__(self):
        return '<Card {}>'.format(self.card_number)