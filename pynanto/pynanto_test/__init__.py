from functools import partial

import pytest

import pynanto
from pynanto.server import find_port
from pynanto.webservers.available_webservers import available_webservers

for_all_webservers = partial(pytest.mark.parametrize, 'webserver_class', available_webservers().classes,
                             ids=available_webservers().ids)


def new_config(webserver_class) -> pynanto.Config:
    return pynanto.Config().quickstart(
        webserver_instance=webserver_class(),
        port=find_port(),
        blocking=False,
        stack_backtrack=2
    )
