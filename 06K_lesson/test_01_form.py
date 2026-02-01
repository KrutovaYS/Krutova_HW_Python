from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Edge()

    wait = WebDriverWait(driver, 15)

    # Открываем сайт
    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    wait.until(
        EC.presence_of_element_located((By.NAME, 'first-name'))
        )
    # Заполняем форму значениями
    data_form = {
        'first-name': 'Иван',
        'last-name': 'Петров',
        'address': 'Ленина, 55-3',
        'e-mail': 'test@skypro.com',
        'phone': '+7985899998787',
        'city': 'Москва',
        'country': 'Россия',
        'job-position': 'QA',
        'company': 'SkyPro'
        }

    for field, value in data_form.items():
        driver.find_element(By.NAME, field).send_keys(value)

    # Нажимаем на кнопку submit
    driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger"))
        )

    # Проверки
    zip_div = wait.until(
        EC.presence_of_element_located((By.ID, "zip-code"))
        )

    assert 'alert-danger' in zip_div.get_attribute(
        'class'), 'поле zip-code не красное'

    green_fields = [
        'first-name',
        'last-name',
        'address',
        'e-mail',
        'phone',
        'city',
        'country',
        'job-position',
        'company'
        ]

    for field in green_fields:
        element = driver.find_element(By.ID, field)
    assert 'alert-success' in element.get_attribute(
        'class'), f'{field} не зеленое'

    driver.quit()


test_form()
