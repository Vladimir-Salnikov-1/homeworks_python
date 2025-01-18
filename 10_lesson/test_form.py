from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.FormPage import FormPage
import allure


@allure.epic("Тестирование Формы")
@allure.feature("Проверка подсветки поля с невалидным значением")
@allure.title("Пустое поле zip-code")
@allure.description("В результате теста проверяется что поле zip-code\
    подсвечивается крассным цветом если введено невалидное значение")
def test_illumination_in_form():
    with allure.step("Иницилируем хром драйвер."):
        browser = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
    with allure.step("Создаем объект класса FormPage"):
        form_page = FormPage(browser)

    with allure.step("Отрыть сайт"):
        form_page.open_form()
    with allure.step("Ввести имя"):
        form_page.send_first_name("Иван")
    with allure.step("Ввести фамилию"):
        form_page.send_last_name("Петров")
    with allure.step("Ввести адрес"):
        form_page.send_address("Ленина, 55-3")
    with allure.step("Ввести email"):
        form_page.send_email("test@skypro.com")
    with allure.step("Ввести номер телефона"):
        form_page.send_phone("+7985899998787")
    with allure.step("Ввести zip_code"):
        form_page.send_zip_code("")
    with allure.step("Ввести город"):
        form_page.send_city("Москва")
    with allure.step("Ввести страну"):
        form_page.send_country("Россия")
    with allure.step("Ввести должность"):
        form_page.send_job_position("QA")
    with allure.step("Ввести компанию"):
        form_page.send_company("SkyPro")
    with allure.step("Нажать кнопку submit"):
        form_page.press_button_submit()

    with allure.step("Проверить что поле zip-code подсвечено красным цветом"):
        with allure.step("Получить значение класса поля zip-code"):
            r_cl = form_page.get_class_red()
        with allure.step("Проверить что в классе элемента есть alert-danger"):
            assert "alert-danger" in r_cl, f"в поле нет класса {r_cl}"
    with allure.step("Проверить что остальные поля подсвечены зеленым цветом"):
        with allure.step("Получить количество элементов отмечнных\
                зеленым цветом"):
            len_green_fields = form_page.get_class_green()
        with allure.step("Проверить что оставшихся полей\
                подсвеченных полей 9"):
            assert len_green_fields == 9, (
                f"Ожидается 9 зеленых полей, найдено: {len(len_green_fields)}"
                )

    browser.quit()
