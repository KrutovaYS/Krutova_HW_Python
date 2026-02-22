from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage():
    """ Класс для работы с главной страницей сайта SauceDemo"""
    def __init__(self, driver: WebDriver) -> None:
        """ Инициализация главной страницы"""
        self.driver = driver

    def add_to_cart(self) -> None:
        """ Найти и добавить товары в корзину """
        backpack = self.driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-backpack')
        backpack.click()
        bolt_t_shirt = self.driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
        bolt_t_shirt.click()
        labs_onesie = self.driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-onesie')
        labs_onesie.click()

    def go_to_cart(self) -> None:
        """ Перейти в корзину """
        cart_link = self.driver.find_element(
            By.CLASS_NAME, 'shopping_cart_link')
        cart_link.click()
