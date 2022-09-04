from selene.support.shared import browser
from selene import be, have, driver,by

#выполняем поиск
def test_search_selene():
    browser.element('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').should(be.blank).type('selene').press_enter()
    browser.element('//*[@id="rso"]/div[1]/div/div/div[1]/div/a/h3').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


