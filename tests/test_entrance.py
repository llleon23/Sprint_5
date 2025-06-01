from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import curl
from data import Credentials
from locators import Locators

faker = Faker()

class