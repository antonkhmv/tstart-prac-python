from flask_sqlalchemy import SQLAlchemy
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Purchases(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    type = db.Column(db.String(16))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    

class User(db.Model, UserMixin): 
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    account_balance = db.Column(db.Integer())
    #purchaces = db.relationship('Purchases')
    