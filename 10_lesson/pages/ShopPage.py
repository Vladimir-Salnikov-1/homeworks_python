from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class ShopPage:

    def __init__(self, browser):
        self._browser = browser
        self._browser.maximize_window()

    # Заходим на сайт на страницу авторизации:
    def open_page_authorization(self):
        """Этот метод заходит на сайт на страницу авторизации."""
        with allure.step("Зайти на сайт"):
            self._browser.get("https://www.saucedemo.com/")
        with allure.step("Подождать прогрузки всего сайта"):
            WebDriverWait(self._browser, 10, 0.1).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div"))
                )

    # Вводим логин:
    def input_login(self, login: str):
        """Этот метод принимает на вход Логин
        и вводит его в соответствующее поле."""
        input_username = self._browser.find_element(
            By.CSS_SELECTOR, "#user-name")
        input_username.clear()
        input_username.send_keys(login)

    # Вводим пароль:
    def input_password(self, password: str):
        """Этот метод принимает на вход Пароль
        и вводит его в соответствующее поле."""
        input_password = self._browser.find_element(
            By.CSS_SELECTOR, "#password")
        input_password.clear()
        input_password.send_keys(password)

    # Нажимаем на кнопку Login:
    def press_button_login(self):
        """Этот метод нажимает на кнопку Login
        и ждет появления новой страницы."""
        with allure.step("Нажать на кнопку"):
            button_login = self._browser.find_element(
                By.CSS_SELECTOR, "#login-button")
            button_login.click()
        with allure.step("Подождат прогрузки новой страницы"):
            WebDriverWait(self._browser, 10, 0.1).until(
                EC.visibility_of_all_elements_located(
                    (By.CSS_SELECTOR, ".inventory_item_description")))

    # Добавляем необходимые товары в корзину:
    def add_the_desired_items_to_the_cart(self):
        """Этот метод добавляет необходимые товары в корзину."""
        with allure.step("Добавить 1 товар"):
            add_backpack = self._browser.find_element(
                By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
            add_backpack.click()
        with allure.step("Добавить 2 товар"):
            add_t_shirt = self._browser.find_element(
                By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
            add_t_shirt.click()
        with allure.step("Добавить 3 товар"):
            add_onesie = self._browser.find_element(
                By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
            add_onesie.click()

    # Переходим в корзину:
    def go_in_cart(self):
        """Этот метод переходит в корзину,
        и ждет появления необходимых элементов."""
        with allure.step("Нажать на корзину"):
            self._browser.find_element(
                By.CSS_SELECTOR, ".shopping_cart_link").click()
        with allure.step("Подождать прогрузки"):
            WebDriverWait(self._browser, 10, 0.1).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout"))
                )

    # Нажимаем на кнопку checkout:
    def press_button_checkout(self):
        """Этот метод нажимает на кнопку Checkout,
        и ждет появления необходимых элементов."""
        with allure.step("нажать на кнопку"):
            self._browser.find_element(By.CSS_SELECTOR, "#checkout").click()
        with allure.step("Подождать прогрузки"):
            WebDriverWait(self._browser, 10, 0.1).until(
                EC.visibility_of_all_elements_located(
                    (By.CSS_SELECTOR, ".form_input")))

    # Вводим Имя:
    def input_first_name(self, first_name: str):
        """Этот метод принимает на вход параметр Имя
        и вводит его в соответствующее поле."""
        with allure.step("Найти поле ввода"):
            input_first_name = self._browser.find_element(
                By.CSS_SELECTOR, "#first-name")
        with allure.step("Очистить поле ввода"):
            input_first_name.clear()
        with allure.step("Ввести имя"):
            input_first_name.send_keys(first_name)

    # Вводим Фамилию:
    def input_last_name(self, last_name: str):
        """Этот метод принимает на вход параметр Фамилия
        и вводит его в соответствующее поле."""
        with allure.step("Найти поле ввода"):
            input_last_name = self._browser.find_element(
                By.CSS_SELECTOR, "#last-name")
        with allure.step("Очистить поле ввода"):
            input_last_name.clear()
        with allure.step("Ввести фамилию"):
            input_last_name.send_keys(last_name)

    # Вводим почтовый индекс:
    def input_postal_code(self, postal_code: str):
        """Этот метод принимает на вход параметр Почтовый индекс
        и вводит его в соответствующее поле."""
        with allure.step("Найти поле ввода"):
            input_username = self._browser.find_element(
                By.CSS_SELECTOR, "#postal-code")
        with allure.step("Очистить поле ввода"):
            input_username.clear()
        with allure.step("Ввести почтовый индекс"):
            input_username.send_keys(postal_code)

    # Нажимаем на кнопку continue:
    def press_button_continue(self):
        """Этот метод нажимает на кнопку Continue."""
        self._browser.find_element(By.CSS_SELECTOR, "#continue").click()

    # Получаем итоговую сумму (без лишних слов):
    def get_itog_sum(self) -> str:
        """Этот метод получает итоговую сумму всех заказов"""
        with allure.step("Получить весь текст с итоговой суммой"):
            total = self._browser.find_element(
                By.CSS_SELECTOR, "[data-test='total-label'").text
        with allure.step("Вычленить из этого текста только сумму"):
            total = total.replace("Total: ", "")
        return total
