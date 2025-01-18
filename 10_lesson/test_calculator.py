from pages.CalculatorPage import CalculatorPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import allure


@allure.epic("Тестирование калькулятора")
@allure.feature("Выдержка результата определенное время")
@allure.title("результат 15 за 3 секунды")
@allure.description("В результате теста должно вывестись на экран калькулятора\
    результат операции ровно за время прописанное в спец. окошке")
def test_result_15_after_3_seconds():
    with allure.step("Инициализируем хром драйвер"):
        browser = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
    with allure.step("Создаем объект CalculatorPage"):
        calculator_page = CalculatorPage(browser)

    with allure.step("Открыть калькулятор"):
        calculator_page.open_calculator()
    with allure.step("Ввести в форму секунды"):
        input_text = calculator_page.fill_form(3)
    with allure.step("Нажать кнопку 7"):
        calculator_page.click_button_7()
    with allure.step("Нажать кнопку +"):
        calculator_page.click_button_plus()
    with allure.step("Нажать кнопку 8"):
        calculator_page.click_button_8()
    with allure.step("Нажать кнопку ="):
        waiting_time = calculator_page.click_button_equal()
    with allure.step("Получить ответ из окошка калькулятора"):
        result_in_window = calculator_page.get_result()

    with allure.step("Проверяем что введенное время = времени ожидания"):
        assert waiting_time == input_text, f"Ошибка. Введенное время: {
            input_text}, время ожидания: {waiting_time}"
    with allure.step("Проверяем что результат в окне калькулятора = 15"):
        assert result_in_window == "15", f"Ожидалось 15 а в ответе - {
            result_in_window}"

    browser.quit()
