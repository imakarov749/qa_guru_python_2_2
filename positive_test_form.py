from selene.support.shared import browser
from selene import be, have, command, driver

from selenium.webdriver.common.keys import Keys

browser.config.hold_browser_open = True
browser.open('https://demoqa.com/automation-practice-form')
browser.driver.set_window_size(1920,1080)
browser.element('[class="practice-form-wrapper"]').should(have.text('Student Registration Form'))

#browser.execute_script("document.body.style.zoom='33%'")

first_name = browser.element('//*[@id="firstName"]')
first_name.should(be.blank).type('Ivan')

last_name = browser.element('//*[@id="lastName"]')
last_name.should(be.blank).type('Ivanov')

email = browser.element('//*[@id="userEmail"]')
email.should(be.blank).type('ivan.ivanov@kljh.com')

input_gender = browser.element('//*[@id="genterWrapper"]/div[2]/div[1]/label')
input_gender.click()

mobile = browser.element('//*[@id="userNumber"]')
mobile.should(be.blank).type('7123456789')

birth = browser.element('//*[@id="dateOfBirthInput"]')
birth.send_keys(Keys.CONTROL + 'a').type('12 Dec 1912')

close_calendar = browser.element('//*[@id="app"]/div/div/div[2]/div[3]')
close_calendar.click()

input_hobbies = browser.element('//*[@id="hobbiesWrapper"]/div[2]/div[1]/label')
input_hobbies.click()

adress = browser.element('//*[@id="currentAddress"]')
adress.should(be.blank).type('Moscow')

submit = browser.element('//*[@id="submit"]')
submit.click()

submitting_window = browser.element('//*[@id="example-modal-sizes-title-lg"]').should(have.text('Thanks for submitting the form'))

close_button = browser.element('//*[@id="closeLargeModal"]')
close_button.click()