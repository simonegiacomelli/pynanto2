from functools import partial
from threading import Thread
from typing import Optional

from flask import Flask, Response

import pynanto.response
from pynanto import Webserver
from pynanto.routes import Route


class WsFlask(Webserver):
    def __init__(self):
        super().__init__()

        self.app = Flask(__name__)
        # @self.app.route('/')
        # def x():
        #     pass
        self.thread: Optional[Thread] = None

    def _setup_routes(self):
        def func(r: Route) -> Response:
            return self.to_native_response(r.callback())

        for route in self.routes.list:
            self.app.add_url_rule(route.path, route.path, partial(func, route))

    def to_native_response(self, pn_response: pynanto.response.Response) -> Response:
        return Response(pn_response.content, status=200, content_type=pn_response.content_type)

    def _start_listen(self):
        def flask_run():
            self.app.run(host=self.host, port=self.port)

        self.thread = Thread(target=flask_run, daemon=True)
        self.thread.start()
