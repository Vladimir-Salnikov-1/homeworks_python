from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:

    def __init__(self, browser):
        self._browser = browser
        self._browser.maximize_window()

    # Заходим на сайт на страницу авторизации:
    def open_page_authorization(self):
        self._browser.get("https://www.saucedemo.com/")
        WebDriverWait(self._browser, 10, 0.1).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div"))
            )

    # Вводим логин:
    def input_login(self, login):
        input_username = self._browser.find_element(
            By.CSS_SELECTOR, "#user-name")
        input_username.clear()
        input_username.send_keys(login)

    # Вводим пароль:
    def input_password(self, password):
        input_password = self._browser.find_element(
            By.CSS_SELECTOR, "#password")
        input_password.clear()
        input_password.send_keys(password)

    # Нажимаем на кнопку Login:
    def press_button_login(self):
        button_login = self._browser.find_element(
            By.CSS_SELECTOR, "#login-button")
        button_login.click()
        WebDriverWait(self._browser, 10, 0.1).until(
            EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, ".inventory_item_description")))

    # Добавляем необходимые товары в корзину:
    def add_the_desired_items_to_the_cart(self):
        add_backpack = self._browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
        add_backpack.click()
        add_t_shirt = self._browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
        add_t_shirt.click()
        add_onesie = self._browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
        add_onesie.click()

    # Переходим в корзину:
    def go_in_cart(self):
        self._browser.find_element(
            By.CSS_SELECTOR, ".shopping_cart_link").click()
        WebDriverWait(self._browser, 10, 0.1).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout"))
            )

    # Нажимаем на кнопку checkout:
    def press_button_checkout(self):
        self._browser.find_element(By.CSS_SELECTOR, "#checkout").click()
        WebDriverWait(self._browser, 10, 0.1).until(
            EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, ".form_input")))

    # Вводим Имя:
    def input_first_name(self, first_name):
        input_first_name = self._browser.find_element(
            By.CSS_SELECTOR, "#first-name")
        input_first_name.clear()
        input_first_name.send_keys(first_name)

    # Вводим Фамилию:
    def input_last_name(self, last_name):
        input_last_name = self._browser.find_element(
            By.CSS_SELECTOR, "#last-name")
        input_last_name.clear()
        input_last_name.send_keys(last_name)

    # Вводим почтовый индекс:
    def input_postal_code(self, postal_code):
        input_username = self._browser.find_element(
            By.CSS_SELECTOR, "#postal-code")
        input_username.clear()
        input_username.send_keys(postal_code)

    # Нажимаем на кнопку checkout:
    def press_button_continue(self):
        self._browser.find_element(By.CSS_SELECTOR, "#continue").click()

    # Получаем итоговую сумму (без лишних слов):
    def get_itog_sum(self):
        total = self._browser.find_element(
            By.CSS_SELECTOR, "[data-test='total-label'").text
        total = total.replace("Total: ", "")
        return total
