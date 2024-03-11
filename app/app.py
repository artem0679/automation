import datetime
from flask import Flask, render_template, abort, send_from_directory, redirect, url_for, request
from flask_login import current_user
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
application = app

app.config.from_pyfile('config.py')

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)

from models import User, Form_of_education
from auth import bp as auth_bp, init_login_manager

app.register_blueprint(auth_bp)

init_login_manager(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/count_students', methods=["GET", "POST"])
def count_students():
    forms = Form_of_education.query.all()
    if request.method == "POST":
        form = request.form.get('form_of_education')
        students = User.query.filter_by(form_of_education_id=form).all()
        count_students = len(students)
        form = Form_of_education.query.get(form)
        return render_template('students/count_students.html', forms=forms, count_students=count_students, form=form)
    return render_template('students/count_students.html', forms=forms)