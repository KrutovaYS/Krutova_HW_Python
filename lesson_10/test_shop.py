from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure
import pytest

from page_shop.MainPage import MainPage
from page_shop.CartPage import CartPage
from page_shop.AuthPage import AuthPage
from page_shop.InputFormPage import InputFormPage


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Web Shop SauceDemo")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("""
    Тест на авторизацию, добавление товаров в корзину
    и проверку их наличия в корзине
""")
@allure.description("""
    Проверка работы корзины на сайте SauceDemo.

    Шаги проверки:
    1. Авторизация на сайте,
    2. Добавление товаров в корзину:
        - Sauce labs backpack,
        - Sauce labs bolt t shirt,
        - Sauce labs onesie.
    3. Переходим в корзину и нажимаем Checkout.
    4. Заполняем форму ввода данными и нажимаем Continue.
    5. Проверяем итоговую стоимость: должна быть равна $58.29
""")
def test_Shop(driver):
    """
    Тест проверки работы корзины на сайте SauceDemo.
    Выполняет авторизацию, добавление товаров в корзину,
    заполнение данных и проверку итоговой суммы
    """
    wait = WebDriverWait(driver, 10)

    with allure.step("Создаем экземпляр страницы Авторизации"):
        auth_page = AuthPage(driver)

    with allure.step("Открываем сайт магазина: страницу авторизации"):
        auth_page.open_shop()

    with allure.step("Вводим логин"):
        auth_page.enter_login('standard_user')

    with allure.step("Вводим пароль"):
        auth_page.enter_password('secret_sauce')

    with allure.step("Нажимаем login"):
        auth_page.click_login()

    with allure.step("Ожидаем загрузки страницы с товарами"):
        wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'inventory_list'))
        )

    with allure.step("Создаем экземпляр главной страницы"):
        main_page = MainPage(driver)

    with allure.step("Добавляем товары в корзину"):
        main_page.add_to_cart()

    with allure.step("Переходим в корзину"):
        main_page.go_to_cart()

    with allure.step("Ожидаем появления кнопки Checkout"):
        wait.until(EC.presence_of_element_located((By.ID, 'checkout')))

    with allure.step("Создаем экземпляр страницы Корзины"):
        cart_page = CartPage(driver)

    with allure.step("Нажимаем Checkout"):
        cart_page.click_checkout()

    with allure.step("Ожидаем открытия страницы ввода данных"):
        wait.until(EC.presence_of_element_located((By.ID, 'continue')))

    with allure.step("Создаем экземпляр страницы с формой ввода данных"):
        input_form_page = InputFormPage(driver)

    with allure.step("Вводим first_name(имя)"):
        input_form_page.input_first_name('Yuliya')

    with allure.step("Вводим last_name(фамилия)"):
        input_form_page.input_last_name('Krutova')

    with allure.step("Вводим postal_code(индекс)"):
        input_form_page.input_postal_code('445144')

    with allure.step("Нажимаем Continue"):
        input_form_page.enter_continue()

    with allure.step("Получаем итоговую сумму со страницы"):
        total_label = input_form_page.total()

    with allure.step("Проверяем итоговую сумму"):
        assert '$58.29' in total_label, \
            f"Ожидалось '$58.29' в строке, получено '{total_label}'"
