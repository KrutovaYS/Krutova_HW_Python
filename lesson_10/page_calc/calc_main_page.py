from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
import allure


class Main_Page():
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    @allure.step("Открыть страницу с калькулятором")
    def open_calculator(self) -> None:
        """ Открыть сайт с калькулятором """
        base_url = "https://bonigarcia.dev"
        path = "/selenium-webdriver-java/slow-calculator.html"

        self.driver.get(base_url + path)
        self.wait = WebDriverWait(self.driver, 5)

    @allure.step("Установка задержки {delay_value}")
    def set_delay(self, delay_value: int) -> None:
        """ Ввести значение в поле delay.
            Значение delay - тип данных int.
            Определяет задержку показа результата в секундах"""
        delay = self.driver.find_element(By.ID, 'delay')
        delay.clear()
        delay.send_keys(str(delay_value))

    @allure.step("Нажатие кнопки '{button_text}'")
    def click_button(self, button_text: str) -> None:
        """ Нажать на кнопку button.
            Значение button-text - тип данных str.
            Это текст на кнопке, которую нужно нажать
        """
        self.driver.find_element(
            By.XPATH, f"//span[text()='{button_text}']").click()

    @allure.step("Получить результат вычислений")
    def get_result(self) -> str:
        """Получает результат вычислений"""
        txt = self.driver.find_element(By.CLASS_NAME, 'screen').text
        return txt
