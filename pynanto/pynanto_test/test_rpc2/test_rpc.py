from playwright.sync_api import Page, expect

from pynanto import Webserver
from pynanto_test import for_all_webservers, new_config


@for_all_webservers()
def test_rpc_1234567890(page: Page, webserver: Webserver):
    new_config(webserver)

    page.goto(webserver.localhost_url())
    expect(page.locator('body')).to_have_text('42')
