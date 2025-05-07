from flask_sqlalchemy import SQLAlchemy
"""
This is an example code snippet to illustrate the one-to-one SQL DB interations and relationships.
This code snippet was provided within the course documents, and is only for reference of the one-to-one format.
"""
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    profile = db.relationship('UserProfile', backref='user', uselist=False)

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.Text)
    profile_picture = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))