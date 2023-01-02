from playwright.sync_api import Page, expect

import pynanto as pn
from pynanto.server import find_port
from pynanto_test import for_all_webservers


def new_config(webserver_class) -> pn.Config:
    return pn.Config().quickstart(webserver_instance=webserver_class(), port=find_port(), blocking=False)


@for_all_webservers()
def test_rpc_1234567890(page: Page, webserver_class):
    config = new_config(webserver_class)

    page.goto(config.webserver.localhost_url())
    expect(page.locator('body')).to_have_text('42')
