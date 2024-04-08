from sqlalchemy.sql import select

from db.repository.base import BaseRepo
from db.schemas.edge import Edge


class EdgeRepo(BaseRepo):

    def __init__(self, session):
        super().__init__(session)


    def get_all(self):
        db_edges = self.session.execute(select(Edge)).all()
        return [e[0] for e in db_edges]


    def get_by_id(self, id):
        pass