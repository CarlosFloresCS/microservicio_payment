from app import db
from .user import User
from .card import Card

from datetime import datetime
from enum import Enum

class TransactionState(Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    DECLINED = "DECLINED"
    REFUNDED = "REFUNDED"

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    card_id = db.Column(db.Integer, db.ForeignKey('card.id'), nullable=False)
    date_hour = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    mount = db.Column(db.Float, nullable=False)
    state = db.Column(db.Enum(TransactionState), default=TransactionState.PENDING)

    def as_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'card_id': self.card_id,
            'date_hour': self.date_hour.strftime('%Y-%m-%d %H:%M:%S'),
            'mount': self.mount,
            'state': self.state.name
        }

    def __repr__(self):
        return '<Transaction {}>'.format(self.id)