from datetime import datetime
from time import sleep
from urllib.parse import urljoin
from client import get_post


class Combine:
    """
    Класс Combine используется для хранения констант и содержит методы
    которые по заданному идентификатору поста возвращают ответ метода API
    """
    MAX_REQUESTS_COUNT = 30
    STOREDGE = {
        'https://jsonplaceholder.typicode.com/': [],
        'http://188.127.251.4:8240/': [],
    }

    def _clear(self):
        """
        Очищает из значений STOREDGE все timestamp старше одной минуты
        """
        curent_tm = int(datetime.now().timestamp())
        for k, v in self.STOREDGE.items():
            self.STOREDGE[k] = [el for el in v if el < curent_tm - 60]

    def _get_free_host(self) -> str:
        """ Из числа доступных заркал, формирут url для обращения к серверу
        и добавляет в значение STOREDGE, timestamp текущего обращеня
        """
        while True:
            self._clear()
            for k, v in self.STOREDGE.items():
                if len(v) < self.MAX_REQUESTS_COUNT:
                    self.STOREDGE[k].append(int(datetime.now().timestamp()))
                    return urljoin(k, 'posts/')
            sleep(1)

    def get_post(self, id_: int):
        """
        По заданному идентификатору поста возвращают ответ метода API
        :param id_: заданный идентификатор поста
        :return: модель класса Post
        """
        url = self._get_free_host()
        return get_post(url, id_)