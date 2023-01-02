from pathlib import Path

from playwright.sync_api import Page, expect

import pynanto as pn
from pynanto.server import find_port
from pynanto_test import for_all_webservers


def new_config(webserver_class) -> pn.Config:
    return pn.Config().quickstart(webserver_instance=webserver_class(), port=find_port(), blocking=False)


@for_all_webservers()
def test_bootstrap(page: Page, webserver_class):
    config = new_config(webserver_class)
    config.bootstrap.set_python(
        """from js import document\n"""
        """document.body.innerHTML='<input id="tag1" value="Hello world 1!">'\n"""
    )
    page.goto(config.webserver.localhost_url())
    expect(page.locator('id=tag1')).to_have_value('Hello world 1!')


@for_all_webservers()
def test_bootstrap_bundle(page: Page, webserver_class):
    config = new_config(webserver_class)
    config.bundles.add_file_content(
        'script1.py',
        """from js import document\n"""
        """document.body.innerHTML='<input id="tag1" value="Hello world 2!">'\n"""
    )
    config.set_main_module('script1')

    page.goto(config.webserver.localhost_url())
    expect(page.locator('id=tag1')).to_have_value('Hello world 2!')


@for_all_webservers()
def test_bootstrap_bundle_from_filesystem(page: Page, webserver_class):
    config = new_config(webserver_class)
    config.bundles.add_flat_folder(Path(__file__).parent / 'data' / 'for_remote')
    config.set_main_module('main')

    page.goto(config.webserver.localhost_url())
    expect(page.locator('id=tag1')).to_have_value('Hello world 3!')
