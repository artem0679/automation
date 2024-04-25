import datetime
from flask import Flask, render_template,flash, abort, send_from_directory, redirect, url_for, request
from flask_login import current_user
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from prometheus_client import generate_latest
from prometheus_client import Counter
from prometheus_client import Summary

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

from models import User, Form_of_education, Curriculum, Reporting_form, Journal_of_performance
from auth import bp as auth_bp, init_login_manager, check_rights

app.register_blueprint(auth_bp)

init_login_manager(app)

INDEX_TIME = Summary('index_request_processing_seconds', 'DESC: INDEX time spent processing request')
c = Counter('requests_for_host', 'Number of runs of the process_request method', ['method', 'endpoint'])




@app.route('/')
@INDEX_TIME.time()
def index():
    return render_template('index.html')


@app.route('/metrics')
def metrics():
    return generate_latest()


@app.route('/count_students', methods=["GET", "POST"])
def count_students():
    forms = Form_of_education.query.all()
    if request.method == "POST":
        form = request.form.get('form_of_education')
        students = User.query.filter_by(form_of_education_id=form).all()
        len_s = len(students)
        str_count_students = None
        if len_s == 1:
            str_count_students = f'Найден {len_s} студент, обучающийся'
        elif len_s > 1 and len_s < 5:
            str_count_students = f'Найдено {len_s} студента, обучающихся'
        elif len_s > 4:
            str_count_students = f'Найдено {len_s} студентов, обучающихся'
        form = Form_of_education.query.get(form)
        return render_template('students/count_students.html', forms=forms, str_count_students=str_count_students, form=form)
    return render_template('students/count_students.html', forms=forms)


@app.route('/count_hours', methods=["GET", "POST"])
def count_hours():
    disciplines = Curriculum.query.all()
    if request.method == "POST":
        discipline_id = int(request.form.get('discipline'))
        discipline = None
        for item in disciplines:
            if item.id == discipline_id:
                discipline = item
        return render_template('disciplines/count_hours.html', disciplines=disciplines, discipline=discipline)
    return render_template('disciplines/count_hours.html', disciplines=disciplines)

def get_json(fields_list):
    dict_ = {}
    for field in fields_list:
        dict_[field] = request.form.get(field)
    return dict_

@app.route('/add_student', methods=["GET", "POST"])
def add_student():
    forms = Form_of_education.query.all()
    if request.method=="POST":
        fields_list = [
            'login', 'last_name', 'first_name', 
            'middle_name', 'year_of_admission', 
            'form_of_education_id', 'group_number']
        dict_ = get_json(fields_list)
        dict_['role_id'] = app.config.get('STUDENT_ROLE_ID')
        student = User(**dict_)
        student.set_password(request.form.get('password'))
        try:
            db.session.add(student)
            db.session.commit()
            flash('Студент успешно добавлен', 'success')
            return redirect(url_for('index'))
        except:
            db.session.rollback()
            flash('Во время добавления студента произошла ошибка', 'danger', student='')
    return render_template('students/add_student.html', forms=forms, student='')


@app.route('/edit_student')
def edit_student_index():
    students = User.query.filter(User.role_id == app.config.get('STUDENT_ROLE_ID')).all()
    return render_template('students/edit_student_index.html', students=students)
    
@app.route('/edit_student/<int:student_id>', methods=["GET", "POST"])
def edit_student(student_id): 
    student = User.query.get(student_id)
    forms = Form_of_education.query.all()
    if request.method == "POST":
        student.login = request.form.get('login')
        student.last_name = request.form.get('last_name')
        student.first_name = request.form.get('first_name')
        student.middle_name = request.form.get('middle_name')
        student.year_of_admission = request.form.get('year_of_admission')
        student.form_of_education_id = request.form.get('form_of_education_id')
        student.group_number = request.form.get('group_number')
        try:
            db.session.commit()
            flash('Информация о студенте успешно отредактирована', 'success')
            return redirect(url_for('edit_student_index'))
        except:
            flash('При редактировании информации о студенте возникла ошибка', 'danger')
            db.session.rollback()
    return render_template('students/edit_student.html', student=student, forms=forms)

@app.route('/add_curriculum', methods=["GET", "POST"])
def add_curriculum():
    forms = Reporting_form.query.all()
    if request.method=="POST":
        fields_list = [
            'discipline_name', 'name_of_specialty', 'semester', 
            'number_of_hours', 'reporting_form_id']
        dict_ = get_json(fields_list)
        curriculum = Curriculum(**dict_)
        try:
            db.session.add(curriculum)
            db.session.commit()
            flash('Учбеный план успешно добавлен', 'success')
            return redirect(url_for('index'))
        except:
            db.session.rollback()
            flash('Во время добавления учебного плана произошла ошибка', 'danger')
    return render_template('curriculums/add_curriculum.html', forms=forms, curriculum='')

@app.route('/journal_of_performance')
def journal_of_performance():
    journals = Journal_of_performance.query.all()
    return render_template('journal_of_performance/index.html', journals=journals)
