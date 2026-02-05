from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InputFormPage():
    def __init__(self, driver):
        self.driver = driver

    def input_first_name(self, text):
        # Ввести имя
        first_name = self.driver.find_element(By.ID, 'first-name')
        first_name.send_keys(text)

    def input_last_name(self, text):
        # Ввести фамилию
        last_name = self.driver.find_element(By.ID, 'last-name')
        last_name.send_keys(text)

    def input_postal_code(self, text):
        # Ввести индекс
        postal_code = self.driver.find_element(By.ID, 'postal-code')
        postal_code.send_keys(text)

    def enter_continue(self):
        # Нажать continue
        self.driver.find_element(By.ID, 'continue').click()

    def total(self):
        # Прочитать текст итога
        wait = WebDriverWait(self.driver, 10)
        total_label = wait.until(
            EC.presence_of_element_located((
                By.CLASS_NAME, 'summary_total_label'))).text
        return total_label
