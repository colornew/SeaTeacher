from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, NumberRange
from wtforms.widgets import TextArea, TextInput, PasswordInput, ListWidget, FileInput
from flask_wtf.file import FileField, FileAllowed, FileRequired
from datetime import date


class Registration(FlaskForm):
    username = StringField('Никнэйм', validators=[DataRequired()], widget=TextInput(),
                           render_kw={"placeholder": "Никнейм"})
    firstName = StringField('Имя', validators=[DataRequired()], widget=TextInput(), render_kw={"placeholder": "Имя"})
    secondName = StringField('Фамилия', validators=[DataRequired()], widget=TextInput(),
                             render_kw={"placeholder": "Фамилия"})
    email = StringField('Почта', validators=[DataRequired(), Email()], widget=TextInput(),
                        render_kw={"placeholder": "Почта"})
    password = StringField('Пароль', validators=[DataRequired()], widget=PasswordInput(),
                           render_kw={"placeholder": "Пароль"})
    password_confirm = StringField('Подтверждение пароля', validators=[DataRequired(), EqualTo('password')],
                                   widget=PasswordInput(), render_kw={"placeholder": "Повторите пароль"})
    register = SubmitField('Регистрация')


class LoginForm(FlaskForm):
    username = StringField('Никнэйм', validators=[DataRequired()], widget=TextInput(),
                           render_kw={"placeholder": "Никнейм"})
    password = PasswordField('Пароль', validators=[DataRequired()], widget=PasswordInput(),
                             render_kw={"placeholder": "Пароль"})
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class Settings(FlaskForm):
    username = StringField('Никнэйм', widget=TextInput())
    image = FileField('Аватар', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    submit = SubmitField('Изменить')


class UploadCurse(FlaskForm):
    name = StringField('Название курса', widget=TextInput())
    text = StringField('Контент', validators=[DataRequired()], widget=TextArea())
