import pytest
from playwright.sync_api import Page, expect

from pynanto.server.find_port import find_port
from pynanto.server.wait_url import wait_url
from pynanto.test.avaialable_webservers import available_webservers


@pytest.mark.parametrize('webserver_class', available_webservers.classes, ids=available_webservers.ids)
def test_end2end(page: Page, webserver_class):
    import pynanto as pn

    setup = pn.Setup().quickstart()
    setup.bootstrap.set_python(
        """from js import document\n"""
        """document.body.innerHTML='<input id="tag1" value="Hello world!">'\n"""
    )
    setup.attach_webserver(webserver_class())
    setup.webserver.set_binding(('0.0.0.0', find_port()))
    setup.webserver.start_listen()

    url = f'http://127.0.0.1:{setup.webserver.port}'
    wait_url(url + '/is_server_running')

    page.goto(url)
    expect(page.locator('id=tag1')).to_have_value('Hello world!')
