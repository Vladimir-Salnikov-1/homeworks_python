from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

browser.get("http://uitestingplayground.com/ajax")
browser.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

waiter = WebDriverWait(browser, 20, 0.1)
wait_plashka = waiter.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success")))
print("Нашел элемент")
text_plashka = browser.find_element(By.CSS_SELECTOR, ".bg-success").text

print(f'Текст на зеленой плашке: "{text_plashka}"')

browser.quit()
