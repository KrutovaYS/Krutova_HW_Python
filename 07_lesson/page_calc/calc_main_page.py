from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Main_Page():
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def open_calculator(self):   # Метод на открытие сайта
        self.driver.get(
            """https://bonigarcia.dev/selenium-webdriver-java/
            slow-calculator.html"""
        )
        self.wait = WebDriverWait(self.driver, 5)

    def set_delay(self, delay_value):
        # Вводит значение в поле
        delay = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        delay.clear()
        delay.send_keys(delay_value)

    def click_button(self, button_text):
        # Нажимает кнопку по тексту
        self.driver.find_element(
            By.XPATH, f"//span[text()='{button_text}']").click()

    def get_result(self):
        # Получает результат вычислений и сравнивает с ожидаемым
        txt = self.driver.find_element(By.CLASS_NAME, 'screen').text
        return txt
