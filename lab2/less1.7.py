import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")

try:
    treasure_img = browser.find_element(By.CSS_SELECTOR, "#treasure")

    x_value = treasure_img.get_attribute("valuex")

    y = calc(x_value)

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
    browser.quit()