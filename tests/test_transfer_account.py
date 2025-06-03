from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import curl
from locators import Locators

#Переход в личный кабинет Проверь переход по клику на «Личный кабинет».
class TestTransferAccount:
    def test_transfer_account(self,driver,enter_page_login_and_password):
        driver = enter_page_login_and_password
        driver.find_element(*Locators.LK_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.profile_site))

        assert driver.current_url == curl.profile_site