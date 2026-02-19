from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    driver = webdriver.Chrome(
        service=ChromeService((ChromeDriverManager().install())))

    wait = WebDriverWait(driver, 50)

    # Открываем сайт
    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    # Вводим значение 45
    delay = driver.find_element(By.CSS_SELECTOR, '#delay')
    delay.clear()
    delay.send_keys('45')

    # Нажимаем на кнопки
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    wait.until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )

    result = driver.find_element(By.CLASS_NAME, 'screen').text
    assert result == '15'

    driver.quit()


test_calc()
