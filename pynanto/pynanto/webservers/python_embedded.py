from functools import partial
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
from typing import Optional, Callable, Dict
from urllib.parse import urlparse, parse_qs

from pynanto.response import Response
from pynanto.routes import Route
from pynanto.webserver import Webserver
from pynanto.webserver import wait_forever


class WsPythonEmbedded(Webserver):
    def __init__(self):
        super().__init__()
        self.thread: Optional[Thread] = None
        self._routes: Dict[str, Route] = {}

    def _setup_route(self, route: Route):
        self._routes[route.path] = route

    def _start_listen(self):
        httpd = ThreadingHTTPServer((self.host, self.port), partial(RequestHandler, handler=self._handler))

        def run():
            print(f'Starting embedded python web server on http://{self.host}:{self.port}')
            httpd.serve_forever()

        self.thread = Thread(target=run, daemon=True)
        self.thread.start()

    def _handler(self, request: 'RequestHandler') -> bool:
        params, rpath = request.decode_request()
        route = self._routes.get(rpath, None)
        if route is None:
            nf = HTTPStatus.NOT_FOUND
            request.send_bytes(bytes(nf.phrase, 'utf8'), code=nf.value)
        else:
            resp = route.callback()
            content = resp.content
            if isinstance(content, str):
                content = bytes(content, 'utf8')
            if not isinstance(content, bytes):
                raise Exception(f'type of the content not supported: {type(content)}')
            request.send_bytes(content, content_type=resp.content_type)
        return True


class RequestHandler(SimpleHTTPRequestHandler):
    query_index = 4
    path_index = 2

    def __init__(self, *args
                 , handler: Callable[['RequestHandler'], bool]
                 , **kwargs):
        self.handler = handler
        super(RequestHandler, self).__init__(*args, **kwargs)

    def do_GET(self):
        if not self.handler(self):
            super(RequestHandler, self).do_GET()

    def decode_request(self):
        p = urlparse(self.path)
        query_str = p[self.query_index]
        rpath = p[self.path_index]
        di = parse_qs(query_str)
        params = {k: v[0] for k, v in di.items()}
        return params, rpath

    def send_bytes(self, content, code=200, content_type='text/plain'):
        self.protocol_version = "HTTP/1.1"
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(content)))
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Allow-Methods", "*")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(content)

    def serve_file(self, directory, filename):
        self.directory = directory
        self.path = '/' + filename
        super(RequestHandler, self).do_GET()


if __name__ == '__main__':
    s = WsPythonEmbedded()
    s._setup_route(Route('/', lambda: Response('ciao', 'text/html')))
    s.start_listen()
    wait_forever()