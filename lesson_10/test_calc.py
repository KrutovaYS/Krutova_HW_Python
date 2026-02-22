from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import pytest

from page_calc.calc_main_page import Main_Page


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome(
        service=ChromeService((ChromeDriverManager().install()))
    )
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест калькулятора: 7 + 8 = 15")
@allure.description("""
    Проверка работы калькулятора:
    7 + 8 должно быть равно 15.
    Результат должен отобразиться через 45 секунд"
""")
def test_calc(driver):
    """
    Тест проверки работы калькулятора.
    Выполняет сложение двух чисел: 7 и 8.
    Ожидаемый результат: 15.
    """
    with allure.step("Создаем экземпляр класса Main_Page"):
        main_page = Main_Page(driver)

    with allure.step("Открываем калькулятор"):
        main_page.open_calculator()

    with allure.step("Вводим значение задержки {delay_value}: 45 секунд"):
        main_page.set_delay(45)

    with allure.step("Нажимаем кнопку '7'"):
        main_page.click_button('7')

    with allure.step("Нажимаем кнопку '+'"):
        main_page.click_button('+')

    with allure.step("Нажимаем кнопку '8'"):
        main_page.click_button('8')

    with allure.step("Нажимаем кнопку '='"):
        main_page.click_button('=')

    with allure.step("Ожидаем появление результата"):
        WebDriverWait(driver, 50).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )

    with allure.step("Получаем результат со страницы"):
        result = main_page.get_result()

    with allure.step("Проверяем, что результат равен 15"):
        assert result == '15', f"Ожидалось '15', но получено '{result}'"
