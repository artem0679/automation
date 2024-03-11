import os
import sqlalchemy as sa
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from flask import url_for, current_app
from app import db
import markdown
import bleach
from sqlalchemy.dialects.mysql import YEAR


class Role(db.Model):
    __tablename__ = 'roles'
    
    id = db.Column(db.Integer, primary_key=True)
    # Название роли
    name = db.Column(db.String(100), nullable=False)
    # Описание роли
    description = db.Column(db.Text, nullable=False)

    def __repr__(self) -> str:
        return '<Role %r>' % self.name


class Form_of_education(db.Model):
    __tablename__ = 'forms_of_education'
    
    id = db.Column(db.Integer, primary_key=True)
    # Название формы обучения (дневная/вечерняя/заочная)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        return '<Role %r>' % self.name


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    # ФИО
    last_name = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    middle_name = db.Column(db.String(100))
    # Идентификатор роли
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=False)
    # Год поступления
    year_of_admission = db.Column(YEAR)
    # Форма обучения
    form_of_education_id = db.Column(db.Integer, db.ForeignKey("forms_of_education.id"))
    group_number = db.Column(db.String(100))

    role = db.relationship('Role')
    form_of_education = db.relationship("Form_of_education")

    def set_password(self, password) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password) -> bool:
        return check_password_hash(self.password_hash, password)

    @property
    def full_name(self) -> str:
        return ' '.join([self.last_name,
                         self.first_name,
                         self.middle_name or ''])

    def is_admin(self):
        return self.role_id == current_app.config['ADMIN_ROLE_ID']

    def is_student(self):
        return self.role_id == current_app.config['STUDENT_ROLE_ID']

    def __repr__(self):
        return '<User %r>' % self.login


class Reporting_form(db.Model):
    __tablename__ = "reporting_forms"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(100))


class Curriculum(db.Model):
    __tablename__ = "curriculums"

    id = db.Column(db.Integer, primary_key=True)
    # Название дисциплины
    discipline_name = db.Column(db.String(100), nullable=False)
    # Название специальности
    name_of_specialty = db.Column(db.String(100), nullable=False)
    # Семестр
    semester = db.Column(db.Integer, nullable=False)
    # Количество отводимых на дисциплину часов
    number_of_hours = db.Column(db.Integer, nullable=False)
    # Форма отчетности (экзамен/зачет)
    reporting_form_id = db.Column(db.Integer, db.ForeignKey("reporting_forms.id"), nullable=False)

    reporting_form = db.relationship("Reporting_form")

    def __repr__(self) -> str:
        return "<Curriculum> %r" % self.id


class Mark(db.Model):
    __tablename__ = "marks"

    id = db.Column(db.Integer, primary_key=True)
    # Оценка в двух доступных формах: цифра и текст
    number_mark = db.Column(db.Integer, nullable=False)
    text_mark = db.Column(db.String(20), nullable=False)


""" О журнале успеваемости студентов
год/семестр
студент
дисциплина
оценка
"""
class Journal_of_performance(db.Model):
    __tablename__ = "journals_of_performance"

    id = db.Column(db.Integer, primary_key=True)
    # Семестр
    semester = db.Column(db.Integer, nullable=False)
    # Студент
    student_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    # Дисциплина
    curriculum_id = db.Column(db.Integer, db.ForeignKey("curriculums.id"), nullable=False)
    # Оценка
    mark_id = db.Column(db.Integer, db.ForeignKey("marks.id"), nullable=False)

    student = db.relationship("User")
    curriculum = db.relationship("Curriculum")
    mark = db.relationship("Mark")

    def __repr__(self):
        return "<Journal_of_performance> %r" % self.id
