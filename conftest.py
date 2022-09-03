from selene.support.shared import browser
import pytest

#открываем браузер, закрываем после теста
@pytest.fixture()
def open_browser():
    url = ('https://google.com')
    browser.open(url)

    #Тут не уверен в правильности и нужности assert, хотел проверить открытый url, но не смог понять, как
    #broweser.get() и прочие штуки не помогли
    assert url == 'https://google.com'
    yield
    browser.close()

#задаем конфигурацию браузера
@pytest.fixture(autouse=True)
def browser_configure(open_browser):
    browser.config.hold_browser_open = True
    browser.driver.set_window_size(1920, 1080)