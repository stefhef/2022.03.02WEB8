import datetime
import sqlalchemy
from sqlalchemy import String, Integer, Boolean, Date, ForeignKey
from sqlalchemy.orm import relation
from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(Integer, ForeignKey('users.id'))
    job = sqlalchemy.Column(String)
    work_size = sqlalchemy.Column(Integer)
    collaborators = sqlalchemy.Column(String)
    end_date = sqlalchemy.Column(Date)
    start_date = sqlalchemy.Column(Date, default=datetime.datetime.now)
    is_finished = sqlalchemy.Column(Boolean)

    team_leader_instance = relation("User")
