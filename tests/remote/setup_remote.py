from playwright.sync_api import sync_playwright, expect

from tests import new_config
from wwwpy.webservers.python_embedded import WsPythonEmbedded


def fun():
    webserver = WsPythonEmbedded()
    new_config(webserver)

    p = sync_playwright().start()
    # browser = p.chromium.launch(headless=False)
    browser = p.chromium.launch()

    page = browser.new_page()

    page.on('console', lambda msg: print(f'console [{msg.type}] ==== {msg.text}'))
    sep = '\n' + ('=' * 60) + '\n'
    page.on('pageerror', lambda exc: print(f'{sep}uncaught exception through pageerror: {sep}{exc}{sep}'))

    page.goto(webserver.localhost_url())
    meta = page.locator('meta[name="unittest-result"]')
    meta.wait_for(state='attached')
    expect(meta).to_have_attribute('content', 'wasSuccessful=True', timeout=1)

    p.stop()


if __name__ == '__main__':
    fun()
