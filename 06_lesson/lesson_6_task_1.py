from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(20)  # поместим метод ожидания перед переходом на сайт

driver.get("http://uitestingplayground.com/ajax")  # Перейдите на страницу

# Нажимаем на синюю кнопку
element = driver.find_element(By.CSS_SELECTOR, '#ajaxButton').click()
# Получаем текст из зеленой плашки
text = driver.find_element(By.CSS_SELECTOR, "p.bg-success").text
# Печатаем в консоль полученный текст
print(text)

driver.quit()
