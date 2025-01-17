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
    def open_calculator(self):
        """Этот метод открывает калькулятор и ждет появления
        необходимых элементов."""
        self._browser.get(
            "https://bonigarcia.dev/selenium-webdriver-java/\
                slow-calculator.html")
        WebDriverWait(self._browser, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".col-sm-12.py-10"))
        )

    # Вводим значение в поле ввода секунд ожидания, фиксируем значение:
    def fill_form(self, second: int) -> str:
        """Этот метод принимает на вход параметр "секунды",
        вводит это значение в поле ввода секунд ожидания,
        фиксирует значение."""
        input = self._browser.find_element(By.CSS_SELECTOR, "#delay")
        input.clear()
        input.send_keys(second)
        input_text = int(self._browser.find_element(
            By.CSS_SELECTOR, "#delay").get_attribute("value"))
        return input_text

    # Нажимаем кнопку 7:
    def click_button_7(self):
        """Этот метод нажимает на калькуляторе кнопку "7"."""
        ls = self._browser.find_elements(By.CSS_SELECTOR, ".btn")
        ls[1].click()

    # Нажимаем кнопку +:
    def click_button_plus(self):
        """Этот метод нажимает на калькуляторе кнопку "+"."""
        ls = self._browser.find_elements(By.CSS_SELECTOR, ".btn")
        ls[4].click()

    # Нажимаем кнопку 8:
    def click_button_8(self):
        """Этот метод нажимает на калькуляторе кнопку "8"."""
        ls = self._browser.find_elements(By.CSS_SELECTOR, ".btn")
        ls[2].click()

    # Нажимаем кнопку =, фиксируем время ожидания ответа:
    def click_button_equal(self) -> int:
        """Этот метод нажимает на калькуляторе кнопку "=" и фиксирует
        время ожидания"""
        ls = self._browser.find_elements(By.CSS_SELECTOR, ".btn")
        ls[15].click()
        start_time = time.time()
        waiter = WebDriverWait(self._browser, 55, 0.1)
        waiter.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"))
        end_time = time.time()
        waiting_time = int(end_time - start_time)
        return waiting_time

    # Получаем и фиксируем ответ:
    def get_result(self) -> str:
        """Этот метод берет значение из окошка калькулятора и
        переводит его в текстовое значение"""
        result_in_window = self._browser.find_element(
            By.CSS_SELECTOR, ".screen").text
        return result_in_window
