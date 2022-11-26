import pytest
from selene.support.shared import browser

base_url = 'https://google.com'

@pytest.fixture()
def open_browser():
    browser.config.window_width = 800
    browser.config.window_height = 600
    browser.open(base_url)
