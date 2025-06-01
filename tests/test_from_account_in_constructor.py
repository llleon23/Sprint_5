from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import curl
from locators import Locators


# Проверь переход по клику на «Конструктор»
class TestFromAccountInConstructor:
    def test_from_account_in_constr(self, driver, enter_page_login_and_password):
        driver = enter_page_login_and_password
        driver.find_element(*Locators.LK_BUTTON).click()
        driver.find_element(*Locators.CONSTRUKT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.main_site))

        assert driver.current_url == curl.main_site

#Проверь переход по клику на логотип Stellar Burgers
class TestFromAccountInLogo:
    def test_from_account_in_logo(self, driver, enter_page_login_and_password):
        driver = enter_page_login_and_password
        driver.find_element(*Locators.LK_BUTTON).click()
        driver.find_element(*Locators.LOGO_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.main_site))

        assert driver.current_url == curl.main_site

