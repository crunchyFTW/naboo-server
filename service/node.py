from service.base import BaseService


class NodeService(BaseService):

    def __init__(self):
        super().__init__()
        self.repo = self.uow.node


    def get_nodes(self):
        return self.repo.get_all()


    def get_node_by_id(self, node_id: int):
        return self.repo.get_by_id(node_id)