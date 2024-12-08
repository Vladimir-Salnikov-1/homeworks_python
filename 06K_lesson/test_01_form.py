import pytest
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


# Тест на правильность подсветки полей для формы
def test_form_submission(browser):
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение формы данными
    browser.find_element(By.CSS_SELECTOR, "[name='first-name']").send_keys(
        "Иван")
    browser.find_element(By.CSS_SELECTOR, "[name='last-name']").send_keys(
        "Петров")
    browser.find_element(By.CSS_SELECTOR, "[name='address']").send_keys(
        "Ленина, 55-3")
    browser.find_element(By.CSS_SELECTOR, "[name='e-mail']").send_keys(
        "test@skypro.com")
    browser.find_element(By.CSS_SELECTOR, "[name='phone']").send_keys(
        "+7985899998787")
    browser.find_element(By.CSS_SELECTOR, "[name='zip-code']").send_keys(
        "")  # оставить пустым
    browser.find_element(By.CSS_SELECTOR, "[name='city']").send_keys(
        "Москва")
    browser.find_element(By.CSS_SELECTOR, "[name='country']").send_keys(
        "Россия")
    browser.find_element(By.CSS_SELECTOR, "[name='job-position']").send_keys(
        "QA")
    browser.find_element(By.CSS_SELECTOR, "[name='company']").send_keys(
        "SkyPro")

    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, ".mt-3")
    submit_button.click()

    # Ожидание обработки формы
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#zip-code.alert-danger"))
    )

    # Проверка подсветки поля "Zip code" красным
    zip_code_field = browser.find_element(By.CSS_SELECTOR, "#zip-code")
    assert "alert-danger" in zip_code_field.get_attribute(
        "class"), "Поле Zip Code не подсвечено красным"

    # Изъятие данных для проверки
    green_fields = browser.find_elements(By.CSS_SELECTOR, ".alert-success")

    # Проверка что остальные поля подсвечены зеленым
    assert len(green_fields) == 9, f"Ожидается 9 зеленых полей, но найдено {
        len(green_fields)}"
