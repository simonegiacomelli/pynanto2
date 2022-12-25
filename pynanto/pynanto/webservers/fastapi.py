from threading import Thread
from typing import Optional

import uvicorn
from fastapi import FastAPI
from fastapi.responses import Response

import pynanto.common
import pynanto.response
from pynanto import Webserver


class WsFastapi(Webserver):
    def __init__(self):
        super().__init__()
        self.app = FastAPI()
        self.thread: Optional[Thread] = None

    def _setup_routes(self):
        for route in self.routes.list:
            def func(*args) -> Response:
                pn_response: pynanto.response.Response = route.callback()
                return Response(content=pn_response.content, media_type=pn_response.content_type)

            self.app.add_route(route.path, route=func)

    def _start_listen(self):
        def run():
            uvicorn.run(self.app, host=self.host, port=self.port)

        self.thread = Thread(target=run, daemon=True)
        self.thread.start()
