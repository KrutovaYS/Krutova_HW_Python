from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    driver.get('https://www.saucedemo.com/')
    wait = WebDriverWait(driver, 20)
    # Авторизоваться
    user_name = driver.find_element(By.ID, 'user-name')
    user_name.send_keys('standard_user')
    password = driver.find_element(By.ID, 'password')
    password.send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    # Подождать загрузки
    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, 'inventory_list'))
        )
    # Найти и добавить товары в корзину
    backpack = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
    bolt_t_shirt = driver.find_element(
        By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    labs_onesie = driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie')
    backpack.click()
    bolt_t_shirt.click()
    labs_onesie.click()
    # Перейти в корзину
    cart_link = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    cart_link.click()
    # Нажать checkout
    checkout = driver.find_element(By.ID, 'checkout')
    checkout.click()
    # Заполнить форму своими данными
    first_name = driver.find_element(By.ID, 'first-name')
    first_name.send_keys('Yuliya')
    last_name = driver.find_element(By.ID, 'last-name')
    last_name.send_keys('Krutova')
    postal_code = driver.find_element(By.ID, 'postal-code')
    postal_code.send_keys('445144')
    # Нажать continue
    driver.find_element(By.ID, 'continue').click()
    # Прочитать текст итога
    total_label = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, 'summary_total_label'))
        ).text
    # закрыть браузер
    driver.quit()
    # Проверить условие
    assert '$58.29' in total_label


test_shop()
