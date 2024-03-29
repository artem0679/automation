"""initial migration

Revision ID: 46ffd7593894
Revises: 
Create Date: 2024-03-10 22:27:04.980023

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '46ffd7593894'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('forms_of_education',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_forms_of_education'))
    )
    op.create_table('marks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number_mark', sa.Integer(), nullable=False),
    sa.Column('text_mark', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_marks'))
    )
    op.create_table('reporting_forms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_reporting_forms'))
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_roles'))
    )
    op.create_table('curriculums',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('discipline_name', sa.String(length=100), nullable=False),
    sa.Column('name_of_specialty', sa.String(length=100), nullable=False),
    sa.Column('semester', sa.Integer(), nullable=False),
    sa.Column('number_of_hours', sa.Integer(), nullable=False),
    sa.Column('reporting_form_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['reporting_form_id'], ['reporting_forms.id'], name=op.f('fk_curriculums_reporting_form_id_reporting_forms')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_curriculums'))
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=100), nullable=False),
    sa.Column('password_hash', sa.String(length=200), nullable=False),
    sa.Column('last_name', sa.String(length=100), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=False),
    sa.Column('middle_name', sa.String(length=100), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('year_of_admission', mysql.YEAR(), nullable=False),
    sa.Column('form_of_education_id', sa.Integer(), nullable=False),
    sa.Column('group_number', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['form_of_education_id'], ['forms_of_education.id'], name=op.f('fk_users_form_of_education_id_forms_of_education')),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], name=op.f('fk_users_role_id_roles')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('login', name=op.f('uq_users_login'))
    )
    op.create_table('journals_of_performance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('semester', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('curriculum_id', sa.Integer(), nullable=False),
    sa.Column('mark_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['curriculum_id'], ['curriculums.id'], name=op.f('fk_journals_of_performance_curriculum_id_curriculums')),
    sa.ForeignKeyConstraint(['mark_id'], ['marks.id'], name=op.f('fk_journals_of_performance_mark_id_marks')),
    sa.ForeignKeyConstraint(['student_id'], ['users.id'], name=op.f('fk_journals_of_performance_student_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_journals_of_performance'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('journals_of_performance')
    op.drop_table('users')
    op.drop_table('curriculums')
    op.drop_table('roles')
    op.drop_table('reporting_forms')
    op.drop_table('marks')
    op.drop_table('forms_of_education')
    # ### end Alembic commands ###
