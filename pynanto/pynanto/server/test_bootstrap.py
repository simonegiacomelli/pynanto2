from playwright.sync_api import Page, expect

import pynanto
from pynanto.common import Response, Routes
from pynanto.server.find_port import find_port
from pynanto.server.ws_flask import WsFlask


def test_bootstrap(page: Page):
    # pynanto.common.bootstrap_javascript
    bootstrap_javascript = """
    document.getElementById('tag1').value = 'Hello world!';
    """
    response = Response(f'<input id="tag1" value="Hello">'
                        f'<script>{bootstrap_javascript}</script>', 'text/html')

    def callback():
        return response

    routes = Routes().add_route('/', callback)

    port = find_port()
    ws = WsFlask()

    ws \
        .set_routes(routes) \
        .set_host('0.0.0.0') \
        .set_port(port) \
        .start_listen()

    url = f'http://127.0.0.1:{port}'
    pynanto.server.wait_url(url + '/is_server_running')
    page.goto(url)

    expect(page.locator('id=tag1')).to_have_value('Hello world!')
