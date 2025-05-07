from flask_sqlalchemy import SQLAlchemy
"""
This is an example code snippet to illustrate the one-to-many SQL DB interations and relationships.
This code snippet was provided within the course documents, and is only for reference of the one-to-many format.
"""
db = SQLAlchemy()

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    posts = db.relationship('Post', backref='blog')

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.Text)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'))