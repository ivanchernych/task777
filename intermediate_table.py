import sqlalchemy
from data.db_session import SqlAlchemyBase


class Jobs_intermediate(SqlAlchemyBase):
    __tablename__ = 'jobs_intermediate'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'), autoincrement=True)
    job = sqlalchemy.Column(sqlalchemy.String)
    work_size = sqlalchemy.Column(sqlalchemy.Integer)
    collaborators = sqlalchemy.Column(sqlalchemy.String)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean)
    creates_user_id = sqlalchemy.Column(sqlalchemy.Integer)
    hazard_category = sqlalchemy.Column(sqlalchemy.Integer)