from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Открыть браузер Google Chrome
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

# Перейти на страницу: http://uitestingplayground.com/classattr
driver.get("http://uitestingplayground.com/classattr")

# Кликнуть на синюю кнопку
blue_button = driver.find_element(
    By.XPATH, "//button[contains(@class, 'btn-primary')]")
blue_button.click()
sleep(30)
