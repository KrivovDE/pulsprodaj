from pydantic import BaseModel


class Post(BaseModel):
    """Модель для хранения и сериализвции данных, предоставленных
       методом API, возвращающий информацию о посте
    """
    userId: int
    id: int
    title: str
    body: str


