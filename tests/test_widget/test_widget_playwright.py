from playwright.sync_api import Page, expect

from tests import new_config
from wwwpy.webservers.python_embedded import WsPythonEmbedded


def test_widget_playwright(page: Page):
    webserver = WsPythonEmbedded()
    new_config(webserver)

    page.goto(webserver.localhost_url())

    meta = page.locator('meta[name="unittest-result"]')
    meta.wait_for(state='attached')
    expect(meta).to_have_attribute('content', 'wasSuccessful=True', timeout=1)
