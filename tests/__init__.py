from functools import partial
from types import ModuleType

import pytest

import wwwpy
from wwwpy import Webserver
from wwwpy.server import find_port
from wwwpy.webservers.available_webservers import available_webservers


def for_all_webservers():
    return partial(pytest.mark.parametrize, 'webserver', available_webservers().instances(),
                   ids=available_webservers().ids)()


def new_config(webserver: Webserver, rpc_module: ModuleType = None) -> wwwpy.Config:
    return wwwpy.Config().quickstart(
        webserver_instance=webserver,
        port=find_port(),
        blocking=False,
        stack_backtrack=2,
        rpc_module=rpc_module
    )
