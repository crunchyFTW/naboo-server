from pydantic import BaseModel


class NodeModel(BaseModel):
    id: int
    name: str
