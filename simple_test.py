from selene.support.shared import browser
from selene import have, be

def test_try_find_selen(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))

def test_negative_case(open_browser):
    browser.element('[name="q"]').should(be.blank).type('uefpiqwf w1efpqwgefqbve').press_enter()
    browser.element('[id="result-stats"]').should(have.text('About 0 results'))
