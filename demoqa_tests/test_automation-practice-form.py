from selene.support.shared import browser
from selenium.webdriver import Keys
from selene import be, have


def test_fill_form():
    first_name = browser.element('#firstName')
    first_name.should(be.blank).type('Ivan')

    last_name = browser.element('#lastName')
    last_name.should(be.blank).type('Ivanov')

    email = browser.element('#userEmail')
    email.should(be.blank).type('ivan.ivanov@kljh.com')

    input_gender = browser.element("[for='gender-radio-1']")
    input_gender.click()

    mobile = browser.element('#userNumber')
    mobile.should(be.blank).type('7123456789')

    birth = browser.element('#dateOfBirthInput')
    #тут мб зря использовал Keys, но через clear не получилось
    #birth.clear().set_value('12 Dec 1912').press_enter()
    birth.send_keys(Keys.CONTROL + 'a').type('12 Dec 1912').press_enter()

    checkbox_hobbies = browser.element("[for='hobbies-checkbox-1']")
    checkbox_hobbies.click()

    adress = browser.element('#currentAddress')
    adress.should(be.blank).type('Moscow')

    # state_dropdown = browser.element('#state')
    # state_dropdown.click()

    submit = browser.element('#submit')
    submit.click()

    submitting_window = browser.element('#example-modal-sizes-title-lg')
    submitting_window.should(have.text('Thanks for submitting the form'))

    close_button = browser.element('#closeLargeModal')
    close_button.click()
