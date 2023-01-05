from pathlib import Path
from typing import Optional, Iterator

from pynanto.bootstrap import Bootstrap
from pynanto.bundles import Bundles, external_filename
from pynanto.resource import Resource, PathResource
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
            port: Optional[int] = None,
            stack_backtrack=1
    ) -> 'Config':

        self.set_routes(
            Routes()
            .add_route(self.bundle_route, self.bundles.to_response)
            .add_route('/', self.quickstart_index_response)
        )

        ef = external_filename(stack_backtrack)
        if ef is not None:
            self.bundles.add_flat_folder(ef.parent / 'remote', relative_to=ef.parent)
            self.bundles.add_flat_folder(ef.parent / 'common', relative_to=ef.parent)
            self.bundles.add_flat_folder(ef.parent / 'server/rpc', relative_to=ef.parent)
            remotepy = ef.parent / 'remote.py'
            server_rpc = ef.parent / 'server/rpc.py'

            def gen_remotepy() -> Iterator[Resource]:
                if remotepy.exists():
                    yield PathResource('remote.py', remotepy)
                if server_rpc.exists():
                    yield PathResource('server/rpc.py', server_rpc)
            self.bundles.add_resources(gen_remotepy)

        pynanto_remote = Path(__file__).parent
        self.bundles.add_flat_folder(pynanto_remote / 'remote', relative_to=pynanto_remote.parent)
        # language=python
        load_default_bundle = f"""
import sys
from pyodide.http import pyfetch
response = await pyfetch('{self.bundle_route}')
await response.unpack_archive(extract_dir='/default_bundle')
sys.path.insert(0, '/default_bundle')
"""
        self.bootstrap.add_python(load_default_bundle)
        # language=python
        self.bootstrap.add_python("""
import remote
await remote.main()
""")
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
