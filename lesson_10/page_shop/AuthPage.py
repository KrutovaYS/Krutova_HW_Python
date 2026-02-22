from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AuthPage():
    """
    Класс для работы со страницей авторизации на сайте Sauce Demo
    """
    def __init__(self, driver: WebDriver) -> None:
        """ Открыть браузер на весь экран"""
        self.driver = driver

    def open_shop(self) -> None:
        """ Открыть сайт """
        self.driver.get("https://www.saucedemo.com/")

    def enter_login(self, username: str) -> None:
        """ Ввести логин """
        user_name_field = self.driver.find_element(By.ID, 'user-name')
        user_name_field.clear()
        user_name_field.send_keys(username)

    def enter_password(self, password: str) -> None:
        """ Ввести пароль """
        password_field = self.driver.find_element(By.ID, 'password')
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self) -> None:
        """ Нажать кнопку login """
        self.driver.find_element(By.ID, 'login-button').click()
