from db.repository.naboo import NabooRepo
from db.repository.node import NodeRepo
from db.repository.edge import EdgeRepo
from common.db.db_context import DbContext


class UnitOfWork:
    node: NodeRepo
    edge: EdgeRepo
    naboo: NabooRepo


    def __init__(self):
        self.session = DbContext().SessionContext().get_session()
        self._initialize_repos()


    def _initialize_repos(self) -> object:
        UnitOfWork.node = NodeRepo(self.session)
        UnitOfWork.edge = EdgeRepo(self.session)
        UnitOfWork.naboo = NabooRepo(self.session)


    def clean(self):
        DbContext().SessionContext().close_session()
        self.session = None