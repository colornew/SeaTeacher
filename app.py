from flask import Flask, render_template, request, redirect, url_for, abort, flash
from flask_wtf import form
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
import datetime
import locale
from os import environ
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from models import Users, db
from cfg import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db.init_app(app)
login = LoginManager(app)


@login.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@app.route('/')
def index():
    return render_template('index.html', title='MainPage')


if __name__ == '__main__':
    app.run()
