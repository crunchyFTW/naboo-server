from sqlalchemy import Column, Integer, ForeignKey

from db.schemas.base_model import BaseDB


class Edge(BaseDB):
    __tablename__ = 'edges'

    parent_id = Column(Integer, ForeignKey('nodes.node_id'), primary_key=True)
    child_id = Column(Integer, ForeignKey('nodes.node_id'), primary_key=True)


    def __repr__(self):
        return f"<Edge(parent_id={self.parent_id}, child_id={self.child_id})>"