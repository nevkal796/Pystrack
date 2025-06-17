from . import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    email = db.Column(db.String(100), unique=True)  
    password = db.Column(db.String(200))  # fix: capitalize 'String'
    entries = db.relationship('JournalEntry', backref='author', lazy=True)  
    # 'entries' allows accessing all JournalEntry objects by this user
    # backref='author' adds a .author attribute to JournalEntry for user reference

class JournalEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)  # journal text content, can't be empty
    mood = db.Column(db.String(20))  # mood label from sentiment analysis
    date = db.Column(db.DateTime, default=datetime.utcnow)  # default to current time
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  
    # foreign key linking to User.id, required for ownership
