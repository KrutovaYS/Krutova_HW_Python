from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Открыть браузер FireFox
driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

# Перейти на страницу http://the-internet.herokuapp.com/login
driver.get("http://the-internet.herokuapp.com/login")

# В поле username ввести значение tomsmith.
search_username = driver.find_element(By.ID, "username")
search_username.send_keys("tomsmith")

# В поле password ввести значение SuperSecretPassword!
search_password = driver.find_element(By.ID, "password")
search_password.send_keys("SuperSecretPassword!")

# Нажать кнопку Login
login_button = driver.find_element(
    By.XPATH, "//button[contains(@class, 'radius')]")
login_button.click()

# Вывести текст с зеленой плашки в консоль
text = driver.find_element(By.ID, "flash").text
print(text)

sleep(3)
driver.quit()  # Закрыть браузер
