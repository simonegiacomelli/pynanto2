from functools import partial
from types import ModuleType

import pytest

import pynanto
from pynanto import Webserver
from pynanto.server import find_port
from pynanto.webservers.available_webservers import available_webservers


def for_all_webservers():
    return partial(pytest.mark.parametrize, 'webserver', available_webservers().instances(),
                   ids=available_webservers().ids)()


def new_config(webserver: Webserver, rpc_module: ModuleType = None) -> pynanto.Config:
    return pynanto.Config().quickstart(
        webserver_instance=webserver,
        port=find_port(),
        blocking=False,
        stack_backtrack=2,
        rpc_module=rpc_module
    )
