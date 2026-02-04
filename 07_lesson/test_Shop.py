from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


from page_shop.MainPage import MainPage
from page_shop.CartPage import CartPage
from page_shop.AuthPage import AuthPage
from page_shop.InputFormPage import InputFormPage


def test_Shop():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    wait = WebDriverWait(driver, 20)

    auth_page = AuthPage(driver)  # Переменная хранит экземпляр класса AuthPage
    auth_page.open_shop()
    auth_page.enter_login('standard_user')
    auth_page.enter_password('secret_sauce')
    auth_page.click_login()
    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, 'inventory_list')))

    main_page = MainPage(driver)  # Переменная хранит экземпляр класса MainPage
    main_page.add_to_cart()
    main_page.go_to_cart()
    wait.until(EC.presence_of_element_located((By.ID, 'checkout')))

    cart_page = CartPage(driver)  # Переменная хранит экземпляр класса CartPage
    cart_page.click_checkout()
    wait.until(EC.presence_of_element_located((By.ID, 'continue')))

    input_form_page = InputFormPage(driver)
    input_form_page.input_first_name('Yuliya')
    input_form_page.input_last_name('Krutova')
    input_form_page.input_postal_code('445144')
    input_form_page.enter_continue()
    total_label = input_form_page.total()

    driver.quit()

    # Проверить условие
    assert '$58.29' in total_label
