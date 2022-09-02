import sqlalchemy
from models.db_session import *


class Lecturer(SqlAlchemyBase):
    __tablename__ = 'lecturers'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.VARCHAR(100))
    academic_degree = sqlalchemy.Column(sqlalchemy.VARCHAR(50))
