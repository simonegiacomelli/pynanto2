from threading import Thread
from typing import Optional

from flask import Flask, Response

import pynanto.common
from pynanto.common import Webserver


class WsFlask(Webserver):
    def __init__(self):
        super().__init__()
        self.app = Flask(__name__)
        self.thread: Optional[Thread] = None

    def _setup_routes(self):
        for route in self.routes.list:
            def func() -> Response:
                pn_response: pynanto.common.Response = route.callback()
                return Response(pn_response.content, status=200, content_type=pn_response.content_type)

            self.app.add_url_rule(route.path, view_func=func)

    def _start_listen(self):
        def flask_run():
            self.app.run(host=self.host, port=self.port)

        self.thread = Thread(target=flask_run, daemon=True)
        self.thread.start()
