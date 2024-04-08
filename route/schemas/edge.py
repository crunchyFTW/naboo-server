from pydantic import BaseModel


class EdgeModel(BaseModel):
    parent_id: int
    child_id: int