from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


#Раздел «Конструктор» Проверь, что работают переходы к разделам: «Булки»
class TestConstructorBread:
    def test_constructor_bread(self, driver, enter_page_login_and_password):
        driver = enter_page_login_and_password
        WebDriverWait(driver,10).until(EC.visibility_of_element_located(Locators.SAUCE_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BREAD_BUTTON)).click()

        assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.ACTIVE_ELEMENT))

#Раздел «Конструктор» Проверь, что работают переходы к разделам: «Соусы»
class TestConstructorSauce:
    def test_constructor_sauce(self, driver, enter_page_login_and_password):
        driver = enter_page_login_and_password
        WebDriverWait(driver,10).until(EC.visibility_of_element_located(Locators.SAUCE_BUTTON)).click()

        assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.ACTIVE_ELEMENT))

#Раздел «Конструктор» Проверь, что работают переходы к разделам: «Начинки»
class TestConstructorTopping:
    def test_constructor_topping(self, driver, enter_page_login_and_password):
        driver = enter_page_login_and_password
        WebDriverWait(driver,10).until(EC.visibility_of_element_located(Locators.TOPPING_BUTTON)).click()

        assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.ACTIVE_ELEMENT))
