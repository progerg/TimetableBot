import sqlalchemy
from sqlalchemy import orm

from models.db_session import *


class Subject(SqlAlchemyBase):
    __tablename__ = 'subjects'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.VARCHAR(100))
    lecturer_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('lecturers.id'))
    lecturer = orm.relationship('Lecturer', lazy='selectin')
