import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    
    yield browser
    browser.quit()