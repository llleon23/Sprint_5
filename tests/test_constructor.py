from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


#Раздел «Конструктор» Проверь, что работают переходы к разделам: «Булки»
class TestConstructorComponents:
    def test_constructor_bread(self, driver, enter_page_login_and_password):
        driver = enter_page_login_and_password
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SAUCE_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BREAD_BUTTON)).click()
        bread_activ = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.ACTIVE_ELEMENT))

        assert bread_activ.is_displayed()

        button_activ = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.ACTIVE_ELEMENT))
        assert "Булки" in button_activ.text

#Раздел «Конструктор» Проверь, что работают переходы к разделам: «Соусы»
    def test_constructor_sauce(self, driver, enter_page_login_and_password):
        driver = enter_page_login_and_password
        WebDriverWait(driver,10).until(EC.visibility_of_element_located(Locators.SAUCE_BUTTON)).click()
        sauce_activ = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.ACTIVE_ELEMENT))

        assert sauce_activ.is_displayed()

        button_activ = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.ACTIVE_ELEMENT))
        assert "Соусы" in button_activ.text

    #Раздел «Конструктор» Проверь, что работают переходы к разделам: «Начинки»
    def test_constructor_topping(self, driver, enter_page_login_and_password):
        driver = enter_page_login_and_password
        WebDriverWait(driver,10).until(EC.visibility_of_element_located(Locators.TOPPING_BUTTON)).click()
        topping_activ = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.ACTIVE_ELEMENT))

        assert topping_activ.is_displayed()

        button_activ = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.ACTIVE_ELEMENT))
        assert "Начинки" in button_activ.text
