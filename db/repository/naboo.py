from sqlalchemy.sql import select
from typing import List

from db.repository.base import BaseRepo
from db.schemas.node import Node
from db.schemas.edge import Edge


class NabooRepo(BaseRepo):

    def __init__(self, session):
        super().__init__(session)
        # self.base_edge_query = select(Edge).where(Edge.parent_id == 1)
        self.base_edge_id = 1


    def get_all(self):
        db_nodes = self.session.execute(select(Node)).all()
        nodes = [n[0] for n in db_nodes]
        db_edges = self.session.execute(select(Edge)).all()
        edges = [e[0] for e in db_edges]
        return {"nodes": nodes, "edges": edges}


    def get_by_id(self, parent_id_list: List[int]):
        parent_id_list.append(self.base_edge_id)
        db_nodes = self.session.execute(select(Node)).all()
        nodes = [n[0] for n in db_nodes]
        db_edges = self.session.execute(select(Edge).where(Edge.parent_id.in_(parent_id_list))).all()
        # db_edges_2 = self.session.execute(self.base_edge_query.where(or_(Edge.parent_id.in_(parent_id_list)))).all()
        # db_edges_3 = self.session.execute(self.base_edge_query.where(Edge.parent_id.in_(parent_id_list))).all()
        edges = [e[0] for e in db_edges]
        return {"nodes": nodes, "edges": edges}