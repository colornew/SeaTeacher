from flask import Flask, render_template, request, redirect, url_for, abort, flash
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from os import environ
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from functions.models import Users, db
from functions.forms import *
from cfg import *
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = S_KEY
db.init_app(app)
login = LoginManager(app)
login.init_app(app)
migrate = Migrate(app, db)


@login.user_loader
def load_user(id):
    return Users.query.get(int(id))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/')
def index():
    return render_template('index.html', title='MainPage')


@app.errorhandler(403)
def not_found_error(error):
    return render_template('errors/403.html'), 403


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 403


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


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    register_form = Registration()
    if register_form.validate_on_submit():
        email = register_form.email.data
        name = register_form.username.data
        password = register_form.password.data
        first_name = register_form.firstName.data
        second_name = register_form.secondName.data
        existing_user = Users.query.filter_by(email=email).first()
        if existing_user:
            abort(400)
        user = Users(username=name, email=email, firstName=first_name, secondName=second_name)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('registration.html', form=register_form, title='Registration')


@app.route('/user/<int:user_id>')
def profile(user_id):
    user = Users.query.filter_by(id=user_id).first()
    return render_template('user.html', title=user.username, user=user)


@app.route('/roadmap')
def roadmap():
    return render_template('roadmap.html', user=current_user)


if __name__ == '__main__':
    app.run()
