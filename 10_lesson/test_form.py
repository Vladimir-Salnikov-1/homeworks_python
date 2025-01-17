from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.FormPage import FormPage


def test_illumination_in_form():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    form_page = FormPage(browser)

    form_page.open_form()
    form_page.send_first_name("Иван")
    form_page.send_last_name("Петров")
    form_page.send_address("Ленина, 55-3")
    form_page.send_email("test@skypro.com")
    form_page.send_phone("+7985899998787")
    form_page.send_zip_code("")
    form_page.send_city("Москва")
    form_page.send_country("Россия")
    form_page.send_job_position("QA")
    form_page.send_company("SkyPro")
    form_page.press_button_submit()

    r_cl = form_page.get_class_red()
    assert "alert-danger" in r_cl, f"в поле нет класса {r_cl}"

    len_green_fields = form_page.get_class_green()
    assert len_green_fields == 9, (
        f"Ожидается 9 зеленых полей, но найдено {len(len_green_fields)}")

    browser.quit()
