import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/math.html")

try:
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text

    y = calc(x)

    answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_input.send_keys(y)

    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robot_checkbox.click()

    robots_rule_radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    robots_rule_radio.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    time.sleep(10)

finally:
    # Закрываем браузер
    browser.quit()