from service.base import BaseService


class EdgeService(BaseService):

    def __init__(self):
        super().__init__()
        self.repo = self.uow.edge


    @staticmethod
    def generate_edges(edges_data):
        edges_result = {}
        for edge in edges_data:
            if edge.parent_id not in edges_result:
                edges_result[edge.parent_id] = [edge.child_id]
            else:
                edges_result[edge.parent_id].append(edge.child_id)
        return edges_result


    def get_edges(self):
        edges_data = self.repo.get_all()
        return EdgeService.generate_edges(edges_data)