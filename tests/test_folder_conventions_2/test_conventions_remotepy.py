from playwright.sync_api import Page, expect

from tests import for_all_webservers, new_config
from wwwpy import Webserver


@for_all_webservers()
def test_convention_remotepy_async_main(page: Page, webserver: Webserver):
    config = new_config(webserver)
    page.goto(config.webserver.localhost_url())
    expect(page.locator('body')).to_have_text('hello from remote.py')
