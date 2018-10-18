from .base import db


class User(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"<User> {self.username}: {self.password}"
