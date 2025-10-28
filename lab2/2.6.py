import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("https://SunInJuly.github.io/execute_script.html")

try:
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text

    y = calc(x)

    answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_input.send_keys(y)

    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robot_checkbox.click()

    robots_rule_radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")

    browser.execute_script("return arguments[0].scrollIntoView(true);", robots_rule_radio)
    robots_rule_radio.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()

    time.sleep(10)

finally:
    browser.quit()