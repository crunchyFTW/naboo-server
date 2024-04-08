from pydantic import BaseModel
from typing import List

from route.schemas.node import NodeModel


class NabooModel(BaseModel):
    id: int
    name: str
    children: List[int]


class NabooResponse(BaseModel):
    nodes: List[NodeModel]
    edges:  List[NabooModel]
