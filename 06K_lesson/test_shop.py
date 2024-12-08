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


# тест на правильность подсчета итоговой суммы
def test_total_sum(browser):
    browser.get("https://www.saucedemo.com/")

    # Вводим данные для входа, вход (username, password, кнопка вход)
    input_username = browser.find_element(By.CSS_SELECTOR, "#user-name")
    input_username.clear()
    input_username.send_keys("standard_user")
    input_password = browser.find_element(By.CSS_SELECTOR, "#password")
    input_password.clear()
    input_password.send_keys("secret_sauce")
    button_login = browser.find_element(By.CSS_SELECTOR, "#login-button")
    button_login.click()

    # дожидаемся видимость следующего используемого элемента
    waiter = WebDriverWait(browser, 10, 0.1)
    waiter.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")))

    # Добавляем нужные товары в корзину
    add_backpack = browser.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    add_backpack.click()
    add_t_shirt = browser.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
    add_t_shirt.click()
    add_onesie = browser.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
    add_onesie.click()

    # Переход в корзину, переход к заполнению данных
    browser.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    browser.find_element(By.CSS_SELECTOR, "#checkout").click()

    # Заполнение данных, кнопка "продолжить"
    browser.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Владимир")
    browser.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Сальников")
    browser.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("186500")
    browser.find_element(By.CSS_SELECTOR, "#continue").click()

    # Изъятие данных для проверки (итоговая сумма без лишних слов)
    total = browser.find_element(
        By.CSS_SELECTOR, "[data-test='total-label'").text
    total = total.replace("Total: ", "")

    # Проверка
    assert total == "$58.29", "Ошибка. Итоговая сумма не верна"
