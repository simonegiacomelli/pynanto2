from abc import ABC, abstractmethod
from typing import Tuple

from pynanto.routes import Routes, Route


class Webserver(ABC):
    def __init__(self):
        self.host: str = '0.0.0.0'
        self.port: int = 7777
        self.routes = Routes()

    def set_host(self, host: str) -> 'Webserver':
        self.host = host
        return self

    def set_port(self, port: int) -> 'Webserver':
        self.port = port
        return self

    def set_binding(self, binding: Tuple[str, int]) -> 'Webserver':
        self.set_host(binding[0])
        self.set_port(binding[1])
        return self

    def set_routes(self, routes: Routes) -> 'Webserver':
        if routes is None:
            raise Exception(f'Parameter routes cannot be None')
        self.routes = routes

        for route in self.routes.list:
            self._setup_route(route)

        return self

    def start_listen(self) -> 'Webserver':
        self._start_listen()
        return self

    @abstractmethod
    def _setup_route(self, route: Route):
        pass

    @abstractmethod
    def _start_listen(self):
        pass
