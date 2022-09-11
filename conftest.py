from selene.support.shared import browser
import pytest
from selene import have

#открываем браузер, проверяем корректность url закрываем после теста
@pytest.fixture()
def open_browser():
    url = ('https://google.com')
    browser.open(url)

    #проверяем, что открытый url корректный
    check_url = browser.should(have.url('https://www.google.com/'))
    print(check_url)
    yield
    browser.close()

#задаем конфигурацию браузера
@pytest.fixture(autouse=True)
def browser_configure(open_browser):
    browser.config.hold_browser_open = True
    browser.driver.set_window_size(1920, 1080)