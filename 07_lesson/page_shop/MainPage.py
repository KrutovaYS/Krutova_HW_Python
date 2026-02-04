from selenium.webdriver.common.by import By


class MainPage():
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        # Найти и добавить товары в корзину
        backpack = self.driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-backpack')
        backpack.click()
        bolt_t_shirt = self.driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
        bolt_t_shirt.click()
        labs_onesie = self.driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-onesie')
        labs_onesie.click()

    def go_to_cart(self):
        # Перейти в корзину
        cart_link = self.driver.find_element(
            By.CLASS_NAME, 'shopping_cart_link')
        cart_link.click()
