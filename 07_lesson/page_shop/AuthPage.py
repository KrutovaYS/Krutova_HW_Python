from selenium.webdriver.common.by import By


class AuthPage():
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def open_shop(self):   # метод на открытие сайта
        self.driver.get("https://www.saucedemo.com/")

    def enter_login(self, username):
        user_name_field = self.driver.find_element(By.ID, 'user-name')
        user_name_field.clear()
        user_name_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.ID, 'password')
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, 'login-button').click()
