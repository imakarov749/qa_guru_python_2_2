from selene.support.shared import browser
from selene import be, have

import pytest


@pytest.fixture()
def open_browser():
    browser.open("https://google.com")


def test_first(open_browser):
    pass
