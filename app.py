import random

from flask import Flask, render_template, request, redirect, url_for, abort, flash, jsonify
import os
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from functions.models import Users, db, Lesson, TestList, UserAchievements, Achievements
from functions.forms import *
from cfg import *
from flask_migrate import Migrate
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm
from wtforms.fields import RadioField
from wtforms.widgets import TextArea, TextInput, PasswordInput, ListWidget, FileInput, RadioInput
import ast

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = S_KEY
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Max file size = 16 megaByte
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


@app.errorhandler(500)
def not_found_error(error):
    print(error)
    return render_template('errors/500.html'), 500


@app.route('/authentication', methods=['GET', 'POST'])
def authentication():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    forms = LoginForm()
    register_form = Registration()
    if forms.validate_on_submit() and register_form.email.data is None:
        nick = forms.username.data
        password = forms.password.data
        user = Users.query.filter_by(username=nick).first()
        user_mail = Users.query.filter_by(email=nick).first()
        if not (user and user.check_password(password)):
            if user_mail and user_mail.check_password(password):
                login_user(user_mail, remember=forms.remember_me)
                return redirect(url_for('roadmap'))
            abort(403)
        login_user(user, remember=forms.remember_me)
        return redirect(url_for('roadmap'))
    elif register_form.validate_on_submit() and register_form.username.data:
        email, name, password = register_form.email.data, register_form.username.data, register_form.password.data
        first_name, second_name = register_form.firstName.data, register_form.secondName.data
        existing_user = Users.query.filter_by(email=email).first()
        if existing_user:
            abort(400)
        user = Users(username=name, email=email, firstName=first_name, secondName=second_name)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        user = Users.query.filter_by(username=name).first()
        login_user(user, remember=forms.remember_me)
        return redirect(url_for('roadmap'))
    return render_template('authentication.html', form=forms, reg_form=register_form)


@app.route('/user/<int:user_id>')
def profile(user_id):
    user = Users.query.filter_by(id=user_id).first()
    image = 'images/users/' + user.image_url
    achievements = user.get_achievement_list()
    return render_template('user.html', title=user.username, user=user, url_img=image, achievements_list=achievements)


@app.route('/roadmap')
def roadmap():
    lesson_list = Lesson.query.all()
    return render_template('roadmap.html', title='Roadmap', user=current_user, lessons=lesson_list)


@app.route('/lesson/<int:lesson_id>')
def lesson(lesson_id):
    lessons = Lesson.query.filter_by(id=lesson_id).first()
    if lessons is None:
        return render_template('errors/404.html'), 403
    return render_template('lesson.html', title='Lesson', lesson_format=lessons)


@app.route('/settings', methods=['GET', 'POST'])
def settings():
    setting = Settings()
    if setting.is_submitted():
        image, username = setting.image.data, setting.username.data
        if setting.image.validate(Settings):
            filename = secure_filename(image.filename)
            filename = str(current_user.id) + '.' + filename.split('.')[1]
            image.save(os.path.join(
                app.instance_path[0:-9], 'static/images/users', filename
            ))
            current_user.image_url = filename
            db.session.commit()
        existing_user = Users.query.filter_by(username=username).first()
        if existing_user:
            flash('Человекс с таким именем уже есть')
        else:
            if username != '':
                current_user.username = username
                db.session.commit()
        return redirect(url_for('settings'))
    return render_template('settings.html', title='Settings', form=setting)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if current_user.is_admin:
        form = UploadCurse()
        lesson_list = Lesson.query.all()
        if form.validate_on_submit():
            name, text = form.name.data, form.text.data
            data = date.today().strftime("%d/%m/%Y")
            less = Lesson(name=name, text=text, date_create=data)
            db.session.add(less)
            db.session.commit()
            return redirect(url_for('roadmap'))
        return render_template('panel.html', curse=form, lesson_list=lesson_list)
    else:
        return render_template('errors/403.html'), 403


@app.route('/curse_correct/<int:curse_id>', methods=['GET', 'POST'])
def curse_correct(curse_id):
    if current_user.is_admin:
        curse = CorrectCurse()
        lesson_s = Lesson.query.filter_by(id=curse_id).first()
        if curse.validate_on_submit():
            if curse.name.data != '':
                lesson_s.name = curse.name.data
            if curse.text.data != '':
                lesson_s.text = curse.text.data
            db.session.commit()
            redirect(url_for('admin'))
        return render_template('curserender.html', curse=curse, lesson=lesson_s)
    else:
        return render_template('errors/403.html'), 403


@app.route('/delete_curse/<int:curse_id>')
def delete_curse(curse_id):
    if current_user.is_admin:
        lesson_s = Lesson.query.filter_by(id=curse_id).first()
        db.session.delete(lesson_s)
        db.session.commit()
        return redirect(url_for('roadmap'))
    else:
        return render_template('errors/403.html'), 403


@app.route('/test/<int:test_id>', methods=['GET', 'POST'])
def testing(test_id):
    if current_user.is_authenticated:
        test = TestList.query.filter_by(id=test_id).first()
        content = test.content.split('*')
        test_list = []
        for i in content:
            test_list.append(ast.literal_eval('{' + i + '}'))

        class Answer(FlaskForm):
            list_forms = []
            for quest in test_list:
                if quest['format'] == 'test':
                    list_answer = quest['answers'].split(',')
                    random.shuffle(list_answer)
                    choices = []
                    for i in list_answer:
                        choices.append([i, i])
                    obj = RadioField(quest['question'], choices=choices, id=quest['id'])
                    locals()['form' + quest['id']] = obj
                elif quest['format'] == 'question':
                    obj = StringField(quest['question'], widget=TextInput())
                    locals()['form' + quest['id']] = obj
            submit = SubmitField('Завершить')

        test_form = Answer()
        if test_form.is_submitted():
            count = 0
            for i in range(1, 11):
                answer = test_form.data['form' + str(i)]
                if (answer == test_list[i - 1]['answers'].split(',')[0] and
                    test_list[i - 1]['format'] == 'test') or (test_list[i - 1]['format'] == 'question' and
                                                              answer.lower() in test_list[i - 1][
                                                                  'answers'].lower().split(',')):
                    count += 1
            current_user.score += count
            db.session.commit()
            if count >= 9:
                achivka = UserAchievements(id_user=current_user.id, id_achievement=test_id)
                db.session.add(achivka)
                db.session.commit()
            return redirect(url_for('roadmap'))
        else:
            return render_template('test.html', test_format=test, answer_form=test_form, list_test=test_list)
    else:
        return render_template('errors/403.html'), 403


@app.route('/help')
def help_menu():
    return render_template('help.html')


@app.route('/rating')
def rating():
    users = Users.query.order_by(Users.score.desc()).all()[0:10]
    return render_template('rating.html', title='Рейтинг', users=users)


if __name__ == '__main__':
    app.run()
