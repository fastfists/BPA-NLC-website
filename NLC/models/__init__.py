from flask import Flask
from os import environ
from .base import db
from . import user

def init_app(app:Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
    db.init_app(app)
    db.app = app
    db.create_all()
