import sys

from playwright.sync_api import Page, expect

from pynanto import available_webservers, Config
from pynanto.common.bundle import bundle_definition


def main():
    print(sys.path)


if __name__ == '__main__':
    main()


def xtest1(page: Page):
    print('=' * 30)
    print(sys.path)
    return
    webserver_class = available_webservers().classes[0]
    cfg = Config().quickstart()
    cfg.attach_webserver(webserver_class())
    cfg.webserver.start_listen()
    cfg.webserver.wait_ready()
    cfg.bundle.add_resources(bundle_definition())
    config = cfg

    page.goto(config.webserver.localhost_url())
    expect(page.locator('id=tag1')).to_have_value('Hello world!')
