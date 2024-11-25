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
    driver.get('http://the-internet.herokuapp.com/inputs')
    field_input_selector = "div #content"
    driver.find_element(By.CSS_SELECTOR, field_input_selector)
    print("Сайт доступен.")
    sleep(1)
except NoSuchElementException:
    print("Сайт не доступен.")
    driver.quit()
    sys.exit(1)

# Введите в поле текст 1000
field_input = driver.find_element(By.CSS_SELECTOR, "input")
field_input.send_keys("1000")
print("написал 1000")
sleep(1)

# Очистите это поле
field_input.clear()
print("очистил")
sleep(1)

# Введите в поле текст 900
field_input.send_keys("900")
print("написал 900")
sleep(1)

# Преравание работы драйвера
driver.quit()
