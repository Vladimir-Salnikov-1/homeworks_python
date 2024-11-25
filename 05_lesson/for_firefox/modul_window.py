from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import sys

# Установка Firefox WebDriver
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install(
                                                                            )))

# Открыть страницу
try:
    driver.get('http://the-internet.herokuapp.com/entry_ad')
    modul_selector = "#modal .underlay"
    driver.find_element(By.CSS_SELECTOR, modul_selector)
    print("Сайт доступен.")
    sleep(1)
except NoSuchElementException:
    print("Сайт не доступен.")
    driver.quit()
    sys.exit(1)

# В модальном окне нажмите на кнопку Сlose
close_selector = ".modal-footer p"

try:
    close_button = driver.find_element(By.CSS_SELECTOR, close_selector)
    driver.execute_script("arguments[0].click();", close_button)
    print("Кнопка close успешно нажата")
except Exception as e:
    print(f"Ошибка: {e}")
    driver.quit()

# Преравание работы драйвера
driver.quit()
