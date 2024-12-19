from pages.CalculatorPage import CalculatorPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


def test_result_15_after_45_seconds():

    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    calculator_page = CalculatorPage(browser)

    calculator_page.open_calculator()
    input_text = calculator_page.fill_form(3)
    calculator_page.click_button_7()
    calculator_page.click_button_plus()
    calculator_page.click_button_8()
    waiting_time = calculator_page.click_button_equal()
    result_in_window = calculator_page.get_result()

    assert waiting_time == input_text, f"Ошибка. Введенное время: {
        input_text}, время ожидания: {waiting_time}"
    assert result_in_window == "15", f"Ожидалось 15 а в ответе - {
        result_in_window}"

    browser.quit()
