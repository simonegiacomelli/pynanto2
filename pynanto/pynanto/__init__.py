from pathlib import Path
from typing import Union, Callable, List, NamedTuple, Optional, Tuple

from pynanto import server
from pynanto.common.bundle import PathResource, Resource, StringResource


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

    def set_binding(self, binding: Tuple[str, int]):
        self.set_host(binding[0])
        self.set_port(binding[1])

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
    def __init__(self):
        self.list: List[Resource] = []

    def add_file_content(self, filename: str, content: str):
        self.list.append(StringResource(filename, content))


class Setup:
    def __init__(self):
        self.routes = Routes()
        self.bootstrap = Bootstrap()
        self._webserver: Optional[Webserver] = None
        self.bundles: List[Bundle] = []
        self.entrypoint = ''

    @property
    def webserver(self) -> Webserver:
        result = self._webserver
        if result is None:
            raise Exception('')

        return result

    def set_routes(self, routes: Routes) -> 'Setup':
        if not self.routes.is_empty:
            raise Exception('routes are already set')
        self._error_if_attached()
        self.routes = routes
        return self

    def add_bundle(self, bundle: Bundle) -> 'Setup':
        self.bundles.append(bundle)
        return self

    def new_bundle(self) -> Bundle:
        bundle = Bundle()
        self.bundles.append(bundle)
        return bundle

    def set_main(self, script) -> 'Setup':
        return self

    def quickstart(self) -> 'Setup':

        def quickstart_index() -> Response:
            bootstrap_javascript = self.bootstrap.get_javascript()
            return Response(f'<h1>loading...</h1>'
                            f'<script>{bootstrap_javascript}</script>', 'text/html')

        self.set_routes(Routes().add_route('/', quickstart_index))

        return self

    def attach_webserver(self, webserver: Webserver):
        self._error_if_attached()
        self._webserver = webserver
        webserver.set_routes(self.routes)

    def _error_if_attached(self):
        if self._webserver is not None:
            raise Exception('Webserver already attached')

    def set_entrypoint(self, entrypoint: str):
        self.entrypoint = entrypoint


class Bootstrap:
    def __init__(self):
        self.remote_python = 'from js import document\n' + \
                             'document.body.innerHTML = "<h1>bootstrap done. No remote python specified</h1>"'

    def set_python(self, remote_python: str) -> 'Bootstrap':
        self.remote_python = remote_python
        return self

    def get_javascript(self) -> str:
        parent = Path(__file__).parent
        js = parent / 'bootstrap_pyodide.js'
        return js.read_text().replace('# python replace marker', self.remote_python)
