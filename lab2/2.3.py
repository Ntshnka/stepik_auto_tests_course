from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/selects1.html")

try:
    num1_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    num2_element = browser.find_element(By.CSS_SELECTOR, "#num2")

    num1 = int(num1_element.text)
    num2 = int(num2_element.text)

    total = num1 + num2

    total_str = str(total)

    dropdown = browser.find_element(By.CSS_SELECTOR, "#dropdown")

    select = Select(dropdown)

    select.select_by_value(total_str)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    time.sleep(10)

finally:
    browser.quit()