from selene.support.shared import browser
from selene import be, have, driver,by

import pytest
import urllib

@pytest.fixture()
def open_browser():
    url = ('https://google.com')

    #Открываем браузер в инкогнито, задаем его разрешение, оставляем открытым
    browser.config.hold_browser_open = True
    browser.open(url)
    browser.driver.set_window_size(1920, 1080)
    #assert opened_url == 'https://google.com'


def test_search_selene(open_browser):
    browser.element('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').should(be.blank).type('selene').press_enter()
    #browser.element('//*[@id="rso"]/div[1]/div/div/div[1]/div/a/h3').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
    browser.close()


