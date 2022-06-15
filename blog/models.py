from sqlalchemy import false
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from blog import db

# Add Database 
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://eiqmpxtufmdwuq:b197fc1d42f4d610c67c71c58a39a2ce5740a9cd193971351d03f9668ec70896@ec2-52-73-184-24.compute-1.amazonaws.com:5432/deh0qe196p6dv4"



class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(400), nullable=False)
    #date_added = db.Column(db.DateTime, default=datetime.utcnow)
    full_name = db.Column(db.String(100), nullable=False)
    user_pic = db.Column(db.String(255), nullable=True)
    about_author  = db.Column(db.String(200), nullable=True)
    email  = db.Column(db.String(200), nullable=False)
    is_admin  = db.Column(db.String(10), nullable=False, default='False')
    


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    file = db.Column(db.String(512), nullable=True)
    content = db.Column(db.Text, nullable=False)
    user_id =  db.Column(db.Integer , db.ForeignKey('users.id', ondelete="cascade"),nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)



class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment_msg = db.Column(db.String(512), nullable=False)
    user_id =  db.Column(db.Integer , db.ForeignKey('users.id', ondelete="cascade"),nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    post_id =  db.Column(db.Integer , db.ForeignKey('post.id', ondelete="cascade"),nullable=False)


class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id =  db.Column(db.Integer , db.ForeignKey('users.id', ondelete="cascade"),nullable=False)
    post_id =  db.Column(db.Integer , db.ForeignKey('post.id', ondelete="cascade"),nullable=False)


class Follower_Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id =  db.Column(db.Integer , db.ForeignKey('users.id', ondelete="cascade"),nullable=False)
    follower_id =  db.Column(db.Integer , db.ForeignKey('users.id', ondelete="cascade"),nullable=False)
