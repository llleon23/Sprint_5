import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from curl import *

@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")

    service = Service('/Users/leonfatov/Documents/WebDriver/bin/chromedriver')
    browser = webdriver.Chrome(options=options, service=service)

    yield browser
    browser.quit()
