from __future__ import annotations

from time import sleep
from typing import TYPE_CHECKING, Optional

from .bootstrap import Bootstrap
from .bundle import Bundle
from .bundles import Bundles
from .resource import Resource, StringResource, PathResource
from .response import Response
from .routes import Routes, Route
from .webserver import Webserver
from .webservers.available_webservers import available_webservers

if True:  # workaround to stop Pycharm reordering Config import
    pass

from .config import Config

if TYPE_CHECKING:
    from .webservers.flask import WsFlask
    from .webservers.fastapi import WsFastapi


def ws_flask() -> WsFlask:
    from .webservers.flask import WsFlask
    return WsFlask()


def ws_fastapi() -> WsFastapi:
    from .webservers.fastapi import WsFastapi
    return WsFastapi()


def start_default(webserver_instance: Optional[Webserver] = None, port=None) -> Config:
    cfg = Config().quickstart()
    if webserver_instance is None:
        webserver_instance = available_webservers().new_instance()
    cfg.attach_webserver(webserver_instance)
    if port is not None:
        cfg.webserver.set_port(port)
    cfg.webserver.start_listen()
    cfg.webserver.wait_ready()
    return cfg


def wait_forever():
    while True:
        sleep(10)
