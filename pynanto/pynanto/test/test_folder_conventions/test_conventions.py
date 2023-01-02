from playwright.sync_api import Page, expect

import pynanto as pn
from pynanto.server import find_port


def new_config(webserver_class) -> pn.Config:
    return pn.Config().quickstart(webserver_instance=webserver_class(), port=find_port(), blocking=False)


@pn.test.for_all_webservers()
def test_convention(page: Page, webserver_class):
    config = new_config(webserver_class)

    page.goto(config.webserver.localhost_url())
    expect(page.locator('id=tag1')).to_have_value('Hello conventions!', timeout=60000)
