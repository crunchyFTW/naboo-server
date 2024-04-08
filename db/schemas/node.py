from sqlalchemy import Column, Integer, String

from db.schemas.base_model import BaseDB


class Node(BaseDB):
    __tablename__ = 'nodes'

    node_id = Column(Integer, primary_key=True)
    node_name = Column(String(30))


    def __repr__(self):
        return f"<Node(node_id={self.node_id}, node_name={self.node_name})>"