from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, NumberRange
from wtforms.widgets import TextArea, TextInput, PasswordInput, ListWidget


class Registration(FlaskForm):
    username = StringField('Никнэйм', validators=[DataRequired()], widget=TextInput())
    firstName = StringField('Имя', validators=[DataRequired()], widget=TextInput())
    secondName = StringField('Фамелия', validators=[DataRequired()], widget=TextInput())
    email = StringField('Почта', validators=[DataRequired(), Email()], widget=TextInput())
    password = StringField('Пароль', validators=[DataRequired()], widget=PasswordInput())
    password_confirm = StringField('Подтверждение пароля', validators=[DataRequired(), EqualTo('password')],
                                   widget=PasswordInput())


class LoginForm(FlaskForm):
    username = StringField('Никнэйм', validators=[DataRequired()], widget=TextInput())
    password = PasswordField('Пароль', validators=[DataRequired()], widget=PasswordInput())
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class Settings(FlaskForm):
    username = StringField('Никнэйм', widget=TextInput())
    submit = SubmitField('Изменить')
