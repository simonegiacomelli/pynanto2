from playwright.sync_api import Page, expect

from tests import for_all_webservers, new_config
from wwwpy import Webserver


@for_all_webservers()
def test_rpc_1234567890(page: Page, webserver: Webserver):
    new_config(webserver)

    page.goto(webserver.localhost_url())
    expect(page.locator('body')).to_have_text('42')
