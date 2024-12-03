from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

browser.get("http://uitestingplayground.com/textinput")
input_selector = browser.find_element(By.CSS_SELECTOR, "#newButtonName")
input_selector.send_keys("SkyPro")
sleep(2)
button_selector = browser.find_element(By.CSS_SELECTOR, "#updatingButton")
button_selector.click()
sleep(2)
print(f'Текст кнопки: "{button_selector.text}"')


browser.quit()
