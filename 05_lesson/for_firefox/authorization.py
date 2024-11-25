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
    driver.get('http://the-internet.herokuapp.com/login')
    authorization_selector = "div #content"
    driver.find_element(By.CSS_SELECTOR, authorization_selector)
    print("Сайт доступен.")
    sleep(1)
except NoSuchElementException:
    print("Сайт не доступен.")
    driver.quit()
    sys.exit(1)

# В поле username введите значение tomsmith
username_input = driver.find_element(By.CSS_SELECTOR, "#username")
username_input.send_keys("tomsmith")
print("Ввел значение в поле username")
sleep(1)

# В поле password введите значение SuperSecretPassword!
password_input = driver.find_element(By.CSS_SELECTOR, "#password")
password_input.send_keys("SuperSecretPassword!")
print("Ввел значение в поле password")
sleep(1)

# Нажмите кнопку Login
button_login = driver.find_element(By.CSS_SELECTOR, ".fa-sign-in")
button_login.click()
print("Нажал на кнопку Login")
sleep(1)

# Преравание работы драйвера
driver.quit()
