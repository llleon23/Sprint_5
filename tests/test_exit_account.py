from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import curl
from locators import Locators

#Выход из аккаунта. Проверь выход по кнопке «Выйти» в личном кабинете.
class TestExitAccount:
    def test_exit_account(self, driver, enter_page_login_and_password):
        driver = enter_page_login_and_password
        driver.find_element(*Locators.LK_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.profile_site))
        driver.find_element(*Locators.EXIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.enter_site))

        assert driver.current_url == curl.enter_site