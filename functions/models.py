from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


db = SQLAlchemy()


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    firstName = db.Column(db.String(255), index=True, nullable=True)
    secondName = db.Column(db.String(255), index=True, nullable=True)
    password = db.Column(db.String(255), nullable=True)
    is_admin = db.Column(db.Boolean, default=False)
    score = db.Column(db.Integer, default=0)
    class_user = db.Column(db.Integer, default=5)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(2048), nullable=True)
    date_create = db.Column(db.String(64))
    name = db.Column(db.String(64), index=True, unique=True)