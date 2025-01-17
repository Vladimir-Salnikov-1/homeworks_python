from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class FormPage:

    def __init__(self, browser):
        self._browser = browser
        self._browser.maximize_window()

    # Открываем сайт с формой, ждем появления необходимых элементов:
    def open_form(self):
        """Этот метод открывает сайт с формой и ждет
        появления необходимых элементов."""
        self._browser.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        WebDriverWait(self._browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "main"))
        )

    # Водим Имя:
    def send_first_name(self, first_name: str):
        """Этот метод принимает на вход Имя и вводит его
        в соответствующее поле."""
        self._browser.find_element(
            By.CSS_SELECTOR, "[name='first-name']").send_keys(first_name)

    # Вводим Фамилию:
    def send_last_name(self, last_name: str):
        """Этот метод принимает на вход Фамилия и вводит его
        в соответствующее поле."""
        self._browser.find_element(
            By.CSS_SELECTOR, "[name='last-name']").send_keys(last_name)

    # Вводим адрес:
    def send_address(self, address: str):
        """Этот метод принимает на вход Адрес и вводит его
        в соответствующее поле."""
        self._browser.find_element(
            By.CSS_SELECTOR, "[name='address']").send_keys(address)

    # Вводим почту:
    def send_email(self, email: str):
        """Этот метод принимает на вход Email и вводит его
        в соответствующее поле."""
        self._browser.find_element(
            By.CSS_SELECTOR, "[name='e-mail']").send_keys(email)

    # Вводим номер телефона:
    def send_phone(self, phone: str):
        """Этот метод принимает на вход Телефон и вводит его
        в соответствующее поле."""
        self._browser.find_element(
            By.CSS_SELECTOR, "[name='phone']").send_keys(phone)

    # Вводим зип-код:
    def send_zip_code(self, zip_code: str):
        """Этот метод принимает на вход Zip_code и вводит его
        в соответствующее поле."""
        self._browser.find_element(
            By.CSS_SELECTOR, "[name='zip-code']").send_keys(zip_code)

    # Вводим город:
    def send_city(self, city: str):
        """Этот метод принимает на вход Город и вводит его
        в соответствующее поле."""
        self._browser.find_element(
            By.CSS_SELECTOR, "[name='city']").send_keys(city)

    # Вводим страну:
    def send_country(self, country: str):
        """Этот метод принимает на вход Страна и вводит его
        в соответствующее поле."""
        self._browser.find_element(
            By.CSS_SELECTOR, "[name='country']").send_keys(country)

    # Вводим должность:
    def send_job_position(self, job_position: str):
        """Этот метод принимает на вход Должность и вводит его
        в соответствующее поле."""
        self._browser.find_element(
            By.CSS_SELECTOR, "[name='job-position']").send_keys(job_position)

    # Вводим компанию:
    def send_company(self, company: str):
        """Этот метод принимает на вход Компания и вводит его
        в соответствующее поле."""
        self._browser.find_element(
            By.CSS_SELECTOR, "[name='company']").send_keys(company)

    # Нажимаем кнопку submit:
    def press_button_submit(self):
        """Этот метод имитирует нажатие на кнопку Submit
        и ждет загрузки следующей страницы"""
        self._browser.find_element(By.CSS_SELECTOR, ".mt-3").click()
        WebDriverWait(self._browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "main"))
        )

    # Получаем значение класса поля zip-code:
    def get_class_red(self) -> str:
        """Этот метод получает значение класса поля zip-code."""
        classs = self._browser.find_element(
            By.CSS_SELECTOR, "#zip-code").get_attribute("class")
        return classs

    # Получаем количество элементов отмечнных зеленым цветом:
    def get_class_green(self) -> int:
        """Этот метод получает количество элементов
        отмечнных зеленым цветом."""
        green_fields = self._browser.find_elements(
            By.CSS_SELECTOR, ".alert-success")
        return len(green_fields)
