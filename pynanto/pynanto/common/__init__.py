from pathlib import Path
from typing import Union, Callable, List, NamedTuple


class Response(NamedTuple):
    content: Union[str, bytes]
    content_type: str


from abc import ABC, abstractmethod


class Route(NamedTuple):
    path: str
    callback: Callable[[], Response]


class Routes:
    def __init__(self):
        self.list: List[Route] = []

    def add_root_index(self) -> 'Routes':
        return self

    def add_route(self, path: str, callback: Callable[[], Response]) -> 'Routes':
        self.list.append(Route(path, callback))
        return self

    @property
    def is_empty(self) -> bool:
        return len(self.list) == 0


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

    def set_routes(self, routes: Routes) -> 'Webserver':
        if routes is None:
            raise Exception(f'Parameter routes cannot be None')
        self.routes = routes
        self._setup_routes()
        return self

    def start_listen(self) -> 'Webserver':
        self._start_listen()
        return self

    @abstractmethod
    def _setup_routes(self):
        pass

    @abstractmethod
    def _start_listen(self):
        pass


class Bundle:
    def add_file(self, file: Path) -> 'Bundle':
        return self


class Remote:
    def set_routes(self, bootstrap: Routes) -> 'Remote':
        return self

    def add_bundle(self, bundle: Bundle) -> 'Remote':
        return self

    def set_main(self, script) -> 'Remote':
        return self

    def attach_webserver(self, webserver: Webserver):
        pass


class Bootstrap:
    def __init__(self):
        self.remote_python = ''

    def set_python(self, remote_python: str) -> 'Bootstrap':
        self.remote_python = remote_python
        return self

    def get_javascript(self) -> str:
        parent = Path(__file__).parent
        js = parent / 'bootstrap.js'
        return js.read_text().replace('# python replace marker', self.remote_python)
