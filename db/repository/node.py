from sqlalchemy.sql import select

from db.schemas.node import Node
from db.repository.base import BaseRepo


class NodeRepo(BaseRepo):

    def __init__(self, session):
        super().__init__(session)


    def get_all(self):
        result = self.session.execute(select(Node)).all()
        return result


    def get_by_id(self, _id: int):
        query = select(Node).where(Node.node_id == _id)
        result = self.session.execute(query).one()
        return {"id": result[0].node_id, "name": result[0].node_name}
