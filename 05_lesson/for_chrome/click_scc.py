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
    driver.get('http://uitestingplayground.com/classattr')
    navbar_selector = "nav.navbar.navbar-expand-lg.navbar-light.bg-light"
    driver.find_element(By.CSS_SELECTOR, navbar_selector)
    print("сайт доступен.")
    sleep(1)
except NoSuchElementException:
    print("Сайт не доступен.")
    driver.quit()
    sys.exit(1)

# Кликните на синюю кнопку
blue_button_selector = ".btn-primary"
driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
print("Кнопка успешно нажата")
sleep(1)

# Преравание работы драйвера
driver.quit()
