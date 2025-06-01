import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from curl import *
from locators import Locators
from data import Credentials




@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")
    service = Service('/Users/leonfatov/Documents/WebDriver/bin/chromedriver')
    browser = webdriver.Chrome(options=options, service=service)
    yield browser
    browser.quit()

@pytest.fixture
def enter_page_login_and_password(driver):
    enter_page = enter_site
    driver.get(enter_page)

    driver.find_element(*Locators.ENTR_EMAIL).send_keys(Credentials.email)
    driver.find_element(*Locators.ENTR_PASSWORD).send_keys(Credentials.password)
    driver.find_element(*Locators.ENTR_BUTTON).click()

    return driver

