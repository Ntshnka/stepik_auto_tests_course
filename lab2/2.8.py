from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

try:
    first_name = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']")
    first_name.send_keys("Иван")

    last_name = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']")
    last_name.send_keys("Петров")

    email = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
    email.send_keys("test@example.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test_file.txt')

    with open(file_path, 'w') as file:
        file.write("This is a test file for automation\n")
        file.write("Файл для тестирования загрузки")

    file_input = browser.find_element(By.CSS_SELECTOR, "#file")
    file_input.send_keys(file_path)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    time.sleep(10)

finally:
    browser.quit()

    if os.path.exists(file_path):
        os.remove(file_path)