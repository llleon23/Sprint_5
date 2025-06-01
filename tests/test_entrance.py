from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import curl
from data import Credentials
from locators import Locators


#Проверка вход по кнопке «Войти в аккаунт» на главной
class TestLogInAccountOnMainSite:
    def test_login_account_on_main_site(self, driver):
        driver.get(curl.main_site)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.enter_site))
        driver.find_element(*Locators.ENTR_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.ENTR_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.ENTR_BUTTON).click()

        assert WebDriverWait(driver, 10).until(EC.url_to_be(curl.main_site))

#Проверка вход через кнопку «Личный кабинет»
class TestLogInProfile:
    def test_login_profile(self, driver):
        driver.get(curl.main_site)
        driver.find_element(*Locators.LK_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.enter_site))
        driver.find_element(*Locators.ENTR_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.ENTR_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.ENTR_BUTTON).click()

        assert WebDriverWait(driver, 10).until(EC.url_to_be(curl.main_site))

#Проверка вход через кнопку в форме регистрации
class TestLogInPageRegistration:
    def test_login_page_reg(self, driver):
        driver.get(curl.reg_site)
        driver.find_element(*Locators.REG_ENTER_BUTTON).click()
        driver.find_element(*Locators.ENTR_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.ENTR_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.ENTR_BUTTON).click()

        assert WebDriverWait(driver, 10).until(EC.url_to_be(curl.main_site))

#Проверка вход через кнопку в форме восстановления пароля
class TestLogInForgotPassword:
    def test_login_forgot_password(self, driver):
        driver.get(curl.enter_site)
        driver.find_element(*Locators.FORGOT_PAS_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.forgot_password_site))
        driver.find_element(*Locators.FOG_ENTER_BUTTON).click()
        driver.find_element(*Locators.ENTR_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.ENTR_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.ENTR_BUTTON).click()

        assert WebDriverWait(driver, 10).until(EC.url_to_be(curl.main_site))

