from playwright.sync_api import Page, expect

from pynanto import Webserver
from tests import for_all_webservers, new_config


@for_all_webservers()
def test_convention_remote_async_main(page: Page, webserver: Webserver):
    from .server import rpc
    config = new_config(webserver, rpc_module=rpc)
    page.goto(config.webserver.localhost_url())
    expected = 'remote=hello, common=42, server=42'
    expect(page.locator('body')).to_have_text(expected)
