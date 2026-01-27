from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

# Переход на страницу
driver.get("http://uitestingplayground.com/textinput")

# Указываем в поле ввода текст SkyPro
element = driver.find_element(
    By.CSS_SELECTOR, '#newButtonName')  # поиск элемента
element.send_keys("SkyPro")  # отправляем текст

# Нажимаем на синюю кнопку
driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()

# Получаем текст кнопки и печатаем в консоль
text = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text
print(text)

driver.quit()
