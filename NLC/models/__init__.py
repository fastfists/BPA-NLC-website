from flask import Flask
from os import environ
from .base import db
from . import users

def init_app(app:Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = environ["CLEARDB_DATABASE_URL"]
    db.init_app(app)