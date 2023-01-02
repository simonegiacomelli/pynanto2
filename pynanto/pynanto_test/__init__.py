from functools import partial

import pytest

from pynanto.webservers.available_webservers import available_webservers

for_all_webservers = partial(pytest.mark.parametrize, 'webserver_class', available_webservers().classes,
                             ids=available_webservers().ids)
