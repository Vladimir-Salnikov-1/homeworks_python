import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Создаем экземпляр драйвера Chrome с помощью фикстуры
@pytest.fixture
def browser():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


# Тест на определенный результат через определенное время
def test_result_over_time(browser):
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Очистка и заполнение формы
    input = browser.find_element(By.CSS_SELECTOR, "#delay")
    input.clear()
    input.send_keys("5")

    # Ввод цифр в калькулятор
    buttons = browser.find_elements(By.CSS_SELECTOR, ".btn")
    buttons[1].click()  # кнопка 7
    buttons[4].click()  # кнопка +
    buttons[2].click()  # кнопка 8
    buttons[15].click()  # кнопка =

    # Добавляем ожидание и фиксируем время ожидания
    start_time = time.time()
    waiter = WebDriverWait(browser, 55, 0.1)
    waiter.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
    end_time = time.time()
    waiting_time = int(end_time - start_time)  # Вычисление время ожидания

    # берем значение с окна калькулятора и сравниваем с правильным ответом
    window = browser.find_element(By.CSS_SELECTOR, ".screen").text
    assert window == "15", f"Ожидалось 15 а в ответе - {window}"

    # Изъятие данных для проверки
    input_text = int(browser.find_element(
        By.CSS_SELECTOR, "#delay").get_attribute("value"))

    # Проверка. Сравниваем время ожидания и введеное время
    assert waiting_time == input_text, f"Ошибка. Введенное время: {
        input_text}, время ожидания: {waiting_time}"
