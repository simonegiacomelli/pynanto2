import inspect
from pathlib import Path
from typing import Optional

from pynanto.bootstrap import Bootstrap
from pynanto.bundles import Bundles
from pynanto.response import Response
from pynanto.routes import Routes
from pynanto.webserver import Webserver
from pynanto.webserver import wait_forever
from pynanto.webservers.available_webservers import available_webservers


class Config:
    def __init__(self):
        self._routes = Routes()
        self.bootstrap = Bootstrap()
        self.bundles = Bundles()
        self.main_module = ''
        self._webserver: Optional[Webserver] = None
        self.bundle_route = '/pynanto/bundle/default.zip'

    @property
    def webserver(self) -> Webserver:
        if self._webserver is None:
            self._webserver = available_webservers().new_instance()
        return self._webserver

    def set_routes(self, routes: Routes) -> 'Config':
        if not self._routes.is_empty:
            raise Exception('routes are already set')
        self._error_if_attached()
        self._routes = routes
        return self

    def quickstart(
            self,
            blocking: bool = True,
            webserver_instance: Optional[Webserver] = None,
            port: Optional[int] = None
    ) -> 'Config':

        self.set_routes(
            Routes()
            .add_route(self.bundle_route, self.bundles.to_response)
            .add_route('/', self.quickstart_index_response)
        )

        source_file = Path(inspect.stack()[1].filename).resolve()
        root_folder = source_file.parent
        self.bundles.add_flat_folder(root_folder / 'remote', relative_to=root_folder)

        self.set_main_module('remote')
        if webserver_instance is None:
            webserver_instance = available_webservers().new_instance()

        self.attach_webserver(webserver_instance)
        if port is not None:
            self.webserver.set_port(port)
        self.webserver.start_listen()

        if blocking:
            wait_forever()
        else:
            self.webserver.wait_ready()

        return self

    def quickstart_index_response(self) -> Response:
        bootstrap_javascript = self.bootstrap.get_javascript()
        return Response(
            f'<h1>loading...</h1>'
            f'<script>{bootstrap_javascript}</script>'
            , 'text/html'
        )

    def attach_webserver(self, webserver: Webserver) -> 'Config':
        self._error_if_attached()
        self._webserver = webserver
        webserver.set_routes(self._routes)
        return self

    def _error_if_attached(self):
        if self._webserver is not None:
            raise Exception('Webserver already attached')

    def set_main_module(self, main_module: str):
        self.main_module = main_module
        self.bootstrap.set_python(self.entrypoint_code)

    @property
    def entrypoint_code(self) -> str:
        # language=python
        start_main_code = ''
        if self.main_module != '':
            start_main_code = f'import {self.main_module}'
        return f"""
import sys

from pyodide.http import pyfetch


response = await pyfetch('{self.bundle_route}')
await response.unpack_archive(extract_dir='/default_bundle')

sys.path.insert(0, '/default_bundle')

{start_main_code}
            """
