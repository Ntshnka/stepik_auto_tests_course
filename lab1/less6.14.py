from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")

    input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    input1.send_keys("Иван")

    input2 = browser.find_element(By.XPATH, "//label[text()='Last name*']/following-sibling::input")
    input2.send_keys("Петров")

    input3 = browser.find_element(By.CLASS_NAME, "third")
    input3.send_keys("test@example.com")

    input4 = browser.find_element(By.XPATH, "//input[@placeholder='Input your phone:']")
    input4.send_keys("+79991234567")

    input5 = browser.find_element(By.XPATH, "//label[text()='Address:']/following-sibling::input")
    input5.send_keys("Москва")

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()