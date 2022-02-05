from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


db = SQLAlchemy()


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    firstName = db.Column(db.String(255), index=True, nullable=True, default='Unknown')
    secondName = db.Column(db.String(255), index=True, nullable=True, default='Unknown')
    password = db.Column(db.String(255), nullable=True)
    is_admin = db.Column(db.Boolean, default=False)
    score = db.Column(db.Integer, default=0)
    class_user = db.Column(db.Integer, default=5)
    image_url = db.Column(db.String(255), default='uk.jpg')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_rating(self):
        users = self.query.order_by(Users.score.desc()).all()
        n = 1
        for user in users:
            if user.username == self.username:
                return n
            else:
                n += 1
        return None

    def get_achievement_list(self):
        user_to_achievement = self.achievement
        achievements = []
        for achievement in user_to_achievement:
            ida = achievement.id_achievement
            achievements.append(Achievements.query.filter_by(id=ida).first())
        return achievements

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(2048), nullable=True)
    date_create = db.Column(db.String(64))
    name = db.Column(db.String(64), index=True, unique=True)


class Achievements(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(200), nullable=True)


class UserAchievements(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))
    id_achievement = db.Column(db.Integer, db.ForeignKey('achievements.id'))
    user = db.relationship('Users', backref=db.backref('achievement', lazy=True))
    achievement = db.relationship('Achievements', backref=db.backref('user', lazy=True))


class TestList(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    test_type = db.Column(db.String(64), index=True, nullable=True)
    content = db.Column(db.String(2048), nullable=True)
    id_lesson = db.Column(db.Integer, db.ForeignKey('lesson.id'))
    lesson = db.relationship('Lesson', backref=db.backref('test', lazy=True))
