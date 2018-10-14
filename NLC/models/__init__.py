from flask import Flask
from os import environ
from .base import db
from models import user

def init_app(app:Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
    db.init_app(app)
    db.app = app