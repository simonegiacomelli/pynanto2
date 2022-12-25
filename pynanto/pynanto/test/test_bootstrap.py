import pytest
from playwright.sync_api import Page, expect

import pynanto
import pynanto.server.wait_url
from pynanto import Response, Routes, Bootstrap
from pynanto.server.find_port import find_port
from pynanto.test.avaialable_webservers import available_webservers


@pytest.mark.parametrize('webserver_class', available_webservers.classes, ids=available_webservers.ids)
def test_bootstrap(page: Page, webserver_class):
    bootstrap_javascript = Bootstrap().set_python(
        'from js import document\n' +
        'document.getElementById("tag1").value = "Hello world!"\n'
    ).get_javascript()

    response = Response(f'<input id="tag1" value="Hello">'
                        f'<script>{bootstrap_javascript}</script>', 'text/html')

    routes = Routes().add_route('/', lambda: response)

    port = find_port()

    webserver_class() \
        .set_routes(routes) \
        .set_host('0.0.0.0') \
        .set_port(port) \
        .start_listen()

    url = f'http://127.0.0.1:{port}'
    pynanto.server.wait_url.wait_url(url + '/is_server_running')
    page.goto(url)

    expect(page.locator('id=tag1')).to_have_value('Hello world!')
