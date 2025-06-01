from selenium.webdriver.common.by import By


class Locators:
    # Страница входа в лк https://stellarburgers.nomoreparties.site/login
    ENTR_EMAIL = (By.XPATH, "//div[label[contains(text(),'Email')]]//input")  # поле email
    ENTR_PASSWORD = (By.XPATH, "//input[@name='Пароль']")  # поле Пароль
    ENTR_BUTTON = (By.XPATH, "//button[text()='Войти']")  # кнопка Войти
    CONSTRUKT_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # кнопка Конструктор
    LOGO_BUTTON = (By.CSS_SELECTOR, "svg[width='290'][height='50']")  # кнопка логотипа
    FORGOT_PAS_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']") # кнопка Восстановить пароль

    # Страница "Регистрация" https://stellarburgers.nomoreparties.site/register
    REG_NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::*")  # поле Имя
    REG_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::*")  # поле Email
    REG_PASSWORD = (By.XPATH, "//input[@name='Пароль']")  # поле Пароль
    REG_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # кнопка Зарегистрироваться
    REG_TEXT_NO = (By.XPATH, "//p[text()='Некорректный пароль']") # текст "Некорректный пароль" при вводе невалидного пароля
    REG_TEXT_USER = (By.XPATH, "//p[text()='Такой пользователь уже существует']") # текст 'Такой пользователь уже существует' при вводе данных зареганного пользователя
    REG_ENTER_BUTTON = (By.XPATH, "//a[text()='Войти']") # кнопка войти

    # Страница "Восстановление пароля" https://stellarburgers.nomoreparties.site/forgot-password
    FOG_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::*")  # поле Email
    FOG_BUTTON = (By.XPATH, "//button[text()='Восстановить']")  # кнопка Восстановить
    FOG_ENTER_BUTTON = (By.XPATH, "//a[text()='Войти']") # кнопка войти

    # Страница конструктора https://stellarburgers.nomoreparties.site/
    BREAD_BUTTON = (By.XPATH, "//span[text()='Булки']")  # кнопка Булки
    SAUCE_BUTTON = (By.XPATH, "//span[text()='Соусы']")  # кнопка Соусы
    TOPPING_BUTTON = (By.XPATH, "//span[text()='Начинки']")  # кнопка Начинки
    LK_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # кнопка Личный Кабинет
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") # кнопка войти в аккаунт
    ACTIVE_ELEMENT = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")

    # Страница профиля https://stellarburgers.nomoreparties.site/account/profile
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # кнопка "Выход"
