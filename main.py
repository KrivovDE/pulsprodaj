from datetime import datetime
from time import sleep
from urllib.parse import urljoin

from client import get_post, get_posts


class Combine:
    MAX_REQUESTS_COUNT = 30
    STOREDGE = {
        'https://jsonplaceholder.typicode.com/': [],
        'http://188.127.251.4:8240/': [],
    }

    def _clear(self):
        curent_tm = int(datetime.now().timestamp())
        for k, v in self.STOREDGE.items():
            self.STOREDGE[k] = [el for el in v if el < curent_tm - 60]

    def _get_free_host(self) -> str:
        while True:
            self._clear()
            for k, v in self.STOREDGE.items():
                if len(v) < self.MAX_REQUESTS_COUNT:
                    self.STOREDGE[k].append(int(datetime.now().timestamp()))
                    return urljoin(k, 'posts/')
            sleep(1)

    def get_post(self, id_: int):
        url = self._get_free_host()
        return get_post(url, id_)