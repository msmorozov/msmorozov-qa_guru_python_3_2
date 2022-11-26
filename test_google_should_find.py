from selene.support.shared import browser
from selene import have, be


def test_try_find_selen(open_browser):
    positive_search = 'selene'
    positive_search_result = 'yashaka/selene: User-oriented Web UI browser tests in Python'

    browser.element('[name="q"]').should(be.blank).type(positive_search).press_enter()
    browser.element('[id="search"]').should(have.text(positive_search_result))
