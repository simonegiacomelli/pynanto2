from typing import Optional

from pynanto import Bootstrap, Bundle, Response, Routes, Webserver
from pynanto.common.bundle import build_archive


class Config:
    def __init__(self):
        self._routes = Routes()
        self.bootstrap = Bootstrap()
        self.bundle = Bundle()
        self.main_module = ''
        self._webserver: Optional[Webserver] = None
        self.bundle_route = '/pynanto/bundle/default.zip'

    @property
    def webserver(self) -> Webserver:
        result = self._webserver
        if result is None:
            raise Exception('')

        return result

    def set_routes(self, routes: Routes) -> 'Config':
        if not self._routes.is_empty:
            raise Exception('routes are already set')
        self._error_if_attached()
        self._routes = routes
        return self

    def quickstart(self) -> 'Config':

        self.set_routes(
            Routes()
            .add_route(self.bundle_route, self.bundle_to_response)
            .add_route('/', self.quickstart_index_response)
        )

        return self

    def quickstart_index_response(self) -> Response:
        bootstrap_javascript = self.bootstrap.get_javascript()
        return Response(
            f'<h1>loading...</h1>'
            f'<script>{bootstrap_javascript}</script>'
            , 'text/html'
        )

    def bundle_to_response(self) -> Response:
        return Response(
            build_archive(self.bundle.list),
            'application/zip, application/octet-stream, application/x-zip-compressed, multipart/x-zip'
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
