from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.ShopPage import ShopPage


def test_total_sum():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    shop_page = ShopPage(browser)

    shop_page.open_page_authorization()
    shop_page.input_login("standard_user")
    shop_page.input_password("secret_sauce")
    shop_page.press_button_login()
    shop_page.add_the_desired_items_to_the_cart()
    shop_page.go_in_cart()
    shop_page.press_button_checkout()
    shop_page.input_first_name("Владимир")
    shop_page.input_last_name("Сальников")
    shop_page.input_postal_code("186500")
    shop_page.press_button_continue()
    itog_sum = shop_page.get_itog_sum()

    assert itog_sum == "$58.29", "Ошибка. Итоговая сумма не верна"

    browser.quit()
