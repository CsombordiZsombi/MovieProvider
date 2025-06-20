from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(70), nullable=False)
    rank = db.Column(db.Enum('admin', 'premium', 'basic', name='user_rank'), nullable=False, default='basic')

    def __repr__(self):
        return f'User: {self.id} {self.username}, {self.rank}'

