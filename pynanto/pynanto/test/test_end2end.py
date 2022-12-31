from pathlib import Path

from playwright.sync_api import Page, expect

import pynanto
from pynanto.common.bundle import bundle_definition


@pynanto.test.for_all_webservers()
def test_bootstrap(page: Page, webserver_class):
    config = pynanto.start_default(webserver_class=webserver_class)
    config.bootstrap.set_python(
        """from js import document\n"""
        """document.body.innerHTML='<input id="tag1" value="Hello world!">'\n"""
    )
    page.goto(config.webserver.localhost_url())
    expect(page.locator('id=tag1')).to_have_value('Hello world!')


@pynanto.test.for_all_webservers()
def test_bootstrap_bundle(page: Page, webserver_class):
    config = pynanto.start_default(webserver_class=webserver_class)
    config.bundle.add_file_content(
        'script1.py',
        """from js import document\n"""
        """document.body.innerHTML='<input id="tag1" value="Hello world!">'\n"""
    )
    config.set_main_module('script1')

    page.goto(config.webserver.localhost_url())
    expect(page.locator('id=tag1')).to_have_value('Hello world!')


@pynanto.test.for_all_webservers()
def test_bootstrap_bundle_from_filesystem(page: Page, webserver_class):
    parent = Path(__file__).parent
    for_remote = parent / 'data' / 'for_remote'
    config = pynanto.start_default(webserver_class=webserver_class)
    config.bundle.add_resources(bundle_definition(for_remote))
    config.set_main_module('main')

    page.goto(config.webserver.localhost_url())
    expect(page.locator('id=tag1')).to_have_value('Hello world!')
