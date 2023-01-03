from playwright.sync_api import Page, expect

from pynanto_test import for_all_webservers, new_config


@for_all_webservers()
def test_convention_remotepy_async_main(page: Page, webserver_class):
    config = new_config(webserver_class)
    page.goto(config.webserver.localhost_url())
    expect(page.locator('body')).to_have_text('hello from remote.py')
