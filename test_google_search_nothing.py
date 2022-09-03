from selene.support.shared import browser
from selene import be, have, driver,by

#выполняем поиск без результатов
def test_search_selene():
    for_search_nothing = '<,.?":L{}||||-___+&%DFGHJK!@#!@#$%^&ERTYU'
    browser.element('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').should(be.blank).type(for_search_nothing).press_enter()
    browser.element('//*[@id="topstuff"]/div/div/p[1]').should(have.text(f'По запросу {for_search_nothing} ничего не найдено'))


