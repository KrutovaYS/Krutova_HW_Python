from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

waiter = WebDriverWait(driver, 15)
# Переходим на страницу
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Дождитесь загрузки всех картинок.
waiter.until(
    lambda driver: len(driver.find_elements(
        By.CSS_SELECTOR, "#image-container img"
    )) == 4
)

images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")

# Берем 3-ю, находим атрибут и выводим в консоль
src_img3 = images[2].get_attribute("src")
print(src_img3)

driver.quit()
