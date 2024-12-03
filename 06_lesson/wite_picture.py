from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

browser.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter = WebDriverWait(browser, 40, 0.1)
landscape_element = waiter.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#landscape")))

img_conteyner = browser.find_element(By.CSS_SELECTOR, "#image-container")
list_img = img_conteyner.find_elements(By.CSS_SELECTOR, "img")
atribute = list_img[2].get_attribute("src")
print(atribute)

browser.quit()
