from pathlib import Path

import pytest
from playwright.sync_api import Page, expect

import pynanto
from pynanto.common.bundle import bundle_definition
from pynanto.server.find_port import find_port
from pynanto.server.wait_url import wait_url
from pynanto.test.avaialable_webservers import available_webservers


@pytest.mark.parametrize('webserver_class', available_webservers.classes, ids=available_webservers.ids)
def test_bootstrap(page: Page, webserver_class):
    setup = pynanto.Config().quickstart()
    setup.bootstrap.set_python(
        """from js import document\n"""
        """document.body.innerHTML='<input id="tag1" value="Hello world!">'\n"""
    )
    url = webserver_start(setup, webserver_class)

    page.goto(url)
    expect(page.locator('id=tag1')).to_have_value('Hello world!')


@pytest.mark.parametrize('webserver_class', available_webservers.classes, ids=available_webservers.ids)
def test_bootstrap_bundle(page: Page, webserver_class):
    setup = pynanto.Config().quickstart()
    setup.bundle.add_file_content(
        'script1.py',
        """from js import document\n"""
        """document.body.innerHTML='<input id="tag1" value="Hello world!">'\n"""
    )
    setup.set_main_module('script1')
    url = webserver_start(setup, webserver_class)

    page.goto(url)
    expect(page.locator('id=tag1')).to_have_value('Hello world!')


@pytest.mark.parametrize('webserver_class', available_webservers.classes, ids=available_webservers.ids)
def test_bootstrap_bundle_from_filesystem(page: Page, webserver_class):
    parent = Path(__file__).parent
    for_remote = parent / 'data' / 'for_remote'
    setup = pynanto.Config().quickstart()
    setup.bundle.add_resources(bundle_definition(for_remote))
    setup.set_main_module('main')
    url = webserver_start(setup, webserver_class)

    page.goto(url)
    expect(page.locator('id=tag1')).to_have_value('Hello world!')


def webserver_start(setup, webserver_class):
    setup.attach_webserver(webserver_class())
    setup.webserver.set_binding(('0.0.0.0', find_port()))
    setup.webserver.start_listen()
    url = f'http://127.0.0.1:{setup.webserver.port}'
    wait_url(url + '/is_server_running')
    return url
