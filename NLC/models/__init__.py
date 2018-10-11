from flask import Flask
from os import environ
from .base import db
from . import users

def init_app(app:Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://bccfea76054235:cf209ee2@us-cdbr-iron-east-01.cleardb.net/heroku_3a392d53d178674?reconnect=true" #TODO: Export to envionment variable
    db.init_app(app)