import sqlalchemy
from models.db_session import *


class User(SqlAlchemyBase):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    first_name = sqlalchemy.Column(sqlalchemy.VARCHAR(100))
    last_name = sqlalchemy.Column(sqlalchemy.VARCHAR(100))
    vk_id = sqlalchemy.Column(sqlalchemy.BigInteger, unique=True)
    course = sqlalchemy.Column(sqlalchemy.SmallInteger)
    group = sqlalchemy.Column(sqlalchemy.SmallInteger)
    subgroup = sqlalchemy.Column(sqlalchemy.SmallInteger)

