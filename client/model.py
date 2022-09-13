from typing import List
from pydantic import BaseModel


class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str


# class Posts(BaseModel):
#     __root__: List[Post]