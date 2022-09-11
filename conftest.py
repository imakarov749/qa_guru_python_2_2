from selene.support.shared import browser
import pytest
from selene import have, be

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


#открываем браузер, проверяем корректность url закрываем после теста
@pytest.fixture()
def demo_qa_open_browser():
    browser.open('https://demoqa.com/automation-practice-form')

    # проверяем, что открытый url корректный
    browser.should(have.url('https://demoqa.com/automation-practice-form'))
    browser.element('.main-header').should(be.visible)
    yield
    browser.close()

#задаем конфигурацию браузера
@pytest.fixture(autouse=True)
def browser_configure(demo_qa_open_browser):
    browser.config.hold_browser_open = True
    browser.driver.set_window_size(1920, 1080)