import json
from urllib.parse import urljoin
import requests

from .model import Post


def get_post(url: str, id_: int) -> Post:
    """Получает данные с сервера и возвращает в виде объекта модели  Post"""
    url = urljoin(url, str(id_))
    response = requests.get(url)
    if response.status_code == 200:
        return Post.parse_obj(json.loads(response.content.decode('utf-8')))
    else:
        raise ValueError(response.status_code)
