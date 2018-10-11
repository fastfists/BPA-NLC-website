from .base import db

class User(db.model):
    __tablename__ = "Users"
    id = db.Column('id', db.Integer, primary_key=True)