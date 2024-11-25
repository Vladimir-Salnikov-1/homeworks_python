from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import sys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()
                                                ))

# Открыть страницу
try:
    driver.get('http://the-internet.herokuapp.com/add_remove_elements/')
    site_selector = "div.row"
    driver.find_element(By.CSS_SELECTOR, site_selector)
    print("сайт доступен.")
    sleep(1)
except NoSuchElementException:
    print("Сайт не доступен.")
    driver.quit()
    sys.exit(1)

# Пять раз кликните на кнопку Add Element
button_add_selector = "button[onclick='addElement()']"

try:
    for x in range(5):
        driver.find_element(By.CSS_SELECTOR, button_add_selector).click()
    print("Нажал 5 раз на кнопку Add Element.")
    sleep(2)
except NoSuchElementException:
    print("Не удалось найти кнопку 'Add Element'. Завершение программы.")
    driver.quit()
    sys.exit(1)

# Соберите со страницы список кнопок Delete
button_delete_selector = "button[onclick='deleteElement()']"
try:
    buttons_delete = driver.find_elements(By.CSS_SELECTOR,
                                          button_delete_selector)
    print("Кнопки Delete присутствуют.")
# Выведите на экран размер списка
    print(f"на странице {len(buttons_delete)} кнопок Delete.")
except NoSuchElementException:
    print("Не удалось найти кнопки 'Delete'. Завершение программы.")

# Преравание работы драйвера
driver.quit()
