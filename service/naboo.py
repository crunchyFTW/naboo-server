from service.base import BaseService
from route.schemas.node import NodeModel
from service.edge import EdgeService


class NabooService(BaseService):

    def __init__(self):
        super().__init__()


    @staticmethod
    def build_tree(node_id: int, nodes, edges):
        def _build_tree(_node_id):
            node_data = next((node for node in nodes if node['id'] == _node_id), None)
            if not node_data:
                return None

            children_ids = edges.get(_node_id, [])
            node_children = [_build_tree(child_id) for child_id in children_ids]
            return {
                "node_id": node_data["id"],
                "node_name": node_data["name"],
                "node_children": node_children
            }


        return _build_tree(node_id)


    def tree_get_all(self):
        naboo_items = self.uow.naboo.get_all()

        # get edges
        edges = EdgeService.generate_edges(naboo_items["edges"])

        # get nodes
        nodes = [NodeModel(id=n.node_id, name=n.node_name).dict() for n in naboo_items["nodes"]]
        root_node = next(filter(lambda node: node["id"] == 1, nodes))

        # generate tree
        node_tree = NabooService.build_tree(root_node["id"], nodes, edges)
        return {"tree": node_tree, "edges": edges}


    def get_tree_by_parent_id(self, id_list):
        naboo_items = self.uow.naboo.get_by_id(id_list)

        # get edges
        edges = EdgeService.generate_edges(naboo_items["edges"])

        # get nodes
        nodes = [NodeModel(id=n.node_id, name=n.node_name).dict() for n in naboo_items["nodes"]]
        root_node = next(filter(lambda node: node["id"] == 1, nodes))

        # generate tree
        node_tree = NabooService.build_tree(root_node["id"], nodes, edges)
        return {"tree": node_tree, "edges": edges}