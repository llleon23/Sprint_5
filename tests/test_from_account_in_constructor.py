from selenium.webdriver.support.wait import WebDriverWait

import curl
from tests.conftest import driver
from data import Credentials
from locators import Locators
from selenium.webdriver.support import expected_conditions
import time

class TestTransitionsSection:
    def test_transitions_bread_section(self, driver):
        driver.get(curl.main_site)
        time.sleep(1)
        driver.find_element(*Locators.SAUCE_BUTTON).click()
        time.sleep(1)
        driver.find_element(*Locators.TOPPING_BUTTON).click()
        time.sleep(1)
        driver.find_element(*Locators.BREAD_BUTTON).click()
        time.sleep(1)

