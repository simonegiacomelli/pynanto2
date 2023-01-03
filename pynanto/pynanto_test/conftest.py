import pytest
from playwright.sync_api import Page


@pytest.yield_fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    page.on('console', lambda msg: print(f'console [{msg.type}] ==== {msg.text}'))
    sep = '\n' + ('=' * 60) + '\n'
    page.on('pageerror', lambda exc: print(f'{sep}uncaught exception through pageerror: {sep}{exc}{sep}'))
    yield
    # print("I just experienced that this is not printed if the test fails")
