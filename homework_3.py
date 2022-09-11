def func_print(func_name, *args):
    func_name = func_name.__name__.replace("_", " ").capitalize()
    print(f"Function name: {func_name}. Function Arguments:", *args)


def open_browser(browser_name):
    func_print(open_browser, browser_name)


def go_to_company_name_homepage(page_url):
    func_print(go_to_company_name_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    func_print(find_registration_button_on_login_page, page_url, button_text)


open_browser('Google Chrome')
go_to_company_name_homepage('https://vk.com/')
find_registration_button_on_login_page('https://vk.com/', 'Зарегистрироваться')
