from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_calc.calc_main_page import Main_Page


def test_calc():
    driver = webdriver.Chrome(
        service=ChromeService((ChromeDriverManager().install())))
    wait = WebDriverWait(driver, 50)

    main_page = Main_Page(driver)  # Хранит экземпляр класса MainPage
    main_page.open_calculator()
    main_page.set_delay('45')
    main_page.click_button('7')
    main_page.click_button('+')
    main_page.click_button('8')
    main_page.click_button('=')

    wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
            )
    result = main_page.get_result()
    assert result == '15'

    driver.quit()
