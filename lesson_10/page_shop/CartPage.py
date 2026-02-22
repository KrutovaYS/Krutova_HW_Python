from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage():
    """ Класс для работы со страницей Корзины на сайте SauceDemo.
    """
    def __init__(self, driver: WebDriver) -> None:
        """ Инициализация драйвера"""
        self.driver = driver

    def click_checkout(self) -> None:
        """ Нажать кнопку checkout """
        checkout = self.driver.find_element(By.ID, 'checkout')
        checkout.click()
