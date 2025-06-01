from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import curl
from data import Credentials
from locators import Locators

faker = Faker()

#Успешную регистрацию
class TestRegistaionSucces:
    def test_registration_true(self, driver):
        driver.get(curl.reg_site)
        driver.find_element(*Locators.REG_NAME).send_keys(*Credentials.name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(faker.email())
        driver.find_element(*Locators.REG_PASSWORD).send_keys(faker.password())
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.enter_site))

        assert driver.current_url == curl.enter_site

#Поле «Имя» должно быть не пустым
class TestRegistaionNoName:
    def test_registration_no_name(self, driver):
        driver.get(curl.reg_site)
        driver.find_element(*Locators.REG_EMAIL).send_keys(faker.email())
        driver.find_element(*Locators.REG_PASSWORD).send_keys(faker.password())
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.reg_site))

        assert driver.current_url == curl.reg_site

#B поле Email введён email в формате логин@домен: например, 123@ya.ru.
class TestRegistaionEmailNoCorrect:
    def test_registration_email_no_correct(self, driver):
        driver.get(curl.reg_site)
        driver.find_element(*Locators.REG_NAME).send_keys(*Credentials.name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(faker.password()) # проверка без "123@ya.ru"
        driver.find_element(*Locators.REG_PASSWORD).send_keys(faker.password())
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.reg_site))

        assert driver.current_url == curl.reg_site

#Минимальный пароль — шесть символов.
class TestRegistaionMinimalPassword:
    def test_registration_five_symbol_password(self, driver):
        driver.get(curl.reg_site)
        driver.find_element(*Locators.REG_NAME).send_keys(*Credentials.name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(faker.email())
        driver.find_element(*Locators.REG_PASSWORD).send_keys(faker.password(5))
        driver.find_element(*Locators.REG_BUTTON).click()

        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.REG_TEXT_NO))

#Ошибку для некорректного пароля.
class TestRegistaionRegisteredUser:
    def test_registration_registered_user(self, driver):
        driver.get(curl.reg_site)
        driver.find_element(*Locators.REG_NAME).send_keys(*Credentials.name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(*Credentials.email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(*Credentials.password)
        driver.find_element(*Locators.REG_BUTTON).click()

        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.REG_TEXT_USER))

# Поле «Email» должно быть не пустым
class TestRegistaionNoEmail:
    def test_registration_no_email(self, driver):
        driver.get(curl.reg_site)
        driver.find_element(*Locators.REG_NAME).send_keys(*Credentials.name)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(faker.password())
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.reg_site))

        assert driver.current_url == curl.reg_site

# Поле «Пароль» должно быть не пустым
class TestRegistaionNoPassword:
    def test_registration_no_password(self, driver):
        driver.get(curl.reg_site)
        driver.find_element(*Locators.REG_NAME).send_keys(*Credentials.name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(faker.email())
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.reg_site))

        assert driver.current_url == curl.reg_site