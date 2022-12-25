from typing import Optional, List

from pynanto import Bootstrap, Bundle, Response, Routes, Webserver


class Config:
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

    def set_routes(self, routes: Routes) -> 'Config':
        if not self.routes.is_empty:
            raise Exception('routes are already set')
        self._error_if_attached()
        self.routes = routes
        return self

    def add_bundle(self, bundle: Bundle) -> 'Config':
        self.bundles.append(bundle)
        return self

    def new_bundle(self) -> Bundle:
        bundle = Bundle()
        self.bundles.append(bundle)
        return bundle

    def set_main(self, script) -> 'Config':
        return self

    def quickstart(self) -> 'Config':

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
