from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.ShopPage import ShopPage
import allure


@allure.epic("Тестирование магазина")
@allure.feature("Подсчет итоговой суммы")
@allure.title("Подсчет итоговой суммы трех товаров")
@allure.description("Данный тест проверяет правильность подсчета итоговой\
    суммы трех товаров добавленных в корзину")
def test_total_sum():
    with allure.step("Иницилируем хром драйвер"):
        browser = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
    with allure.step("Создаем объект класса FormPage"):
        shop_page = ShopPage(browser)

    with allure.step("Зайти на сайт"):
        shop_page.open_page_authorization()
    with allure.step("Ввести логин"):
        shop_page.input_login("standard_user")
    with allure.step("Ввести пароль"):
        shop_page.input_password("secret_sauce")
    with allure.step("Нажать на кнопку login"):
        shop_page.press_button_login()
    with allure.step("Добавить необходимые товары в корзину"):
        shop_page.add_the_desired_items_to_the_cart()
    with allure.step("Перейти в корзину"):
        shop_page.go_in_cart()
    with allure.step("Нажать на кнопку Checkout"):
        shop_page.press_button_checkout()
    with allure.step("Ввести имя"):
        shop_page.input_first_name("Владимир")
    with allure.step("Ввести фамилию"):
        shop_page.input_last_name("Сальников")
    with allure.step("Ввести почтовый индекс"):
        shop_page.input_postal_code("186500")
    with allure.step("Нажать на кнопку Continue"):
        shop_page.press_button_continue()
    with allure.step("Получить итоговую сумму"):
        itog_sum = shop_page.get_itog_sum()

    with allure.step(f"Проверить что итоговая сумма = {itog_sum}"):
        assert itog_sum == "$58.29", "Ошибка. Итоговая сумма не верна"

    browser.quit()
