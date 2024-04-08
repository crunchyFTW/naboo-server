from sqlalchemy.sql import text, select

from common.db.db_context import DbContext
from db.schemas.base_model import BaseDB
from db.schemas.node import Node
from db.schemas.edge import Edge


def _create_db():
    engine = DbContext().get_or_create_connection()
    BaseDB.metadata.create_all(engine)
    with DbContext().SessionContext() as session:
        query = select(Node)
        result = session.execute(query).first()

    if not result:
        print("Table is empty")
        _insert_db_data()
    else:
        print("Table is not empty")
        result = session.execute(text("SHOW DATABASES;")).all()
        print(result)
        result = session.execute(text("SHOW TABLES;")).all()
        print(result)


def _insert_db_data():
    # Insert data into nodes table
    node_a = Node(node_id=1, node_name='Node A')
    node_b = Node(node_id=2, node_name='Node B')
    node_c = Node(node_id=3, node_name='Node C')
    node_d = Node(node_id=4, node_name='Node D')
    node_e = Node(node_id=5, node_name='Node E')
    node_f = Node(node_id=6, node_name='Node F')
    node_g = Node(node_id=7, node_name='Node G')
    node_h = Node(node_id=8, node_name='Node H')

    edge_ab = Edge(parent_id=1, child_id=2)
    edge_ac = Edge(parent_id=1, child_id=3)
    edge_ag = Edge(parent_id=1, child_id=7)
    edge_bd = Edge(parent_id=2, child_id=4)
    edge_ce = Edge(parent_id=3, child_id=5)
    edge_cf = Edge(parent_id=3, child_id=6)
    edge_eh = Edge(parent_id=5, child_id=8)

    with DbContext().SessionContext() as session:
        session.add_all([node_a, node_b, node_c, node_d, node_e, node_f, node_g, node_h])
        session.flush()
        session.add_all([edge_ab, edge_ac, edge_ag, edge_bd, edge_ce, edge_cf, edge_eh])
        session.flush()
        session.commit()


def setup_db():
    _create_db()