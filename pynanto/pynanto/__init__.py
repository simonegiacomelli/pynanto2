from __future__ import annotations

from typing import TYPE_CHECKING

from pynanto.common.bundle import PathResource, Resource, StringResource
from .bootstrap import Bootstrap
from .bundle import Bundle
from .response import Response
from .routes import Routes, Route
from .webserver import Webserver

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
