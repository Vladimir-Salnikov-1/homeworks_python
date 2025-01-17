from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import allure


class CalculatorPage:

    def __init__(self, browser):
        self._browser = browser
        self._browser.maximize_window()

    # Открываем калькулятор, ждем появления необходимых элементов:
    @allure.step("Открыть калькулятор")
    def open_calculator(self):
        """Этот метод открывает калькулятор и ждет появления
        необходимых элементов."""
        with allure.step("Открыть сайт"):
            self._browser.get(
                "https://bonigarcia.dev/selenium-webdriver-" +
                "java/slow-calculator.html")

        with allure.step("Дождаться прогрузки страницы"):
            WebDriverWait(self._browser, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".col-sm-12.py-10"))
            )

    # Вводим значение в поле ввода секунд ожидания, фиксируем значение:
    @allure.step("Ввести в форму секунды, в данном случае: {second} сек.")
    def fill_form(self, second: int) -> str:
        """Этот метод принимает на вход параметр "секунды",
        вводит это значение в поле ввода секунд ожидания,
        фиксирует значение."""
        with allure.step("Находим поле ввода для времени ожидания"):
            input = self._browser.find_element(By.CSS_SELECTOR, "#delay")
        with allure.step("Очищаем поле ввода"):
            input.clear()
        with allure.step("Вводим необходимое значение"):
            input.send_keys(second)
        with allure.step("Берем значение атрибута value из формы ввода"):
            input_text = int(self._browser.find_element(
                By.CSS_SELECTOR, "#delay").get_attribute("value"))
        return input_text

    # Нажимаем кнопку 7:
    @allure.step("Нажать кнопку 7")
    def click_button_7(self):
        """Этот метод нажимает на калькуляторе кнопку "7"."""
        ls = self._browser.find_elements(By.CSS_SELECTOR, ".btn")
        ls[1].click()

    # Нажимаем кнопку +:
    @allure.step("Нажать кнопку +")
    def click_button_plus(self):
        """Этот метод нажимает на калькуляторе кнопку "+"."""
        ls = self._browser.find_elements(By.CSS_SELECTOR, ".btn")
        ls[4].click()

    # Нажимаем кнопку 8:
    @allure.step("Нажать кнопку 8")
    def click_button_8(self):
        """Этот метод нажимает на калькуляторе кнопку "8"."""
        ls = self._browser.find_elements(By.CSS_SELECTOR, ".btn")
        ls[2].click()

    # Нажимаем кнопку =, фиксируем время ожидания ответа:
    @allure.step("Нажать кнопку =")
    def click_button_equal(self) -> int:
        """Этот метод нажимает на калькуляторе кнопку "=" и фиксирует
        время ожидания"""
        with allure.step("Нажать на ="):
            ls = self._browser.find_elements(By.CSS_SELECTOR, ".btn")
            ls[15].click()
        with allure.step("Фиксируем время"):
            with allure.step("запускаем таймер"):
                start_time = time.time()
            with allure.step("Ждем пока в окошке не появится результат"):
                waiter = WebDriverWait(self._browser, 55, 0.1)
                waiter.until(
                    EC.text_to_be_present_in_element(
                        (By.CSS_SELECTOR, ".screen"), "15"))
            with allure.step("Останавливаем время"):
                end_time = time.time()
            with allure.step("берем значение из нашего секундомера"):
                waiting_time = int(end_time - start_time)
        return waiting_time

    # Получаем и фиксируем ответ:
    @allure.step("Получить ответ из окошка калькулятора")
    def get_result(self) -> str:
        """Этот метод берет значение из окошка калькулятора и
        переводит его в текстовое значение"""
        result_in_window = self._browser.find_element(
            By.CSS_SELECTOR, ".screen").text
        return result_in_window
