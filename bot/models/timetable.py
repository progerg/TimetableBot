import sqlalchemy
from sqlalchemy import orm

from models.db_session import *


class Timetable(SqlAlchemyBase):
    __tablename__ = 'timetable'
    __table_args__ = {"extend_existing": True}

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    subject_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('subjects.id'))
    subject = orm.relationship('Subject', lazy='selectin')
    course = sqlalchemy.Column(sqlalchemy.SmallInteger)
    group = sqlalchemy.Column(sqlalchemy.SmallInteger)
    subgroup = sqlalchemy.Column(sqlalchemy.SmallInteger)
    day = sqlalchemy.Column(sqlalchemy.VARCHAR(50))
    excel = sqlalchemy.Column(sqlalchemy.VARCHAR(10))
    start = sqlalchemy.Column(sqlalchemy.VARCHAR(5))
    end = sqlalchemy.Column(sqlalchemy.VARCHAR(5))
    numerator = sqlalchemy.Column(sqlalchemy.Boolean)
    cabinet = sqlalchemy.Column(sqlalchemy.VARCHAR(10))
    distance = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
