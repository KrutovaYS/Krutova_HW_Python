from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Открыть браузер FireFox.
driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

# Перейти на страницу: http://the-internet.herokuapp.com/inputs
driver.get("http://the-internet.herokuapp.com/inputs")

# Ввести в поле текст Sky.
search_input = driver.find_element(By.CSS_SELECTOR, "input")
search_input.send_keys("Sky")

sleep(3)
# Очистить это поле (метод clear())
search_input.clear()

sleep(3)
# Ввести в поле текст Pro
search_input.send_keys("Pro")

sleep(3)
driver.quit()  # Закрыть браузер
