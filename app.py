from flask import Flask, render_template, request, redirect, url_for, abort, flash
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from os import environ
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from functions.models import Users, db
from functions.forms import *
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    forms = LoginForm()
    if forms.validate_on_submit():
        nick = forms.username.data
        password = forms.password.data
        user = Users.query.filter_by(username=nick).first()
        if not (user and user.check_password(password)):
            abort(403)
        login_user(user, remember=forms.remember_me)
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=forms)


if __name__ == '__main__':
    app.run()
